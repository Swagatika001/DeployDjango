from django.urls import path
from .views import BookList,BookDetails,BookCreate

urlpatterns=[
    path('',BookCreate.as_view(),name='bookcreate'),
    path('list/',BookList.as_view(),name='booklist'),
    path('<int:pk>/',BookDetails.as_view(),name='bookdetails'),

]