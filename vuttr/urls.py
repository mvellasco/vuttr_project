from django.conf.urls import url
from vuttr.tools_api.views import ToolsView
from vuttr.accounts.views import login_view, logout_view, create_user


urlpatterns = [
    url(r'^accounts/create_user', create_user, name='create_user'),
    url(r'^accounts/login', login_view, name='login'),
    url(r'^accounts/logout', logout_view, name='logout'),
    url(r'^tools$', ToolsView.as_view(), name='get_and_create_tools'),
    url(r'^tool/(?P<id>\d+)$', ToolsView.as_view(), name='update_and_delete_tool'),
]
