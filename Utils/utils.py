import requests
import json
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def load_user_queries_from_excel(excel_file):
    # Read the Excel file into a DataFrame (using openpyxl engine for .xlsx files)
    df = pd.read_excel(excel_file, engine='openpyxl')

    # Print the columns to confirm the correct column name
    print("Columns in the Excel file:", df.columns)

    # Standardize column names: remove extra spaces and convert to lowercase
    df.columns = df.columns.str.strip().str.lower()

    # Extract the questions from the 'user query' column
    if 'user query' not in df.columns:
        raise ValueError("Column 'user query' not found in the Excel file.")

    user_queries = df['user query'].tolist()
    return user_queries

def format_response(response_json):
    if not response_json:
        return "Error: No valid response to format."

    # Extract the 'answer' and split by newline to get steps
    steps = response_json.get("result", {}).get("answer", "").split("\n")

    # Build the formatted text
    formatted_answer = "\n".join(steps)

    # Add "For more information" section with file links
    formatted_answer += "\n\nFor more information, please refer to files below:"

    # Append the source links if available
    for link in response_json.get("result", {}).get("source_link", []):
        formatted_answer += f"\n{link.get('filename', '')}"

    return formatted_answer

# Function to save responses back to a new Excel file
def save_responses_to_excel(responses, excel_file):
    # Load the existing Excel file into a DataFrame
    df = pd.read_excel(excel_file, engine='openpyxl')
    
    # Check if the length of responses matches the number of rows in the DataFrame
    if len(responses) != len(df):
        raise ValueError("Number of responses does not match the number of rows in the Excel file.")

    # Add or overwrite the 'API response' column using a loop
    for idx, query in enumerate(df['User query']):
        df.at[idx, 'API response'] = responses[idx]

    # **DO NOT** overwrite the input file. Save to a new file
    output_file = "/Users/L074028/Documents/output.xlsx"  # New path to save the output in Documents folder
    
    # Save the updated DataFrame to the new Excel file (output.xlsx)
    df.to_excel(output_file, index=False, engine='openpyxl')
    
    print(f"Responses saved to {output_file}")



# def send_email_with_attachment(subject, body, to_email, attachment_path):
#     # Sender's email credentials (Outlook email and app password if using 2FA)
#     sender_email = "bhanuprasad.mohapatra@network.lilly.com"  # Replace with your Outlook email
#     sender_password = "Bengaluru@123"  # Replace with your Outlook password or app password if 2FA enabled

#     # Create a MIMEMultipart message
#     msg = MIMEMultipart()
#     msg['From'] = sender_email
#     msg['To'] = to_email  # To can be a single or multiple emails
#     msg['Subject'] = subject

#     # Attach the body message
#     msg.attach(MIMEText(body, 'plain'))  # Correct way to attach the body as text

#     # Attach the Excel file (or any other file)
#     try:
#         attachment = open(attachment_path, "rb")
#         part = MIMEBase('application', 'octet-stream')
#         part.set_payload(attachment.read())
#         encoders.encode_base64(part)
#         part.add_header('Content-Disposition', f"attachment; filename={os.path.basename(attachment_path)}")
#         msg.attach(part)
#         attachment.close()
#     except Exception as e:
#         print(f"Error attaching file: {e}")
#         return

#     # Set up the Outlook SMTP server (use 587 for TLS)
#     try:
#         server = smtplib.SMTP('smtp.office365.com', 587)
#         server.starttls()  # Start TLS encryption
#         server.login(sender_email, sender_password)  # Login to your Outlook account

#         # Send the email
#         text = msg.as_string()
#         server.sendmail(sender_email, to_email, text)
#         server.quit()
#         print(f"Email successfully sent to {to_email}")
#     except Exception as e:
#         print(f"Error sending email: {e}")




