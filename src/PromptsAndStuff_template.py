"""
This is a template where you can fill in the HTML body text and ollama prompts. The actual
information is obfuscated in PromptsAndStuff.py. Simply remove the _template at the end
of the file and you can use this instead.
"""

from MailFlower import MessageContent

SENDER_NAME = "John Doe"
SENDER_POSITION = "Outreach Director"
EMAIL_ADDRESS = "email@org.com"
YOUR_ORG = "ORG"
SYSTEM_PROMPT = f"""
    You are the Outreach Director for a student club at
    your university.
    
    Email Content:
    Good Afternoon, CONTACT
    I hope this email finds you well. My name is DIRECTOR, and I am the Outreach Director for the CLUB student chapter at the University.
    [INFO ABOUT YOUR ORGANIZATION] <- Filled by a human
    
    [YOUR PERSONAL TOUCH HERE] <- Filled by AI
    Thank you for your time, and I look forward to your response.
    
    Given the company you are asked about, you must research information about their values and work, and write
    in a persuasive tone about how their values align with ours and how their field of technology would
    provide a great opportunity for students, as well as networking opportunities.
    We are specifically inviting them to speak at one of our General Body Meetings
    There may also be some extra considerations, such as us having a past history with the company or lab in question.
    Be sure to bring up this information in your response
    [YOUR VALUES HERE] <- Filled by a human
    [PROVIDE EXAMPLE OUTPUT FOR BETTER RESPONSES]
    Example 1:
    We would love to hear insights into the world of Fintech from top engineers in the industry at Deloitte!
    Example 2:
    This would provide a great opportunity for students to learn more about the tech industry and AI, providing a great opportunity for learning and networking.  
    We would love to have a representative from Nvidia speak at one of our General Body Meetings and give their insights!
    """


# Wow I love HTML
def create_body_text(c: MessageContent, extra_content:str) -> str:
    return  f"""
    <html>
    <body>
    <span style="font-family: Georgia, serif; font-size: 11pt;">
    <p>
    Good Morning, {c.title} {c.lastname},
    </p>
    <p>
    [INSERT GREETING HERE]
    </p>
    <p>
    [ABOUT YOUR ORGANIZATION]
    </p>
    <p>
    {extra_content} We would love to have a representative from {c.company} speak at one of our GBM's this Fall!
    </p>
    <br>
    <p><span style="font-size: 11pt;">
    Thank you for your time, and I look forward to your response.
    </span></p>
    <br>
    <p><span style="font-size: 12pt;">
    Regards,
    </span></p>
    <p><span style="font-size: 16pt;"><b>
    {SENDER_NAME}
    </b></span></p>
    <p><span style="font-size: 14pt;"><b><i>
    {SENDER_POSITION}
    </i></b></span></p>
    <p><span style="font-size: 12pt;">
    ORGANIZATION
    </span></p>
    </span>
    <img src="cid:logo" alt="ORG Logo">
    </body>
    </html>
"""