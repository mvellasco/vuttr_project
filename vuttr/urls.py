from django.urls import path
from vuttr.api.views import ToolView

urlpatterns = [
    path('tools/', ToolView.as_view(), name='tools'),
    path('tools/<int:id>/', ToolView.as_view(), name='delete_tool')
]
