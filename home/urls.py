from django.urls import path, include, re_path
from django.conf.urls import url
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact),
    path('about/', views.about),
    path('about/developer/', views.aboutdeveloper),
    path('feedback/', views.feedback),
    path('stopworking/', views.stopworking),
    path('history/', views.history, name='history'),
    path('order/', views.orderspage, name='order'),
    path('order/accept/', views.acceptorder),
    path('location/<str:location>/', views.handlelocation, name='location'),
    path('location/<str:location>/<str:restaurant>', views.handlelocationrestaurant),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/increase/', views.increase),
    path('checkout/decrease/', views.decrease),
    path('checkout/promo/', views.promo),
    path('checkout/placeorder/', views.placeorder),
    path('login/', views.handlelogin),
    re_path(r'[a-zA-Z0-9/!@#$%^&*]*logout[a-zA-Z0-9/!@#$%^&*]*', views.handlelogout),
    path('signup/', views.handlesignup),
    # path('viewprofile/logout/', views.handlelogout),
    path('viewprofile/', views.viewprofile, name='profile'),
    path('viewprofile/account/viewprofile/', views.viewprofile2),
    path('viewprofile/account/', views.account, name='account'),
    path('viewprofile/account/addaddress/', views.addadress),
    path('viewprofile/account/updateaddress/', views.updateaddress),
    path('viewprofile/account/addphone/', views.addphone),
    path('viewprofile/account/updatephone/', views.updatephone),
    path('viewprofile/account/editimage/', views.editimage),

    path('viewprofile/accept/', views.acceptrestaurant),
    path('viewprofile/reject/', views.rejectrestaurant),

    path('viewprofile/additem/', views.additem),

    path('viewprofile/removerestaurant/', views.removerestaurant),
    path('viewprofile/removecustomer/', views.removecustomer),

    # JSON
    path('new_restaurants_request_json/', views.new_restaurants_request_json, name='new_restaurants_request_json'),
    path('owners_json/', views.owners_json, name='owners_json'),
    path('users_json/', views.users_json, name='users_json'),
    path('customers_count_json/', views.get_customers_count_json, name='customers_count_json'),
]