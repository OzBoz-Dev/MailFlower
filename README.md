# MailFlower

An automated Email drafting tool for the Gmail API, with AI message personalization powered by Ollama!

## Installation:

Pull this GitHub repository:
```
git clone --depth 1 https://github.com/OzBoz-Dev/MailFlower.git
```

Install the required packages
```
pip install -r requirements.txt
```

## Setup:

**IMPORTANT: This project will not work out of the box. You will need to provide a few things.**

### Ollama:
#### Installing Ollama:
This project uses Ollama, a solution allowing you to run lightweight LLM models on your own device. This means that you will need to download and install Ollama on the device you want to run this script on. Ollama can be downloaded [here.](https://ollama.com/)

#### Once Ollama is Installed
Pull the model you want to use. In this case, I am using Google Gemma 3 with 4b parameters. Depending on the specs of your system, you may want to use a more or less powerful model. Make sure to specify the model in AugmentContent.py. If Gemma 3 4b is too heavy for your system, you can try Gemma 3 1b, or Gemma 3n, a more lightweight model.

```
ollama pull gemma3:4b
```

### Secrets:
- credentials.json: This is your Gmail API Key. You must download this from your Google Cloud console and place it in the /secrets/ directory.
    - For more information, [read the docs.](https://developers.google.com/workspace/gmail/api/quickstart/python)
- token.json: Provided you put the credentials in the right place, on the first run, you will be prompted to log in and link your account to this app. 
    - If you see an error saying "Access Blocked", make sure to add the Gmail account you want to use as a test user in the Google Cloud Console. [More info.](https://stackoverflow.com/questions/75454425/access-blocked-project-has-not-completed-the-google-verification-process)
    - Once successful, token.json should appear in the /secrets/ directory.
- PromptsAndStuff.py: This is where system prompts and the HTML body are kept. I have included a file called **PromptsAndStuff_template.py** in /src/ with a sample. Edit however you see fit and rename the file to use.

### Assets:
These are the files that MailFlower needs to read in. You will need to provide them yourself. If you do not want to attach them, you will need to remove the corresponding code.
- contacts.csv: This file will contain your "mailing list". It includes fields for email, first name, last name, company, extra considerations for the LLM, and whether or not the file has been sent. An example template has been provided in **contacts_template.csv** in /assets/.
- logo.png: This is an organization logo that you can embed into the email body.
- Outreach_Presentation.pdf: This is a pdf presentation that you can attach to the email.


## Usage:
Once all setup is complete, simply run MailFlower.py

```
python MailFlower.py
```

The script will go through every email on the mailing list that hasn't been marked as sent. 

For each email, you will be asked to review output from the LLM. If you are not satisfied with the output, answer "n" when prompted, add feedback, and rerun the message generation. Answer  "Y" once you are happy with the output. MailFlower will then create a ready-made draft in your Gmail accounnt.

If you would like to test prompts and responses, you can also run AugmentContent.py, manually changing the prompt and provided example until you get responses you find fit.

```
python AugmentContent.py
```

## Issues and Contributions
If you are having any problems, please feel free to open an issue. Pull requests are welcome.

## License
[MIT](https://choosealicense.com/licenses/mit/)
