import requests
from google_auth_oauthlib.flow import InstalledAppFlow
from config import client_id, client_secret, refresh_token, credentials_file

class Token:

    def __init__(self, client_id, client_secret, refresh_token, credentials_file, scopes=None):
        # Initialize client information
        self.client_id = client_id
        self.client_secret = client_secret
        self.refresh_token = refresh_token
        self.credentials_file = credentials_file
        self.scopes = 'https://www.googleapis.com/auth/youtube.force-ssl'
        self.access_token = None  # Access token will be set by methods





    def get_initial_token(self):
        """Runs the OAuth flow to obtain an initial access and refresh token."""
        flow = InstalledAppFlow.from_client_secrets_file(self.credentials_file, self.scopes)
        creds = flow.run_local_server(port=8080)
        
        # Access and refresh tokens
        self.access_token = creds.token
        self.refresh_token = creds.refresh_token  # Save refresh token for future use
        print("Initial Access Token:", self.access_token)
        print("Initial Refresh Token:", self.refresh_token)
        
        return self.access_token

    def refresh_access_token(self):
        """Uses the refresh token to obtain a new access token."""
        token_url = "https://oauth2.googleapis.com/token"
        
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": self.refresh_token,
            "grant_type": "refresh_token"
        }
        
        response = requests.post(token_url, data=data)
        
        if response.status_code == 200:
            tokens = response.json()
            self.access_token = tokens.get('access_token')
            print("Refreshed Access Token:", self.access_token)
            return self.access_token
        else:
            print("Error: Unable to refresh token. Status code:", response.status_code)
            return None
        
        
    # helper function to handle fauiler 
    def refactor(self):

        if not self.refresh_access_token():
            #print("Refreshing token failed. Running initial OAuth flow...")
            self.initial = self.get_initial_token()
            #print("This is the initial token:", self.initial)
        else:
            #print("This is the refreshed token:", self.refreshed_token)
            return self.refresh_access_token

            
        
        
def main():
    
    token_handler = Token(client_id, client_secret, refresh_token, credentials_file)
    
    refreshed_token = token_handler.refresh_access_token()
    tok = token_handler.refactor()

    
    

if __name__ == "__main__":
    main()
