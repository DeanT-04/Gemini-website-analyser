# Website Analyzer with Generative AI

This project is a Python application that allows you to analyze websites using generative AI. It fetches the website content, extracts the title and description, and generates an analysis using a generative AI model. Additionally, you can ask questions about the website, and the application will provide answers based on the analysis results.

## Features

- Analyze websites by providing the URL
- Extract website title and description
- Generate analysis using a generative AI model
- Ask questions about the website and receive answers based on the analysis

## Prerequisites

Before running the application, make sure you have the following prerequisites installed:

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/website-analyzer.git
   ```

2. Navigate to the project directory:

   ```bash
   cd website-analyzer
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Setup

1. Obtain an API key from the Anthropic Gem AI API. You can sign up for an account and generate an API key on their website: [https://www.anthropic.com/](https://www.anthropic.com/)

2. Create a `.env` file in the project directory and add your API key:

   ```ini
   GEM_API_API=your_api_key_here
   ```

## Usage

1. Run the application:

   ```bash
   python app2.0.py
   ```

2. Enter a website URL when prompted.
3. The application will fetch the website content, generate an analysis using the generative AI model, and display the results.
4. You can then ask questions about the website. Type "quit" to exit the question-answering loop.

## Caching

The application implements caching to improve performance and avoid recomputing analysis results and question answers. The caching mechanism stores the analysis results and question answers in dictionaries, allowing for faster retrieval of previously computed data.
