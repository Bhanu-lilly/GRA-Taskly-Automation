
    # Main execution flow
from Api.chatbot_api import get_chatbot_response
from Config.settings import url, headers
from Utils.utils import format_response, save_responses_to_excel,load_user_queries_from_excel

if __name__ == "__main__":
    responses = []
    excel_file = 'data/Input.xlsx'  # Path to the input file
    user_queries = load_user_queries_from_excel(excel_file)  # Load user queries from Excel
    
    # Loop through each question and get the response from the chatbot API
    for question in user_queries:
        print(f"Fetching answer for: {question}")
        response_json = get_chatbot_response(url, question, headers=headers)
        print(response_json)
        
        if response_json:
            formatted_answer = format_response(response_json)
            responses.append(formatted_answer)
            print(f"Response: {formatted_answer}")
        else:
            responses.append("Error: No response received")

    # Save all responses back to the Excel file
    save_responses_to_excel(responses, excel_file)
    
    # # After saving, send the email with the attachment
    # send_email_with_attachment(
    #     subject="GRA Automated Response",  # Email subject
    #     body="Please find the attachment with the Tasly chatbot automated response.",  # Email body
    #     to_email="kulkarni_sowmya@lilly.com",  # Recipient's email
    #     attachment_path=excel_file  # Path to the Excel file to attach
    # )
