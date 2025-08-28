def recommend_fitness(steps, sleep_hours):
    if steps < 5000:
        return (
            f"🚶‍♂️ You walked only **{steps} steps**, which is below the recommended level.\n\n"
            f"💡 Try to include more movement today: a **20-minute brisk walk** or even some **light stretching** at home.\n"
            f"😴 Also, you got **{sleep_hours} hours of sleep** — remember, better sleep can improve motivation to move!"
        )
    elif steps < 8000:
        return (
            f"👍 You walked **{steps} steps**, which is decent!\n\n"
            f"🏃 Consider adding a **10-minute jog or yoga session** to improve cardiovascular health.\n"
            f"💤 With **{sleep_hours} hours of sleep**, you're in a good range to sustain activity."
        )
    else:
        return (
            f"🎉 Great job! You reached **{steps} steps** — an excellent level of physical activity.\n\n"
            f"🏋️‍♀️ To take it up a notch, consider **30 minutes of resistance training** or a **bike ride** today.\n"
            f"😌 With **{sleep_hours} hours of sleep**, your body is likely recovering well. Keep it up!"
        )
