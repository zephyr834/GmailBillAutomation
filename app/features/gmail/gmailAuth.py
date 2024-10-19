#!/usr/bin/env python
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

def get_credentials():  
    # If modifying these scopes, delete the file token.json.
    SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
    
    creds = None
    app_dir = os.getcwd()
    cred_file = "credentials.json"
    token_file = "token.json"
    cred_path = os.path.join(app_dir, cred_file)
    token_path = os.path.join(app_dir, token_file)
    
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(cred_path, SCOPES)
            creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
        with open(token_path, "w") as token:
            token.write(creds.to_json())
    
    return creds