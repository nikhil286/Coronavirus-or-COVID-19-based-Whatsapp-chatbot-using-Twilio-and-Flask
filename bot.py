from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from bs4 import BeautifulSoup
import csv
import pandas as pd

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    #Scraping Data
    source = requests.get("https://www.mohfw.gov.in/").text
    soup = BeautifulSoup(source, 'lxml')
    table = soup.find('table', class_='table table-striped').tbody

    t_headers = ['State','Confirmed cases','Cured/Migrated','Deaths']
    table_data = []
    for tr in table.find_all("tr"):
        t_row = {}
        for td, th in zip(tr.find_all("td")[1:], t_headers): 
            t_row[th] = td.text.replace('\n', '').strip()
        table_data.append(t_row)

    #Converting data to DataFrame
    dataset = pd.DataFrame(table_data)
    dataset = dataset[:-2]
    dataset['State'] = dataset['State'].str.lower()
        
    State = request.values.get('Body', '').lower() #User input State value
    resp = MessagingResponse()
    msg = resp.message()
    
    #Find row number of Input State in DataFrame
    try:
        row_index = dataset.loc[dataset['State'] == State].index[0]
        Confirmed = dataset.at[row_index, 'Confirmed cases']
        Cured = dataset.at[row_index, 'Cured/Migrated']
        Deaths = dataset.at[row_index, 'Deaths']
       
        res = f'COVID-19 situation in {State} \nConfirmed cases : {Confirmed} \nCured/Migrated : {Cured} \nNo. of Deaths : {Deaths} \n#StayAtHome'
        msg.body(res)
        
    except Exception as e:
        msg.body('Please Enter correct info')
        

    return str(resp)

if __name__=='__main__':
    app.run(debug=True)
