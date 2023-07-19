from django.urls import path
from .views import *

urlpatterns = [
    path('kPOP/', kPOPListView.as_view(), name='kPOP_list'),
    path('kPOP/create/', kPOPCreateView.as_view(), name='kPOP_create'),
    path('kPOP/<int:pk>/', kPOPDetailView.as_view(), name='kPOP_detail'),
    path('kPOP/<int:pk>/update/', kPOPUpdateView.as_view(), name='kPOP_update'),
    path('kPOP/<int:pk>/delete/', kPOPDeleteView.as_view(), name='kPOP_delete'),
]