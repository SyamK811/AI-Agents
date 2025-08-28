import re

def mood_insight(mood):
    # Fallback: detect mood keywords in full sentence if mood not directly one of known types
    if not mood or mood.lower() not in ["happy", "okay", "sad", "low", "anxious"]:
        text = mood.lower()

        if re.search(r"\b(sad|down|depressed|unhappy|gloomy)\b", text):
            mood = "sad"
        elif re.search(r"\blow\b|\banxious\b|\bstressed\b", text):
            mood = "low"
        elif re.search(r"\bhappy\b|\bgood\b|\bcheerful\b", text):
            mood = "happy"
        elif re.search(r"\bokay\b|\bneutral\b", text):
            mood = "okay"
        else:
            mood = "unknown"

    mood = mood.lower()

    if mood in ["sad", "low", "anxious"]:
        return (
            "😔 You're experiencing a low or anxious mood. That’s okay — mental well-being fluctuates. "
            "Try engaging in a calming activity like **deep breathing**, **meditation**, or a walk in nature. "
            "Also, don't hesitate to **talk to a friend or journal your thoughts** — expressing emotions can help lighten the burden."
        )
    elif mood == "okay":
        return (
            "🙂 You're feeling neutral today — emotionally steady. This is a great time to do something light and enjoyable, "
            "like **listening to music**, **reading**, or a **casual stroll** to maintain your mental balance."
        )
    elif mood == "happy":
        return (
            "😄 You're in a good mood! That's fantastic. Take advantage of this energy to engage in something fulfilling — "
            "**connect with loved ones**, **pursue a hobby**, or **spread positivity** around you. Keep doing what nourishes your joy."
        )
    else:
        return (
            "🤔 Mood not clearly recognized. Try selecting from moods like **happy**, **sad**, **okay**, or **anxious** for personalized insights."
        )
