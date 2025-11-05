# VS Code Codex Integration Guide
# Career Pivot Navigator - Developer-Ready Prompts

## Overview
This guide provides layered prompts for VS Code Codex/Copilot to extend or customize the Career Pivot Navigator.

## Layer 1: Architecture & Setup

### Prompt: "Set up LangChain project structure"
```
Create a production-ready LangChain project with:
- Config management (.env for API keys)
- Logging setup
- Error handling
- Type hints throughout
- Unit tests
- CI/CD ready

Focus on:
- FastAPI wrapper for deployment
- Async support
- Rate limiting for LLM calls
- Caching of LLM responses
- Monitor token usage
```

### Prompt: "Add database layer for persistent storage"
```
Extend the Career Pivot Navigator to store:
- User profiles (anonymized)
- Pivot history/iterations
- Completed plans
- Feedback/outcomes

Use SQLAlchemy with:
- PostgreSQL for production
- SQLite for local dev
- Migrations with Alembic
- Data anonymization
```

## Layer 2: LLM Chain Enhancements

### Prompt: "Add memory to track pivot evolution"
```
Implement LangChain memory that:
1. Stores conversation history per user session
2. Allows users to refine recommendations based on feedback
3. Tracks "what worked" vs "what didn't"
4. Builds user profiles over time

Use ConversationBufferMemory or ConversationSummaryMemory.
Show how user can ask: "Wait, I didn't mention I have UX experience..."
and the system re-analyzes with that info.
```

### Prompt: "Create multi-agent workflow"
```
Build a multi-agent system where:
1. Intake Agent: Validates & clarifies user input
2. Analysis Agent: Maps to careers & pain points
3. Plan Agent: Creates 3-step strategy
4. Coach Agent: Provides motivation & mindset work
5. Export Agent: Formats output (MD, PDF, JSON, Notion)

Use LangChain's AgentExecutor to orchestrate.
Each agent should handle its specialty.
Agents can call each other (e.g., Plan Agent asks Coach for encouragement).
```

### Prompt: "Add retrieval-augmented generation (RAG)"
```
Enhance career recommendations by:
1. Indexing real job postings (from Indeed, LinkedIn API)
2. Embedding job descriptions
3. Finding patterns in what skills are actually in demand
4. Recommending based on REAL market data, not just career_map.json

Use LangChain's document loaders + vector store (Pinecone or Chroma).
Update embeddings weekly.
Show trending skills in each career path.
```

## Layer 3: User Experience

### Prompt: "Add interactive conversation mode"
```
Create a multi-turn conversation where:
1. System asks clarifying questions
2. User can push back ("No, I'm not interested in that")
3. System refines recommendations in real-time
4. User can ask "Why?" and system explains reasoning

Use LangChain's ConversationChain.
Implement conversation validation (did we get meaningful input?).
Add a "skip/no/maybe" option after each question.
```

### Prompt: "Build a comparison tool"
```
Let users compare two career paths side-by-side:
- Salary progression
- Work-life balance indicators
- Learning curve
- Income-to-pivot-time ratio
- Freelance viability
- Remote work prevalence

Create a visual comparison (CLI table + Streamlit dashboard).
Include: "Which pivot is best for YOUR constraints?"
```

### Prompt: "Add a "trial pivot" simulation"
```
Let users test a pivot path without committing:
- Generate a mock 30-day "trial plan"
- Suggest 3 free/low-cost experiments
- Identify potential blockers early
- Ask: "Does this feel right?"

If yes: Unlock full 3-step plan.
If no: Suggest alternatives.
Build in reflection questions between steps.
```

## Layer 4: Data & Insights

### Prompt: "Create outcome tracking"
```
Build a system where users can log outcomes:
- "I took the course → here's what I learned"
- "I had 5 informational interviews → insights"
- "I landed a freelance gig → earned $X"

Store anonymized outcomes.
Generate aggregate insights:
- "80% of people who did X succeeded at Y"
- "Average time to first freelance gig: 6 weeks"
- "Top skills for healthtech UX: A, B, C"
```

### Prompt: "Build a community dashboard"
```
Create a (private, opt-in) community view:
- See anonymized pivot stories from others
- Filter by: original role, target role, timeline
- Real timelines: "It took me 4 months"
- What actually worked
- What surprised them

Privacy: Full anonymization, no identifying info.
Make it opt-in to share story.
```

### Prompt: "Add salary negotiation coaching"
```
For each career, add:
- Market rate by location/experience
- Negotiation playbook for career changers
- Common lowball offers (watch out!)
- Counter-offer strategies
- Equity vs salary trade-offs

Pull real data from Levels.fyi, Glassdoor API, PayScale.
Personalize by user location & target company type.
```

## Layer 5: Monetization & Deployment

### Prompt: "Create a FastAPI backend for deployment"
```
Build production API:
- POST /analyze: Submit pivot data, get recommendations
- GET /careers: List available career paths
- POST /plan: Generate 3-step plan
- POST /export: Export in format (md/json/pdf)
- POST /feedback: Log user outcomes

Add:
- Rate limiting (free tier: 2 analyses/day)
- Authentication (OAuth or API keys)
- Usage tracking (for future "pro" tier)
- Error handling & logging
```

### Prompt: "Add Stripe integration for premium features"
```
Implement freemium model:
- Free: 1 analysis, 1 export, basic career map
- Premium ($9/mo): Unlimited analyses, all export formats, RAG job insights, 1:1 coaching option

Use Stripe for:
- Subscription management
- Usage limits
- Invoice generation
- Webhook handling
```

### Prompt: "Create a 1:1 coaching option"
```
Add optional paid coaching:
- 30-min sessions with career strategist
- Personalized advice beyond LLM
- Accountability check-ins
- LinkedIn profile review

Use Calendly API for scheduling.
Stripe for payments.
Store notes in database for continuity.
```

## Layer 6: Accessibility & Equity

### Prompt: "Add accessibility features"
```
Ensure:
- WCAG 2.1 AA compliance
- Alt text for all visuals
- Keyboard navigation (CLI + web)
- Dark mode support
- Adjustable text size
- Screen reader testing
- Multi-language support (start with Spanish)
- PDFs with proper tagging

Add: "Accessibility Statement" page.
```

### Prompt: "Build in equity checks"
```
The system should:
1. Recognize systemic barriers
2. Suggest actionable accommodations
3. Flag when advice assumes privilege
4. Provide resources for marginalized communities

Examples:
- If user mentions disability: suggest EDS-aware companies, hybrid roles
- If user is immigrant: suggest roles that don't require specific credential
- If user is single parent: recommend flexible/remote-first paths
- If user mentions trauma: suggest trauma-informed career coaches
```

### Prompt: "Create industry-specific resources"
```
Build a resource library:
- Healthtech: companies, conferences, newsletters
- EdTech: entry-level roles, startup list, communities
- Nonprofit tech: job boards, funding landscape
- QBIPOC-focused tech: community groups, mentorship

Make it:
- Vetted (no predatory courses)
- Free/low-cost prioritized
- Intersectional
- Updated quarterly
```

## Layer 7: Testing & Validation

### Prompt: "Add comprehensive unit tests"
```
Test:
- Input validation
- Skill/pain mapping logic
- Career matching algorithm
- Export functionality
- LLM prompt consistency

Use pytest.
Mock OpenAI calls (use VCR for recorded responses).
Aim for 80%+ coverage.
```

### Prompt: "Add integration tests"
```
Test full flows:
1. User submits input → system returns valid recommendations
2. User selects career → system generates valid 3-step plan
3. User exports → file is valid markdown/json
4. User refines → system updates based on feedback

Use test fixtures with sample users.
Test error cases (invalid input, API errors, etc.).
```

### Prompt: "Create a user testing guide"
```
Conduct usability testing with:
- Neurodivergent professionals
- Career changers
- Disabled folks
- QBIPOC in tech

Test for:
- Clarity of prompts (jargon check)
- Usefulness of recommendations (did it help?)
- Emotional impact (did it feel validating or dismissive?)
- Accessibility (can they use it?)

Iterate based on feedback.
```

## Layer 8: Scaling & Performance

### Prompt: "Optimize LLM costs"
```
Reduce OpenAI API spend by:
1. Caching repeated recommendations
2. Using prompt templates efficiently
3. Shortening prompts without losing quality
4. Using gpt-3.5-turbo for non-critical tasks
5. Batch processing for bulk analyses

Track: Cost per analysis, token usage per step.
Target: < $1 per analysis.
```

### Prompt: "Add response caching"
```
Cache:
- Career map (static, cache for 24h)
- LLM responses for similar inputs (semantic similarity)
- Exported plans (avoid regenerating same output)

Use Redis for distributed cache.
SQLite for local dev cache.
Implement cache invalidation strategy.
```

### Prompt: "Create analytics dashboard"
```
Track:
- Number of analyses run
- Popular career pivots (top 10)
- Success rate (% who followed through)
- User feedback sentiment
- API latency & error rates
- User retention (7-day, 30-day)

Use: Streamlit for internal dashboard.
Export to: Notion, Google Sheets for stakeholders.
```

## Integration Checklist

- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Set OpenAI API key: `export OPENAI_API_KEY="..."`
- [ ] Run CLI test: `python main.py`
- [ ] Run Streamlit: `python main.py streamlit`
- [ ] Test LLM chains: See analyze.py examples
- [ ] Extend as needed using prompts above

## Recommended Next Steps

**If you have LIMITED time (1-2 weeks):**
1. Add database layer for persistence
2. Implement multi-turn conversation
3. Deploy FastAPI backend

**If you have MEDIUM time (1 month):**
1. Add memory + conversation refinement
2. Implement RAG with real job data
3. Build outcome tracking
4. Launch Stripe integration

**If you have FULL time (ongoing):**
1. Multi-agent workflow
2. Community dashboard
3. 1:1 coaching option
4. Full accessibility audit
5. International expansion

---

**Remember**: Each layer adds value. You don't need everything at once.
Start with what solves the biggest user pain point.
