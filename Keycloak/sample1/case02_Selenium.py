from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urlparse, parse_qs
import requests
import time
from datetime import datetime
import jwt
import getpass

AUTH_URL = "http://localhost:8080/realms/sample_realm/protocol/openid-connect/auth"
TOKEN_URL = "http://localhost:8080/realms/sample_realm/protocol/openid-connect/token"
REDIRECT_URI = "http://localhost:3000/callback"
RESPONSE_TYPE = "code"
CLIENT_ID = "sample_client"
CLIENT_SECRET = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
SCOPE = "openid"
STATE = "1234567890abcdef"
# username = input("input username : ")
# password = getpass.getpass("input password : ")
# USERNAME = username  # Keycloak username
# PASSWORD = password  # Keycloak password
USERNAME = "user1"
PASSWORD = "1234"

def decode_token(access_token):
    try:
        decoded_payload = jwt.decode(access_token, options={"verify_signature": False, "verify_aud": False})
        print("Decoded Token Payload:", decoded_payload)

        if "sub" in decoded_payload:
            print("User ID (sub):", decoded_payload["sub"])
        if "preferred_username" in decoded_payload:
            print("Username:", decoded_payload["preferred_username"])

        return decoded_payload  # Return the decoded payload

    except jwt.exceptions.DecodeError:
        print("Error: Failed to decode the token.")
        return None

def get_token_expiry(access_token):
    try:
        decoded_payload = jwt.decode(access_token, options={"verify_signature": False, "verify_aud": False})
        if "exp" in decoded_payload:
            expiry_time = datetime.utcfromtimestamp(decoded_payload["exp"])
            return expiry_time
        else:
            print("Expiration field ('exp') not found in token.")
            return None
    except jwt.exceptions.DecodeError:
        print("Error: Failed to decode the token to check expiry.")
        return None

def main():
    # Create authentication URL
    auth_url = f"{AUTH_URL}?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type={RESPONSE_TYPE}&scope={SCOPE}&state={STATE}"

    # Set up web browser
    driver = webdriver.Chrome()  # Ensure you have the proper webdriver set up
    driver.get(auth_url)

    try:
        # Step 1: Log in to Keycloak
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys(USERNAME)

        next_button = driver.find_element(By.ID, "kc-login")
        next_button.click()
        time.sleep(2)

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys(PASSWORD)

        login_button = driver.find_element(By.ID, "kc-login")
        login_button.click()
        time.sleep(3)

        # Step 2: Get authorization code
        current_url = driver.current_url
        print("Redirect URL:", current_url)

        parsed_url = urlparse(current_url)
        query_params = parse_qs(parsed_url.query)
        auth_code = query_params.get("code", [None])[0]

        if auth_code:
            print("Authorization Code:", auth_code)

            # Step 3: Exchange code for token
            token_payload = {
                "grant_type": "authorization_code",
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "code": auth_code,
                "redirect_uri": REDIRECT_URI,
            }
            token_response = requests.post(TOKEN_URL, data=token_payload)

            if token_response.status_code == 200:
                token_data = token_response.json()
                access_token = token_data.get("access_token")

                print("Access Token          : ", access_token)
                print("Refresh Token         : ", token_data.get("refresh_token"))

                # Decode and check token expiry
                decoded_payload = decode_token(access_token)
                expiry_time = get_token_expiry(access_token)

                if expiry_time and expiry_time < datetime.utcnow():
                    print("Token is expired:", expiry_time)
                else:
                    print("Token is valid:", expiry_time)

            else:
                print("Failed to retrieve token. Response:", token_response.status_code, token_response.text)
        else:
            print("Authorization Code not found.")

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    main()
