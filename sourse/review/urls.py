from django.urls import path

from review.views import ProductsView, CreateProductView, UpdateProduct, DeleteProduct, ProductView, CreateRecallView, \
    UpdateRecall, DeleteRecall, RecallView

app_name = "review"

urlpatterns = [
    path('', ProductsView.as_view(), name="index_view"),
    path('product/create', CreateProductView.as_view(), name="create-view"),
    path('product/<int:pk>/view', ProductView.as_view(), name="product-view"),
    path('product/<int:pk>/update', UpdateProduct.as_view(), name="p-update"),
    path('product/<int:pk>/delete', DeleteProduct.as_view(), name="p-delete"),
    path('product/<int:pk>/recall/create', CreateRecallView.as_view(), name="recall-create"),
    path('recall/<int:pk>/view', RecallView.as_view(), name="recall-view"),
    path('recall/<int:pk>/update', UpdateRecall.as_view(), name="r-update"),
    path('recall/<int:pk>/delete', DeleteRecall.as_view(), name="r-delete"),


]


