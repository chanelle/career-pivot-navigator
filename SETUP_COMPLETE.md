# 🎯 Career Pivot Navigator - Setup Complete!

## ✅ What's Done

1. **Python Environment**: Virtual environment created with Python 3.13.7
2. **Dependencies Installed**: All required packages are installed:
   - langchain, langchain-openai, langchain-core
   - python-dotenv
   - streamlit
   - openai
   - pydantic

3. **Environment File**: `.env` file created in project root
4. **Path Fixes**: Updated `utils.py` to correctly locate `career_map.json`
5. **API Key Validation**: Added OpenAI API key check to `main.py`

---

## 🚀 Next Steps - You Need to Do This!

### 1. Add Your OpenAI API Key

Edit the `.env` file in the project root:

```bash
# Open the file
code /Users/chanellehenry/Desktop/career-pivot-nav/.env
```

Replace this line:
```
OPENAI_API_KEY=sk-your-key-here
```

With your actual key:
```
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxx
```

**Where to get your key**: https://platform.openai.com/api-keys

---

## ▶️ How to Run

### Option 1: CLI Mode (Recommended for First Run)

```bash
cd "/Users/chanellehenry/Desktop/career-pivot-nav/Core Logic"
python main.py
```

This will:
- Ask you questions about your career situation
- Analyze your skills and pain points
- Suggest 1-3 career pivots
- Generate a detailed 3-step action plan
- Offer monetization strategies
- Provide mindset coaching
- Export to Markdown

### Option 2: Web Interface (Streamlit)

```bash
cd "/Users/chanellehenry/Desktop/career-pivot-nav/Core Logic"
python main.py streamlit
```

Then open: http://localhost:8501

This gives you:
- Nice web UI with forms
- Instant visualization of results
- Easy export options
- Better for demos

---

## 🧪 Test Your Setup

Run the verification script:

```bash
cd "/Users/chanellehenry/Desktop/career-pivot-nav/Core Logic"
python test_setup.py
```

This checks:
- Python version
- All packages installed
- API key configured
- All files present

---

## 📁 Project Structure

```
career-pivot-nav/
├── .env                          # ← YOUR API KEY GOES HERE
├── .venv/                        # Virtual environment (auto-created)
├── QUICKSTART.md                 # Quick reference guide
│
├── Core Logic/
│   ├── main.py                   # ← RUN THIS FILE
│   ├── analyze.py                # LangChain analysis engine
│   ├── plan_generator.py         # 3-step plan generator
│   ├── prompts.py                # LLM prompt templates
│   ├── utils.py                  # Helper functions
│   └── test_setup.py             # Setup verification
│
├── Data and Infrastructure/
│   ├── career_map.json           # Career database (8 careers)
│   └── requirements.txt          # Python dependencies
│
└── Documentation/
    ├── README.md
    ├── SETUP.md
    ├── CODEX_GUIDE.md
    ├── PROJECT_SUMMARY.md
    ├── examples.py
    └── QUICK_REFERENCE.txt
```

---

## 🎨 Example Usage

### CLI Mode Example:

```
╔═════════════════════════════════════════════════════════════════╗
║                  🔥 CAREER PIVOT NAVIGATOR 🔥                  ║
║                                                                 ║
║  For neurodivergent, marginalized, and burnt-out professionals ║
║  who know the system is broken—and are building exits.         ║
╚═════════════════════════════════════════════════════════════════╝

📋 Let's understand your career situation.

What's your name? (or 'Anonymous'): Alex

What's your current role/job title? Customer Service Rep

List your skills (comma-separated):
Examples: communication, CRM systems, data analysis, design, writing, etc.
> communication, problem-solving, CRM, empathy

What do you HATE about your current situation? (comma-separated)
Examples: low pay, angry customers, no creativity, toxic culture, long hours, etc.
> low pay, angry customers, repetitive work

What interests or excites you? (comma-separated)
Examples: tech, mental health, writing, helping people, building things, etc.
> tech, UX design, psychology

⚙️  A few logistics:
Budget for transition (low/medium/high): low
Hours per week you can dedicate (e.g., '5-10'): 10
Any constraints we should know? (disabilities, care responsibilities, etc.): 
Remote work preference (high/medium/low): high

🚀 Analyzing your pivot opportunities...
```

---

## 💡 What You Can Do with This

1. **Personal Use**: Run it for yourself to explore career pivots
2. **Help Others**: Use it to coach friends/family
3. **Customize**: Edit `career_map.json` to add more careers
4. **Extend**: Use `CODEX_GUIDE.md` to add features with GitHub Copilot
5. **Deploy**: Host on Streamlit Cloud or Render for public access

---

## 🔧 Common Issues & Fixes

### "OPENAI_API_KEY not found"
→ Edit `.env` file and add your actual API key

### "ModuleNotFoundError: No module named 'langchain'"
→ Run: `pip install -r "Data and Infrastructure/requirements.txt"`

### "FileNotFoundError: career_map.json"
→ Make sure you're in the `Core Logic` directory when running

### Streamlit won't start
→ Check if port 8501 is available: `lsof -i :8501`

---

## 🎯 Your Command Cheat Sheet

```bash
# Navigate to project
cd "/Users/chanellehenry/Desktop/career-pivot-nav/Core Logic"

# Test setup
python test_setup.py

# Run CLI mode
python main.py

# Run web interface
python main.py streamlit

# Install dependencies (if needed)
pip install -r "../Data and Infrastructure/requirements.txt"

# Check API key
cat ../.env
```

---

## 📚 Learn More

- **QUICKSTART.md** - Detailed setup guide
- **Documentation/CODEX_GUIDE.md** - How to extend with new features
- **Documentation/examples.py** - Code examples
- **Documentation/PROJECT_SUMMARY.md** - Technical architecture

---

## 🔥 Ready to Launch?

1. ✅ Set your API key in `.env`
2. ✅ Run `python test_setup.py` to verify
3. ✅ Run `python main.py` to start

**You're one API key away from launching!** 🚀
