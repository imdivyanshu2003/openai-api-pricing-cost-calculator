import os
import openai
import streamlit as st
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv("env/.env")

# Load your OpenAI API key from .env file
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_completion(prompt, model="gpt-3.5-turbo", messages=None):
    if messages is None:
        messages = []
    messages.append({"role": "user", "content": prompt})

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"], messages


def format_content_ideas(content):
    return content.split("\n")


def collect_messages(prompt, messages=None):
    if messages is None:
        messages = []
    response, messages = get_completion(prompt, messages=messages)
    messages.append({"role": "user", "content": f"{prompt}"})
    formatted_response = format_content_ideas(response)
    messages.append({"role": "assistant", "content": response})
    return formatted_response, messages


# Function to run the Streamlit app
def run_app():
    st.title("Open AI API Pricing Cost Calculator")
    st.markdown(
        """
        Hello! I’m your OpenAI API Pricing Calculator. Just enter your usage
        in dollars and the number of API calls you made or received for that
        amount, and I will tell you the exact cost per prompt of your AI
        tool in both dollars and rupees!
    """
    )

    # Include the content of index.html using streamlit's html component
    with open("index.html", "r") as file:
        st.components.v1.html(file.read())

    # Add your Streamlit app code here
    # For example, you can use st.sidebar to take input from the user
    # and st.write to display the output to the user.
    usage_dollars = st.sidebar.number_input(
        "Enter Usage in Dollars", min_value=0.0, step=0.01
    )
    num_requests = st.sidebar.number_input(
        "Enter Number of Requests", min_value=0, step=1
    )

    if st.sidebar.button("Calculate"):
        user_input = (
            f"Usage in Dollars: {usage_dollars}, No. of Requests: {num_requests}"
        )
        response, context = collect_messages(user_input, context)

        st.write("Per Prompt Cost is:")
        st.write(f"USD: ${response[0]}")
        st.write(f"INR: ₹{response[1]}")


if __name__ == "__main__":
    context = [
        {
            "role": "system",
            "content": """
You are Professional Open AI API Pricing Cost Calculator. You Just tell user per prompt cost of their AI tool! \
You get the values of usage in dollars and number of requests from the user then you divide the number of dollars by no. of request or prompts like this for example for $Dollars: Usage in Dollars / No. of Requests = Per Prompt Cost. \
You get the values of usage in dollars and number of requests from the user then you divide the number of dollars by no. of request or prompts and then multiply by 82 like this for example for ₹INR Rupees: Usage in Dollars / No. of Requests * 82 = Per Prompt Cost. \
Don't use your mind just use the calculation I have given you and give the output to the user. \
Make sure to give the user the per prompt cost in dollars and rupees line by line and in one words and make sure it should be correct after calculation. \
Do not go out of context in the conversation and do not give the user any other information than the per prompt cost of their AI tool. \
Ensure not to give any explanation and give your output like this:
Per Prompt Cost is:
USD: $ 
INR: ₹ \
Ensure to give the per prompt or request cost in INR and USD correct & accurate based on the calculation above and it should be up to four decimal points only. \
Make sure the output is in the same format as above and the results should be accurate. \
Make sure your conversation is in a friendly manner and you are not rude to the user. \
""",
        }
    ]

    # Run the Streamlit app
    run_app()

    # Note: The Flask app will not run in this mode as Streamlit handles the server.
