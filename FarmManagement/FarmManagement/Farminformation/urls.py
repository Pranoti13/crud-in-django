from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Workerdetails/', views.index1, name='index1'),
    path('Workerdetails/add/', views.add, name='add'),
    path('Workerdetails/add/addrecord/', views.addrecord, name='addrecord'),
    path('Workerdetails/delete/<int:id>', views.delete, name='delete'),
    path('Workerdetails/update/<int:id>', views.update, name='update'),
    path('Workerdetails/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('Workers Payment History/', views.workerspayhistory, name='workerspayhistory'),
    path('Workers Payment History/addworkerpay/', views.addworkerpay, name='addworkerpay'),
    path('Workers Payment History/addworkerpay/addnewrecord/', views.addnewrecord, name='addnewrecord'),
    path('Workers Payment History/delete/<int:id>', views.deleteworkerpayhistory, name='deleteworkerpayhistory'),
    path('Workers Payment History/updateworkerpayhistory/<int:id>', views.updateworkerpayhistory,
         name='updateworkerpayhistory'),
    path('Workers Payment History/updateworkerpayhistory/updatepayrecord/<int:id>', views.updatepayrecord,
         name='updatepayrecord'),


]

