import cohere

# Initialize Cohere client
COHERE_API_KEY = "6BSCGuUKQzPneU3jW7ABaUUCQsyHLBTjjKf9tK0V"  # Replace with your Cohere API Key
co = cohere.Client(COHERE_API_KEY)

def chat_with_pdf(question, pdf_text):
    """
    Uses Cohere Chat API to answer questions based on PDF content.
    """
    prompt = f"""
You are a helpful assistant. Answer the question based ONLY on the following PDF content.
PDF content:
{pdf_text}

Question: {question}
Answer:
"""
    response = co.chat(
        model="command-a-03-2025",
        message=prompt
    )
    return response.text.strip()
