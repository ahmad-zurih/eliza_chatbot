import streamlit as st
from nltk.chat.eliza import eliza_chatbot


def get_eliza_response(message):
    """
    Function that takes a string and return the eliza chatbot response
    """
    return eliza_chatbot.respond(message)


def main():
    st.title("Eliza Chatbot")

    # Conversation history
    if 'history' not in st.session_state:
        st.session_state['history'] = []

    # User input
    user_input = st.text_input("You: ", key="user_input", value="")

    # Handling the response
    if st.button("Send") or user_input:
        eliza_response = get_eliza_response(user_input)
        st.session_state.history.append(f"You: {user_input}")
        st.session_state.history.append(f"Eliza: {eliza_response}")

    # Display conversation history
    for message in st.session_state.history:
        st.text(message)

# Run the app
if __name__ == "__main__":
    main()

