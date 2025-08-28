def recommend_diet(diet_quality):
    # Normalize input
    diet_quality = diet_quality.lower()

    # Responses dictionary
    responses = {
        "poor": (
            "🥴 Your current diet appears poor. This could affect your mood, energy levels, and long-term health.\n\n"
            "👉 Try the following to improve:\n"
            "- Add fresh fruits (bananas, apples, berries)\n"
            "- Include leafy greens and colorful vegetables (spinach, carrots, bell peppers)\n"
            "- Choose lean proteins (lentils, eggs, grilled chicken)\n"
            "- Reduce sugary and fried foods\n"
            "- Drink 6–8 glasses of water daily"
        ),
        "average": (
            "🙂 Your diet is average – some good elements, but room to improve.\n\n"
            "✅ Suggestions:\n"
            "- Switch to whole grains (brown rice, oats)\n"
            "- Replace snacks with nuts or fruits\n"
            "- Cook meals at home more often\n"
            "- Include fermented foods (yogurt, curd, kimchi) for gut health"
        ),
        "good": (
            "🌟 Great job maintaining a good diet! Keep the momentum going.\n\n"
            "💡 Reminders:\n"
            "- Stay hydrated (carry a water bottle)\n"
            "- Don’t skip meals, especially breakfast\n"
            "- Add variety: rotate vegetables, fruits, and grains\n"
            "- Treat yourself occasionally to stay balanced"
        )
    }

    # Fallback
    if diet_quality not in responses:
        return "⚠️ Unable to assess diet quality. Please choose from: poor, average, or good."

    return responses[diet_quality]
