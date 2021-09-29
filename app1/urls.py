
from django.urls import path,include
from.import views
urlpatterns = [
   path('',views.IndexFun,name='index'),  
   path('about',views.AboutFun,name='about'),
   path('contact',views.contactFun,name='contact')

  
]

    



