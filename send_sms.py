from twilio.rest import Client
import yaml

with open("parameters.yaml") as f:
    params = yaml.load(f, Loader=yaml.FullLoader)

sender_number = params["sender_number"]
account_sid = params["account_sid"]
auth_token = params["auth_token"]
client = Client(account_sid, auth_token)


def send_message(msg: str, to_number: str):
    """This function sends the given message to the requested number
    """
    message = client.messages.create(to=to_number, from_=sender_number, body=msg)
    print(f"Message sent successfully : {message.sid}")


if __name__ == "__main__":
    send_message("Hey this is test from Twilio ! ", "+91xxxxxxxx")
