import openai
import os
import logging
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

# Configure logging
logging.basicConfig(
    filename="question_generator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Validate API Key
if not API_KEY:
    logging.error("⚠ API Key not found! Ensure you have a valid OpenAI API key in the .env file.")
    raise ValueError("API Key not found! Please set OPENAI_API_KEY in the .env file.")

# Initialize OpenAI client (Correct way in v1.0.0+)
client = openai.OpenAI(api_key=API_KEY)

def generate_questions(experience, tech_stack, num_questions=5, model="gpt-3.5-turbo"):
    """
    Creates a comprehensive prompt to generate technical interview questions.

    Parameters:
        tech_stack (str): Comma-separated list of technologies (e.g., "Python, Django, AWS").
        num_questions (int): Number of technical questions to generate.
        experience_level (str): Candidate experience level (Beginner, Intermediate, Advanced).

    Returns:
        str: Optimized prompt for OpenAI GPT.
    """
    
    prompt = f"""
    You are an expert technical interviewer tasked with evaluating a candidate's proficiency.
    The candidate has stated they are proficient in the following technologies: {tech_stack}.
    
    Please generate {num_questions} technical interview questions that:
    
    - Are **relevant** to the specified technologies.
    - Include a **mix of basic, intermediate, and advanced** difficulty levels based on the candidate's experience level ({experience}).
    - **Avoid generic trivia** (e.g., "Who created Python?") and instead focus on **practical coding, problem-solving, and best practices**.
    - If the candidate listed multiple technologies, distribute the questions evenly.
    - If an uncommon or vague technology is mentioned, generate **general best-practice or problem-solving** questions related to that domain.
    - Ensure questions are concise, clear, and test real-world application knowledge.
    
    Example:
    - If "Python, Django, AWS" is provided, generate questions like:
      1. "Explain how Django handles database migrations. Provide a code example."
      2. "What is the difference between EC2 and Lambda in AWS? When would you use each?"
      3. "Optimize the following Python function for performance: [Code Example]"
    
    Please format the output as a numbered list, with each question on a new line.
    """

    try:
        # Correct OpenAI API call for v1.0.0+
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500  # Ensures response is within token limit
        )

        # Extract questions
        questions_text = response.choices[0].message.content.strip()
        questions = questions_text.split("\n")

        logging.info(f"✅ Successfully generated {num_questions} questions for: {tech_stack}")
        return questions

    except openai.OpenAIError as e:  # Corrected exception handling
        logging.error(f"❌ OpenAI API Error: {str(e)}")
        return [f"⚠ Error: Unable to generate questions due to API error ({str(e)})."]

    except Exception as e:
        logging.error(f"❌ General Error: {str(e)}")
        return [f"⚠ Error: Unexpected issue occurred - {str(e)}."]

# Example usage for testing
if __name__ == "__main__":
    sample_questions = generate_questions("Python, Django, AWS")
    for i, q in enumerate(sample_questions, 1):
        print(f"{i}. {q}")
