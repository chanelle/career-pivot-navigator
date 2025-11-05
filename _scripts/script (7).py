
# Create requirements.txt and a README

requirements_content = '''langchain>=0.1.0
langchain-openai>=0.0.5
langchain-core>=0.1.0
python-dotenv>=1.0.0
streamlit>=1.28.0
openai>=1.0.0
pydantic>=2.0.0
'''

with open('requirements.txt', 'w') as f:
    f.write(requirements_content)

readme_content = '''# 🔥 Career Pivot Navigator

**For neurodivergent, marginalized, and burnt-out professionals who know the system is broken—and are building exits.**

## Overview

Career Pivot Navigator is a LangChain-powered tool that helps you identify realistic career pivots based on your skills, pain points, and passions. It goes beyond generic career tests by:

- ✅ **Honoring lived experience**: Recognizes systemic barriers (ableism, racism, sexism, classism)
- ✅ **Anti-hustle-culture**: No "just follow your passion" nonsense
- ✅ **Realistic paths**: Suggests free/low-cost options and incremental steps
- ✅ **Accessibility first**: Built for neurodivergent professionals with different work styles
- ✅ **Concrete plans**: 3-step bridge strategies, not just inspiration

## Quick Start

### Installation

```bash
git clone <repo-url>
cd career_pivot_navigator
pip install -r requirements.txt
```

Set your OpenAI API key:
```bash
export OPENAI_API_KEY="your-key-here"
```

### Run via CLI (Default)

```bash
python main.py
```

This launches an interactive CLI where you answer questions about your role, skills, pain points, and interests.

### Run via Streamlit Web App

```bash
python main.py streamlit
```

Opens a web interface at `localhost:8501`.

## Project Structure

```
career_pivot_navigator/
├── main.py                 # CLI + Streamlit entry point
├── analyze.py              # CareerPivotAnalyzer (LangChain chains)
├── plan_generator.py       # PivotPlanGenerator (detailed plans + exports)
├── prompts.py              # Custom LLM prompt templates
├── utils.py                # Helpers (formatting, file I/O, validation)
├── career_map.json         # Skills-to-career database (8 roles, 12+ skills)
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## How It Works

### 1. **Input**
You provide:
- Current role
- Skills (technical + soft)
- What you hate about your job
- What interests you
- Constraints (budget, time, health, remote preference)

### 2. **Analysis**
The system uses LangChain to:
- Map your skills to in-demand careers
- Identify which roles address your pain points
- Recognize hidden superpowers you didn't realize you had
- Assess transition difficulty & timeline

### 3. **Output**
You get:
- 1-2 recommended career pivots with explanations
- **3-Step Bridge Plan**: Concrete steps to explore/transition
- **Monetization Strategy**: How to earn during the pivot
- **Resume Reframe**: How to position yourself for the new role
- **Mindset Coaching**: Honest pep talk about the journey
- **Export Options**: Save as Markdown, JSON, or Notion-compatible format

## Example Output

```
🔄 Career Pivot: UX Researcher (Healthtech)

Why it fits:
Your de-escalation skills + empathy = gold in user research.
You understand pain—literally and figuratively.

🪜 3-Step Plan:

Step 1: Free UX Crash Course (2-3 weeks, 5hrs/week)
- Take Google UX Design Certificate (free on Coursera)
- Why: Learn the language + basic research methods
- Success: Complete at least 3 modules

Step 2: Portfolio Project (4-6 weeks, 8hrs/week)
- Conduct 3 user interviews about a problem you care about
- Why: Show you can DO research, not just theory
- Success: 3-min video demo of your findings

Step 3: Outreach (ongoing)
- Connect with 3 healthtech researchers on LinkedIn
- Why: Build network + gather intel before applying
- Success: 1 informational interview scheduled

💰 Monetization While Pivoting:
- Freelance user research ($30-50/hr on UserTesting.com)
- Help startups with customer interviews ($500/project)
- Start a Medium blog about UX for health (ad revenue + credibility)

🧠 Truth Time:
This pivot is possible because you already have the hardest part: empathy.
Yes, you'll learn new tools. Yes, there's risk. But staying in CS is the bigger risk.
Start small. One step at a time. You don't need permission—you need a plan.
```

## Customization

### Modify Career Database

Edit `career_map.json` to:
- Add more career paths
- Update salary ranges
- Adjust skill mappings
- Add resources/links

### Customize Prompts

Edit `prompts.py` to change:
- Tone (more formal, more casual, etc.)
- Language (translate to other languages)
- Emphasis (add specific equity considerations)
- Output format

### Extend the Analyzer

The `CareerPivotAnalyzer` class can be extended to:
- Add salary negotiation coaching
- Generate job search strategies
- Create LinkedIn profile recommendations
- Add API integrations (job boards, course platforms)

## Bonus Features (Future)

- [ ] Memory: Track user's pivot evolution across sessions
- [ ] Job board integration: Real listings for matched careers
- [ ] Course aggregation: Find best learning resources by budget
- [ ] Salary data: Real market rates by location/experience
- [ ] Community: Forum where users share pivot stories
- [ ] API: Embed in other apps/platforms

## Philosophy

This tool is built on these core beliefs:

1. **The system is broken.** Not your fault. It's designed to exploit you.
2. **You deserve better.** Work that pays well, treats you with respect, and aligns with your values.
3. **Pivots are normal.** Especially for neurodivergent & marginalized people navigating an ableist, classist, racist system.
4. **Incremental change works.** You don't need massive loans or years off to pivot. Small steps compound.
5. **Your lived experience is an asset.** Not a liability. Reframe it.
6. **Community matters.** You're not alone. Thousands of people are building exits right now.

## Contributing

Found a bug? Have a career to add? Want to translate? Open an issue or PR.

This project is open-source and community-driven.

## License

MIT License (do what you want, credit appreciated)

## Author

Built for neurodivergent, marginalized, and burnt-out professionals by someone who gets it.

---

**Remember**: You don't need permission to pivot. You need a plan. 🔥

'''

with open('README.md', 'w') as f:
    f.write(readme_content)

print("✅ Created requirements.txt and README.md")
print("\n" + "="*70)
print("✅ ALL FILES CREATED SUCCESSFULLY!")
print("="*70)
