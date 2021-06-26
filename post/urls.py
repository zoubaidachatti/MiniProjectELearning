from django.urls import path
from . import views
urlpatterns=[
    path('admin',views.home,name='home'),
    path('admin/add',views.add,name='add'),
    path('admin/update/<int:id>',views.update,name='update'),
    path('admin/delete/<int:id>',views.delete,name='delete'),
    

]