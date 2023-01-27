
from django.contrib import admin
from django.urls import path
from app import views
from django.contrib.auth import  views as auth_views
from .forms import LoginForm
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.ProductView.as_view(),name='home'),
    path('base/',views.base),
    path('productdetails/<int:pk>',views.ProductDetailView.as_view(),name='product-details'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('search', views.search, name='search'),
    path('orders/', views.orders, name='orders'),
    path('mobile/<slug:data>', views.mobile, name='mobile'),
    path('recommendation/',views.Recommendation,name='recommendation'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm)),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
