from django.urls import path, include

from S_Admin import views

urlpatterns = [

    # admin login

    path('',views.admin_login,name='admin_login'),
    path('admin_home/',views.admin_home,name='admin_home'),
    path('admin_home1/',views.admin_home1,name='admin_home1'),
    path('admin_logout/',views.admin_logout,name='admin_logout'),


    # state curd operations

    path('open_state/',views.open_state,name='open_state'),
    path('save_state/',views.save_state,name='save_state'),
    path('edit_state/',views.edit_state,name='edit_state'),
    path('update_state/',views.update_state,name='update_state'),
    path('delete_state/',views.delete_state,name='delete_state'),

    # city curd operations

    path('open_city/',views.open_city,name='open_city'),
    path('save_city/',views.save_city,name='save_city'),
    path('edit_city/',views.edit_city,name='edit_city'),
    path('update_city/',views.update_city,name='update_city'),
    path('delete_city/',views.delete_city,name='delete_city'),

    # area curd operations

    path('open_area/',views.open_area,name='open_area'),
    path('save_area/',views.save_area,name='save_area'),
    path('edit_area/',views.edit_area,name='edit_area'),
    path('update_area/',views.update_area,name='update_area'),
    path('delete_area/',views.delete_area,name='delete_area'),

    # type crud operations
    path('open_type/',views.open_type,name='open_type'),
    path('save_type/',views.save_type,name='save_type'),
    path('edit_restaurant_type/',views.edit_restaurant_type,name='edit_restaurant_type'),
    path('update_restaurant_type/',views.update_restaurant_type,name='update_restaurant_type'),
    path('delete_restaurant_type/',views.delete_restaurant_type,name='delete_restaurant_type'),

    # restaurant Info

    path('show_pending_restaurant_list/',views.show_pending_restaurant_list,name='show_pending_restaurant_list'),
    path('approved_restaurant_info/',views.approved_restaurant_info,name='approved_restaurant_info'),
    path('cancelled_restaurant_info/',views.cancelled_restaurant_info,name='cancelled_restaurant_info'),
    path('show_approved_restaurant_list/',views.show_approved_restaurant_list,name='show_approved_restaurant_list'),
    path('show_cancelled_restaurant_list/',views.show_cancelled_restaurant_list,name='show_cancelled_restaurant_list'),
    path('sample/',views.sample,name='sample'),
]
