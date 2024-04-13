from django.urls import path
from . import views

urlpatterns = [
    path('',views.dash,name='dash'),

    path('/login/register',views.register,name='register'),
    path('/register/inserted',views.registerprocess,name='registerprocess'),
    path('/login/change',views.loginchange,name='loginchange'),
    path('/login/forgot',views.loginforgot,name='loginforgot'),
    path('/slogout',views.slogout,name='slogout'),


    path('/dash',views.dash,name='dash'),

    path('/home',views.home,name='home'),


    
    path('booking/add',views.bookingadd,name='bookingadd'),
    path('booking/inserted/',views.bookingaddprocess,name='bookingaddprocess'),
    path('/booking/view',views.bookingview,name='bookingview'),
    path('booking/delete/<int:id>',views.bookingdelete,name='bookingdelete'),
    path('booking/edit/<int:id>',views.bookingedit,name="bookingedit"),
    path('booking/update/',views.bookingupdate,name="bookingupdate"),
    
    
   

    
    

    
    path('/product/add',views.productadd,name='productadd'),
    path('/product/inserted/',views.productaddprocess,name='productaddprocess'),
    path('/product/view',views.productview,name='productview'),
    path('product/delete/<int:id>',views.productdelete,name='productdelete'),
    path('product/edit/<int:id>',views.productedit,name="productedit"),
    path('product/update/',views.productupdate,name="productupdate"),

    
   

    
    path('feedback/add',views.feedbackadd,name='feedbackadd'),
    path('feedback/inserted', views.feedbackaddprocess, name="feedbackaddprocess"),
    path('/feedback/view',views.feedbackview,name='feedbackview'),
    path('feedback/delete/<int:id>',views.feedbackdelete,name='feedbackdelete'),
    path('feedback/edit/<int:id>',views.feedbackedit,name="feedbackedit"),
    path('feedback/update/',views.feedbackupdate,name="feedbackupdate"),

    
   

    
]
