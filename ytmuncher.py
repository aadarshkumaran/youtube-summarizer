import os
import streamlit as st
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain.schema import Document  # For LangChain's document processing
from dotenv import load_dotenv
from cc_extractor import get_transcript

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_conversational_chain(context):
    prompt_template = """
    I have a transcript that needs a clear and detailed summary. Please provide an in-depth summary of the key discussions, main points, and important details from the conversation. Ensure the summary is well-structured, accurate, and maintains the context of the discussion. Here's the transcript:
    Transcript text: \n{context}\n
    """


    model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context"])

    input_documents = [Document(page_content=context)]
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    result = chain.run(input_documents)

    return result


def main():
    st.title("YouTube Transcript Summarizer")

    youtube_url = st.text_input("Enter YouTube URL:", "")

    if youtube_url:
        st.write("Extracting transcript and summarizing...")

        try:
            context = get_transcript(youtube_url)

            summary = get_conversational_chain(context)

            st.subheader("Transcript Summary")
            st.write(summary)

        except Exception as e:
            st.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
