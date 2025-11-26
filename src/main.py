"""
src/main.py
Minimal single-file prototype for AI Saathi.
All agents are implemented as simple functions (rule-based).
"""

import json
import re

def normalize(text):
    return text.strip().lower()

# ---- Agents ----
def teaching_agent(query):
    """Explain concepts simply (Hinglish-friendly)."""
    q = normalize(query)
    # very simple heuristics for demo
    if "photosynthesis" in q or "photosynth" in q:
        return ("Photosynthesis: Plants use sunlight to turn water and carbon dioxide "
                "into food (sugar) and oxygen. Simple: sunlight + water + CO2 -> food + O2.")
    if "pythagoras" in q or "pythagorean" in q:
        return ("Pythagoras theorem: In a right-angled triangle, a² + b² = c² where c is hypotenuse.")
    # fallback
    return ("Yeh concept samajhne ke liye main ek short summary de rahi hoon: "
            "Break the topic into small parts, give one-line definition, then an example.")

def doubt_agent(query):
    """Short direct answers for 'what is', 'define' style questions."""
    q = normalize(query)
    if q.startswith("what is ") or q.startswith("define "):
        # tiny mock knowledge
        if "atom" in q:
            return "Atom: smallest unit of matter, made of protons, neutrons and electrons."
        if "mit" in q:
            return "MIT: Massachusetts Institute of Technology, a top engineering institute."
    # fallback short answer
    return "Short answer: I can give quick definitions — try 'What is X?'"

def learning_path_agent(query):
    """Suggest next topics / short study plan."""
    q = normalize(query)
    if "math" in q or "mathematics" in q:
        return ("Start with fundamentals: (1) Algebra basics, (2) Functions, (3) Trigonometry, "
                "(4) Coordinate geometry, (5) Practice problems daily.")
    if "computer" in q or "programming" in q:
        return ("Begin with: (1) Variables & control flow, (2) Functions, (3) Data structures, "
                "(4) Simple projects e.g., calculator, (5) practice on examples.")
    return ("Study plan: Break topic into 3 steps — basics (10 days), examples (10 days), "
            "practice & small project (10 days).")

def motivation_agent(query):
    """Short motivational messages."""
    return ("Bohot badhiya! Thoda consistency rakho — roz 30 minutes padhai se bahut farq padega. "
            "Tum kar sakti ho! 💪")

def parent_guide_agent(query):
    """Simple tips for parents/guardians in Hindi."""
    return ("Parents ke liye tip: Roz thodi der bachche ke saath padhai schedule discuss karein, "
            "encourage karein aur performance ko praise karein. Practical help > strictness.")

# ---- Router / Intent detection ----
def detect_intent(query):
    """Very simple keyword-based intent detection. Returns agent key."""
    q = normalize(query)
    # priority matching
    if any(k in q for k in ["explain", "explain like", "what is", "define", "meaning of", "describe"]):
        # could be teaching or doubt; choose teaching for 'explain', doubt for 'what is'
        if q.startswith("what is") or q.startswith("define"):
            return "doubt"
        return "teaching"
    if any(k in q for k in ["what next", "study plan", "learn", "next topic", "how to prepare", "syllabus"]):
        return "learning_path"
    if any(k in q for k in ["motivate", "i am demotivated", "need motivation", "confidence", "unable"]):
        return "motivation"
    if any(k in q for k in ["parent", "guardian", "mom", "dad", "parents", "pariksha", "exam at home"]):
        return "parent_guide"
    # fallback: if short question → doubt, else teaching
    if len(q.split()) <= 4:
        return "doubt"
    return "teaching"

def ai_saathi(query):
    """Main entrypoint: routes query to appropriate agent and returns response."""
    intent = detect_intent(query)
    if intent == "teaching":
        return teaching_agent(query)
    if intent == "doubt":
        return doubt_agent(query)
    if intent == "learning_path":
        return learning_path_agent(query)
    if intent == "motivation":
        return motivation_agent(query)
    if intent == "parent_guide":
        return parent_guide_agent(query)
    # default
    return "Sorry, I couldn't understand. Try simple English/Hinglish."

# ---- CLI demo ----
if __name__ == "__main__":
    print("AI Saathi — simple demo. Type 'exit' to quit.")
    while True:
        q = input("\nYou: ").strip()
        if q.lower() in {"exit", "quit"}:
            print("Bye! All the best 😊")
            break
        print("\nAI Saathi:", ai_saathi(q))

