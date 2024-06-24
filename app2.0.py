import os
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import google.generativeai as genai

# Initialize cache dictionaries
# These dictionaries will store analysis results and question answers to avoid recomputing them
analysis_cache = {}
question_cache = {}

def analyze_website(url):
    # Check if the analysis is already cached
    if url in analysis_cache:
        print("Using cached analysis results.")
        return analysis_cache[url]

    # Fetch the website content
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error fetching website: {response.status_code}")
        return None

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string if soup.title else "No title found"
    description_tag = soup.find("meta", attrs={"name": "description"})
    description = description_tag["content"] if description_tag else "No description found"

    # Analyze website using generative AI
    prompt = f"Analyze the website. Title: {title}. Description: {description}."
    analysis = model.generate_content(prompt)
    print(f"Analysis: {analysis.text}")

    # Cache the analysis results
    analysis_results = {
        "title": title,
        "description": description,
        "analysis": analysis.text
    }
    analysis_cache[url] = analysis_results

    return analysis_results

def answer_questions(analysis_results):
    while True:
        question = input("Ask a question about the website: ")
        if question.lower() == "quit":
            break

        # Check if the answer is already cached
        if question in question_cache:
            print("Using cached answer.")
            print(f"Answer: {question_cache[question]}")
            continue

        # Use generative AI to answer question based on analysis results
        prompt = f"Answer the question: '{question}' based on the website with title '{analysis_results['title']}' and description '{analysis_results['description']}'."
        answer = model.generate_content(prompt)
        print(f"Answer: {answer.text}")

        # Cache the answer
        question_cache[question] = answer.text

if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()
    if os.environ.get("GEM_API_API") is None:
        print("GEM_API_API not found in environment variables")
        exit(1)

    # Configure the generative AI model
    genai.configure(api_key=os.environ["GEM_API_API"])
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Get the website URL from the user
    url = input("Enter a website URL: ")
    analysis_results = analyze_website(url)
    if analysis_results:
        answer_questions(analysis_results)
