from langchain.chat_models import ChatOpenAI

def summarize_data(data):
    llm = ChatOpenAI(model="gpt-3.5-turbo", api_key="your_openai_api_key")
    response = llm(data)
    return response
