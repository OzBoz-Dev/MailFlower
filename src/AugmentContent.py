from ollama import web_search
from ollama import chat
from ollama import Client
from dotenv import load_dotenv
import os
import PromptsAndStuff
from ollama import ChatResponse

def get_extra_content(company_name:str, extra_considerations:str) -> str:

    response:ChatResponse = chat(model="gemma3:4b", messages=[
        {
            "role" : "system",
            "content" : PromptsAndStuff.SYSTEM_PROMPT
        },
        {
            "role" : "user",
            "content" : f"""How does {company_name} align with ACM, and why should they consider speaking at our GBM?
            Keep in mind the following extra considerations: {extra_considerations}.
            Only write the PERSONAL TOUCH part, no subject line, no greeting, that's already written.
            This should be a complete response.
            Keep it short but sweet (no more than 2-3 sentences).
            Unless you are explicitly told that we had a prior collaboration, assume this is the first time we are communicating.
            """
        }
    ],
    options = {
        "temperature" : 0.2
    }
    )
    return str(response.message.content)

def main():
    print(get_extra_content("Streamline Technologies", "Orlando-based company providing water simulation services"))

if __name__ == "__main__":
    main()