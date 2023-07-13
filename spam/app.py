import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the saved model
with open('spam_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load the TfidfVectorizer
with open('tfidf_vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

def preprocess_text(text):
    # Preprocess the text (same preprocessing as during training)
    preprocessed_text = text.lower()
    preprocessed_text = vectorizer.transform([preprocessed_text])
    return preprocessed_text

def classify_email(text):
    # Preprocess the text
    preprocessed_text = preprocess_text(text)

    # Make predictions
    prediction = model.predict(preprocessed_text)[0]
    if prediction == 0:
        return 'Spam'
    else:
        return 'Ham'

def main():
    st.title('Email Spam Classifier')
    st.write('Enter an email to classify it as spam or ham:')
    
    # Create a textarea for user input
    email = st.text_area('Email Text', height=200)
    
    # Classify the email when a button is clicked
    if st.button('Classify'):
        result = classify_email(email)
        st.write('Result:', result)

if __name__ == '__main__':
    main()
