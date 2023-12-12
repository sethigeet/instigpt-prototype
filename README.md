# InstiGPT Prototype

This prototype is for a ChatGPT-like AI assistant for the students at IIT Bombay. It can help students find information more easily and help them in day to day tasks such as getting previous year question papers for a particular course, getting reviews about a particular course, seeing who is teaching a particular course, and many more things!

## Running the application

> NOTE: You may choose to create a virtual environment.

1. Install the dependencies using `pip install -r requirements.txt`
1. Run the API using `python main.py`
1. Run the web app using `streamlit run ui.py`
1. Now visit [localhost:8501](http://localhost:8501)

## Demo

![Question 1](<docs/question 1.png>)

![Question 2](<docs/question 2.png>)

## Why it was created?

This project aims to assist college students by simplifying everyday tasks and helping them find information that is not easily available. It will also make the information concise and provide it more efficiently.

## Technical Details

- This app uses RAG to incorporate information from many sources with live updates.
- It uses [pathway](https://github.com/pathwaycom/pathway) and [LLMApp](https://github.com/pathwaycom/llm-app) to process live data, generate embeddings and generate text from LLMs.
- It offers a good-looking UI built using streamlit.
