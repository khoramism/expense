from django.urls import path
from . import views 
app_name = 'transaction'
urlpatterns = [
    path('detail/<int:id>/', views.transaction_detail ,name = 'detail'), 
    path('', views.TransactionListView.as_view(), name='transaction-list'),
    path('create/',views.TransactionCreateView.as_view(), name='create'),
]
