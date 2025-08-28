import re
from agents.health_insights_agent import generate_daily_plan
from agents.symptom_checker_agent import check_symptom
from agents.diet_agent import recommend_diet
from agents.fitness_agent import recommend_fitness
from agents.mood_agent import mood_insight
from agents.reminder_agent import get_reminders
from llm_utils import call_llm

# Utility: Match whole words only
def keyword_in_text(keywords, text):
    return any(re.search(rf"\b{re.escape(kw)}\b", text) for kw in keywords)

def route_query(user_query, df):
    latest = df.iloc[-1]
    user_query_lower = user_query.lower()

    # Symptom checker
    if keyword_in_text(["symptom", "fatigue", "dizzy", "headache", "nausea", "cough", "fever", "chest pain"], user_query_lower):
        return check_symptom(user_query, latest["symptoms"])

    # Diet agent
    elif keyword_in_text(["diet", "nutrition", "food"], user_query_lower):
        # Check for explicit quality if mentioned in query
        for quality in ["poor", "average", "good"]:
            if re.search(rf"\b{quality}\b", user_query_lower):
                return recommend_diet(quality)
        return recommend_diet(latest["diet_quality"])

    # Fitness agent
    elif keyword_in_text(["fitness", "exercise", "walk", "steps", "activity"], user_query_lower):
        return recommend_fitness(int(latest["steps"]), float(latest["sleep_hours"]))
    

    # Mood insight
    elif keyword_in_text(["mood", "feeling", "emotion"], user_query_lower):
        return mood_insight(latest["mood"])

    # Reminder agent
    elif keyword_in_text(["reminder", "remind", "alert"], user_query_lower):
        reminders = get_reminders(latest)
        return "\n".join(reminders) if reminders else "You're doing great! No reminders today."

    # Daily plan
    elif keyword_in_text(["plan", "suggest", "summary", "advice"], user_query_lower):
        return generate_daily_plan(latest)

    # Fallback to LLM
    else:
        context = f"""Patient Info:
- Sleep Hours: {latest["sleep_hours"]}
- Steps: {latest["steps"]}
- Mood: {latest["mood"]}
- Diet Quality: {latest["diet_quality"]}
- Symptoms: {latest["symptoms"]}"""
        prompt = f"""You are a personal health assistant. Given the following patient data:

{context}

Now answer this user query intelligently and helpfully: "{user_query}"
"""
        return call_llm(prompt)
