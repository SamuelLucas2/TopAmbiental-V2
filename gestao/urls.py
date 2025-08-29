from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='home'),
    path('login/admin/', views.admin_login_view, name='admin_login'),
    path('login/cliente/', views.client_login_view, name='client_login'),
    path('logout/admin/', views.user_logout, name='admin_logout'),
    path('logout/cliente/', views.client_logout_view, name='client_logout'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/clientes/', views.client_list, name='client_list'),
    path('admin/clientes/novo/', views.client_create, name='client_create'),
    path('admin/clientes/<int:pk>/editar/', views.client_update, name='client_update'),
    path('admin/clientes/<int:pk>/excluir/', views.client_delete, name='client_delete'),
    path('admin/clientes/<int:pk>/', views.client_detail, name='client_detail'),
    path('admin/documentos/<int:doc_pk>/excluir/', views.delete_document, name='delete_document'),
    path('admin/usuarios/', views.user_list, name='user_list'),
    path('admin/usuarios/novo/', views.user_create, name='user_create'),
    path('admin/usuarios/<int:pk>/excluir/', views.user_delete, name='user_delete'),
    path('cliente/dashboard/', views.client_dashboard, name='client_dashboard'),
] 