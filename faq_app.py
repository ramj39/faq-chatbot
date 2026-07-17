import streamlit as st
import json
from datetime import datetime

# Load FAQ data
with open("faq.json", "r", encoding="utf-8") as f:
    faq_data = json.load(f)

# Load intent filter data
with open("intent_filter.json", "r", encoding="utf-8") as f:
    intent_filters = json.load(f)["intents"]

# Simple intent detection
def detect_intent(user_input):
    user_input = user_input.lower()
    for intent, keywords in intent_filters.items():
        for keyword in keywords:
            if keyword in user_input:
                return intent
    return None

# Match FAQ answer
def get_answer(intent):
    if not intent:
        return "Sorry, I couldn’t understand your question. Please try rephrasing."
    for item in faq_data:
        if intent in item["question"].lower():
            return item["answer"]
    for item in faq_data:
        if intent in item["answer"].lower():
            return item["answer"]
    return "I don’t have an answer for that yet."

# Streamlit UI
st.title("🤖 FAQ Chatbot - Industrial Plating Solutions")
st.write("Ask me about our products, services, industries, location, or contact details.")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_input = st.text_input("Type your question here:")

if user_input:
    intent = detect_intent(user_input)
    answer = get_answer(intent)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Save to chat history with timestamp
    st.session_state.chat_history.append({
        "question": user_input,
        "answer": answer,
        "time": timestamp
    })

# Search bar for filtering chat history
search_query = st.text_input("🔍 Search chat history by keyword:")

# Display chat history
st.subheader("Chat History")
filtered_history = st.session_state.chat_history
if search_query:
    search_query = search_query.lower()
    filtered_history = [
        chat for chat in st.session_state.chat_history
        if search_query in chat["question"].lower() or search_query in chat["answer"].lower()
    ]

for chat in filtered_history:
    st.markdown(f"**[{chat['time']}] You:** {chat['question']}")
    st.markdown(f"**[{chat['time']}] Bot:** {chat['answer']}")
    st.markdown("---")

# Clear chat history button
if st.button("Clear Chat History"):
    st.session_state.chat_history = []
    st.info("Chat history cleared. Start fresh!")

# Download chat history button
if st.session_state.chat_history:
    chat_text = "\n".join(
        [f"[{c['time']}] You: {c['question']}\n[{c['time']}] Bot: {c['answer']}" 
         for c in st.session_state.chat_history]
    )
    st.download_button(
        label="📥 Download Chat History",
        data=chat_text,
        file_name="chat_history.txt",
        mime="text/plain"
    )
