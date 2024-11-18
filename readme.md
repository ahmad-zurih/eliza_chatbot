# Eliza Chatbot Implementation

## Overview
This repository contains a Python implementation of the historical Eliza chatbot, using the Natural Language Toolkit (NLTK). Eliza is one of the earliest examples of a natural language processing program, created in the mid-1960s at the MIT Artificial Intelligence Laboratory by Joseph Weizenbaum. The implementation in this repository showcases the capabilities of Eliza in a modern web interface, using the Streamlit framework.

## Eliza Chatbot
Eliza simulates a psychotherapist by using a pattern matching and substitution methodology, which gives users an illusion of understanding on the part of the program, but has no built-in framework for contextualizing events. The original Eliza program was designed to demonstrate the superficiality of communication between humans and machines. For more detailed information about the Eliza chatbot, refer to its [Wikipedia page](https://en.wikipedia.org/wiki/ELIZA).

## Application Demo
Experience the Eliza chatbot in action by visiting the Streamlit app: [Eliza Chatbot Streamlit App](https://elizachatbot-nltk.streamlit.app/). The app provides a simple and intuitive user interface for interacting with Eliza, allowing you to engage in a conversation similar to one you might have with a psychotherapist.

## Local Setup
To run this application locally, you will need Python installed on your system. After cloning the repository, install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```
then run the following from inside the project directory:

```bash
streamlit run home.py
