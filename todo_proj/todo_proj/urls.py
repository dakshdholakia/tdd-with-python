"""
URL configuration for todo_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

# from django.urls import path
# from graphene_django.views import GraphQLView
# from rest_framework.routers import DefaultRouter
# from todo_app.schema import schema
# from .views import TodoViewSet  # Your DRF viewset
#
# router = DefaultRouter()
# router.register(r'todos', TodoViewSet)
#
# urlpatterns = [
#     path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
#     path('api/', include(router.urls)),
# ]

from django.urls import path
from todo_app.views import *

urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view()),
    path('', ListTodo.as_view()),
    path('create', CreateTodo.as_view()),
    path('delete/<int:pk>', DeleteTodo.as_view())
]