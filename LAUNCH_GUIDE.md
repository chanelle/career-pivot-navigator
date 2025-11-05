# 🎬 Career Pivot Navigator - Step-by-Step Launch Guide

## 📍 You Are Here

Your project is set up at:
```
/Users/chanellehenry/Desktop/career-pivot-nav
```

✅ **What's Already Done:**
- Python virtual environment created
- All dependencies installed (langchain, streamlit, openai, etc.)
- Project structure organized
- Helper scripts created
- Path fixes applied

---

## 🚨 ONE THING YOU MUST DO NOW

### Add Your OpenAI API Key

**Open this file:**
```bash
/Users/chanellehenry/Desktop/career-pivot-nav/.env
```

**Change this line:**
```
OPENAI_API_KEY=sk-your-key-here
```

**To your actual key:**
```
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxx
```

**Get your key here:** https://platform.openai.com/api-keys

---

## 🎮 Three Ways to Launch

### Method 1: Use the Launch Script (Easiest)

```bash
cd /Users/chanellehenry/Desktop/career-pivot-nav
./launch.sh
```

This will:
- Activate the virtual environment
- Check dependencies
- Ask if you want CLI or Web mode
- Launch the app

---

### Method 2: Manual Launch - CLI Mode

```bash
cd "/Users/chanellehenry/Desktop/career-pivot-nav/Core Logic"
python main.py
```

You'll see:
```
╔═════════════════════════════════════════════════════════════════╗
║                  🔥 CAREER PIVOT NAVIGATOR 🔥                  ║
║                                                                 ║
║  For neurodivergent, marginalized, and burnt-out professionals ║
║  who know the system is broken—and are building exits.         ║
╚═════════════════════════════════════════════════════════════════╝

📋 Let's understand your career situation.
```

Then answer the questions and get your personalized career pivot plan!

---

### Method 3: Manual Launch - Web Interface

```bash
cd "/Users/chanellehenry/Desktop/career-pivot-nav/Core Logic"
python main.py streamlit
```

Then open browser to: **http://localhost:8501**

You'll see a beautiful web interface with:
- Sidebar form for your info
- "🚀 Analyze My Pivot" button
- Real-time results
- Download options

---

## 🧪 Test Before Running (Optional)

Verify everything is set up correctly:

```bash
cd "/Users/chanellehenry/Desktop/career-pivot-nav/Core Logic"
python test_setup.py
```

This checks:
- ✅ Python version
- ✅ All packages installed
- ✅ API key configured
- ✅ All files present
- ✅ career_map.json found

---

## 📋 Quick Terminal Commands

Copy-paste these into your terminal:

**Test setup:**
```bash
cd "/Users/chanellehenry/Desktop/career-pivot-nav/Core Logic" && python test_setup.py
```

**Run CLI:**
```bash
cd "/Users/chanellehenry/Desktop/career-pivot-nav/Core Logic" && python main.py
```

**Run Streamlit:**
```bash
cd "/Users/chanellehenry/Desktop/career-pivot-nav/Core Logic" && python main.py streamlit
```

**Edit API key:**
```bash
code /Users/chanellehenry/Desktop/career-pivot-nav/.env
```

---

## 🎯 What Happens When You Run It

### CLI Mode Flow:

1. **Intro Screen** → Shows project title and mission
2. **Input Questions** → Asks about your role, skills, pain points, interests
3. **Analysis** → LangChain analyzes your situation (takes 10-30 seconds)
4. **Career Matches** → Shows 1-3 recommended career pivots
5. **Choose Career** → Select which one to deep-dive
6. **3-Step Plan** → Generates concrete action plan
7. **Monetization** → Shows how to earn during transition
8. **Mindset Coaching** → Provides encouragement (without toxic positivity)
9. **Export** → Saves to Markdown file

### Streamlit Mode Flow:

1. **Web Interface Opens** → Beautiful UI loads at localhost:8501
2. **Fill Form** → Enter your info in the sidebar
3. **Click Button** → "🚀 Analyze My Pivot"
4. **View Results** → See analysis and career matches instantly
5. **Expand Careers** → Click to see details for each match
6. **Get Plan** → See your 3-step plan automatically
7. **Download** → Export in Markdown or JSON format

---

## 💬 Example Input (Use This to Test)

When running CLI mode, try this sample data:

```
Name: Alex
Current role: Customer Service Representative
Skills: communication, CRM systems, problem-solving, empathy, multitasking
Hates: angry customers, low pay, repetitive work, no creativity
Interests: tech, UX design, psychology, helping people
Budget: low
Time availability: 10 hours/week
Constraints: (leave blank or add any real constraints)
Remote preference: high
```

This will generate a full career pivot analysis!

---

## 🔍 Troubleshooting

### Issue: "OPENAI_API_KEY not found"
**Solution:** Edit `.env` file and add your key

### Issue: "ModuleNotFoundError: No module named 'langchain'"
**Solution:** Run:
```bash
cd /Users/chanellehenry/Desktop/career-pivot-nav
pip install -r "Data and Infrastructure/requirements.txt"
```

### Issue: "FileNotFoundError: career_map.json"
**Solution:** Make sure you're in the `Core Logic` directory:
```bash
cd "/Users/chanellehenry/Desktop/career-pivot-nav/Core Logic"
```

### Issue: Streamlit won't start
**Solution:** Check if something is using port 8501:
```bash
lsof -i :8501
```
Kill it and try again, or use a different port:
```bash
streamlit run main.py --server.port 8502
```

---

## 📊 What You'll Get

After running the analysis, you'll receive:

✅ **Career Analysis** - Deep dive into your situation
✅ **1-3 Career Matches** - Realistic pivots based on your skills
✅ **Salary Ranges** - Know what you can earn
✅ **Remote Options** - Which careers support remote work
✅ **3-Step Action Plan** - Concrete steps with timelines
✅ **Free Resources** - Courses, communities, tools
✅ **Monetization Strategy** - How to earn during transition
✅ **Mindset Coaching** - Honest encouragement
✅ **Exported Plan** - Markdown file you can share/edit

---

## 🎨 Customization Options

### Add More Careers
Edit: `Data and Infrastructure/career_map.json`

### Change LLM Prompts
Edit: `Core Logic/prompts.py`

### Adjust Analysis Logic
Edit: `Core Logic/analyze.py`

### Modify UI
Edit: `Core Logic/main.py` (search for "streamlit")

---

## 🚀 Ready to Launch Checklist

- [ ] I've added my OpenAI API key to `.env`
- [ ] I've run `test_setup.py` and all checks passed
- [ ] I'm in the right directory (`Core Logic/`)
- [ ] I know which mode I want (CLI or Streamlit)

**Once all checked, run:**
```bash
python main.py
```

or

```bash
./launch.sh
```

---

## 🎓 Next Steps After Running

1. **Try it yourself** - Run your own career analysis
2. **Customize** - Add careers that match your interests
3. **Share** - Help friends/family find their pivots
4. **Extend** - Use CODEX_GUIDE.md to add features
5. **Deploy** - Host on Streamlit Cloud for public access

---

## 📚 Documentation Files

- **SETUP_COMPLETE.md** ← You are here
- **QUICKSTART.md** - Quick reference guide
- **Documentation/CODEX_GUIDE.md** - Advanced features guide
- **Documentation/examples.py** - Code examples
- **Documentation/PROJECT_SUMMARY.md** - Technical details

---

## 💪 You're Ready!

Everything is set up. Just:
1. Add your API key to `.env`
2. Run `python main.py`
3. Answer the questions
4. Get your personalized career pivot plan

**The system is broken. You're building exits. Let's go.** 🔥
