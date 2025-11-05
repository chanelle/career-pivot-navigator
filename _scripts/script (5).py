
# Create plan_generator.py - The 3-step plan generation and export

plan_gen_content = '''"""
Career Pivot Navigator - Plan Generator
Generates and exports 3-step pivot plans in multiple formats
"""

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from typing import Dict, List, Any, Optional
from datetime import datetime
from utils import export_to_markdown, export_to_notion_format
import json

class PivotPlanGenerator:
    """Generate detailed 3-step pivot plans with exports."""
    
    def __init__(self, model: str = "gpt-4o", temperature: float = 0.7):
        """Initialize the plan generator."""
        self.llm = ChatOpenAI(model_name=model, temperature=temperature)
        self.setup_prompts()
    
    def setup_prompts(self):
        """Setup plan generation prompts."""
        
        self.step_plan_prompt = PromptTemplate.from_template("""You are creating a REALISTIC 3-step pivot plan for someone making a career transition.

Person: {person_name}
Current role: {current_role}
Target role: {target_role}
Their skills: {skills}
Their constraints: {constraints}
Budget: {budget}
Time available per week: {time_per_week}

Create 3 concrete, low-barrier steps. For EACH step:

STEP TITLE: [what they will achieve]
ACTION: [specific, concrete task—not vague]
TIME: [realistic estimate, e.g., "1-2 weeks working 5 hrs/week"]
RESOURCES: [prioritize FREE/low-cost options]
WHY: [why this step matters for the transition]
SUCCESS: [how they know it worked]

Make it tactical, achievable, and encouraging. No "follow your passion" nonsense.
Use markdown formatting for clarity.
""")
        
        self.monetization_prompt = PromptTemplate.from_template("""How can {person_name} start earning money during this career transition to {target_role}?

Current skills: {skills}
Budget constraints: {constraints}
Time available: {time_per_week} hours/week
Remote preference: {remote}

Suggest 2-3 specific ways to monetize while pivoting:
1. Freelance gigs they could start THIS MONTH
2. Side projects that build relevant portfolio
3. Internal opportunities (if staying at current company)

For each, provide:
- How to start (specific steps)
- Realistic first-month earnings potential
- How it supports the pivot goal

Keep it grounded and not "get rich quick" nonsense.
""")
        
        self.resume_prompt = PromptTemplate.from_template("""Reframe 3 resume bullets for {person_name}'s transition from {current_role} to {target_role}.

Original accomplishments: {accomplishments}
New industry they're targeting: {target_role}

For each bullet, show:
1. Original version: [what they wrote]
2. Reframed version: [new language/focus]
3. Why it works: [what changed]

Use language that resonates in the NEW industry while being honest about what they did.
""")
        
        self.mindset_prompt = PromptTemplate.from_template("""Give {person_name} an honest, warm pep talk about this career pivot:

Their situation: {situation}
Their fears: {fears}
What they want: {dreams}
Constraints: {constraints}

Provide:
1. **Permission slip**: Why this IS possible
2. **Reality check**: What's true vs. brain lies
3. **Mindset reframe**: How to think about this journey
4. **First micro-action**: ONE tiny thing to do today

Be direct, warm, and real. Call out both hope and barriers without dismissing either.
""")
    
    def create_step(self, step_number: int, content: str) -> Dict[str, Any]:
        """Parse step content into structured format."""
        
        # Simple parsing - LLM should provide structured output
        lines = content.split("\\n")
        step_data = {
            "step_number": step_number,
            "title": f"Step {step_number}",
            "action": "",
            "time_estimate": "",
            "resources": [],
            "rationale": "",
            "success_metric": ""
        }
        
        current_section = None
        for line in lines:
            line = line.strip()
            if "STEP TITLE" in line:
                step_data["title"] = line.split(":")[-1].strip()
            elif "ACTION" in line:
                current_section = "action"
            elif "TIME" in line:
                current_section = "time"
            elif "RESOURCES" in line:
                current_section = "resources"
            elif "WHY" in line:
                current_section = "rationale"
            elif "SUCCESS" in line:
                current_section = "success"
            elif line and current_section:
                if current_section == "resources" and (line.startswith("-") or line.startswith("*")):
                    step_data["resources"].append(line.lstrip("-*").strip())
                elif current_section == "action":
                    step_data["action"] += " " + line
                elif current_section == "time":
                    step_data["time_estimate"] = line
                elif current_section == "rationale":
                    step_data["rationale"] = line
                elif current_section == "success":
                    step_data["success_metric"] = line
        
        return step_data
    
    def generate_3_step_plan(self, user_data: Dict[str, Any], target_career: Dict[str, Any]) -> Dict[str, Any]:
        """Generate the full 3-step pivot plan."""
        
        chain = self.step_plan_prompt | self.llm
        
        result = chain.invoke({
            "person_name": user_data.get("name", "You"),
            "current_role": user_data.get("current_role", ""),
            "target_role": target_career.get("title", ""),
            "skills": ", ".join(user_data.get("skills", [])),
            "constraints": user_data.get("constraints", ""),
            "budget": user_data.get("budget", "low"),
            "time_per_week": user_data.get("time_availability", "flexible")
        })
        
        plan_text = result.content if hasattr(result, 'content') else str(result)
        
        # Parse into steps
        step_blocks = plan_text.split("STEP")
        steps = []
        for i, block in enumerate(step_blocks[1:], 1):
            steps.append(self.create_step(i, f"STEP{block}"))
        
        return {
            "target_career": target_career,
            "plan_text": plan_text,
            "steps": steps,
            "generated_at": datetime.now().isoformat()
        }
    
    def generate_monetization_strategy(self, user_data: Dict[str, Any], target_career: Dict[str, Any]) -> str:
        """Generate ways to earn during transition."""
        
        chain = self.monetization_prompt | self.llm
        
        result = chain.invoke({
            "person_name": user_data.get("name", "You"),
            "target_role": target_career.get("title", ""),
            "skills": ", ".join(user_data.get("skills", [])),
            "constraints": user_data.get("constraints", ""),
            "time_per_week": user_data.get("time_availability", "flexible"),
            "remote": user_data.get("remote_preference", "high")
        })
        
        return result.content if hasattr(result, 'content') else str(result)
    
    def generate_resume_reframe(self, user_data: Dict[str, Any], target_career: Dict[str, Any], 
                               accomplishments: Optional[List[str]] = None) -> str:
        """Generate reframed resume bullets."""
        
        if accomplishments is None:
            accomplishments = [
                "Managed customer interactions with 95% satisfaction rate",
                "Handled 50+ inquiries daily with 99% accuracy",
                "Trained 3 junior team members"
            ]
        
        chain = self.resume_prompt | self.llm
        
        result = chain.invoke({
            "person_name": user_data.get("name", "You"),
            "current_role": user_data.get("current_role", ""),
            "target_role": target_career.get("title", ""),
            "accomplishments": "\\n".join([f"- {acc}" for acc in accomplishments])
        })
        
        return result.content if hasattr(result, 'content') else str(result)
    
    def generate_mindset_coaching(self, user_data: Dict[str, Any], fears: Optional[List[str]] = None,
                                 dreams: Optional[List[str]] = None) -> str:
        """Generate motivational coaching for the pivot."""
        
        if fears is None:
            fears = ["I'm too old", "I don't have the right skills", "I can't afford to learn"]
        
        if dreams is None:
            dreams = ["Work remotely", "Help people", "Make good money doing meaningful work"]
        
        chain = self.mindset_prompt | self.llm
        
        situation = f"They're in {user_data.get('current_role')} and hate {', '.join(user_data.get('hates', [])[:2])}"
        
        result = chain.invoke({
            "person_name": user_data.get("name", "You"),
            "situation": situation,
            "fears": "\\n".join([f"- {f}" for f in fears]),
            "dreams": "\\n".join([f"- {d}" for d in dreams]),
            "constraints": user_data.get("constraints", "")
        })
        
        return result.content if hasattr(result, 'content') else str(result)
    
    def export_full_plan(self, user_data: Dict[str, Any], analysis: str, 
                         plan: Dict[str, Any], format: str = "markdown") -> str:
        """Export complete plan in specified format."""
        
        if format.lower() == "markdown":
            return export_to_markdown(user_data, analysis, plan)
        elif format.lower() == "notion":
            return export_to_notion_format(user_data, analysis, plan)
        elif format.lower() == "json":
            output = {
                "user": user_data,
                "analysis": analysis,
                "plan": plan,
                "exported_at": datetime.now().isoformat()
            }
            filename = f"pivot_plan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(filename, 'w') as f:
                json.dump(output, f, indent=2)
            return filename
        else:
            raise ValueError(f"Unsupported format: {format}")
'''

with open('plan_generator.py', 'w') as f:
    f.write(plan_gen_content)

print("✅ Created plan_generator.py with PivotPlanGenerator class")
