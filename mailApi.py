import requests as requests

with open('apikey.txt', 'r') as f:
    api_key = f.read()

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox3fe2641695ac44f8887754cdc669e099.mailgun.org/messages",
        auth=("api", api_key),
        data={"from": "Excited User sandbox3fe2641695ac44f8887754cdc669e099.mailgun.org",
              "to": ["lurpos@spaml.de", "sandbox3fe2641695ac44f8887754cdc669e099.mailgun.org"],
              "subject": "Hello from Python",
              "text": "Testing some Mailgun awesomness!"})