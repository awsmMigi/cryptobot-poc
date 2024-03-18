import requests
import pandas as pd
from time import sleep
import pyttsx3

tts_engine = pyttsx3.init()

# Function to get crypto price
def get_crypto_price(tokens=['eth','wld','btc','xrp']):
    url = 'https://dummy-api.hivaibhav.xyz/api/price'
    payload = {
        'tokens': ','.join(tokens),
    }
    response = requests.get(url, params=payload)

    data = response.json()
    data_list = list(data.values())
    # print(data_list) 

    name, symbol, price, timestamp = [], [], [], []

    for token in data_list:
        name.append(token['name'])
        symbol.append(token['symbol'])
        price.append(token['price'])
        timestamp.append(token['timestamp'])

    raw_data = {
        'name': name,
        'symbol': symbol,
        'price': price,
        'timestamp': timestamp
    }
    df = pd.DataFrame(raw_data)

    return df

# Function to set alert
def set_alert(data_frame, asset, alert_high, alert_low):
    asset_value = data_frame.loc[data_frame['symbol'] == asset.upper()]['price'].item()
    # print(asset_value)

    prompt = f'{asset.upper()} High Alert: {alert_high}, {asset.upper()} Low Alert: {alert_low}\n[ {asset.upper()} Price: {asset_value} ]'

    if asset_value > alert_high:
        print(prompt +' <<--- It\'s High!!!\n')
        tts_engine.say(f'Alert {asset.upper()} is high 😂')
        tts_engine.runAndWait()
    elif asset_value < alert_low:
        print(prompt+' <<--- It\'s Low!!!\n')
        tts_engine.say(f'uffff! {asset.upper()} is low 🥲')
        tts_engine.runAndWait()
    else:
        print(prompt+'\n')
    

# Alert loop for crypto price
loop_count = 0
while True:
    print(f'################### Loop: {loop_count} ###################\n')

    try:
        data_frame = get_crypto_price(['eth','btc'])
        
        set_alert(data_frame, 'eth', 3636.63, 1000)
        set_alert(data_frame, 'btc', 50000, 30000)

    
    except Exception as e:
        print('We couldn\'t get the data. Error:', e)
    
    loop_count += 1
    sleep(10)

