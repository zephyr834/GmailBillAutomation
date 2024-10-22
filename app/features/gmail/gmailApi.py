#!/usr/bin/env python
from googleapiclient.errors import HttpError
import base64

class GmailApi():
    
    def __init__(self, service):
        self.service = service
        
    def getLabels(self):
        try:
            # Call the Gmail API
            results = self.service.users().labels().list(userId="me").execute()
            labels = results.get("labels", [])

            if not labels:
                print("No labels found.")
                return
            print("Labels:")
            for label in labels:
                print(label["name"])

        except HttpError as error:
            # TODO(developer) - Handle errors from gmail API.
            print(f"An error occurred: {error}")
            
    def getMessages(self, query):
        results = self.service.users().messages().list(userId="me", q=query).execute()
        return results
    
    def getMessageById(self, msgId):
        msg = self.service.users().messages().get(userId="me", id=msgId, format="raw").execute()
        return msg
    
    def parseMessage(self, message):
        if message:
            return base64.urlsafe_b64decode(message['raw'].encode('ASCII')).decode('utf-8')
        
        return None