from django.http import HttpResponse, HttpResponseNotFound
from django.views import View
from vuttr.core.models import Tools
from .helpers.serializer import serialize
import json

class ToolView(View):

    def get(self, request, id=None):
        if request.GET.get('tag'):
            tag = request.GET.get('tag')
            tools = Tools.objects.filter(tags__name=tag)
            if len(tools) > 0:
                return HttpResponse(serialize(tools), content_type="application/json")
            else:
                return HttpResponseNotFound()
        else:
            tools = Tools.objects.all()
            return HttpResponse(serialize(tools), content_type="application/json")

    def post(self, request):
        resp = json.loads(request.body)
        tool = Tools.objects.create(
            title = resp['title'],
            link = resp['link'],
            description = resp['description'],
        )
        for tag in resp['tags']:
            tool.tags.create(name=tag)
        return HttpResponse(serialize(tool), status=201, content_type="application/json")

    def delete(self, request, id):
        try:
            tool = Tools.objects.get(pk=id)
            tool.delete()
            return HttpResponse(status=204)
        except Tools.DoesNotExist:
            return HttpResponseNotFound()
