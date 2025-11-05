"""
Career Pivot Navigator - Utility Functions
Helpers for formatting, validation, file I/O, and data processing
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Any, Optional
import re

def load_career_map(filepath: str = None) -> Dict[str, Any]:
    """Load the career mapping database."""
    if filepath is None:
        # Try multiple possible locations
        possible_paths = [
            "career_map.json",
            "../Data and Infrastructure/career_map.json",
            os.path.join(os.path.dirname(__file__), "../Data and Infrastructure/career_map.json")
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                filepath = path
                break
        else:
            print(f"Error: career_map.json not found in any of these locations:")
            for p in possible_paths:
                print(f"  - {p}")
            return {}
    
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {filepath} not found. Make sure career_map.json is accessible.")
        return {}

def parse_skill_input(skill_string: str) -> List[str]:
    """Parse comma or newline-separated skill input into a clean list."""
    skills = re.split(r"[,\n]+", skill_string.lower().strip())
    return [s.strip() for s in skills if s.strip()]

def parse_pain_point_input(pain_string: str) -> List[str]:
    """Parse pain point input into a clean list."""
    return parse_skill_input(pain_string)

def validate_user_input(data: Dict[str, Any]) -> tuple[bool, Optional[str]]:
    """Validate that user provided required fields."""
    required_fields = ["current_role", "skills", "hates", "interests"]

    for field in required_fields:
        if field not in data or not data[field]:
            return False, f"Missing required field: {field}"

    return True, None

def format_career_suggestion(career: Dict[str, Any]) -> str:
    """Format a single career suggestion for display."""
    output = f"\n### 💼 {career['title']}\n"
    output += f"**Salary Range**: ${career['salary_range'][0]:,} - ${career['salary_range'][1]:,}\n"
    output += f"**Remote**: {'✅ Yes' if career['remote'] else '❌ No'}\n"
    output += f"**Freelance Viable**: {'✅ Yes' if career['freelance_viable'] else '❌ No'}\n"
    output += f"**Entry Path**: {' → '.join(career['entry_path'])}\n"
    return output

def format_3_step_plan(plan: Dict[str, Any]) -> str:
    """Format the 3-step pivot plan for export."""
    output = "\n## 🪜 Your 3-Step Pivot Plan\n\n"

    for i, step in enumerate(plan.get("steps", []), 1):
        output += f"### Step {i}: {step.get('title', 'Action')}\n"
        output += f"**What to do**: {step.get('action', '')}\n"
        output += f"**Time needed**: {step.get('time_estimate', '')}\n"
        output += f"**Resources**:\n"
        for resource in step.get('resources', []):
            output += f"  - {resource}\n"
        output += f"**Why**: {step.get('rationale', '')}\n"
        output += f"**Success metric**: {step.get('success_metric', '')}\n\n"

    return output

def export_to_markdown(user_data: Dict[str, Any], analysis: str, plan: Dict[str, Any], 
                      filepath: Optional[str] = None) -> str:
    """Export pivot plan as markdown document."""
    if filepath is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = f"pivot_plan_{timestamp}.md"

    output = f"# Career Pivot Plan for {user_data.get('name', 'You')}\n"
    output += f"*Generated on {datetime.now().strftime('%B %d, %Y at %I:%M %p')}*\n\n"

    output += "## 📋 Your Input\n\n"
    output += f"**Current Role**: {user_data.get('current_role', '')}\n"
    output += f"**Skills**: {', '.join(user_data.get('skills', []))}\n"
    output += f"**Pain Points**: {', '.join(user_data.get('hates', []))}\n"
    output += f"**Interests**: {', '.join(user_data.get('interests', []))}\n\n"

    output += "## 🔄 Analysis & Recommendations\n\n"
    output += analysis
    output += "\n\n"

    output += format_3_step_plan(plan)

    output += "---\n\n"
    output += "_Career Pivot Navigator by [Your Brand]_\n"
    output += "_Built for neurodivergent, marginalized, and burnt-out professionals._\n"

    with open(filepath, 'w') as f:
        f.write(output)

    return filepath

def export_to_notion_format(user_data: Dict[str, Any], analysis: str, plan: Dict[str, Any]) -> str:
    """Generate Notion-compatible markdown export."""
    # Notion uses slightly different markdown syntax
    output = f"# Career Pivot Plan for {user_data.get('name', 'You')}\n\n"

    output += "## 📋 Input Summary\n\n"
    output += f"- **Current Role**: {user_data.get('current_role', '')}\n"
    output += f"- **Skills**: {', '.join(user_data.get('skills', []))}\n"
    output += f"- **Pain Points**: {', '.join(user_data.get('hates', []))}\n"
    output += f"- **Interests**: {', '.join(user_data.get('interests', []))}\n\n"

    output += "## 🔄 Recommendations\n\n"
    output += analysis

    return output

def find_matching_careers(user_skills: List[str], pain_points: List[str], 
                         career_map: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Find career matches based on user skills and pain points."""
    matched_careers = []
    skill_mappings = career_map.get("skill_mappings", {})
    pain_solutions = career_map.get("pain_point_solutions", {})

    # Find careers that match skills
    skill_matches = set()
    for skill in user_skills:
        if skill.lower() in skill_mappings:
            skill_matches.update(skill_mappings[skill.lower()])

    # Find careers that solve pain points
    pain_matches = set()
    for pain in pain_points:
        pain_key = pain.lower().replace(" ", "_")
        if pain_key in pain_solutions:
            pain_matches.update(pain_solutions[pain_key])

    # Combine matches (prioritize careers that appear in both)
    all_matches = skill_matches.union(pain_matches)

    for career_id in all_matches:
        for career in career_map.get("careers", []):
            if career["id"] == career_id:
                matched_careers.append(career)
                break

    # Sort by trend relevance
    matched_careers.sort(key=lambda x: x.get("trend_relevance", 0), reverse=True)

    return matched_careers[:3]  # Return top 3 matches

def estimate_pivot_difficulty(current_role: str, target_career: str, 
                             user_skills: List[str], career_map: Dict[str, Any]) -> Dict[str, Any]:
    """Estimate difficulty and time-to-transition for the pivot."""
    target = None
    for career in career_map.get("careers", []):
        if career["id"] == target_career:
            target = career
            break

    if not target:
        return {"difficulty": "unknown", "estimated_months": None}

    # Simple heuristic: count matching skills
    matches = sum(1 for skill in user_skills 
                  if skill.lower() in str(target.get("friendly_skills", [])).lower())

    total_skills_needed = len(target.get("required_skills", []))
    match_percentage = (matches / total_skills_needed * 100) if total_skills_needed > 0 else 0

    if match_percentage >= 70:
        difficulty = "low"
        months = "1-2"
    elif match_percentage >= 40:
        difficulty = "medium"
        months = "3-6"
    else:
        difficulty = "high"
        months = "6-12"

    return {
        "difficulty": difficulty,
        "estimated_months": months,
        "skill_match_percentage": int(match_percentage),
        "skills_to_develop": [s for s in target.get("required_skills", []) 
                             if s.lower() not in str(user_skills).lower()]
    }

def normalize_input_dict(data: Dict[str, Any]) -> Dict[str, Any]:
    """Normalize user input dictionary for consistent processing."""
    normalized = {}

    # Handle various input formats
    normalized["current_role"] = str(data.get("current_role", "")).strip()
    normalized["name"] = str(data.get("name", "You")).strip()
    normalized["skills"] = parse_skill_input(str(data.get("skills", "")))
    normalized["hates"] = parse_pain_point_input(str(data.get("hates", "")))
    normalized["interests"] = parse_skill_input(str(data.get("interests", "")))
    normalized["constraints"] = str(data.get("constraints", "")).strip()
    normalized["budget"] = str(data.get("budget", "low")).strip().lower()
    normalized["remote_preference"] = str(data.get("remote_preference", "high")).strip().lower()

    return normalized

def create_context_for_llm(user_data: Dict[str, Any], career_map: Dict[str, Any]) -> str:
    """Create enriched context for LLM by including matched careers."""
    context = f"Current Role: {user_data['current_role']}\n"
    context += f"Skills: {', '.join(user_data['skills'])}\n"
    context += f"Pain Points: {', '.join(user_data['hates'])}\n"
    context += f"Interests: {', '.join(user_data['interests'])}\n\n"

    # Add relevant career data
    matched = find_matching_careers(user_data['skills'], user_data['hates'], career_map)
    if matched:
        context += "Potential Career Matches (from database):\n"
        for career in matched:
            context += f"  - {career['title']}: {career['id']}\n"

    return context
