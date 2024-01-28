from twilio.rest import Client

account_sid = 'ACd1cce4783bf5ac8bab0ca1c5d1c23db6'
auth_token = 'cb37aab42510523756503bc7054ece44'
client = Client(account_sid, auth_token)


def send_alert_message(body):
    message = client.messages.create(
        from_='+14697707269',
        body=body,
        to='+16478222203'
)


