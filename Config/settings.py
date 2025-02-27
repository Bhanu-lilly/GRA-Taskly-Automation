import pandas as pd
import requests
# import PyJWT

# # The API URL for chatbot suggestions
# url = "https://aex27yjqo6.execute-api.us-east-2.amazonaws.com/prod/ask"
# url = "https://3exg2qgqb3.execute-api.us-east-2.amazonaws.com/dev/ask"
url = "https://k77ornbz5e-vpce-058757a9c034d181c.execute-api.us-east-2.amazonaws.com/qa/ask"

import jwt

# # Corrected cookie_str with a valid cookie format
# cookie_str = "idtoken=abc123; path=https://; domain=qa.taskly.lilly.com"

# name = "idtoken"

# def get_cookie(cookie_str, name):
#     cookies = cookie_str.split('; ')
#     for cookie in cookies:
#         if '=' in cookie:
#             cookie_name, cookie_value = cookie.split('=', 1)
#             if cookie_name == name:
#                 return cookie_value
#     return None  # Return None if the cookie is not found

# def fetch_bearer_token(cookie_str):
#     # Get the 'idtoken' from the cookie string
#     token = get_cookie(cookie_str, name)
    
#     if token:
#         try:
#             # Optionally decode the JWT token
#             decoded = jwt.decode(token, options={"verify_signature": False})  # Disable signature verification (for simplicity)
            
#             # Extract username (optional)
#             username = decoded.get('name', 'Unknown User')  # Extract username
#             print(f"Decoded Username: {username}")  # Optional: Print the username
            
#             return decoded  # Optionally return the decoded token if needed
            
#         except jwt.ExpiredSignatureError:
#             print("Error: The token has expired.")
#         except jwt.InvalidTokenError:
#             print("Error: The token is invalid.")
#         except Exception as e:
#             print(f"Unexpected error during token decoding: {e}")
#         finally:
#             print("Finished processing the token.")
#     else:
#         print("Error: No token found in the cookie.")

# The Bearer token for authorization
BEARER_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImltaTBZMnowZFlLeEJ0dEFxS19UdDVoWUJUayJ9.eyJhdWQiOiJhYmYxM2Q0NC02ODQ4LTQ3YTgtOTMyMS04NmY4Y2UzN2YwNzMiLCJpc3MiOiJodHRwczovL2xvZ2luLm1pY3Jvc29mdG9ubGluZS5jb20vMThhNTlhODEtZWVhOC00YzMwLTk0OGEtZDg4MjRjZGMyNTgwL3YyLjAiLCJpYXQiOjE3NDA2Mzc1MTEsIm5iZiI6MTc0MDYzNzUxMSwiZXhwIjoxNzQwNjQxNDExLCJlbWFpbCI6ImJoYW51cHJhc2FkLm1vaGFwYXRyYUBuZXR3b3JrLmxpbGx5LmNvbSIsIm5hbWUiOiJCSEFOVSBQUkFTQUQgTU9IQVBBVFJBIC0gTmV0d29yayIsIm5vbmNlIjoiMDE5NTQ2MTktMjhiYS03Zjg4LTkyNzktNWZiYTAyZTFmMGIxIiwib2lkIjoiODI5MzljNjMtYjQ4OS00MjNjLTlmNzQtZGY5NWYzOTA3NzBlIiwicHJlZmVycmVkX3VzZXJuYW1lIjoiYmhhbnVwcmFzYWQubW9oYXBhdHJhQG5ldHdvcmsubGlsbHkuY29tIiwicmgiOiIxLkFSZ0FnWnFsR0tqdU1FeVVpdGlDVE53bGdFUTk4YXRJYUtoSGt5R0ctTTQzOEhNWUFMc1lBQS4iLCJzaWQiOiJkYjQ1MjNmMC1iYWQwLTQwZGItOTI5ZS01Njc2ODNiNjMzYTYiLCJzdWIiOiJmMm5XVlUwbGpNSndWZ1p6MEpFTXJrRnpuZEhFU3F6MmRhbXVTLTdGdnBNIiwidGlkIjoiMThhNTlhODEtZWVhOC00YzMwLTk0OGEtZDg4MjRjZGMyNTgwIiwidXRpIjoiQ3BDa1FVMWNTVWFTa011NnRCQnZBQSIsInZlciI6IjIuMCIsInVpZCI6IkwwNzQwMjgiLCJlbXBsb3llZV9pZCI6IjMwNzQwMjgifQ.J7GDXXfGAb-Bv-f4E6qVl6YEKI7DfoENl6yUXMNnpXtAR377AOOJj28n5yiNRdxsr05ycjSEuXZHD9A1SgfXwUBjMzCQQ_fQacQ-uHub1SG7yQicoXHRuC9a6q_J-M_bQxc2qnNAMGHCzi-1ZlwJZDMgpff1XvkoX01tWQfUuavZGfDGQypSl67X_fjfqfFvnF_AKCjoT2RKoTWlyo8P61D8Tf-wNxUGdQDYGzj7QNL_JSP8ah_pVUM3aXzAFNoopBw5lPdAUuLzWjBWORsj3eoTsNg6AoKTMNup_rm3uvE3IaOzbHwlUEi3u7QuQMAbRebPD2tQkw2KiOhI_5JLJg"

# Headers for the request
headers = {
    'Authorization': f'Bearer {BEARER_TOKEN}',
    'Accept': 'application/json',
}






    
