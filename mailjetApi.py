from mailjet_rest import Client
import os

with open('mailjet_api_key.txt', 'r') as f:
    api_key1 = f.read()

with open('mailjet_api_secret.txt', 'r') as f:
    api_secret1 = f.read()

#     # Get your environment Mailjet keys
# API_KEY = os.environ['MJ_APIKEY_PUBLIC']
# API_SECRET = os.environ['MJ_APIKEY_PRIVATE']
#
# mailjet = Client(auth=(API_KEY, API_SECRET))

api_key = api_key1
api_secret = api_secret1

mailjet = Client(auth=(api_key, api_secret), version='v3.1')
data = {
  'Messages': [
    {
      "From": {
        "Email": "dolev146@gmail.com",
        "Name": "dolev"
      },
      "To": [
        {
          "Email": "dolev146@gmail.com",
          "Name": "dolev"
        }
      ],
      "Subject": "Greetings from Mailjet.",
      "TextPart": "My first Mailjet email",
      "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
      "CustomID": "AppGettingStartedTest"
    }
  ]
}
result = mailjet.send.create(data=data)
print(result.status_code)
print(result.json())
