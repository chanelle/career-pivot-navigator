
# First, let's create the complete Career Pivot Navigator project
# We'll generate all necessary files as a comprehensive package

import json
import os

# Create the career_map.json - comprehensive skills-to-career mapping
career_map = {
  "careers": [
    {
      "id": "ux_researcher",
      "title": "UX Researcher (Healthtech/SaaS)",
      "required_skills": ["communication", "empathy", "research", "problem_solving"],
      "friendly_skills": ["de-escalation", "listening", "curiosity", "pattern recognition"],
      "salary_range": [65000, 120000],
      "remote": True,
      "freelance_viable": True,
      "entry_path": ["UX course", "portfolio project", "informational interviews"],
      "good_for_pain": ["low_pay", "no_creativity", "lack_autonomy"],
      "trend_relevance": 0.9,
      "resources": [
        "https://www.nngroup.com/courses/user-research-methods/",
        "https://www.coursera.org/learn/ux-research"
      ]
    },
    {
      "id": "tech_support_specialist",
      "title": "Technical Support Specialist (Remote)",
      "required_skills": ["communication", "troubleshooting", "patience"],
      "friendly_skills": ["empathy", "teaching", "clarity"],
      "salary_range": [45000, 75000],
      "remote": True,
      "freelance_viable": True,
      "entry_path": ["Tech support cert", "help desk basics", "1-2 years exp"],
      "good_for_pain": ["no_creativity", "toxic_environment", "low_pay_partial"],
      "trend_relevance": 0.7,
      "resources": [
        "https://www.comptia.org/certifications/a",
        "https://www.udemy.com/course/comptia-a-core-220-1101"
      ]
    },
    {
      "id": "content_writer",
      "title": "Content Writer / Copywriter (Remote/Freelance)",
      "required_skills": ["communication", "writing", "research"],
      "friendly_skills": ["storytelling", "empathy", "persuasion"],
      "salary_range": [40000, 100000],
      "remote": True,
      "freelance_viable": True,
      "entry_path": ["Build portfolio", "start Medium blog", "pitch 5 publications"],
      "good_for_pain": ["no_creativity", "low_pay", "lack_autonomy"],
      "trend_relevance": 0.85,
      "resources": [
        "https://www.mswl.org/writers-market",
        "https://contently.com/"
      ]
    },
    {
      "id": "customer_success_manager",
      "title": "Customer Success Manager (SaaS)",
      "required_skills": ["communication", "empathy", "problem_solving", "business_acumen"],
      "friendly_skills": ["de-escalation", "relationship_building", "patience"],
      "salary_range": [55000, 95000],
      "remote": True,
      "freelance_viable": False,
      "entry_path": ["Internal transfer", "CSM bootcamp", "6mo ramp time"],
      "good_for_pain": ["low_pay", "lack_autonomy", "no_growth"],
      "trend_relevance": 0.88,
      "resources": [
        "https://www.reforge.com/learn/customer-success",
        "https://www.gainsight.com/university/"
      ]
    },
    {
      "id": "mental_health_advocate",
      "title": "Mental Health Advocate / Peer Support Specialist",
      "required_skills": ["empathy", "communication", "active_listening"],
      "friendly_skills": ["lived_experience", "storytelling", "resilience"],
      "salary_range": [35000, 65000],
      "remote": True,
      "freelance_viable": True,
      "entry_path": ["Certification", "volunteer", "personal story sharing"],
      "good_for_pain": ["burnout", "misalignment", "desire_meaning"],
      "trend_relevance": 0.92,
      "resources": [
        "https://www.naadac.org/",
        "https://www.nami.org/"
      ]
    },
    {
      "id": "product_strategist",
      "title": "Product Strategist / Product Manager",
      "required_skills": ["communication", "data_analysis", "strategic_thinking"],
      "friendly_skills": ["empathy", "storytelling", "systems_thinking"],
      "salary_range": [80000, 150000],
      "remote": True,
      "freelance_viable": True,
      "entry_path": ["PM fundamentals", "case studies", "exec present"],
      "good_for_pain": ["low_pay", "lack_autonomy", "no_growth"],
      "trend_relevance": 0.86,
      "resources": [
        "https://reforge.com/learn/product-strategy",
        "https://www.coursera.org/learn/product-management"
      ]
    },
    {
      "id": "freelance_consultant",
      "title": "Freelance Consultant (Your Niche)",
      "required_skills": ["expertise", "communication", "self_direction"],
      "friendly_skills": ["independence", "autonomy", "thought_leadership"],
      "salary_range": [50000, 200000],
      "remote": True,
      "freelance_viable": True,
      "entry_path": ["Define niche", "build portfolio", "1st 3 clients"],
      "good_for_pain": ["low_pay", "no_autonomy", "toxic_culture"],
      "trend_relevance": 0.89,
      "resources": [
        "https://www.upwork.com/",
        "https://www.toptal.com/"
      ]
    },
    {
      "id": "community_builder",
      "title": "Community Manager / Community Builder",
      "required_skills": ["communication", "empathy", "strategic_thinking"],
      "friendly_skills": ["relationship_building", "storytelling", "authenticity"],
      "salary_range": [45000, 85000],
      "remote": True,
      "freelance_viable": True,
      "entry_path": ["Build community", "share story", "demonstrate impact"],
      "good_for_pain": ["misalignment", "no_meaning", "burnout"],
      "trend_relevance": 0.87,
      "resources": [
        "https://www.commsor.com/",
        "https://www.playbookforcommunity.com/"
      ]
    }
  ],
  "skill_mappings": {
    "communication": ["ux_researcher", "tech_support_specialist", "content_writer", "customer_success_manager", "mental_health_advocate", "product_strategist", "freelance_consultant", "community_builder"],
    "empathy": ["ux_researcher", "customer_success_manager", "mental_health_advocate", "product_strategist", "community_builder"],
    "de-escalation": ["ux_researcher", "customer_success_manager", "mental_health_advocate"],
    "crm_systems": ["customer_success_manager", "product_strategist"],
    "writing": ["content_writer", "product_strategist", "freelance_consultant"],
    "storytelling": ["content_writer", "mental_health_advocate", "community_builder"],
    "research": ["ux_researcher", "product_strategist", "content_writer"],
    "problem_solving": ["ux_researcher", "customer_success_manager", "product_strategist"],
    "data_analysis": ["product_strategist", "ux_researcher"],
    "patience": ["tech_support_specialist", "customer_success_manager", "mental_health_advocate"],
    "listening": ["ux_researcher", "customer_success_manager", "mental_health_advocate"],
    "teaching": ["tech_support_specialist", "community_builder", "mental_health_advocate"]
  },
  "pain_point_solutions": {
    "angry_customers": ["mental_health_advocate", "customer_success_manager", "community_builder"],
    "low_pay": ["freelance_consultant", "product_strategist", "content_writer", "customer_success_manager"],
    "no_creative_work": ["content_writer", "ux_researcher", "product_strategist", "community_builder"],
    "toxic_environment": ["freelance_consultant", "mental_health_advocate", "community_builder"],
    "no_growth": ["product_strategist", "freelance_consultant", "ux_researcher"],
    "lack_autonomy": ["freelance_consultant", "content_writer", "product_strategist"],
    "burnout": ["mental_health_advocate", "freelance_consultant", "community_builder"]
  }
}

# Save career_map.json
with open('career_map.json', 'w') as f:
    json.dump(career_map, f, indent=2)

print("✅ Created career_map.json with 8 career paths and comprehensive skill mappings")
print(f"Total careers: {len(career_map['careers'])}")
print(f"Skill mappings: {len(career_map['skill_mappings'])}")
print(f"Pain point solutions: {len(career_map['pain_point_solutions'])}")
