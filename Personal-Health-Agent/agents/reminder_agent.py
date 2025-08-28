def get_reminders(row):
    reminders = []

    # 🚨 Critical: Symptom monitoring
    if row["symptoms"].lower() not in ["none", "no", ""]:
        reminders.append(
            "🚨 **Health Alert:** You've reported a symptom ('{}'). Monitor it closely. "
            "If it worsens or lasts beyond a day, please consult a healthcare professional.".format(row["symptoms"])
        )

    # ⚠️ Sleep hygiene
    if float(row["sleep_hours"]) < 6.5:
        reminders.append(
            "💤 You’ve had less than 6.5 hours of sleep. Try aiming for **7–8 hours** tonight to support recovery and focus."
        )

    # ⚠️ Diet quality
    if row["diet_quality"].lower() == "poor":
        reminders.append(
            "🍽️ Your diet was marked as **poor**. Consider adding more whole foods like **fruits, veggies, and lean proteins** today."
        )

    # ✅ If no major issues
    if not reminders:
        reminders.append("✅ All looks good! Keep maintaining healthy habits today.")

    return reminders
