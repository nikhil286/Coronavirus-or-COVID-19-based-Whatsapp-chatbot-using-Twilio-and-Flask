#Corona Virus/COVID-19 based Whatsapp chatbot using Twilio and Flask
A Whatsapp bot that provides corona virus(COVID-19) related information of India.
It accesses https://www.mohfw.gov.in/ to scrap data reagrding COVID19 using Beautiful Soup. 

Steps to be Followed (for Windows):

1) Make an account on Twilio (twilio.com)
2) Go to Programmable SMS >> Whatsapp. Follow the instructions to connect your whatsapp account with twilio.
3) Run following commands in cmd-->

        a) cd\Desktop
        b) mkdir Bot  -----> creating Bot folder in Desktop
        c) cd\Bot
        Paste bot.py in Bot folder.
        d) python -m venv botvenv       #creating python virtual environment named "botvenv"
        e) botvenv\Scripts\activate     #activate virtual environment
        f) pip install twilio flask requests    #installing required libs in our virtual environment.
        g) python bot.py                #run bot.py
        
        Here, observe the port number in your local IP address.
        
4) Now, to get URL, download ngrok
5) Install and run ngrok application, cmd opens up. Run --> ngrok http 'PORT number' ----> Use PORT number observed above.
6) ngrok provides a temporary IP address. Copy and paste it in twilio sandbox cofiguration (WHEN A MESSAGE COMES IN) and append "/sms"      at the end of the IP address. Click save.
7) Everything is done, now after you have joined the twilio whatsapp chat, type the name of any Indian state for which you want to          retrieve information.

NOTE* - You can deploy your application on cloud services like heroku to get a personel URL, hence your chatbot would work anytime.
        


        
