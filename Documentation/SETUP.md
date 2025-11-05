# 🚀 Career Pivot Navigator - Setup Guide

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
source venv/bin/activate  # On Windows: venv\Scripts\activate

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
