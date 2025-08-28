
An AI-powered Streamlit app that provides personalized health plans, symptom analysis, mood insights, and reminders using your daily logs and conversation. Built using LangChain Agents + open LLMs.

---

## 💡 Features

- 🩺 Symptom Checker (detects serious issues from natural language)
- 🛌 Sleep analysis and health recommendations
- 🥗 Diet and fitness suggestions based on your logs
- 😌 Mood-based guidance
- 📋 Daily Health Plan Generator
- 🔔 Smart Reminders (e.g., drink water, sleep early)
- 💬 Chat interface powered by LangChain + LLMs
- 📁 Upload CSV logs for smart contextual planning

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) – frontend UI
- [LangChain](https://www.langchain.com/) – LLM agent logic
- Open-source LLMs (e.g., Mistral, Phi, Clinical-BERT via Hugging Face or Ollama)
- Pandas for data handling

Personal Health Agent/
├── app.py
├── llm_utils.py
├── agent_router.py           # <-- route_query() is here
├── data/
│   └── health_data.csv
├── utils/
│   └── preprocess.py
└── agents/
    ├── health_agent.py
    ├── symptom_agent.py