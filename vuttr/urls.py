from django.conf.urls import url
from vuttr.tools_api.views import ToolsView

urlpatterns = [
    url(r'^tools$', ToolsView.as_view(), name='get_and_create_tools'),
    url(r'^tool/(?P<id>\d+)$', ToolsView.as_view(), name='update_and_delete_tool')
]
