
# Create prompts.py - All LangChain prompt templates

prompts_content = '''"""
Career Pivot Navigator - Prompt Templates
Custom prompts for LangChain analysis and career pivot recommendations
"""

CAREER_PIVOT_SYSTEM_PROMPT = """You are an empathetic, strategic career advisor who specializes in helping neurodivergent, marginalized, and burnt-out professionals identify meaningful career pivots.

Your approach:
- Honor their lived experience and pain points without dismissing them
- Recognize systemic barriers they face (ableism, racism, sexism, classism)
- Suggest REALISTIC paths that don't require "hustle culture" nonsense
- Prioritize autonomy, remote work, and flexibility where possible
- Use warm, direct language—no corporate jargon

You understand that:
- Not everyone can afford to "just take a course"—suggest free/low-cost options
- Neurodivergent people have different communication and work styles
- Safety and stability matter as much as passion
- Small wins and incremental pivots are victories
- Lived experience is a superpower, not a liability
"""

CAREER_PIVOT_ANALYSIS_PROMPT = """
You are analyzing a career pivot opportunity for someone stuck in misalignment.

INPUT:
- Current role: {current_role}
- Current skills: {skills}
- Pain points (what they hate): {hates}
- Interests & passions: {interests}
- Career constraints: {constraints}

YOUR TASK:
1. **Pivot Suggestion**: Recommend 1-2 realistic career paths that leverage their skills and address their pain points.
2. **Why it fits**: Explain how their existing skills transfer (even if they don't realize it).
3. **The honest truth**: What might be hard about this pivot? What barriers should they expect?
4. **3-Step Bridge Plan**: Provide concrete, low-barrier steps to test/explore this path.
5. **Monetization angle**: How could they earn while transitioning? (freelance, side project, internal transfer, etc.)
6. **Empowering insight**: One sentence that validates their struggles and positions them for success.

OUTPUT FORMAT:
Use markdown. Be warm and direct. Use emojis sparingly but meaningfully.
"""

SKILL_EXTRACTION_PROMPT = """
Given this user description of their current role and experience, extract and map their transferable skills.

User input: {user_input}

Extract:
1. **Hard skills** (technical, measurable): What can you do with tools/systems?
2. **Soft skills** (interpersonal, emotional intelligence): What do you do with people?
3. **Hidden gems** (often overlooked superpowers): What unique perspective or lived experience do they bring?

Return as a structured list with 1-2 sentence explanations of why each skill is valuable in a new context.
"""

THREE_STEP_PLAN_PROMPT = """
Create a realistic, low-barrier 3-step plan for {person_name} to explore this career pivot: {target_career}

Constraints to honor:
- Budget: {budget_constraint}
- Time availability: {time_availability}
- Health/disability considerations: {health_notes}
- Remote requirement: {remote_preference}

For each step, provide:
1. Specific action (not vague advice)
2. Time estimate
3. Resources (free/low-cost prioritized)
4. Why this step matters
5. Success metric (how they'll know it worked)

Format as a numbered list. Be tactical and encouraging.
"""

RESUME_REFRAME_PROMPT = """
Help {person_name} reframe their resume for this target role: {target_career}

Their current role: {current_role}
Key accomplishments: {accomplishments}
Target career: {target_career}

Rewrite 3 resume bullet points that:
1. Use language that resonates in the new industry
2. Translate pain-points into demonstrated values (e.g., "managed high-stress customer interactions" → "demonstrated empathy under pressure")
3. Highlight transferable skills they may not have realized were valuable

Format as markdown bullet points with original + reframed versions side-by-side.
"""

OUTREACH_MESSAGE_PROMPT = """
Draft a warm, authentic outreach message for {person_name} to send to someone in their target role.

Context:
- Current role: {current_role}
- Target role: {target_career}
- Reason for the pivot: {pivot_motivation}
- What they want to ask: {conversation_goal}

The message should:
1. Be 3-5 sentences max
2. Be specific and personalized (not generic)
3. Show you've researched the person/company
4. Lead with curiosity, not desperation
5. Make it easy to say yes

Include a version they can personalize.
"""

FREELANCE_LAUNCH_PROMPT = """
Help {person_name} create a freelance positioning statement for: {niche}

Their background: {background}
Skills: {skills}
Ideal client problem: {ideal_client_problem}
Rate expectation: {rate_range}
Constraints: {constraints}

Output:
1. **Positioning statement** (1 sentence): Who you serve + problem you solve
2. **Service offering** (2-3 options): What you actually sell
3. **First client strategy**: How to land your first 3 clients (without being creepy)
4. **Platform recommendations**: Where to list yourself
5. **Sample rate card**: How to price your work

Keep it realistic and anti-hustle-culture.
"""

MINDSET_CHECK_PROMPT = """
Reflect this back to {person_name} as honest but loving feedback:

Their situation: {situation}
Their fears: {fears}
Their dreams: {dreams}

Provide:
1. **Permission slip**: What they need to hear about why this is possible
2. **Reality check**: What's actually true vs. what's their brain lying about
3. **Reframe**: How to think about this pivot that's empowering but realistic
4. **Next micro-action**: One tiny thing they can do TODAY that moves them forward

Keep it warm, direct, and unapologetic about calling out both hope and reality.
"""

# Save as file
with open('prompts.py', 'w') as f:
    f.write(prompts_content)

print("✅ Created prompts.py with 8 specialized prompt templates")
