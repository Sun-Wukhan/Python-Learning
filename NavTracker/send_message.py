from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)


def send_alert_message(body):
    message = client.messages.create(
        from_='',
        body=body,
        to=''
)


