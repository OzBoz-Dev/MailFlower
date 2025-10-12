from ollama import web_search
from ollama import chat
from ollama import Client
from dotenv import load_dotenv
import os
from ollama import ChatResponse

def get_extra_content(company_name:str, extra_considerations:str) -> str:

    response:ChatResponse = chat(model="gemma3:4b", messages=[
        {
            "role" : "system",
            "content" : f"""You are the Outreach Director for the Association of Computing Machinery (ACM) student club at
            the University of Central Florida.
            
            Email Content:
            Good Afternoon, CONTACT

            I hope this email finds you well. My name is DIRECTOR, and I am the Outreach Director for the Association of Computing Machinery (ACM) student chapter at the University.

            ACM is a worldwide organization built on the foundation of computer engineering and computer science, focused on providing resources to advance the field and profession. We seek to replicate that mission here at our ACM student chapter, leaving a long-lasting impact on UCF's research ecosystem and supporting students through their growth of technical, leadership, and soft skills.

            [YOUR PERSONAL TOUCH HERE]

            Thank you for your time, and I look forward to your response.
            
            Given the company you are asked about, you must research information about their values and work, and write
            in a persuasive tone about how their values align with ours and how their field of technology would
            provide a great opportunity for students, as well as networking opportunities.
            We are specifically inviting them to speak at one of our General Body Meetings.

            There may also be some extra considerations, such as us having a past history with the company or lab in question.
            Be sure to bring up this information in your response.

            ACM's Values: At ACM, we value student involvement and choice. We want our students to be involved, and want to
            foster a culture of knowledge. We host workshops, work on projects, and want to provide good networking opportunities for students.

            Example personal touches:
            We would love to hear insights into the world of Fintech from top engineers in the industry!

            This would provide a great opportunity for students to learn more about the tech industry and AI, providing a great opportunity for learning and networking.  
            We would love to have a representative speak at one of our General Body Meetings and give their insights!
            """
        },
        {
            "role" : "user",
            "content" : f"""How does {company_name} align with ACM, and why should they consider speaking at our GBM?
            Keep in mind the following extra considerations: {extra_considerations}.
            Only write the PERSONAL TOUCH part, no subject line, no greeting, that's already written.
            This should be a complete response.
            Keep it short but sweet (no more than 2-3 sentences).
            """
        }
    ])
    return str(response.message.content)

def main():
    print(get_extra_content("Google", "We held interview workshops last year and students enjoyed those"))

if __name__ == "__main__":
    main()