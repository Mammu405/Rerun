from django.urls import path
from freeapp import views

urlpatterns = [

    path('search/', views.search),
    
    path('', views.index),
    path('index2/', views.index2),
    path('index3/', views.index3),
    path('index4/', views.index4),
    path('index5/', views.index5),
    path('index6/', views.index6),
    path('contact/', views.contact),
    path('about/', views.about),
    path('tc/', views.tc),
    path('shop/', views.shop),
    path('buyer_register/', views.buyer_register),
    path('seller_register/', views.seller_register),
    path('Buyerlogin_check/', views.Buyerlogin_check),
    path('Sellerlogin_check/', views.Sellerlogin_check),
    path('admin_index/', views.admin_index),
    path('admin_login/', views.admin_login),
    path('logout/', views.logout),
    path('categories/', views.categories),
    path('category_list_admin/', views.category_list_admin),
    path('category_delete_admin/', views.category_delete_admin),
    path('buyer_list_admin/', views.buyer_list_admin),
    path('seller_list_admin/', views.seller_list_admin),
    path('product_details/', views.product_details),
    path('product_list_admin/', views.product_list_admin),
    path('fbooking_list_admin/', views.fbooking_list_admin),
    path('singleproduct_view/', views.singleproduct_view),
    path('fbooking/', views.fbooking),
    path('myorder/', views.myorder),
    path('orders/', views.orders),
    path('sellerapproval/', views.sellerapproval),
    path('booking/', views.booking),
    path('exchange/', views.exchange),
    path('exgsel/', views.exgsel),
    path('exguser/', views.exguser),
    path('ustep/', views.ustep),
    path('sstep/', views.sstep),
    path('selBank/', views.selBank),
    path('selindex/', views.selindex),
    path('selproducts_details/', views.selproducts_details),
    path('selnotification/', views.selnotification),
    path('usernotification/', views.usernotification),
    path('uprofile/', views.uprofile),
    path('uprofile_edit/', views.uprofile_edit),

    
    path('sprofile/', views.sprofile),
    path('sprofile_edit/', views.sprofile_edit),

    path('prd_delete/', views.prd_delete),
    path('prd_edit/', views.prd_edit),
    path('exgapproval/', views.exgapproval),
    path('Exchange_list_admin/', views.Exchange_list_admin),
    path('Payment_list_admin/', views.Payment_list_admin),
    path('Bankdetails_list_admin/', views.Bankdetails_list_admin),
    path('category_view/', views.category_view),
    path('vreview/', views.vreview),






    
   





    

]
