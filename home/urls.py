from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('inventory/', views.inventory, name='inventory'),
    path('orders/', views.orders, name='orders'),
    path('orders/new/', views.order_create, name='order_create'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('orders/<int:order_id>/delete/', views.order_delete, name='order_delete'),
     
 
    
   
    


    path('suppliers/', views.suppliers, name='suppliers'),
    path('suppliers/add/', views.add_supplier, name='add_supplier'),
    path('suppliers/edit/<int:pk>/', views.edit_supplier, name='edit_supplier'),
    path('delete-suppliers/', views.delete_suppliers, name='delete_suppliers'),




   
   

    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),



    #shipmetn part

     path('shipments/', views.shipments, name='shipments'),
    path('edit_shipment/', views.edit_shipment, name='edit_shipment'),
    path('shipments/add/', views.add_shipment, name='add_shipment'),
    path('delete_shipment/<int:shipment_id>/', views.delete_shipment, name='delete_shipment'),

    #inventoryy
    
    path('inventory/', views.inventory, name='inventory'),
    path('add-aisle/', views.add_aisle, name='add_aisle'),
    path('delete-aisle/<int:aisle_id>/', views.delete_aisle, name='delete_aisle'),
    path('aisle/<int:aisle_id>/', views.aisle_detail, name='aisle_detail'),
    path('aisle/<int:aisle_id>/items/', views.view_aisle_items, name='view_aisle_items'),
    path('add-item/', views.add_item, name='add_item'),
    path('aisle/<int:aisle_id>/add-item/', views.add_item_to_aisle, name='add_item_to_aisle'),
    path('item/delete/<int:item_id>/', views.delete_item, name='delete_item'),


    #reportsss

    path('reports/', views.reports, name='reports'),


    #dashboard connctionss

    

]
