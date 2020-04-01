from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def bot():
    user_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    flag = False
    if 'quote' in user_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, Try again later aligator!!.'
        msg.body(quote)
        flag = True
        
    if 'cat' in user_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        flag = True
    if not flag:
        msg.body('The server may be down, try again later!')
    return str(resp)

if __name__=="__main__":
    app.run(debug=True)
