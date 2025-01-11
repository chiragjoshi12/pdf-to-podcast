import streamlit as st
from services.elevenlabs import *
from services.gemini import *
import os

def generate_podcast(prompt: str, system_message: str, pdf_path: str = "") -> dict:
    if pdf_path and not os.path.isfile(pdf_path):
        raise FileNotFoundError(f"The file at path '{pdf_path}' does not exist. Please provide a valid file path.")

    files = upload_to_gemini(pdf_path, "application/pdf")
    chat_history = [{'role': 'user', 'parts': [{'file_data': {'mime_type': files.mime_type, 'file_uri': files.uri}}]}]
    
    dialogue = call_gemini(
        prompt=prompt,
        system_message=system_message,
        history=chat_history
    )
    dialogue_items = []

    for line in dialogue.split('\n'):
        line = line.strip()
        if not line:
            continue
            
        if line.startswith("male-1:"):
            speaker = "male-1"
            text = line[len("male-1:"):].strip()
        elif line.startswith("female-1:"):
            speaker = "female-1"
            text = line[len("female-1:"):].strip()
        else:
            continue
        
        dialogue_items.append(DialogueItem(text=text, speaker=speaker))
    
    return generate_audio(dialogue_items)

st.title("Convert PDF to Podcast")

pdf_file = st.file_uploader("Upload a PDF", type=["pdf"])

# prompt and system message
system_instructions = "Your task is to take the input text provided and transform it into an engaging, informative podcast dialogue. The input text might be messy or unstructured, possibly sourced from PDFs, web pages, or other formats. Your goal is to extract the key topics, main points, and any interesting facts that could be discussed in a podcast. Ignore any irrelevant details or formatting issues in the input.\n\n## Steps to Follow:\n\n1. Read and Analyze:\n- Carefully review the input text to identify the main topics, key points, and notable anecdotes.\n- Consider how these topics can be discussed in a way that’s engaging, fun, and accessible to a general audience.\n\n2. Brainstorm Ideas:\n- Think about creative ways to present the information: use analogies, storytelling, hypothetical scenarios, or thought-provoking questions to keep the dialogue interesting.\n- Keep the tone conversational, avoiding technical jargon or assuming prior knowledge.\n- If complex concepts are necessary, explain them in simple, easy-to-understand terms.\n\n3. Create Dialogue:\n- Write a podcast dialogue using a natural, flowing conversational tone.\n- Incorporate filler words like \"hmmmmm,\" \"ahhhhh,\" \"ohhh,\" or \"you know\" naturally in the dialogue to simulate real, casual conversations.\n- Format the dialogue as:\n    ```\n    male-1: ...  \n    female-1: ...  \n    male-1: ...  \n    ```\n\n- Do not include any introductory music, sound effects, or bracketed placeholders. Start directly with dialogue.\n\n4. Key Points and Takeaways:\n- Ensure the dialogue revisits the key insights and takeaways organically toward the end of the conversation, without sounding like an obvious recap.\n\n5. Detailed and On-Topic:\n- Make the dialogue as detailed and lengthy as possible while staying engaging and on-topic. Use your full capacity to create an in-depth discussion.\n\n## Note:\n- Maintain the specified dialogue format throughout.\n- Avoid using anything other than the required dialogue format in your response.\n- Use filler words and pauses naturally to enhance the conversational flow and make it sound more authentic.Your task is to take the input text provided and transform it into an engaging, informative podcast dialogue. The input text might be messy or unstructured, possibly sourced from PDFs, web pages, or other formats. Your goal is to extract the key topics, main points, and any interesting facts that could be discussed in a podcast. Ignore any irrelevant details or formatting issues in the input.\n\n## Steps to Follow:\n\n1. Read and Analyze:\n- Carefully review the input text to identify the main topics, key points, and notable anecdotes.\n- Consider how these topics can be discussed in a way that’s engaging, fun, and accessible to a general audience.\n\n2. Brainstorm Ideas:\n- Think about creative ways to present the information: use analogies, storytelling, hypothetical scenarios, or thought-provoking questions to keep the dialogue interesting.\n- Keep the tone conversational, avoiding technical jargon or assuming prior knowledge.\n- If complex concepts are necessary, explain them in simple, easy-to-understand terms.\n\n3. Create Dialogue:\n- Write a podcast dialogue using a natural, flowing conversational tone.\n- Incorporate filler words like \"hmmmmm,\" \"ahhhhh,\" \"ohhh,\" or \"you know\" naturally in the dialogue to simulate real, casual conversations.\n- Format the dialogue as:\n    ```\n    male-1: ...  \n    female-1: ...  \n    male-1: ...  \n    ```\n\n- Do not include any introductory music, sound effects, or bracketed placeholders. Start directly with dialogue.\n\n4. Key Points and Takeaways:\n- Ensure the dialogue revisits the key insights and takeaways organically toward the end of the conversation, without sounding like an obvious recap.\n\n5. Detailed and On-Topic:\n- Make the dialogue as detailed and lengthy as possible while staying engaging and on-topic. Use your full capacity to create an in-depth discussion.\n\n## Note:\n- Maintain the specified dialogue format throughout.\n- Avoid using anything other than the required dialogue format in your response.\n- Use filler words and pauses naturally to enhance the conversational flow and make it sound more authentic."
fix_prompt = "Transform the provided text into a natural, engaging podcast dialogue with clear speaker roles, keeping the tone conversational, informative, and accessible for a general audience."

user_prompt = st.text_area("Enter your podcast prompt", value=fix_prompt)

if st.button("Generate Podcast"):
    if pdf_file is not None:
        try:
            pdf_path = f"temp_uploaded_file.pdf"
            with open(pdf_path, "wb") as f:
                f.write(pdf_file.getbuffer())
            
            results = generate_podcast(user_prompt, system_instructions, pdf_path)

            # Save transcript
            transcript_path = "podcast_transcript.txt"
            with open(transcript_path, "w", encoding="utf-8") as transcript_file:
                transcript_file.write(results["transcript"])
            st.success(f"Transcript saved to {transcript_path}")

            # Save audio as mp3
            audio_path = "podcast_audio.mp3"
            with open(audio_path, "wb") as audio_file:
                audio_file.write(results["audio"])
            st.audio(audio_path, format="audio/mp3")
            st.success(f"Audio saved to {audio_path}")

        except FileNotFoundError as e:
            st.error(f"Error: {e}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
    else:
        st.warning("Please upload a PDF file to generate the podcast.")