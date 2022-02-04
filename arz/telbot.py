#from pyrogram import Client , filters 
#from pyrogram.handlers import MessageHandler
#from .models import Transaction 
import json 
import os 
path = os.getcwd()

from dotenv import load_dotenv
load_dotenv()

MY_ENV_VAR = os.getenv('tel_api_hash')
print(MY_ENV_VAR)
"""
app = Client(
	'my_account',
	api_id = os.getenv('tel_api_id'),
	api_hash = os.getenv('tel_api_hash'),
	)

target = -1001508172738  # "me" refers to your own chat (Saved Messages)
'''
def process_data(dics):
	df = {}
	was = ksi.split()
	if len(was) == 13:
		df['price'] = was[4]
		price = was[4]
		price = int(price.replace(',' ,''))
		#df['baghi'] = was[-3]
		#df['hour']= was[-1]
		#df['date']= was[-2]
		#print(df)]
		baghi = was[-3]
		baghi = int(baghi.replace(',',''))'''

def processr(ksi):
	df = {}
	was = ksi.split()
	if len(was) == 13:
		df['price'] = was[4]
		price = was[4]
		price = int(price.replace(',' ,''))
		#df['baghi'] = was[-3]
		#df['hour']= was[-1]
		#df['date']= was[-2]
		#print(df)]
		baghi = was[-3]
		baghi = int(baghi.replace(',',''))
		Transaction.object.create(price=price, baghi = was[-3], hour = was[-1], date=was[-2], full_content=ksi, action=was[2])
	else: 
		print('Message out of order biatch')

@app.on_message(filters.chat(target) & filters.text)
def my_handler(client, message):
	processr(message.text)
	
app.run()	
"""