from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.homepage,name='homepage'),

    path('home',views.homepage,name='homepage'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('vdashboard',views.vdashboard,name='vdashboard'),

    path('contact',views.contact,name='contact'),

    path('offer',views.offer,name='offer'),

    path('about',views.about,name='about'),

    path('listing',views.productlisting,name='productlisting'),
    path('listing/<int:id>',views.productlistingbycategory,name='productlistingbycategory'),
    path('details/<int:id>',views.productdetails,name="productdetails"),

    path('logins',views.logins,name='logins'),
    path('loginprocess',views.loginprocess,name='loginprocess'),

    path('vlogins',views.vlogins,name='vlogins'),
    path('vloginprocess',views.vloginprocess,name='vloginprocess'),
    
    path('logout',views.logouts,name='logouts'),

    path('register',views.register,name='register'),
    path('register/inserted',views.registeraddprocess,name='registeraddprocess'),
    path('vregister',views.vregister,name='vregister'),
    path('vregister/inserted',views.vregisteraddprocess,name='vregisteraddprocess'),
    path('forgot',views.forgot,name='forgot'),
    path('forgot/inserted',views.forgotaddprocess,name='forgotaddprocess'),
    path('vforgot',views.vforgot,name='vforgot'),
    path('vforgot/inserted',views.vforgotaddprocess,name='vforgotaddprocess'),
    

    path('faq',views.faq,name='faq'),


    path('feedback',views.feedbackadd,name='feedbackadd'),
    path('feedback/inserted', views.feedbackaddprocess, name="feedbackaddprocess"),
    path('feedback/view',views.feedbackview,name='feedbackview'),

    path('booking',views.bookingadd,name='bookingadd'),
    path('booking/inserted', views.bookingaddprocess, name="bookingaddprocess"),
    path('booking/view',views.bookingview,name='bookingview'),
]