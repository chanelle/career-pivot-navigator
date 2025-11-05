
# Create SETUP.md - Quick start guide

setup_content = '''# 🚀 Career Pivot Navigator - Setup Guide

## Prerequisites

- Python 3.10+
- OpenAI API key (free tier available: https://platform.openai.com/api-keys)
- pip (comes with Python)

## 5-Minute Setup

### 1. Clone & Install

```bash
# Clone the repo
git clone <repo-url>
cd career_pivot_navigator

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Add Your OpenAI API Key

Create a `.env` file in the project root:

```bash
touch .env  # On Windows: type nul > .env
```

Edit `.env` and add:
```
OPENAI_API_KEY=sk-your-actual-key-here
```

**Where to find your key:**
1. Go to https://platform.openai.com/api-keys
2. Click "Create new secret key"
3. Copy and paste into `.env`

### 3. Run the CLI (Easiest to Start)

```bash
python main.py
```

Follow the interactive prompts. Answer ~10 questions and get your pivot analysis.

### 4. (Optional) Run the Web App

```bash
python main.py streamlit
```

Opens at `http://localhost:8501`

## Troubleshooting

### "ModuleNotFoundError: No module named 'langchain'"
```bash
pip install -r requirements.txt
```

### "OpenAI API key not found"
Check your `.env` file:
- File exists in project root? 
- Correct format: `OPENAI_API_KEY=sk-...`?
- Real key (not placeholder)?

### "Connection timeout"
- Check internet connection
- OpenAI API status: https://status.openai.com/

### "Streamlit not found"
```bash
pip install streamlit
```

## Usage Examples

### Example 1: CLI Mode (Recommended for First Time)

```bash
$ python main.py

╔═════════════════════════════════════════════════════════════════╗
║                  🔥 CAREER PIVOT NAVIGATOR 🔥                  ║
║                                                                 ║
║  For neurodivergent, marginalized, and burnt-out professionals ║
║  who know the system is broken—and are building exits.         ║
╚═════════════════════════════════════════════════════════════════╝

📋 Let's understand your career situation.

What's your name? (or 'Anonymous'): Alex
Current role/job title?: Customer Service Rep

List your skills (comma-separated):
> communication, CRM, de-escalation, empathy, multitasking

What do you HATE about your current situation? (comma-separated)
> angry customers, low pay, no creative work, repetitive tasks

What interests or excites you? (comma-separated)
> tech, mental health, writing, psychology

⚙️  A few logistics:
Budget for transition (low/medium/high): low
Hours per week you can dedicate: 5-10
Any constraints?: chronic pain, ADHD, anxiety
Remote work preference: high

🚀 Analyzing your pivot opportunities...

[System generates analysis...]
```

### Example 2: Programmatic Use (in your own code)

```python
from analyze import CareerPivotAnalyzer
from plan_generator import PivotPlanGenerator

# Initialize
analyzer = CareerPivotAnalyzer()
planner = PivotPlanGenerator()

# Run analysis
user_data = {
    "name": "Alex",
    "current_role": "Customer Service Rep",
    "skills": "communication, CRM, empathy",
    "hates": "angry customers, low pay",
    "interests": "tech, mental health, writing",
    "constraints": "low budget, chronic pain"
}

result = analyzer.analyze_pivot(user_data)
print(result["analysis"])

# Generate detailed plan
if result["matched_careers"]:
    career = result["matched_careers"][0]
    plan = planner.generate_3_step_plan(user_data, career)
    print(plan["plan_text"])
    
    # Export
    filepath = planner.export_full_plan(user_data, result["analysis"], plan)
    print(f"Saved to: {filepath}")
```

### Example 3: API Mode (FastAPI - in development)

```python
from fastapi import FastAPI
from analyze import CareerPivotAnalyzer

app = FastAPI()
analyzer = CareerPivotAnalyzer()

@app.post("/analyze")
async def analyze_pivot(user_data: dict):
    result = analyzer.analyze_pivot(user_data)
    return result

# Run with: uvicorn api:app --reload
```

## Customization

### Add New Careers

Edit `career_map.json`:

```json
{
  "careers": [
    {
      "id": "your_career_id",
      "title": "Career Title",
      "required_skills": ["skill1", "skill2"],
      "salary_range": [50000, 100000],
      "remote": true,
      "freelance_viable": true,
      "entry_path": ["Step 1", "Step 2"],
      "resources": ["https://resource1.com"]
    }
  ]
}
```

### Customize Prompts

Edit `prompts.py` to change tone/focus:

```python
CAREER_PIVOT_ANALYSIS_PROMPT = """
Your custom prompt here...
"""
```

### Extend the Analyzer

```python
from analyze import CareerPivotAnalyzer

class MyCustomAnalyzer(CareerPivotAnalyzer):
    def my_new_method(self):
        # Add your logic here
        pass
```

## Advanced: Deployment

### Deploy to Heroku

```bash
# Create Procfile
echo "web: streamlit run main.py streamlit" > Procfile

# Deploy
heroku create your-app-name
heroku config:set OPENAI_API_KEY=sk-...
git push heroku main
```

### Deploy FastAPI Backend

```bash
# Install
pip install fastapi uvicorn

# Create api.py (see example above)

# Run
uvicorn api:app --host 0.0.0.0 --port 8000

# Deploy to Railway/Render/AWS
```

## Next Steps

1. **Run it**: `python main.py`
2. **Get recommendations**: Answer questions
3. **Export your plan**: Save as markdown
4. **Share feedback**: Tell us what helped!
5. **Customize**: Add your own careers/prompts
6. **Extend**: Use CODEX_GUIDE.md for advanced features

## Resources

- **LangChain Docs**: https://python.langchain.com/
- **OpenAI API**: https://platform.openai.com/docs/
- **Streamlit Docs**: https://docs.streamlit.io/
- **Career Resources**: See career_map.json for links

## Get Help

- Check TROUBLESHOOTING section above
- Read the README.md for full docs
- Review example outputs in this guide
- Look at code comments in each .py file

---

**You've got this! 🔥**

Questions? Check the README or reach out to the community.
'''

with open('SETUP.md', 'w') as f:
    f.write(setup_content)

# Create an examples.py file with usage patterns

examples_content = '''"""
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
    print("\\n" + "="*70)
    print("STEP 1: ANALYZING PIVOT OPPORTUNITIES")
    print("="*70)
    
    result = analyzer.analyze_pivot(user_data)
    print(result["analysis"])
    
    # Step 2: Show career matches
    print("\\n" + "="*70)
    print("STEP 2: TOP CAREER MATCHES")
    print("="*70)
    
    for i, career in enumerate(result["matched_careers"], 1):
        print(f"\\n{i}. {career['title']}")
        print(f"   ID: {career['id']}")
        print(f"   Salary: ${career['salary_range'][0]:,} - ${career['salary_range'][1]:,}")
        print(f"   Remote: {'Yes' if career['remote'] else 'No'}")
    
    # Step 3: Generate detailed plan
    if result["matched_careers"]:
        career = result["matched_careers"][0]
        print(f"\\n" + "="*70)
        print(f"STEP 3: 3-STEP PLAN FOR {career['title'].upper()}")
        print("="*70)
        
        plan = planner.generate_3_step_plan(user_data, career["id"])
        print(plan["plan_text"])
        
        # Step 4: Generate monetization strategy
        print(f"\\n" + "="*70)
        print("STEP 4: MONETIZATION STRATEGY")
        print("="*70)
        
        monetization = planner.generate_monetization_strategy(user_data, career)
        print(monetization)
        
        # Step 5: Export
        filepath = planner.export_full_plan(user_data, result["analysis"], plan, format="markdown")
        print(f"\\n✅ Plan exported to: {filepath}")


# Example 2: Skill Extraction Only
def example_skill_extraction():
    """Extract and enhance user's skills."""
    
    analyzer = CareerPivotAnalyzer()
    
    user_data = {
        "current_role": "Customer Support Manager",
        "skills": "communication, leadership, problem-solving"
    }
    
    print("\\n" + "="*70)
    print("EXTRACTING & ENHANCING SKILLS")
    print("="*70)
    
    skills_result = analyzer.extract_skills(user_data)
    print(skills_result["extracted_skills"])


# Example 3: Career Lookup
def example_career_lookup():
    """Lookup specific career details."""
    
    from utils import load_career_map
    
    career_map = load_career_map()
    
    print("\\n" + "="*70)
    print("AVAILABLE CAREERS IN DATABASE")
    print("="*70)
    
    for career in career_map.get("careers", []):
        print(f"\\n{career['title']} ({career['id']})")
        print(f"  Salary: ${career['salary_range'][0]:,} - ${career['salary_range'][1]:,}")
        print(f"  Skills needed: {', '.join(career['required_skills'][:3])}...")
        print(f"  Entry path: {' → '.join(career['entry_path'][:2])}...")
    
    # Show skill mappings
    print("\\n" + "-"*70)
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
    
    print("\\n" + "="*70)
    print("FINDING CAREERS BY SKILLS & PAIN POINTS")
    print("="*70)
    
    print(f"\\nUser skills: {user_skills}")
    print(f"User pain points: {user_pain_points}")
    
    matches = find_matching_careers(user_skills, user_pain_points, career_map)
    
    print(f"\\nTop {len(matches)} matches:")
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
    
    print("\\n" + "="*70)
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
    
    print("\\n" + "="*70)
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
    
    print("\\n" + "="*70)
    print(f"PIVOT DIFFICULTY: Customer Service → UX Researcher")
    print("="*70)
    
    difficulty = estimate_pivot_difficulty(
        user_data["current_role"],
        target_career_id,
        user_data["skills"],
        career_map
    )
    
    print(f"\\nDifficulty Level: {difficulty['difficulty'].upper()}")
    print(f"Estimated Timeline: {difficulty['estimated_months']} months")
    print(f"Skill Match: {difficulty['skill_match_percentage']}%")
    print(f"\\nSkills to develop:")
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
'''

with open('examples.py', 'w') as f:
    f.write(examples_content)

print("✅ Created SETUP.md and examples.py")
print("\n" + "="*70)
print("PROJECT COMPLETE! 🔥")
print("="*70)
