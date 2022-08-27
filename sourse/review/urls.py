from django.urls import path

from review.views import ProductsView, CreateProductView, UpdateProduct, DeleteProduct, ProductView

app_name = "review"

urlpatterns = [
    path('', ProductsView.as_view(), name="index_view"),
    path('product/create', CreateProductView.as_view(), name="create-view"),
    path('product/<int:pk>/view', ProductView.as_view(), name="product-view"),
    path('product/<int:pk>/update', UpdateProduct.as_view(), name="p-update"),
    path('product/<int:pk>/delete', DeleteProduct.as_view(), name="p-delete"),


]


# path('tasks/', IndexView.as_view(), name="index_view"),
#     path('tasks/create', CreateTaskView2.as_view(), name="create2"),
#     path('task/<int:pk>/', TaskView.as_view(), name="task_view"),
#     path('project/<int:pk>/task/create', CreateTaskView.as_view(), name="create"),
#     path('task/<int:pk>/update', UpdateTask.as_view(), name="update"),
#     path('task/<int:pk>/delete', DeleteTask.as_view(), name="delete"),
#     path('', ProjectsView.as_view(), name="p-view"),
#     path('projects/add', CreateProjectView.as_view(), name="create-view"),
#     path('projects/<int:pk>/view', ProjectView.as_view(), name="project-view"),
#     path('project/<int:pk>/update', UpdateProject.as_view(), name="p-update"),
#     path('project/<int:pk>/delete', DeleteProject.as_view(), name="p-delete"),
#     path('project/<int:pk>/add/user', AddUserView.as_view(), name="add_user"),