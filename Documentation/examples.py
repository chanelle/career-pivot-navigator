"""
Career Pivot Navigator - Usage Examples
Demonstrates different ways to use the system
"""

from analyze import CareerPivotAnalyzer
from plan_generator import PivotPlanGenerator
from utils import export_to_markdown, find_matching_careers


# Example 1: Full Analysis + Export
def example_full_analysis():
    """Complete flow: analyze -> plan -> export."""

    analyzer = CareerPivotAnalyzer()
    planner = PivotPlanGenerator()

    user_data = {
        "name": "Jamie",
        "current_role": "UX Designer",
        "skills": "design, research, communication, prototyping, figma",
        "hates": "agency chaos, low pay, client meetings, imposter syndrome",
        "interests": "psychology, startup building, product strategy, equity",
        "constraints": "single parent, recovering from burnout",
        "budget": "medium",
        "time_availability": "10-15 hours/week",
        "remote_preference": "high"
    }

    # Step 1: Analyze
    print("\n" + "="*70)
    print("STEP 1: ANALYZING PIVOT OPPORTUNITIES")
    print("="*70)

    result = analyzer.analyze_pivot(user_data)
    print(result["analysis"])

    # Step 2: Show career matches
    print("\n" + "="*70)
    print("STEP 2: TOP CAREER MATCHES")
    print("="*70)

    for i, career in enumerate(result["matched_careers"], 1):
        print(f"\n{i}. {career['title']}")
        print(f"   ID: {career['id']}")
        print(f"   Salary: ${career['salary_range'][0]:,} - ${career['salary_range'][1]:,}")
        print(f"   Remote: {'Yes' if career['remote'] else 'No'}")

    # Step 3: Generate detailed plan
    if result["matched_careers"]:
        career = result["matched_careers"][0]
        print(f"\n" + "="*70)
        print(f"STEP 3: 3-STEP PLAN FOR {career['title'].upper()}")
        print("="*70)

        plan = planner.generate_3_step_plan(user_data, career["id"])
        print(plan["plan_text"])

        # Step 4: Generate monetization strategy
        print(f"\n" + "="*70)
        print("STEP 4: MONETIZATION STRATEGY")
        print("="*70)

        monetization = planner.generate_monetization_strategy(user_data, career)
        print(monetization)

        # Step 5: Export
        filepath = planner.export_full_plan(user_data, result["analysis"], plan, format="markdown")
        print(f"\n✅ Plan exported to: {filepath}")


# Example 2: Skill Extraction Only
def example_skill_extraction():
    """Extract and enhance user's skills."""

    analyzer = CareerPivotAnalyzer()

    user_data = {
        "current_role": "Customer Support Manager",
        "skills": "communication, leadership, problem-solving"
    }

    print("\n" + "="*70)
    print("EXTRACTING & ENHANCING SKILLS")
    print("="*70)

    skills_result = analyzer.extract_skills(user_data)
    print(skills_result["extracted_skills"])


# Example 3: Career Lookup
def example_career_lookup():
    """Lookup specific career details."""

    from utils import load_career_map

    career_map = load_career_map()

    print("\n" + "="*70)
    print("AVAILABLE CAREERS IN DATABASE")
    print("="*70)

    for career in career_map.get("careers", []):
        print(f"\n{career['title']} ({career['id']})")
        print(f"  Salary: ${career['salary_range'][0]:,} - ${career['salary_range'][1]:,}")
        print(f"  Skills needed: {', '.join(career['required_skills'][:3])}...")
        print(f"  Entry path: {' → '.join(career['entry_path'][:2])}...")

    # Show skill mappings
    print("\n" + "-"*70)
    print("SKILL MAPPINGS (which careers value which skills)")
    print("-"*70)

    for skill, careers in list(career_map.get("skill_mappings", {}).items())[:5]:
        print(f"  {skill}: {', '.join(careers)}")


# Example 4: Find Careers by Skills/Pain Points
def example_find_matching_careers():
    """Find careers matching user's skills and pain points."""

    from utils import load_career_map, find_matching_careers

    career_map = load_career_map()

    user_skills = ["communication", "empathy", "research"]
    user_pain_points = ["low_pay", "no_creativity"]

    print("\n" + "="*70)
    print("FINDING CAREERS BY SKILLS & PAIN POINTS")
    print("="*70)

    print(f"\nUser skills: {user_skills}")
    print(f"User pain points: {user_pain_points}")

    matches = find_matching_careers(user_skills, user_pain_points, career_map)

    print(f"\nTop {len(matches)} matches:")
    for i, career in enumerate(matches, 1):
        print(f"  {i}. {career['title']}")


# Example 5: Resume Reframing
def example_resume_reframe():
    """Generate reframed resume bullets."""

    planner = PivotPlanGenerator()

    user_data = {
        "name": "Sam",
        "current_role": "Tech Support Specialist",
        "interests": "product management"
    }

    target_career = {
        "title": "Product Manager",
        "id": "product_strategist"
    }

    accomplishments = [
        "Resolved 95% of customer issues within 24 hours",
        "Trained 5 new team members on troubleshooting",
        "Identified process improvements that reduced ticket volume by 20%"
    ]

    print("\n" + "="*70)
    print("RESUME REFRAMING: Tech Support → Product Manager")
    print("="*70)

    reframed = planner.generate_resume_reframe(user_data, target_career, accomplishments)
    print(reframed)


# Example 6: Mindset Coaching
def example_mindset_coaching():
    """Generate personalized motivation & mindset work."""

    planner = PivotPlanGenerator()

    user_data = {
        "name": "Casey",
        "current_role": "Content Writer",
        "hates": ["client pressure", "feast/famine income", "isolation"]
    }

    fears = [
        "I'm not technical enough for Product Strategy",
        "Career changers are at a disadvantage",
        "I'll never make more money"
    ]

    dreams = [
        "Work with a great team",
        "Have stable income",
        "Build something meaningful",
        "Keep my creativity"
    ]

    print("\n" + "="*70)
    print("MINDSET COACHING")
    print("="*70)

    coaching = planner.generate_mindset_coaching(user_data, fears, dreams)
    print(coaching)


# Example 7: Estimate Pivot Difficulty
def example_estimate_difficulty():
    """Estimate how hard a particular pivot will be."""

    from utils import estimate_pivot_difficulty, load_career_map

    career_map = load_career_map()

    user_data = {
        "current_role": "Customer Service",
        "skills": ["communication", "empathy", "patience"],
    }

    target_career_id = "ux_researcher"

    print("\n" + "="*70)
    print(f"PIVOT DIFFICULTY: Customer Service → UX Researcher")
    print("="*70)

    difficulty = estimate_pivot_difficulty(
        user_data["current_role"],
        target_career_id,
        user_data["skills"],
        career_map
    )

    print(f"\nDifficulty Level: {difficulty['difficulty'].upper()}")
    print(f"Estimated Timeline: {difficulty['estimated_months']} months")
    print(f"Skill Match: {difficulty['skill_match_percentage']}%")
    print(f"\nSkills to develop:")
    for skill in difficulty['skills_to_develop']:
        print(f"  - {skill}")


# Run examples
if __name__ == "__main__":

    # Uncomment the example you want to run

    # example_full_analysis()
    # example_skill_extraction()
    # example_career_lookup()
    # example_find_matching_careers()
    # example_resume_reframe()
    # example_mindset_coaching()
    # example_estimate_difficulty()

    print("""
    Examples available:
    1. example_full_analysis() - Complete analysis + plan + export
    2. example_skill_extraction() - Extract skills from role
    3. example_career_lookup() - Browse available careers
    4. example_find_matching_careers() - Find careers by skills
    5. example_resume_reframe() - Reframe resume bullets
    6. example_mindset_coaching() - Get personalized motivation
    7. example_estimate_difficulty() - Assess pivot difficulty

    Uncomment in __main__ to run!
    """)
