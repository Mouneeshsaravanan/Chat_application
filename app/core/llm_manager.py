from langchain_google_genai import ChatGoogleGenerativeAI
from .config import settings

print("API KEY is ", settings.GOOGLE_API_KEY)
class LLMManger:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="models/gemini-1.5-flash",
            temperature=1,
            api_key=settings.GOOGLE_API_KEY
        )
 
    def get_llm(self):
        return self.llm
            
    def invoke(self,message):
        return self.llm.invoke(message)