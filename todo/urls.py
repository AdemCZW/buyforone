from django.urls import path
from .views import (
    TodoListView,

    TodoUpdateView,
    TodoDeleteView,
    TodoDetailView,
    FlightListView,
    FlightCreateView,
    FlightUpdateView,
    FlightDeleteView,
    FlightDetailView,
    FlightMyListView,
    first_page_view,


)

app_name = 'todo'
urlpatterns = [
    path('', FlightListView.as_view(), name='list'),
    path('fg', first_page_view.as_view(), name='fg'),
    path('mylist', FlightMyListView.as_view(), name='mylist'),
    path('create', FlightCreateView.as_view(), name='create'),
    path('update/<int:pk>', FlightUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', FlightDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>', FlightDetailView.as_view(), name='detail'),

]
