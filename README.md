HireMate AI - AI-Powered Hiring Assistant 🤖
📌 Project Overview
HireMate AI is an AI-powered hiring assistant chatbot designed to streamline the candidate screening process for recruiters and hiring managers. The chatbot interacts with candidates to:
✅ Collect essential candidate details (name, experience, tech stack, etc.)
✅ Generate technical interview questions tailored to the candidate’s tech stack
✅ Maintain a smooth, context-aware conversation
✅ Enhance hiring efficiency using AI-driven insights

This chatbot is built using Streamlit for UI, OpenAI's GPT models for question generation, and Python for backend logic.

📌 Installation Instructions
🔹 Step 1: Clone the Repository

git clone https://github.com/your-username/hiremate-ai.git
cd hiremate-ai

🔹 Step 2: Create and Activate Virtual Environment
For Windows:
python -m venv venv
venv\Scripts\activate

For macOS/Linux:
python3 -m venv venv
source venv/bin/activate

🔹 Step 3: Install Required Dependencies
pip install -r requirements.txt
🔹 Step 4: Set Up OpenAI API Key
Create a .env file in the project root and add:
OPENAI_API_KEY=your_openai_api_key_here
Make sure to replace your_openai_api_key_here with your actual OpenAI API key.

🔹 Step 5: Run the Application
streamlit run app.py
This will launch the chatbot in your browser. 🎉

📌 Usage Guide
Open the App: Once the app starts, you’ll see the HireMate AI Chatbot UI.
Enter Candidate Information:
Provide Full Name, Email, Experience, Desired Position, Tech Stack.
Generate Technical Questions:
Click "Generate Technical Questions" to receive AI-generated questions based on the provided tech stack.
Chat with the AI:
You can interact with the chatbot for follow-up questions and clarification.
End of Interaction:
The chatbot will conclude the conversation and display the next steps.

📌 Technical Details
🔹 Tech Stack
Frontend: Streamlit (for UI)
Backend: Python
AI Model: OpenAI GPT-4 (or GPT-3.5-turbo)
Environment Management: Virtual Environment (venv)
API Calls: OpenAI API (openai.ChatCompletion.create)
Configuration: .env file for API key security

🔹 File Structure
hiremate-ai/
│── images/                    # Folder for storing UI images
│── app.py                      # Streamlit application (UI)
│── question_generator.py        # AI question generation logic
│── .env                         # API Key (hidden from GitHub)
│── requirements.txt             # Required dependencies
│── README.md                    # Documentation

🔹 Dependencies
streamlit – For interactive UI
openai – For generating AI-based technical questions
python-dotenv – To securely store API keys
logging – For debugging and monitoring
time – To simulate real-time responses
To install all dependencies:

pip install -r requirements.txt
📌 Prompt Design
The chatbot generates customized technical questions based on the candidate's tech stack.

🔹 Prompt Logic
Extract Candidate's Tech Stack
Generate a Structured Prompt:

f"Generate 5 technical interview questions for a candidate proficient in {tech_stack}. 
Ensure the questions are relevant, practical, and well-balanced between basic, intermediate, and advanced levels."
Use OpenAI GPT to Generate Responses
Format Output as a Numbered List
🔹 Edge Cases Handled
✅ Empty Tech Stack → Requests valid input
✅ Multiple Technologies → Balances questions across them
✅ Uncommon Tech → Generates related best-practice questions
✅ Experience-Based Questions → Adjusts difficulty level

📌 Challenges & Solutions
🔹 Challenge 1: OpenAI API Deprecation Issues
Problem: openai.ChatCompletion.create() was deprecated in OpenAI v1.0.0+.
Solution: Used client.chat.completions.create() instead.
🔹 Challenge 2: Handling Edge Cases in Inputs
Problem: Candidates might enter vague or incomplete tech stacks.
Solution: Added fallback mechanisms to refine user input.
🔹 Challenge 3: Streamlit UI Enhancements
Problem: Needed a modern and interactive UI.
Solution: Used custom CSS styles and gradient buttons for an engaging user experience.
🔹 Challenge 4: API Rate Limits
Problem: OpenAI API rate limits could cause delays.
Solution: Implemented error handling and retries for API failures.
📌 Future Improvements
✅ Integrate Resume Parsing to auto-extract tech stack
✅ Deploy on Cloud (AWS/GCP) for live demo
✅ Support Multilingual Chatbot
✅ Enhance UI with Advanced Animations

📌 Contributing
We welcome contributions!

Fork the repo 🚀
Create a feature branch
Submit a pull request 🎉
For major changes, please open an issue first.

📌 License
This project is MIT Licensed. Feel free to use and modify it.

📌 Contact
📩 Email: rishavrajbhagat123@gmail.com
🔗 GitHub: https://www.github.com/Rishav123raj

🚀 Thank you for using HireMate AI! Happy Hiring! 🎉

