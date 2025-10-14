import PromptsAndStuff
import AugmentContent
import base64
import csv
import os.path
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.compose"]


class MessageContent():

    def __init__(self, email:str, firstname:str, lastname:str, title:str, company:str, considerations:str):
      self.email = email
      self.firstname = firstname
      self.lastname = lastname
      self.title = title
      self.company = company
      self.considerations = considerations

def init():
  # Get the credentials
  creds = validate_creds()
  if creds is None:
    print("Invalid Credentials")
    exit(1)

  try:
    # Call the Gmail API
    service = build("gmail", "v1", credentials=creds)
    return service

  except HttpError as error:
    print(f"An error occurred: {error}")

def create_draft(service, content:MessageContent):
    # Open ACM Logo file as binary
    with open("../assets/logo.png", "rb") as f:
      logo_data = f.read()
    
    # Open Outreach PDF file as binary
    with open("../assets/Outreach_Presentation.pdf", "rb") as f:
      presentation_data = f.read()

    # Create message
    encoded_message = create_message(content, logo_data, presentation_data)

    # Put message into draft form and execute making a draft
    draft_message = {"message": {"raw" : encoded_message}}
    draft = (
        service.users()
        .drafts()
        .create(userId="me", body=draft_message)
        .execute()
    )

    print(f'Draft id: {draft["id"]}\nDraft message: {draft["message"]}')

def create_message(content: MessageContent, logo_data, presentation_data) -> str:
    # Multipart allows putting multiple types of data
    message = MIMEMultipart("related")
    message["To"] = f"{content.email}"
    message["From"] = PromptsAndStuff.EMAIL_ADDRESS
    message["Subject"] = f"{content.company} x ACM@UCF Collaboration"

    # HTML Body content
    message_html = MIMEText(PromptsAndStuff.create_body_text(content, AugmentContent.get_extra_content(content.company, content.considerations)), "html")
    message.attach(message_html)

    # Inlined logo image
    logo = MIMEImage(logo_data, name="logo.png")
    logo.add_header("Content_ID", "<logo>")
    logo.add_header("Content_Disposition", "inline", filename="logo.png")
    logo.add_header("X-Attachment-Id", "logo")
    message.attach(logo)

    # Attached presentation PDF
    presentation = MIMEApplication(presentation_data, _subtype="pdf", name="Outreach_Presentation.pdf")
    presentation.add_header("Content_Disposition", "attachment", filename="Outreach_Presentation.pdf")
    message.attach(presentation)

    # Encode message to base64
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return encoded_message



# From the docs
def validate_creds():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("../secrets/token.json"):
      creds = Credentials.from_authorized_user_file("../secrets/token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
      else:
        flow = InstalledAppFlow.from_client_secrets_file(
            "../secrets/credentials.json", SCOPES
        )
        creds = flow.run_local_server(port=0)
      # Save the credentials for the next run
      with open("../secrets/token.json", "w") as token:
        token.write(creds.to_json())
    return creds

def main():
    service = init()

    # Loop through each item in the csv and create a draft email for each contact
    with open("../assets/contacts.csv", "r") as f:
      csv_reader = csv.DictReader(f)
      for row in csv_reader:
        if row["sent"] == "yes":
          continue
        content = MessageContent(row["email"], row["firstname"], row["lastname"], row["title"], row["company"], row["considerations"])
        print("Creating draft for:")
        for key in row:
          print(key + ":" + row[key])
        create_draft(service, content)
        print()
    

if __name__ == "__main__":
  main()
