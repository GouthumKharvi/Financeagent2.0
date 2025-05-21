# Finance Assistant

## Overview
The Finance Assistant is a multi-source, multi-agent finance assistant that delivers spoken market briefs. It integrates various data sources, processes audio input, and generates market summaries using advanced AI techniques. The application is built using FastAPI for the backend and Streamlit for the frontend.

## Project Structure
finance_assistant/ │ ├── data_ingestion/ │ ├── api_agent.py # Fetches market data from Alpha Vantage API │ ├── scraping_agent.py # Scrapes financial filings from websites │ ├── agents/ │ ├── retriever_agent.py # Handles embeddings and retrieval of data │ ├── language_agent.py # Generates narratives using language models │ ├── voice_agent.py # Processes speech-to-text and text-to-speech │ ├── orchestrator/ │ └── orchestrator.py # FastAPI application to orchestrate agents │ ├── streamlit_app/ │ └── app.py # Streamlit application for user interaction │ ├── docs/ │ └── ai_tool_usage.md # Documentation of AI tool usage │ ├── README.md # Project documentation ├── requirements.txt # Python dependencies └── Dockerfile # Docker configuration for deployment


## Features
- **Data Ingestion**: Fetches real-time and historical market data using the Alpha Vantage API and scrapes financial filings.
- **Multi-Agent Architecture**: Utilizes specialized agents for data retrieval, language processing, and voice interaction.
- **Speech Processing**: Converts audio input to text and generates spoken market briefs using text-to-speech.
- **User -Friendly Interface**: Built with Streamlit for easy interaction and audio playback.

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/finance_assistant.git
   cd finance_assistant


# Create a Virtual Environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install Dependencies:
pip install -r requirements.txt

# Run the FastAPI Server:
uvicorn orchestrator.orchestrator:app --reload

# Run the Streamlit App:
streamlit run streamlit_app/app.py

# Access the Application:
Open your web browser and go to http://localhost:8501 to access the Streamlit app.

# Usage
Upload an Audio File: Use the file uploader in the Streamlit app to upload an audio file containing your finance-related question.

Get Market Brief: Click the "Get Market Brief" button to process the audio input and receive a spoken market brief in response.

Audio Playback: The generated market brief will be played back to you as audio.



# AI Tool Usage Log
LangChain: For language model integration.
FAISS: For efficient similarity search.
gTTS: For text-to-speech conversion.
Whisper: For speech-to-text conversion.

# Code Generation Steps
Implemented API agent to fetch market data.
Developed scraping agent for financial filings.
Created retriever agent for indexing and retrieval.
Built language agent for narrative synthesis.
Developed voice agent for STT and TTS.
Orchestrated agents using FastAPI.
Built Streamlit app for user interaction.

# Deployment
The application can be deployed on cloud platforms  Streamlit Sharing, Ensure to configure the environment variables and API keys as needed.

# License
This project is licensed under the MIT License - see the LICENSE file for details.

# Acknowledgments
Special thanks to the developers of the libraries and tools used in this project, including FastAPI, Streamlit, LangChain, and others.
