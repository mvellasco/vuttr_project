from django.urls import path
from vuttr.tools_api.views import ToolsView

urlpatterns = [
    path('tools/', ToolsView.as_view(), name='tools'),
    path('tools/<int:id>/', ToolsView.as_view(), name='delete_tool')
]
