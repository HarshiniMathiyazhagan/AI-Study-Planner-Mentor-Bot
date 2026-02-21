import streamlit as st
import os
from dotenv import load_dotenv
from google import genai
from streamlit_mermaid import st_mermaid

# ---------------- ENV + GEMINI ----------------
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Study Planner", layout="wide")

st.title("📚 AI Study Planner & Mentor Bot")
st.subheader("Create a personalized study plan using GenAI (Gemini)")

# ---------------- SIDEBAR ----------------
st.sidebar.header("Study Details")

subjects = st.sidebar.text_area(
    "Enter subjects (comma separated)",
    placeholder="Java, SQL, DSA, ML, Aptitude"
)

daily_hours = st.sidebar.slider("Daily study hours", 1, 10, 4)
days = st.sidebar.number_input("Number of days to prepare", 1, 90, 7)

# ---------------- STUDY PLAN ----------------
if st.sidebar.button("Generate Study Plan"):
    if subjects.strip() == "":
        st.warning("Please enter at least one subject.")
    else:
        with st.spinner("AI is creating your personalized study plan..."):
            prompt = f"""
You are an expert study planner for engineering students.

Create a {days}-day study plan for:
{subjects}

Daily study hours: {daily_hours}

Rules:
- Beginner-friendly
- Balanced workload
- Day-wise breakdown
- Include revision slots
"""

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            st.success("✅ Your AI-generated study plan is ready!")
            st.markdown(response.text)

st.divider()

# ---------------- AI MENTOR ----------------
st.header("🤖 AI Mentor – Learn with Text + Diagram")

question = st.text_input("Ask a concept:")

if st.button("Explain with Diagram"):
    if question.strip() == "":
        st.warning("Please enter a concept.")
    else:
        with st.spinner("AI is explaining and generating diagram..."):

            # -------- TEXT EXPLANATION --------
            explanation_prompt = f"""
Explain the concept '{question}' simply for a beginner.
Include a small example.
"""

            explanation = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=explanation_prompt
            )

            st.subheader("📖 Explanation")
            st.markdown(explanation.text)

            # -------- DIAGRAM GENERATION --------
            diagram_prompt = f"""
Generate ONLY valid Mermaid flowchart code.

Strict Rules:
- Start with: flowchart TD
- Maximum 6 nodes
- Use simple node names like A, B, C
- Do NOT include explanation
- Do NOT use markdown
- Do NOT use backticks
- No special characters
- No quotes

Concept: {question}
"""


            diagram_response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=diagram_prompt
            )

            st.subheader("📊 Visual Diagram")

            diagram_code = diagram_response.text.strip()

            # Remove accidental markdown formatting
            diagram_code = diagram_code.replace("```mermaid", "").replace("```", "")

            try:
                st_mermaid(diagram_code)
            except:
                st.warning("Mermaid syntax issue. Showing raw diagram code below.")
                st.code(diagram_code)


st.divider()

# ---------------- MOTIVATION ----------------
st.header("🌟 Daily Motivation")

if st.button("Get Today's Motivation"):
    with st.spinner("Generating motivation..."):
        motivation_prompt = """
Generate a short, powerful motivational message for engineering students preparing for placements.
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=motivation_prompt
        )

        st.success("💡 Motivation for You")
        st.markdown(response.text)

st.divider()

# ---------------- PROGRESS FEEDBACK ----------------
st.header("📊 Daily Progress Feedback")

progress = st.text_area(
    "What did you study today?",
    placeholder="Example: Studied SQL JOINs for 2 hours"
)

if st.button("Get AI Feedback"):
    if progress.strip() == "":
        st.warning("Please enter your study progress.")
    else:
        with st.spinner("AI is analyzing your progress..."):
            feedback_prompt = f"""
You are a supportive AI learning coach.

Based on the student's daily progress:
- Give positive feedback
- Suggest improvements
- Suggest next topic

Student Progress:
{progress}
"""

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=feedback_prompt
            )

            st.success("✅ AI Feedback & Suggestions")
            st.markdown(response.text)
