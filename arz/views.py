from gettext import install
from tempfile import tempdir
from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from .models import Transaction
from pyrogram import Client , filters 
from pyrogram.handlers import MessageHandler
import json 
import os 
from .forms import TransactionUpdateForm
path = os.getcwd()
from dotenv import load_dotenv
load_dotenv()
TEL_API_ID = os.getenv('tel_api_id')
TEL_API_HASH = os.getenv('tel_api_hash')
# Create your views here.
def tel_view():
    MY_ENV_VAR = os.getenv('tel_api_hash')
    print(MY_ENV_VAR)
    app = Client(
        'my_account',
        api_id = TEL_API_ID,
        api_hash = TEL_API_HASH,
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
            baghi = int(baghi.replace(',',''))
    '''

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


def trans_update(request, id):
    instance = get_object_or_404(Transaction, id=id )
    form = TransactionUpdateForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request)
    


class TransactionListView(ListView):
    model = Transaction
    fields = '__all__'
    template_name = 'transaction/transaction_list.html'
    paginate_by = 100 

class TransactionDetailView(DetailView):
    model = Transaction
    fields = '__all__'
    template_name = 'transaction/transaction_detail.html'

def transaction_detail(request, id):
    obj = get_object_or_404(Transaction, id=id)
    return render(request,'transaction/transaction_detail.html', {'obj':obj,})

class TransactionCreateView(CreateView):
    model = Transaction
    fields = '__all__'
    template_name = 'transaction/transaction_create.html'

