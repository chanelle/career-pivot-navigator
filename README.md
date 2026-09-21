# 🔥 Career Pivot Navigator

> **For neurodivergent, marginalized, and burnt-out professionals who know the system is broken—and are building exits.**

AI-powered career pivot analysis using LangChain and GPT-4. Get realistic career recommendations, concrete action plans, and monetization strategies based on your skills, pain points, and interests.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/LangChain-🦜-green.svg)](https://github.com/langchain-ai/langchain)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-orange.svg)](https://openai.com/)

---

## 🎯 What It Does

Career Pivot Navigator helps people escape misaligned jobs by:
- 🧠 Analyzing your skills, pain points, and interests using AI
- 💼 Matching you to 1-3 realistic career pivots (with salary ranges)
- 🪜 Generating concrete 3-step action plans with timelines
- 💰 Providing monetization strategies for transitioning
- 📥 Exporting personalized plans in Markdown/JSON

**Philosophy**: Realistic exits over toxic positivity. Tactical steps over vague inspiration.

---

## ✨ Features

- **AI-Powered Analysis**: LangChain + GPT-4 for intelligent career mapping
- **8 Career Paths**: UX Researcher, Product Strategist, Content Writer, Data Analyst, and more
- **3-Step Action Plans**: Concrete, low-barrier steps with free/low-cost resources
- **Dual Interface**: CLI for quick use, Streamlit web app for demos
- **Export Options**: Save plans as Markdown or JSON
- **Neurodivergent-Affirming**: Recognizes different work styles as strengths
- **Accessibility-First**: Designed for disabilities and constraints

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- OpenAI API key ([get one here](https://platform.openai.com/api-keys))

### Installation

```bash
# Clone the repository
git clone https://github.com/chanelle/career-pivot-navigator.git
cd career-pivot-navigator

# Install dependencies
pip install -r "Data and Infrastructure/requirements.txt"

# Set up your API key
cp .env.example .env
# Edit .env and add your OpenAI API key
```

### Run

**CLI Mode:**
```bash
cd "Core Logic"
python main.py
```

**Web Interface:**
```bash
cd "Core Logic"
python main.py streamlit
```
Then open: http://localhost:8501

---

## 📖 Usage Example

### CLI Flow
```
What's your current role? Customer Service Representative
Skills: communication, CRM, problem-solving, empathy
What you hate: angry customers, low pay, repetitive work
Interests: tech, UX design, psychology

🚀 Analyzing your pivot opportunities...

💼 TOP CAREER MATCHES
1. UX Researcher for Tech Companies
   Salary: $70,000 - $120,000
   Remote: ✅ Yes
   
🪜 YOUR 3-STEP PIVOT PLAN
Step 1: Take free UX fundamentals course (Google UX Certificate)
Step 2: Conduct 3 practice user interviews with friends
Step 3: Build portfolio case study from customer service insights
```

---

## 🏗️ Project Structure

```
career-pivot-nav/
├── Core Logic/
│   ├── main.py              # Entry point (CLI + Streamlit)
│   ├── analyze.py           # LangChain career analysis
│   ├── plan_generator.py    # 3-step plan generation
│   ├── prompts.py           # LLM prompt templates
│   └── utils.py             # Helper functions
├── Data and Infrastructure/
│   ├── career_map.json      # Career database (8 careers)
│   └── requirements.txt     # Python dependencies
└── Documentation/
    ├── CODEX_GUIDE.md       # Development guide
    ├── examples.py          # Usage examples
    └── PROJECT_SUMMARY.md   # Technical details
```

---

## 🛠️ Tech Stack

- **LangChain**: AI orchestration and prompt management
- **OpenAI GPT-4o**: Career analysis and plan generation
- **Streamlit**: Web interface
- **Python 3.8+**: Core language
- **Pydantic**: Data validation

---

## 🎨 Customization

### Add New Careers
Edit `Data and Infrastructure/career_map.json`:
```json
{
  "id": "new_career",
  "title": "Your Career Title",
  "skills_required": ["skill1", "skill2"],
  "salary_range": [60000, 100000],
  "remote": true,
  "freelance_viable": true
}
```

### Modify Prompts
Edit `Core Logic/prompts.py` to adjust AI tone and output format.

### Change LLM Settings
Edit `.env`:
```
MODEL_NAME=gpt-4o
TEMPERATURE=0.7
```

---

## 📚 Documentation

- **[QUICKSTART.md](QUICKSTART.md)** - Quick reference guide
- **[LAUNCH_GUIDE.md](LAUNCH_GUIDE.md)** - Step-by-step launch instructions
- **[Documentation/CODEX_GUIDE.md](Documentation/CODEX_GUIDE.md)** - Advanced features & GitHub Copilot workflow
- **[Documentation/PROJECT_SUMMARY.md](Documentation/PROJECT_SUMMARY.md)** - Full technical summary

---

## 🤝 Contributing

This project welcomes contributions! Some ideas:
- Add more career paths to `career_map.json`
- Improve prompt templates
- Add new analysis features
- Enhance the Streamlit UI
- Add tests

See [CODEX_GUIDE.md](Documentation/CODEX_GUIDE.md) for development workflow with GitHub Copilot.

---

## 🔐 Security Note

**Never commit your `.env` file!** The `.gitignore` protects your API key, but always verify before pushing:
```bash
git status  # Make sure .env is not listed
```

---

## 📄 License

MIT License - feel free to use this for personal or commercial projects.

---

## 🌟 Why This Exists

This tool was built for people who:
- Know the system is broken
- Have disabilities, neurodiversity, or marginalization
- Are tired of toxic "hustle culture" advice
- Want realistic exits, not motivation porn
- Value honesty over inspiration

**You don't need permission to pivot. You need a plan.** 🔥

---

## 🙏 Acknowledgments

Built with LangChain, OpenAI, and a deep understanding that career advice should be tactical, not inspirational.

---

## 📧 Contact

Questions? Issues? Want to share your pivot story?
- Open an issue
- Check existing documentation
- Use GitHub Discussions

---

**Built by someone who gets it. For people who need real exits.** 💪
