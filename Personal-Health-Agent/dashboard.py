import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from utils.preprocess import load_data  # ✅ Your preprocessing function

# Load and preprocess data
df = load_data()
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'])
else:
    st.error("❌ The data must include a 'date' column.")
    st.stop()

# Set Streamlit page layout
st.set_page_config(page_title="Personal Health Dashboard", layout="wide")
st.title("📊 Personal Health Visualization Dashboard")

# Sidebar for date filtering
st.sidebar.header("📅 Filter by Date")
min_date = df["date"].min().date()
max_date = df["date"].max().date()

start_date, end_date = st.sidebar.date_input(
    "Select Date Range:",
    [min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

# Convert to date if not already
if isinstance(start_date, datetime):
    start_date = start_date.date()
if isinstance(end_date, datetime):
    end_date = end_date.date()

# Filter the dataframe
filtered_df = df[(df["date"].dt.date >= start_date) & (df["date"].dt.date <= end_date)]

# Display data table
st.markdown(f"### Showing data from **{start_date}** to **{end_date}**")
st.dataframe(filtered_df.tail(10), use_container_width=True)

# 1. 💤 Sleep Hours Over Time
if "sleep_hours" in filtered_df.columns:
    st.subheader("💤 Sleep Hours Over Time")
    fig1, ax1 = plt.subplots()
    sns.lineplot(data=filtered_df, x="date", y="sleep_hours", marker="o", ax=ax1)
    ax1.axhline(7, color="green", linestyle="--", label="Recommended (7 hrs)")
    ax1.set_ylabel("Hours Slept")
    ax1.set_xlabel("Date")
    ax1.legend()
    st.pyplot(fig1)

# 2. 🚶 Daily Activity vs Steps
if "steps" in filtered_df.columns and "sleep_hours" in filtered_df.columns:
    st.subheader("🚶 Daily Activity vs Steps (Sleep Hours as Color)")
    fig2, ax2 = plt.subplots()
    scatter = ax2.scatter(
        filtered_df["date"],
        filtered_df["steps"],
        c=filtered_df["sleep_hours"],
        cmap="coolwarm",
        s=100,
        edgecolors="black"
    )
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Steps Taken")
    plt.xticks(rotation=45)
    cbar = fig2.colorbar(scatter)
    cbar.set_label("Sleep Hours")
    st.pyplot(fig2)

# 3. 🍽️ Diet Quality Pie Chart
if "diet_quality" in filtered_df.columns:
    st.subheader("🍽️ Diet Quality Distribution")
    diet_counts = filtered_df["diet_quality"].value_counts()
    fig3, ax3 = plt.subplots()
    ax3.pie(diet_counts, labels=diet_counts.index, autopct="%1.1f%%", startangle=90, colors=sns.color_palette("pastel"))
    ax3.axis("equal")
    st.pyplot(fig3)

# 4. ⚠️ Symptom Frequency
if "symptoms" in filtered_df.columns:
    st.subheader("⚠️ Symptom Frequency")
    filtered_symptoms = filtered_df[filtered_df["symptoms"].str.lower() != "none"]
    symptom_counts = filtered_symptoms["symptoms"].value_counts()
    if not symptom_counts.empty:
        fig4, ax4 = plt.subplots()
        sns.barplot(x=symptom_counts.values, y=symptom_counts.index, ax=ax4, palette="Reds_r")
        ax4.set_xlabel("Frequency")
        ax4.set_ylabel("Symptom")
        st.pyplot(fig4)
    else:
        st.info("✅ No symptoms reported in the selected range.")
