"""student URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sahil import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view.home),
    path('registration/',view.registration),
    path('view/',view.view),
    path('viewall/',view.viewall),
    path('viewbybatchtime/',view.viewbybatchtime),
    path('fviewbybatchtime/<str:fbtime>',view.fviewbybatchtime),

    path('viewbyregno/',view.viewbyregno),
    path('fviewbyregno/<str:fregno>',view.fviewbyregno),

    path('viewbyname/',view.viewbyname),
    path('fviewbyname/<str:fname>',view.fviewbyname),

    path('delete/',view.delete),
    
     
    path('update/',view.update), 
    path('update1/<str:fupdate>',view.update1), 
   
   
    path('fee/',view.fee),
    path('subfee/',view.subfee),
    path('subdatafee/<str:fregno>',view.subdatafee),

    path('viewfee/',view.viewfee),
    path('fviewfee/<str:fregno>',view.fviewfee),


    path('passoutdata/',view.passoutdata),
   
    

]
