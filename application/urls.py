from django.urls import path
from . import views

urlpatterns = [
    path('',views.dash,name='dash'),
    path('/home',views.home,name='home'),

    path('/login/add',views.loginadd,name='loginadd'),
    path('/loginprocess',views.loginprocess,name='loginprocess'),
    path('/login/change',views.loginchange,name='loginchange'),
    path('/login/forgot',views.loginforgot,name='loginforgot'),
    path('/slogout',views.slogout,name='logout'),


    path('/dash',views.dash,name='dash'),

    path('/admin/add',views.adminadd,name='adminadd'),
    path('/admin/inserted/',views.adminaddprocess,name='adminaddprocess'),
    path('/admin/view',views.adminview,name='adminview'),
    path('/admin/delete/<int:id>',views.admindelete,name='admindelete'),
    path('/admin/edit/<int:id>',views.adminedit,name="adminedit"),
    path('/admin/update/',views.adminupdate,name="adminupdate"),

    path('/FAQ/add',views.faqadd,name='faqadd'),
    path('/FAQ/inserted/',views.faqaddprocess,name='faqaddprocess'),
    path('/FAQ/view',views.faqview,name='faqview'),
    path('/FAQ/delete/<int:id>',views.faqdelete,name='faqdelete'),
    path('/FAQ/edit/<int:id>',views.faqedit,name="faqedit"),
    path('/FAQ/update/',views.faqupdate,name="faqupdate"),


    
    path('/booking/add',views.bookingadd,name='bookingadd'),
    path('/booking/inserted/',views.bookingaddprocess,name='bookingaddprocess'),
    path('/booking/view',views.bookingview,name='bookingview'),
    path('/booking/delete/<int:id>',views.bookingdelete,name='bookingdelete'),
    path('/booking/edit/<int:id>',views.bookingedit,name="bookingedit"),
    path('/booking/update/',views.bookingupdate,name="bookingupdate"),
    
    
    path('/category/add',views.categoryadd,name='categoryadd'),
    path('/category/inserted/',views.categoryaddprocess,name='categoryaddprocess'),
    path('/category/view',views.categoryview,name='categoryview'),
    path('/category/delete/<int:id>',views.categorydelete,name='categorydelete'),
    path('/category/edit/<int:id>',views.categoryedit,name="categoryedit"),
    path('/category/update/',views.categoryupdate,name="categoryupdate"),

    
    path('/subcategory/add',views.subcategoryadd,name='subcategoryadd'),
    path('/subcategory/inserted/',views.subcategoryaddprocess,name='subcategoryaddprocess'),
    path('/subcategory/view',views.subcategoryview,name='subcategoryview'),
    path('/subcategory/delete/<int:id>',views.subcategorydelete,name='subcategorydelete'),
    path('/subcategory/edit/<int:id>',views.subcategoryedit,name="subcategoryedit"),
    path('/subcategory/update/',views.subcategoryupdate,name="subcategoryupdate"),

    
    path('/image/add',views.imageadd,name='imageadd'),
    path('/image/inserted/',views.imageaddprocess,name='imageaddprocess'),
    path('/image/view',views.imageview,name='imageview'),
    path('/image/delete/<int:id>',views.imagedelete,name='imagedelete'),
    path('/image/edit/<int:id>',views.imageedit,name="imageedit"),
    path('/image/update/',views.imageupdate,name="imageupdate"),
    
    
    path('/offer/add',views.offeradd,name='offeradd'),
    path('/offer/inserted/',views.offeraddprocess,name='offeraddprocess'),
    path('/offer/view',views.offerview,name='offerview'),
    path('/offer/delete/<int:id>',views.offerdelete,name='offerdelete'),
    path('/offer/edit/<int:id>',views.offeredit,name="offeredit"),
    path('/offer/update/',views.offerupdate,name="offerupdate"),

    
    path('/product/add',views.productadd,name='productadd'),
    path('/product/inserted/',views.productaddprocess,name='productaddprocess'),
    path('/product/view',views.productview,name='productview'),
    path('/product/delete/<int:id>',views.productdelete,name='productdelete'),
    path('/product/edit/<int:id>',views.productedit,name="productedit"),
    path('/product/update/',views.productupdate,name="productupdate"),

    
    path('/user/add',views.useradd,name='useradd'),
    path('/user/inserted/',views.useraddprocess,name='useraddprocess'),
    path('/user/view',views.userview,name='userview'),
    path('/user/delete/<int:id>',views.userdelete,name='userdelete'),
    path('/user/edit/<int:id>',views.useredit,name="useredit"),
    path('/user/update/',views.userupdate,name="userupdate"),

    
    path('/feedback/add',views.feedbackadd,name='feedbackadd'),
    path('/feedback/inserted', views.feedbackaddprocess, name="feedbackaddprocess"),
    path('/feedback/view',views.feedbackview,name='feedbackview'),
    path('/feedback/delete/<int:id>',views.feedbackdelete,name='feedbackdelete'),
    path('/feedback/edit/<int:id>',views.feedbackedit,name="feedbackedit"),
    path('/feedback/update/',views.feedbackupdate,name="feedbackupdate"),

    
    path('/vendor/add',views.vendoradd,name='vendoradd'),
    path('/vendor/inserted', views.vendoraddprocess, name="vendoraddprocess"),
    path('/vendor/view',views.vendorview,name='vendorview'),
    path('/vendor/delete/<int:id>',views.vendordelete,name='vendordelete'),
    path('/vendor/edit/<int:id>',views.vendoredit,name="vendoredit"),
    path('/vendor/update/',views.vendorupdate,name="vendorupdate")


    
]