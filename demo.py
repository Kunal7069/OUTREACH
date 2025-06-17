import requests

# Your Dropbox app credentials
APP_KEY = "831rhakm1chm136"
APP_SECRET = "3litvdoqd1djj3c"
AUTH_CODE = "_Aas3UNMT58AAAAAAAAA2KWiuoCM_ncCqTI3FlWnHI4"
REDIRECT_URI = "https://www.sih.gov.in/"

# Dropbox token URL
TOKEN_URL = "https://api.dropboxapi.com/oauth2/token"

# Prepare the payload
payload = {
    "code": AUTH_CODE,
    "grant_type": "authorization_code",
    "client_id": APP_KEY,
    "client_secret": APP_SECRET,
    "redirect_uri": REDIRECT_URI
}

# Make the POST request to exchange code for tokens
response = requests.post(TOKEN_URL, data=payload)

# Parse response
if response.status_code == 200:
    tokens = response.json()
    print("✅ Access Token:", tokens.get("access_token"))
    print("✅ Refresh Token:", tokens.get("refresh_token"))
else:
    print("❌ Failed to get tokens")
    print("Status Code:", response.status_code)
    print("Response:", response.text)
