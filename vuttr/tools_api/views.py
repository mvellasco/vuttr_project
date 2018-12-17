from django.http import HttpResponse, HttpResponseNotFound
from django.views import View
from vuttr.core.models import Tools
from .helpers.serializer import serialize
import json


class ToolsView(View):

    def get(self, request, id=None):
        tag = request.GET.get('tag')
        if tag:
            tools = Tools.objects.filter(tags__name=tag)
            if len(tools) > 0:
                return HttpResponse(serialize(tools), content_type="application/json")
            else:
                return HttpResponseNotFound()
        elif id:
            try:
                tool = Tools.objects.get(pk=id)
                return HttpResponse(serialize(tool), content_type="application/json")
            except Tools.DoesNotExist:
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

    def patch(self, request, id):
        try:
            tool = Tools.objects.get(pk=id)
            data = json.loads(request.body)
            if data:
                for key, value in data.items():
                    tool.__setattr__(key, value)
                tool.save()
            else:
                return HttpResponse(status=400)
        except Tools.DoesNotExist:
            return HttpResponseNotFound()
        except json.decoder.JSONDecodeError:
            return HttpResponse(status=400)
        return HttpResponse(serialize(tool))

    def delete(self, request, id):
        try:
            tool = Tools.objects.get(pk=id)
            tool.delete()
            return HttpResponse(status=204)
        except Tools.DoesNotExist:
            return HttpResponseNotFound()
