def check_symptom(user_query, latest_symptoms=None):
    # Define a symptom knowledge base
    symptom_info = {
        "headache": {
            "severity": "mild",
            "cause": "Stress, dehydration, eye strain, or lack of sleep",
            "remedy": "Drink water, rest in a quiet dark room, and consider a mild pain reliever if needed."
        },
        "fatigue": {
            "severity": "mild",
            "cause": "Lack of rest, overexertion, anemia, or poor diet",
            "remedy": "Prioritize sleep, eat energy-rich foods, and stay hydrated."
        },
        "dizzy": {
            "severity": "serious",
            "cause": "Low blood pressure, dehydration, or inner ear issues",
            "remedy": "Sit or lie down, drink water, and consult a doctor if it persists."
        },
        "nausea": {
            "severity": "mild",
            "cause": "Indigestion, anxiety, or food-related issues",
            "remedy": "Sip ginger tea or cold water, and avoid greasy or spicy food."
        },
        "cough": {
            "severity": "mild",
            "cause": "Viral infection, allergy, or throat irritation",
            "remedy": "Stay hydrated, use honey in warm water, or try steam inhalation."
        },
        "fever": {
            "severity": "serious",
            "cause": "Infection (viral or bacterial)",
            "remedy": "Rest, drink fluids, and consider a fever reducer. See a doctor if it crosses 102°F or lasts more than 2 days."
        },
        "chest pain": {
            "severity": "serious",
            "cause": "Possible heart issue, muscle strain, or acid reflux",
            "remedy": "Seek immediate medical help, especially if accompanied by shortness of breath or sweating."
        }
    }

    # Find symptoms mentioned in the user query
    found = [sym for sym in symptom_info if sym in user_query.lower()]

    # Fallback to latest symptoms if user query is vague
    if not found and latest_symptoms:
        fallback_symptoms = latest_symptoms.lower().split(',')
        found = [sym.strip() for sym in fallback_symptoms if sym.strip() in symptom_info]

    # Nothing matched
    if not found:
        return "❓ I couldn't identify any known symptoms. Please describe how you feel using common terms like 'headache' or 'nausea'."

    # Build response
    response = []
    for sym in found:
        info = symptom_info[sym]
        severity_label = "⚠️ *Serious*" if info["severity"] == "serious" else "ℹ️ *Mild*"
        response.append(
            f"**Symptom:** {sym.capitalize()}\n"
            f"{severity_label}\n"
            f"• **Possible Cause:** {info['cause']}\n"
            f"• **Suggested Remedy:** {info['remedy']}\n"
        )

    return "\n".join(response)
