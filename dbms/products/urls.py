from django.urls import path, include
from products import views
# from dbms.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT

from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_product, name="add"),
    path('update/<int:prod_id>', views.update_product),
    path('delete/<int:prod_id>', views.delete_product),
]

# if DEBUG:
#     urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
#     urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)