from twilio.rest import Client
import os

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
numbers = os.environ.get("DISTRO_NUMBERS").split(',')
from_number = os.environ.get("TWILIO_NUMBER")

def octopus(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    incoming = request.values.get('Body', None)
    print(incoming)

    client = Client(account_sid, auth_token)
    for number in numbers:
        client.messages.create(
            from_ = from_number,
            body=incoming,
            to=number
        )

    return f'ok'
