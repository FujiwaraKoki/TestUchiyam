from django.urls import path
from . import views
from django.conf.urls import handler404 #2024年8月14日追加
from accounts.views import show_error_page #2024年8月14日追加
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('regist/', views.regist, name='regist'),
    path('counselor_regist/', views.counselor_regist, name='counselor_regist'),
    path('counselor_login/', views.counselor_login, name='counselor_login'),
    path('counselor_logout/', views.counselor_logout, name='counselor_logout'),
    path('counselor_edit/', views.counselor_edit, name='counselor_edit'),
    path('activate_user/<uuid:token>/', views.activate_user, name='activate_user'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('user_edit/', views.user_edit, name='user_edit'),
    path('change_password/', views.change_password, name='change_password'),
    path('counselor_profile/', views.counselor_profile, name='counselor_profile'),
]

# handler404 = 'accounts.views.show_error_page'

handler404 = show_error_page

# from django.conf.urls import handler404
# handler404 = 'django.views.defaults.page_not_found'