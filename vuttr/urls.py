from django.urls import path
from vuttr.tools_api.views import ToolsView

urlpatterns = [
    path('tools/', ToolsView.as_view(), name='tools'),
    path('tool/<int:id>/', ToolsView.as_view(), name='manage_tool')
]
