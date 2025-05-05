# Policy Pal

**Know what's behind the legal jargon in Privacy Policies, Terms & Conditions, and more — before you click "Accept."**

![Demo](assets/tcsummarizer.gif)

## Overview

Policy Pal is a web application that helps users understand lengthy terms and conditions documents without having to read them in full. Most people accept terms and conditions without reading them due to their length and complexity. Policy Pal solves this problem by taking a URL or text input and providing a concise, easy-to-understand summary using OpenAI's GPT models.

## Features

- **URL or Text Input**: Paste a URL to terms and conditions or input the text directly
- **Web Scraping**: Automatically extracts relevant content from web pages
- **Powerful AI Processing**: Leverages OpenAI's language models to analyze complex legal text
- **Concise Summaries**: Transforms lengthy documents into clear, readable summaries
- **Web-based Interface**: Simple, user-friendly design


## Installation

1. Clone the repository:
   ```
   git clone https://github.com/kishan5111/policypal.git
   ```

2. Navigate to the project directory:
   ```
   cd policypal
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

5. Run the application:
   ```
   python app.py
   ```

6. Open your browser and go to `http://localhost:8000`

## Usage

1. Enter a URL containing terms and conditions or paste the text directly
2. Click "Summarize"
3. Review the AI-generated summary that highlights key points

## Requirements

- Python 3.8+
- OpenAI API key

## License

[MIT License](LICENSE)
