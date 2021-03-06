"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
# from product.views import ( 
#     product_detail_view,
#     product_create_view,
#     product_update_view,
#     # render_initial_data,
#     # dynamic_lookup_view,
#     product_delete_view,
#     product_list_view
# )
from pages.views import home_view, contact_view, about_view, settings_view 

urlpatterns = [
    # path('products/', product_list_view, name='product-list'),
    # path('products/create/', product_create_view, name='product-create'),
    # # path('products/<int:id>/', dynamic_lookup_view, name='product_detail'),
    # path('products/<int:id>/', product_detail_view, name='product_detail'),
    # path('products/<int:id>/delete/', product_delete_view, name='product-delete'),
    # path('products/<int:id>/update/', product_update_view, name='product-update'),
   
    path('blog/', include('blog.urls')),
    path('product/', include('product.urls')),
    path('courses/', include('courses.urls')),
    path('', home_view, name='home'),
    path('contact/', contact_view),
    path('about/<int:id>/', about_view,  name='product_detail'),
    # path('products/', product_detail_view),
    # path('create/', product_create_view),
    # path('create/',render_initial_data),
    path('settings/', settings_view),
    path('admin/', admin.site.urls),
]
