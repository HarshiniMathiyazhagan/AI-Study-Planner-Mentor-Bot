# AI-Study-Planner-Mentor-Bot

AI Study Planner & Mentor Bot

An AI-powered learning assistant that generates personalized study plans, explains concepts with structured visual diagrams, provides daily motivation, and analyzes study progress using Generative AI.

Built using Python, Streamlit, and Google Gemini API.

 eatures
🗓 Personalized Study Plan Generator

Generates day-wise study plans based on selected subjects

Customizable according to daily study hours and preparation duration

Balanced workload with revision slots

🤖 AI Mentor – Concept Explanation

Beginner-friendly explanations of technical concepts

Structured breakdown of topics

Automatically generated flowchart diagrams using Mermaid.js for visual learning

🌟 Daily Motivation Generator

AI-generated short and practical motivational messages

Encourages consistency and disciplined preparation

📊 Study Progress Feedback

Accepts daily study input

Provides constructive AI-based feedback

Suggests improvements and next study focus areas

🛠 Tech Stack

Python

Streamlit

Google Gemini API

Mermaid.js

Prompt Engineering

🧠 How It Works

User enters subjects, study hours, and preparation duration.

Structured prompts are sent to the Gemini model.

The AI generates:

Personalized study plans

Concept explanations

Flowchart diagrams

Motivation messages

Study feedback

Streamlit renders the output in a clean and interactive web interface.

📂 Project Structure
AI-Study-Planner/
│
├── app.py
├── .env
├── requirements.txt
└── README.md

🔑 Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/yourusername/AI-Study-Planner.git
cd AI-Study-Planner
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Add API Key

Create a .env file and add:

GEMINI_API_KEY=your_api_key_here
4️⃣ Run the Application
streamlit run app.py
🎯 Use Cases

Engineering students preparing for exams

Placement preparation

Self-paced learners

Concept revision with visual understanding

📌 Future Improvements

User authentication and progress tracking

Export study plans as PDF

UI enhancements and theme customization

Topic-wise performance analytics

👩‍💻 Author

Harshini M
B.Tech – Artificial Intelligence and Machine Learning
