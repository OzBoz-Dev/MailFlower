import PromptsAndStuff
from ollama import chat
from ollama import ChatResponse

# A response loop so that the user can vet and provide feedback to responses
def get_extra_content(company_name:str, extra_considerations:str) -> str:
    feedback = ""
    response = ""
    while True:
        response = generate_response(company_name, extra_considerations, response, feedback)
        print(response)
        choice = input("Accept Response? (Y/n): ")
        if choice == 'Y':
            return response
        else:
            feedback = input("Give feedback on this response: ")
        print()

def generate_response(company_name:str, extra_considerations:str, previous_response:str, feedback:str) -> str:
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
            Keep the tone professional but not overenthusiastic
            Last response: {previous_response}
            Keep in mind the feedback from the last run: {feedback}
            """
        }
    ],
    options = {
        "temperature" : 0.5
    }
    )
    return str(response.message.content)

# For testing purposes only
def main():
    print(get_extra_content("Blue Origin", "We were previously sponsored by them for a project involving an autonomous drone"))

if __name__ == "__main__":
    main()