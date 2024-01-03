import streamlit as st
import json

# Define the quiz questions and options
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "Berlin", "Rome"],
        "correct_option": "Paris"
    },
    {"question": "Which is the largest planet in the solar system?",
     "options": ["Jupiter", "Saturn", "Earth"],
     "correct_option": "Jupiter"}
    # Add more questions similarly
    # ...
]

# Initialize a variable to store user's answers
@st.experimental_singleton
def get_user_answers():
    return [None] * len(questions)

@st.experimental_singleton
def get_current_question_index():
    return 0

# Function to render a question
def render_question(current_question_index, user_answers):
    st.write(f"**Q{current_question_index + 1}:** {questions[current_question_index]['question']}")
    selected_option = st.radio("Select an option:", questions[current_question_index]['options'])
    user_answers[current_question_index] = selected_option

# Streamlit app
def main():
    st.title("20 Question Quiz")

    user_answers = get_user_answers()
    current_question_index = get_current_question_index()

    if current_question_index < len(questions):
        render_question(current_question_index, user_answers)

        if st.button("Next Question"):
            current_question_index += 1
            get_current_question_index.set(current_question_index)
            get_user_answers.set(user_answers)

    else:
        st.write("Quiz completed!")
        st.write("Your answers:", user_answers)
        st.button("Submit")

if __name__ == "__main__":
    main()