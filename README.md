# PDF to Podcast Using Gemini and Elevenlabs

This project provides a tool to convert any PDF document into a engaging podcast! Using **Google's Gemini** for dialogue generation and **Elevenlabs** for text-to-speech.


## App Screenshot
Here's what the app looks like:

![App Screenshot](/img/home.png)

## Features
- **Understand PDFs**: Understand PDFs rather than extract text. (It's can understand figure, table, images....)
- **Dialogue Generation**: Uses Gemini to generate conversational dialogues based on the input PDF content.
- **Text-to-Speech**: Converts the generated dialogues into audio using Elevenlabs' text-to-speech service.
- **Streamlit UI**: Provides an easy-to-use interface to upload PDFs and generate podcasts.

## Installation

1. **Clone the Repository**  
   Clone the project to your local machine:

   ```bash
   git clone https://github.com/chiragjoshi12/pdf-to-podcast.git
   cd pdf-to-podcast
   ```

2. **Install Dependencies**  
   Install the required Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up API Keys**  
   Create a `.env` file and add your **Gemini** and **Elevenlabs** API keys:

   ```plaintext
   GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
   ELEVENLABS_API_KEY="YOUR_ELEVENLABS_API_KEY"
   ```

4. **Run the Application**  
   Start the application with Streamlit:

   ```bash
   streamlit run main.py
   ```

   The app will be available in your browser for use.

## Usage

- Upload a PDF file to the app.
- Set your podcast prompt and click "Generate Podcast."
- The app will generate the dialogue and convert it into an audio file, which you can listen to.

## Blog Post

For detailed instructions and insights, check out the blog post:  
[NotebookLM with Gemini and Elevenlabs (Detailed Documentation)](https://chirag-ai.medium.com/notebooklm-with-gemini-and-elevenlabs-detailed-documentation-b8db6739ba9b)

---

Readme made with 💖 using [README Generator by Chirag Joshi](https://github.com/chiragjoshi12/readme-generator)