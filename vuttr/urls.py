from django.urls import path
from vuttr.api.views import tools_view_dispatcher

urlpatterns = [
    path('tools/', tools_view_dispatcher, name='tools'),
    path('tools/<int:id>/', tools_view_dispatcher, name='delete_tool')
]
