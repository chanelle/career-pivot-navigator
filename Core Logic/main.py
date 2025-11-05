"""
Career Pivot Navigator - Main Entry Point
CLI interface and Streamlit app launcher
"""

import sys
import json
import os
from pathlib import Path
from typing import Dict, Any, Optional
from dotenv import load_dotenv
from analyze import CareerPivotAnalyzer
from plan_generator import PivotPlanGenerator
from utils import normalize_input_dict, load_career_map, export_to_markdown

# Load environment variables
load_dotenv()

# Validate OpenAI API key
if not os.getenv("OPENAI_API_KEY"):
    print("\n⚠️  ERROR: OPENAI_API_KEY not found!")
    print("\nPlease set your API key:")
    print("1. Edit the .env file and add your key")
    print("2. Or run: export OPENAI_API_KEY='sk-your-key-here'\n")
    sys.exit(1)


def print_header():
    """Print ASCII art header."""
    header = """
╔═════════════════════════════════════════════════════════════════╗
║                  🔥 CAREER PIVOT NAVIGATOR 🔥                  ║
║                                                                 ║
║  For neurodivergent, marginalized, and burnt-out professionals ║
║  who know the system is broken—and are building exits.         ║
╚═════════════════════════════════════════════════════════════════╝
"""
    print(header)


def get_user_input_cli() -> Dict[str, Any]:
    """Gather user input via CLI."""
    print("\n📋 Let's understand your career situation.\n")

    data = {}

    data["name"] = input("What's your name? (or 'Anonymous'): ").strip() or "You"
    data["current_role"] = input("\nWhat's your current role/job title? ").strip()

    print("\nList your skills (comma-separated):")
    print("Examples: communication, CRM systems, data analysis, design, writing, etc.")
    data["skills"] = input("> ").strip()

    print("\nWhat do you HATE about your current situation? (comma-separated)")
    print("Examples: low pay, angry customers, no creativity, toxic culture, long hours, etc.")
    data["hates"] = input("> ").strip()

    print("\nWhat interests or excites you? (comma-separated)")
    print("Examples: tech, mental health, writing, helping people, building things, etc.")
    data["interests"] = input("> ").strip()

    print("\n⚙️  A few logistics:")
    data["budget"] = input("Budget for transition (low/medium/high): ").strip().lower() or "low"
    data["time_availability"] = input("Hours per week you can dedicate (e.g., '5-10'): ").strip() or "flexible"
    data["constraints"] = input("Any constraints we should know? (disabilities, care responsibilities, etc.): ").strip() or ""
    data["remote_preference"] = input("Remote work preference (high/medium/low): ").strip().lower() or "high"

    return data


def run_analysis_cli():
    """Run full career pivot analysis via CLI."""
    print_header()

    # Get user input
    user_data = get_user_input_cli()

    print("\n\n🚀 Analyzing your pivot opportunities...\n")
    print("=" * 70)

    # Initialize analyzers
    analyzer = CareerPivotAnalyzer()
    plan_gen = PivotPlanGenerator()

    # Run analysis
    analysis_result = analyzer.analyze_pivot(user_data)

    # Display results
    print("\n📊 CAREER PIVOT ANALYSIS\n")
    print(analysis_result["analysis"])

    # Show matched careers
    print("\n\n💼 TOP CAREER MATCHES\n")
    for i, career in enumerate(analysis_result["matched_careers"], 1):
        print(f"{i}. {career['title']}")
        print(f"   Salary: ${career['salary_range'][0]:,} - ${career['salary_range'][1]:,}")
        print(f"   Remote: {'✅ Yes' if career['remote'] else '❌ No'}")
        print(f"   Freelance Viable: {'✅ Yes' if career['freelance_viable'] else '❌ No'}")
        print()

    # Ask which career to deep dive on
    if analysis_result["matched_careers"]:
        print("\n" + "=" * 70)
        choice = input("\nWhich career would you like a detailed plan for? (1-3, or 'all'): ").strip().lower()

        careers_to_plan = []
        if choice == "all":
            careers_to_plan = analysis_result["matched_careers"]
        elif choice.isdigit() and 1 <= int(choice) <= len(analysis_result["matched_careers"]):
            careers_to_plan = [analysis_result["matched_careers"][int(choice) - 1]]

        for target_career in careers_to_plan:
            print(f"\n\n🪜 GENERATING 3-STEP PLAN FOR: {target_career['title'].upper()}\n")
            print("-" * 70)

            # Generate plan
            plan_result = plan_gen.generate_3_step_plan(user_data, target_career)
            print(plan_result["plan_text"])

            # Generate monetization strategy
            print(f"\n\n💰 HOW TO EARN DURING THE PIVOT\n")
            print("-" * 70)
            monetization = plan_gen.generate_monetization_strategy(user_data, target_career)
            print(monetization)

            # Generate mindset coaching
            print(f"\n\n🧠 MINDSET COACHING\n")
            print("-" * 70)
            coaching = plan_gen.generate_mindset_coaching(user_data)
            print(coaching)

        # Export option
        print("\n\n" + "=" * 70)
        export_choice = input("\nExport your plan? (yes/no): ").strip().lower()
        if export_choice in ["yes", "y"]:
            filepath = export_to_markdown(
                user_data, 
                analysis_result["analysis"], 
                plan_result if 'plan_result' in locals() else {}
            )
            print(f"\n✅ Plan exported to: {filepath}")

    print("\n\n" + "=" * 70)
    print("\n🎯 Remember: You don't need permission to pivot. You need a plan.\n")
    print("Good luck out there. You got this. 💪\n")


def run_streamlit_app():
    """Run the Streamlit web interface."""
    try:
        import streamlit as st

        st.set_page_config(
            page_title="Career Pivot Navigator",
            page_icon="🔥",
            layout="wide",
            initial_sidebar_state="expanded"
        )

        st.markdown("""
        # 🔥 Career Pivot Navigator

        For neurodivergent, marginalized, and burnt-out professionals who know the system is broken
        and are building exits.
        """)

        with st.sidebar:
            st.markdown("## 📋 Your Story")

            name = st.text_input("Your name (or stay anonymous)", value="You")
            current_role = st.text_input("Current role/job title")
            skills = st.text_area("Your skills (comma-separated)", height=100)
            hates = st.text_area("What you hate (comma-separated)", height=100)
            interests = st.text_area("What interests you (comma-separated)", height=100)
            constraints = st.text_area("Any constraints? (disabilities, care, etc.)", height=100)
            budget = st.radio("Budget for transition", ["low", "medium", "high"])
            time = st.text_input("Hours per week available", "flexible")
            remote = st.radio("Remote preference", ["high", "medium", "low"])

        if st.button("🚀 Analyze My Pivot", use_container_width=True):

            user_data = {
                "name": name,
                "current_role": current_role,
                "skills": skills,
                "hates": hates,
                "interests": interests,
                "constraints": constraints,
                "budget": budget,
                "time_availability": time,
                "remote_preference": remote
            }

            with st.spinner("Analyzing your pivot opportunities..."):
                analyzer = CareerPivotAnalyzer()
                result = analyzer.analyze_pivot(user_data)

            st.markdown("## 📊 Career Pivot Analysis")
            st.markdown(result["analysis"])

            st.markdown("## 💼 Top Career Matches")
            for i, career in enumerate(result["matched_careers"], 1):
                with st.expander(f"{i}. {career['title']}"):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Salary Range", f"${career['salary_range'][0]:,} - ${career['salary_range'][1]:,}")
                        st.metric("Remote", "✅ Yes" if career["remote"] else "❌ No")
                    with col2:
                        st.metric("Freelance Viable", "✅ Yes" if career["freelance_viable"] else "❌ No")
                        st.metric("Trend Relevance", f"{career.get('trend_relevance', 0) * 100:.0f}%")

                    st.write("**Entry Path:**")
                    for step in career.get("entry_path", []):
                        st.write(f"  → {step}")

            # Generate detailed plan for top match
            if result["matched_careers"]:
                st.markdown("## 🪜 Your 3-Step Pivot Plan")

                plan_gen = PivotPlanGenerator()
                plan = plan_gen.generate_3_step_plan(user_data, result["matched_careers"][0])
                st.markdown(plan["plan_text"])

                # Export options
                st.markdown("### 📥 Export Your Plan")
                export_format = st.radio("Format", ["Markdown", "JSON"], horizontal=True)

                if st.button("Download Plan"):
                    filepath = plan_gen.export_full_plan(
                        user_data,
                        result["analysis"],
                        plan,
                        format=export_format.lower()
                    )
                    st.success(f"Plan saved to: {filepath}")

        st.markdown("---")
        st.markdown(
            "_Career Pivot Navigator: Built for neurodivergent, marginalized, and burnt-out professionals._"
        )

    except ImportError:
        print("Streamlit not installed. Run: pip install streamlit")
        print("Then: streamlit run main.py")


if __name__ == "__main__":

    if len(sys.argv) > 1 and sys.argv[1] == "streamlit":
        run_streamlit_app()
    else:
        # Default: CLI mode
        run_analysis_cli()
