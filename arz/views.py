from tempfile import tempdir
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView
from .models import Transaction
# Create your views here.
def nig_view(request):
    pass

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
