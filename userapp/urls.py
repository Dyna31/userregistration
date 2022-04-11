from django.urls import path
from.import views

urlpatterns=[
    path('',views.user,name='user'),
    path('getdata',views.getdata,name='getdata'),
    path('tableview',views.tableview,name='tableview'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]