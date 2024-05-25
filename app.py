import streamlit as st

# Define the questions and options
questions = [
    {
        "question": "How would you describe your overall personality?",
        "options": ["Introverted", "Extroverted", "Calm", "Energetic"]
    },
    {
        "question": "What are your predominant emotional states?",
        "options": ["Happiness", "Sadness", "Anxiety", "Contentment"]
    },
    {
        "question": "What environments do you feel most comfortable in?",
        "options": ["Forests", "Mountains", "Cities", "Oceans"]
    },
    {
        "question": "What kinds of animals do you feel a strong connection to?",
        "options": ["Dogs", "Cats", "Birds", "Fish"]
    },
    {
        "question": "What are your natural talents or skills?",
        "options": ["Music", "Art", "Leadership", "Athletics"]
    },
    {
        "question": "Do you have recurring dreams or deja vu experiences?",
        "options": ["Yes", "No"]
    },
    {
        "question": "Do you have any strong, irrational fears or phobias?",
        "options": ["Fear of water", "Fear of heights", "Fear of certain animals", "None"]
    },
    {
        "question": "Do you have any spiritual practices or beliefs about the nature of the soul and afterlife?",
        "options": ["Yes", "No"]
    },
    {
        "question": "Have you ever felt a deep sense of purpose or mission in life?",
        "options": ["Yes", "No"]
    }
]

# Define the prediction function
def predict_past_life_responses(responses):
    score = sum([ord(response[0]) for response in responses])
    if score < 500:
        return "You were likely a Human."
    elif score < 600:
        return "You were likely an Animal."
    elif score < 700:
        return "You were likely an Elemental/Spirit."
    else:
        return "You were likely a Deity or Mythical Creature."

# Streamlit app
st.set_page_config(page_title="Past Life Predictor", page_icon="🔮")

# Sidebar for the dashboard
st.sidebar.title("Past Life Predictor")
st.sidebar.image("https://example.com/path/to/image.jpg", use_column_width=True)
st.sidebar.markdown("""
Welcome to the Past Life Predictor! This app is designed to provide you with insights into what kind of being you might have been in a past life based on your current life experiences, personality traits, and preferences.

### How It Works
1. **Answer Questions**: Respond to a series of questions about your personality, likes, dislikes, and experiences.
2. **Get Your Prediction**: The app will analyze your responses and provide a prediction of what kind of being you might have been in a past life.

### Disclaimer
This app is for entertainment purposes only and is based on speculative and philosophical concepts. The results should not be taken as scientific evidence or factual information.

Enjoy the journey into your potential past life!
""")

st.title("Discover Your Past Life")

responses = []
for q in questions:
    response = st.radio(q["question"], q["options"], key=q["question"])
    responses.append(response)

if st.button("Predict"):
    result = predict_past_life_responses(responses)
    st.write(result)
