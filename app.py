# Import necessary modules
import os
import dotenv
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import google.generativeai as genai

# Function to analyze a website
def analyze_website(url):
    # Send a GET request to the website
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Error fetching website: {response.status_code}")
        return None

    # Parse the HTML content of the website
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract the title of the website
    title = soup.title.string if soup.title else "No title found"
    # Extract the description meta tag
    description_tag = soup.find("meta", attrs={"name": "description"})
    description = description_tag["content"] if description_tag else "No description found"

    # Analyze website using generative AI
    prompt = f"Analyze the website. Title: {title}. Description: {description}."
    analysis = model.generate_content(prompt)
    print(f"Analysis: {analysis.text}")

    # Return analysis results
    return {
        "title": title,
        "description": description,
        "analysis": analysis.text
    }

# Function to answer questions about the website
def answer_questions(analysis_results):
    while True:
        question = input("Ask a question about the website: ")
        if question.lower() == "quit":
            break

        # Use generative AI to answer question based on analysis results
        prompt = f"Answer the question: '{question}' based on the website with title '{analysis_results['title']}' and description '{analysis_results['description']}'."
        answer = model.generate_content(prompt)
        print(f"Answer: {answer.text}")

# Main function
if __name__ == "__main__":
    # Load environment variables
    dotenv.load_dotenv()
    # Check if GEM_API_API is set in environment variables
    if os.environ.get("GEM_API_API") is None:
        print("GEM_API_API not found in environment variables")
        exit(1)

    # Configure the generative AI model
    genai.configure(api_key=os.environ["GEM_API_API"])
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Get the website URL from the user
    url = input("Enter a website URL: ")
    # Analyze the website
    analysis_results = analyze_website(url)
    if analysis_results:
        # Answer questions about the website
        answer_questions(analysis_results)
