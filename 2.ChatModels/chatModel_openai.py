from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4.1-mini")
result = model.invoke("what is the capital of INdia?")
print(result)

'''from pathlib import Path
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

model = ChatOpenAI(model="gpt-4")

result = model.invoke("What is the capital of India?")
print(result.content)'''