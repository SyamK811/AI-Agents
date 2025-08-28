def generate_daily_plan(latest):
    plan = []

    # Sleep advice
    sleep_hours = float(latest.get('sleep_hours', 0))
    if sleep_hours < 7:
        plan.append(
            f"😴 You only slept for **{sleep_hours} hours**, which is below the optimal 7–9 hours. "
            "Aim for an earlier bedtime tonight to support recovery, focus, and mood regulation."
        )
    else:
        plan.append(
            f"✅ You slept for **{sleep_hours} hours** — that's great! Keep maintaining a regular sleep schedule."
        )

    # Diet advice
    diet_quality = latest.get('diet_quality', '').lower()
    if diet_quality == 'poor':
        plan.append(
            "🥗 Your diet could use improvement. Try incorporating more **fiber-rich vegetables**, "
            "**lean protein**, and **whole grains** today. Avoid sugary snacks and hydrate well."
        )
    elif diet_quality == 'average':
        plan.append(
            "🍱 Your diet is on the right track. Consider swapping refined carbs with whole grains "
            "and include **healthy fats** like nuts or olive oil to improve overall quality."
        )
    elif diet_quality == 'good':
        plan.append(
            "✅ Your diet quality is good! Keep it balanced by including **colorful veggies**, "
            "**complex carbs**, and staying hydrated."
        )

    # Activity advice
    steps = int(latest.get('steps', 0))
    if steps < 5000:
        plan.append(
            f"🚶 You've logged only **{steps} steps** today. Aim for at least **7,000 steps** — "
            "even short walks after meals or indoor activities count!"
        )
    elif steps < 8000:
        plan.append(
            f"🏃‍♂️ You've walked **{steps} steps**, a decent start. Try to reach **8,000+** "
            "by adding a brisk evening walk or light home workout."
        )
    else:
        plan.append(
            f"🎉 Great job on completing **{steps} steps**! Maintain this momentum and consider "
            "a **strength or flexibility session** to balance your activity."
        )

    # Mood advice
    mood = latest.get('mood', '').lower()
    if mood in ['sad', 'down', 'low']:
        plan.append(
            "🧘 You reported feeling **low**. Try practicing **deep breathing**, a short nature walk, "
            "or journaling your thoughts. Talking to a friend can also help uplift your mood."
        )
    elif mood in ['happy', 'content']:
        plan.append(
            "😊 Glad to hear you're feeling good! Use this energy to take on a productive task or share positivity."
        )

    return "\n\n".join(plan) if plan else "✅ You're doing great overall! Stay consistent and keep prioritizing your health. 💪"
