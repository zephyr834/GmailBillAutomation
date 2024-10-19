#!/usr/bin/env python
from googleapiclient.errors import HttpError

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