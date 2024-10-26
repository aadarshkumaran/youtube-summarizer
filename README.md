# YouTube Summarizer
    #### Video Demo:  <URL HERE>
    #### Description:
    TODO

A tool that leverages AI to generate concise and accurate summaries of YouTube videos. This summarizer helps users save time by providing a quick overview of video content without watching the entire video.

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Description
The YouTube Summarizer analyzes the content of a YouTube video and produces a short, relevant summary based on the video transcript. It’s ideal for people who want to quickly grasp the main ideas without watching the entire video. 

## Features
- **AI-based Summarization**: Uses AI to generate summaries.
- **Transcript Extraction**: Fetches transcripts directly from YouTube videos (if available).

## Installation

### Prerequisites
- [Python 3.x](https://www.python.org/)
- [OpenAI API Key](https://aistudio.google.com/app/apikey) 

### TODO
1. Clone the repository:
   ```bash
   git clone https://github.com/aadarshkumaran/youtube-summarizer.git
   cd youtube-summarizer
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Executing the program

3. Paste your Gemini API in .env file:
   ```bash
   GOOGLE_API_KEY='your_api_key'
   ```
4. Run the application through the terminal:
   ```bash
   streamlit run ytmuncher.py
   ```

## Technologies Used
- **Python**: Core language for the application.
- **youtube_transcript_api**: To fetch video transcripts.
- **GeminiAI API**: For AI-driven summarization.
- **LangChain Framework**: To structure and manage the summarization workflow by connecting various AI components, enabling cohesive and context-aware responses.

## Contributing
Feel free to submit issues or pull requests! Contributions are welcome.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License
This project is licensed under the MIT License.
