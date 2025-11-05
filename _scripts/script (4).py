
# Create analyze.py - LangChain analysis module

analyze_content = '''"""
Career Pivot Navigator - LangChain Analysis Module
Core logic for skill/pain mapping and pivot suggestions
"""

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from utils import (
    load_career_map, parse_skill_input, normalize_input_dict,
    find_matching_careers, estimate_pivot_difficulty, create_context_for_llm
)
import json
from typing import Dict, List, Any, Optional

class CareerPivotAnalyzer:
    """Main analyzer using LangChain for career pivot recommendations."""
    
    def __init__(self, model: str = "gpt-4o", temperature: float = 0.7):
        """Initialize the analyzer with LLM and prompt templates."""
        self.llm = ChatOpenAI(model_name=model, temperature=temperature)
        self.career_map = load_career_map()
        self.setup_prompts()
    
    def setup_prompts(self):
        """Setup all LangChain prompt templates."""
        
        # Main career pivot analysis prompt
        self.pivot_prompt = PromptTemplate.from_template("""You are a warm, direct career strategist for neurodivergent and marginalized professionals.

Context about this person:
{context}

Current role: {current_role}
Skills: {skills}
Pain points: {hates}
Interests: {interests}

Analyze and suggest 1-2 realistic career pivots that:
1. Leverage existing skills
2. Address their pain points
3. Align with their interests
4. Offer path to better pay/autonomy if desired

For each pivot, provide:
- Career title & why it fits
- How their current skills transfer
- The honest challenges they might face
- A quick wins mentality: small first steps

Keep tone warm, direct, anti-hustle culture. Use markdown. Be real about systemic barriers.
""")
        
        # Skill extraction prompt
        self.skill_prompt = PromptTemplate.from_template("""Analyze this person's role and extract their hidden superpowers:

Current role: {current_role}
Experience: {background}

Extract and explain:
1. Hard skills (technical, measurable)
2. Soft skills (people, emotional intelligence)
3. Hidden gems (what they don't realize they're good at)
4. Why each matters for career transitions

Format as markdown with brief explanations.
""")
        
        # 3-step plan prompt
        self.plan_prompt = PromptTemplate.from_template("""Create a realistic, low-barrier 3-step plan for {person_name} to explore this pivot:

Target career: {target_career}
Current skills: {skills}
Budget: {budget}
Time availability: {time}
Constraints: {constraints}

For EACH step provide:
1. Specific action (be concrete, not vague)
2. Time estimate
3. Free/low-cost resources
4. Why this step matters
5. How to know if it's working

Format as a numbered list. Be tactical, encouraging, and realistic.
""")
    
    def analyze_pivot(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """Main method: analyze user input and generate pivot recommendations."""
        
        # Normalize input
        normalized = normalize_input_dict(user_data)
        
        # Create enriched context from career map
        context = create_context_for_llm(normalized, self.career_map)
        
        # Build the analysis chain
        analysis_chain = (
            RunnablePassthrough.assign(context=lambda x: context)
            | self.pivot_prompt
            | self.llm
        )
        
        # Run analysis
        result = analysis_chain.invoke({
            "current_role": normalized["current_role"],
            "skills": ", ".join(normalized["skills"]),
            "hates": ", ".join(normalized["hates"]),
            "interests": ", ".join(normalized["interests"]),
            "context": context
        })
        
        analysis_text = result.content if hasattr(result, 'content') else str(result)
        
        return {
            "user_data": normalized,
            "analysis": analysis_text,
            "matched_careers": find_matching_careers(
                normalized["skills"], 
                normalized["hates"], 
                self.career_map
            )
        }
    
    def extract_skills(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """Extract and enhance user's skill set."""
        
        skill_chain = self.skill_prompt | self.llm
        
        result = skill_chain.invoke({
            "current_role": user_data.get("current_role", ""),
            "background": f"Skills: {', '.join(user_data.get('skills', []))}. Experience: {user_data.get('years_experience', 'unknown')} years."
        })
        
        return {
            "extracted_skills": result.content if hasattr(result, 'content') else str(result),
            "original_input": user_data.get("skills", [])
        }
    
    def generate_3_step_plan(self, user_data: Dict[str, Any], target_career_id: str) -> Dict[str, Any]:
        """Generate a concrete 3-step pivot plan."""
        
        # Find target career details
        target_career = None
        for career in self.career_map.get("careers", []):
            if career["id"] == target_career_id:
                target_career = career
                break
        
        if not target_career:
            return {"error": f"Career {target_career_id} not found in database"}
        
        # Estimate difficulty
        difficulty = estimate_pivot_difficulty(
            user_data.get("current_role", ""),
            target_career_id,
            user_data.get("skills", []),
            self.career_map
        )
        
        # Generate plan
        plan_chain = self.plan_prompt | self.llm
        
        result = plan_chain.invoke({
            "person_name": user_data.get("name", "You"),
            "target_career": target_career["title"],
            "skills": ", ".join(user_data.get("skills", [])),
            "budget": user_data.get("budget", "low"),
            "time": user_data.get("time_availability", "flexible"),
            "constraints": user_data.get("constraints", "")
        })
        
        plan_text = result.content if hasattr(result, 'content') else str(result)
        
        return {
            "target_career": target_career,
            "difficulty_assessment": difficulty,
            "plan": plan_text,
            "resources": target_career.get("resources", [])
        }
    
    def get_quick_wins(self, target_career_id: str) -> List[str]:
        """Get quick wins for a specific career pivot."""
        
        for career in self.career_map.get("careers", []):
            if career["id"] == target_career_id:
                return career.get("entry_path", [])
        
        return []
    
    def get_salary_range(self, target_career_id: str) -> Optional[List[int]]:
        """Get salary range for a career."""
        
        for career in self.career_map.get("careers", []):
            if career["id"] == target_career_id:
                return career.get("salary_range", None)
        
        return None

# Example usage function
def demo_analysis():
    """Demo the analyzer with sample input."""
    
    analyzer = CareerPivotAnalyzer()
    
    sample_user = {
        "name": "Alex",
        "current_role": "Customer Service Rep",
        "skills": "communication, de-escalation, CRM systems, empathy, multitasking",
        "hates": "angry customers, low pay, no creative work, repetitive tasks",
        "interests": "tech, mental health, writing, psychology",
        "constraints": "low budget, need to keep current income while transitioning",
        "budget": "low",
        "time_availability": "5-10 hours/week"
    }
    
    print("\\n🚀 Starting Career Pivot Analysis...")
    print("=" * 60)
    
    # Run analysis
    analysis_result = analyzer.analyze_pivot(sample_user)
    
    print("\\n📊 PIVOT ANALYSIS\\n")
    print(analysis_result["analysis"])
    
    print("\\n\\n💼 MATCHED CAREERS\\n")
    for career in analysis_result["matched_careers"]:
        print(f"  - {career['title']} ({career['id']})")
    
    # Generate 3-step plan for first match
    if analysis_result["matched_careers"]:
        first_match = analysis_result["matched_careers"][0]
        print(f"\\n\\n🪜 Generating 3-step plan for: {first_match['title']}")
        print("-" * 60)
        
        plan_result = analyzer.generate_3_step_plan(sample_user, first_match["id"])
        
        print("\\n📋 PLAN\\n")
        print(plan_result["plan"])
        
        difficulty = plan_result["difficulty_assessment"]
        print(f"\\n\\nDifficulty: {difficulty['difficulty'].upper()}")
        print(f"Estimated Timeline: {difficulty['estimated_months']} months")
        print(f"Skill Match: {difficulty['skill_match_percentage']}%")
'''

with open('analyze.py', 'w') as f:
    f.write(analyze_content)

print("✅ Created analyze.py with LangChain CareerPivotAnalyzer class")
