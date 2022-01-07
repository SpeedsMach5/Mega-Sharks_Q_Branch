from alpaca_trade_api.stream import Stream
from dotenv import load_dotenv
load_dotenv()
import os
import websocket, json
pkey = os.getenv("APCA_API_KEY_ID")
skey = os.getenv("APCA_API_SECRET_KEY_ID")
# print(type(pkey))
# print(type(skey))

async def trade_callback(t):
    print('trade', t)


async def quote_callback(q):
    print('quote', q)

stream = Stream(pkey,
                skey,
                base_url=('https://paper-api.alpaca.markets'),
                data_feed='iex')

stream.subscribe_trades(trade_callback, 'AAPL')
stream.subscribe_quotes(quote_callback, 'IBM')

stream.run()
# Alpaca Websocket
# def on_open(ws):
#     print("opened")
    
#     auth_data = {
#         "action": "authenticate",
#         "params": {"key_id":pkey,
#         "secret_key":skey }
#     }

#     ws.send(json.dumps(auth_data))

#     listen = {"action": "listen", "data":
#      {"streams": ["T.SPY"]}}

#     ws.send(json.dumps(listen))


# def on_message(ws, message):
#     print("received a message")
#     print(message)

# def on_close(ws):
#     print("closed connection")

# socket = 'wss://data.alpaca.markets/stream'

# ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message)
# ws.run_forever()