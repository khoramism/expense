from pyrogram import Client , filters 
from pyrogram.handlers import MessageHandler
#import models.Transaction
import json 
import os 
from peewee import *
import datetime
from jdatetime import JalaliToGregorian, GregorianToJalali

from dotenv import load_dotenv

db = SqliteDatabase('db.sqlite3')

class BaseModel(Model):
    class Meta:
        database = db

db.connect()

class Arz_Transaction(BaseModel):
    #username = CharField(unique=True)
	Choices = (
		('برداشت', 'withdrawal'),
		('واریز', 'deposit'),
	)

	reason =  CharField(default='-',max_length=50, null=True)
	
	Necessary =  BooleanField(default=True,  null=True)
	
	price =  BigIntegerField()

	full_content =  TextField()

	date  =  DateField(null=True)
	
	hour =  TimeField()

	action =  CharField(choices=Choices,max_length=50, default= 'برداشت')

	baghi =  BigIntegerField()


path = os.getcwd()

load_dotenv()

MY_ENV_VAR = os.getenv('tel_api_hash')
print(MY_ENV_VAR)

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
	if len(was) == 13 or len(was) == 12 :
		df['price'] = was[4]
		# Remove , from the SMS price 
		price = was[4]
		price = int(price.replace(',' ,''))

		baghi = was[-3]
		baghi = int(baghi.replace(',',''))

		dates= was[-2].split('/')
		gregorian_date_obj = JalaliToGregorian(int(dates[0]),int(dates[1]),int(dates[2]))
		gregorian_date =gregorian_date_obj.getGregorianList()
		rez = []
		for mn in gregorian_date:
			rez.append(str(mn))
		act_date = '-'.join(rez)

		
		Arz_Transaction.create(price=price, baghi = baghi, hour = was[-1],
								date=act_date, full_content=ksi,action=was[2])
		print('successfuly added!')
	else: 
		print('Message out of order biatch')

@app.on_message(filters.chat(target) & filters.text)
def my_handler(client, message):
	processr(message.text)

app.run()