import requests

def send_message(str):
    # Set the Telegram API token.
    apiToken = "Your Token"

    # Set the chat ID of the channel you want to send the message to.
    chatID1 = "6360011882"
    chatID2 = '817589113'

    # Set the text message you want to send.
    message = str
    # Create the request body.
    sendData1 = {
        "chat_id": chatID1,
        "text": message
    }
    sendData2 = {
    "chat_id": chatID2,
    "text": message
    }

    telegramURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    # Send the request to the Telegram API.
    response1 = requests.post(telegramURL, sendData1)
    response2 = requests.post(telegramURL, sendData2)

    # # Check the response status code.
    # if response1.status_code == 200:
    #     # The message was successfully sent.
    #     print("Message sent successfully!")
    # else:
    #     # An error occurred.
    #     print("Error sending message: {}".format(response1.status_code))

    # # Check the response status code.
    # if response2.status_code == 200:
    #     # The message was successfully sent.
    #     print("Message sent successfully!")
    # else:
    #     # An error occurred.
    #     print("Error sending message: {}".format(response2.status_code))

# if __name__ == '__main__':
#     send_message(city_number = '1')
