# 🔥 Career Pivot Navigator - Quick Start Guide

## Prerequisites
- Python 3.8+ installed
- OpenAI API key (get one at https://platform.openai.com/api-keys)

## Setup (3 Steps - 2 minutes)

### Step 1: Install Dependencies
```bash
cd /Users/chanellehenry/Desktop/career-pivot-nav
pip install -r "Data and Infrastructure/requirements.txt"
```

### Step 2: Set Your OpenAI API Key

**Option A: Using .env file (Recommended)**
1. Open the `.env` file in the project root
2. Replace `sk-your-key-here` with your actual OpenAI API key:
   ```
   OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxx
   ```

**Option B: Using Terminal (Temporary)**
```bash
export OPENAI_API_KEY="sk-proj-xxxxxxxxxxxxx"
```

### Step 3: Run the Application

**CLI Mode (Default):**
```bash
cd "Core Logic"
python main.py
```

**Web Interface (Streamlit):**
```bash
cd "Core Logic"
python main.py streamlit
```
Then open your browser to: http://localhost:8501

---

## Usage Examples

### CLI Mode
The CLI will guide you through questions about:
- Current role
- Skills
- Pain points
- Interests
- Constraints
- Budget & time availability

Then it will:
1. Analyze your situation
2. Suggest 1-3 career pivots
3. Generate a 3-step action plan
4. Provide monetization strategies
5. Offer mindset coaching
6. Export to Markdown

### Streamlit Web Mode
- Fill out the sidebar form
- Click "🚀 Analyze My Pivot"
- Get instant recommendations
- Download your personalized plan

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'langchain'"
Run: `pip install -r "Data and Infrastructure/requirements.txt"`

### "OPENAI_API_KEY not found"
1. Check your `.env` file has the correct key
2. Make sure the key starts with `sk-proj-` or `sk-`
3. Try setting it in terminal: `export OPENAI_API_KEY="your-key"`

### "FileNotFoundError: career_map.json"
Make sure you're running from the `Core Logic` directory:
```bash
cd "Core Logic"
python main.py
```

### Import errors with utils/analyze/plan_generator
These files need to be in the same directory. Check that all files are in `Core Logic/`:
- main.py
- analyze.py
- plan_generator.py
- prompts.py
- utils.py

---

## What's Next?

Check out:
- `Documentation/CODEX_GUIDE.md` - Advanced features to add
- `Documentation/examples.py` - Code examples
- `Documentation/PROJECT_SUMMARY.md` - Full technical details

---

## Architecture

```
career-pivot-nav/
├── Core Logic/
│   ├── main.py              # Entry point (CLI or Streamlit)
│   ├── analyze.py           # LangChain career analysis
│   ├── plan_generator.py    # 3-step plan generation
│   ├── prompts.py           # LLM prompt templates
│   └── utils.py             # Helper functions
├── Data and Infrastructure/
│   ├── career_map.json      # Career database
│   └── requirements.txt     # Python dependencies
├── Documentation/
│   ├── README.md
│   ├── SETUP.md
│   └── CODEX_GUIDE.md       # Development guide
└── .env                     # API keys (DO NOT COMMIT)
```

---

## Philosophy

This tool is built for neurodivergent, marginalized, and burnt-out professionals who:
- Know the system is broken
- Need realistic exits, not motivation porn
- Want tactical steps, not vague advice
- Value honesty over toxic positivity

**You don't need permission to pivot. You need a plan.** 🔥

---

## Support

Questions? Issues? Want to contribute?
- Check existing documentation in `Documentation/`
- Reference the setup guide in `Documentation/SETUP.md`
- Use the examples in `Documentation/examples.py`
