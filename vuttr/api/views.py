from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from vuttr.core.models import Tools
from .helpers.serializer import serialize
import json


@csrf_exempt
def tools_view_dispatcher(request, id=None):
    if request.method == "GET":
        if request.GET.get('tag'):
            tag = request.GET.get('tag')
            tools = serialize(Tools.objects.filter(tags__name=tag))
            return HttpResponse(tools, content_type="application/json")
        else:
            tools = serialize(Tools.objects.all())
            return HttpResponse(tools, content_type="application/json")

    elif request.method == "POST":
        resp = json.loads(request.body)
        tool = Tools.objects.create(
            title = resp['title'],
            link = resp['link'],
            description = resp['description'],
        )
        for tag in resp['tags']:
            tool.tags.create(name=tag)
        return HttpResponse(serialize(tool), status=201, content_type="application/json")

    elif request.method == "DELETE":
        tool = Tools.objects.get(pk=id)
        tool.delete()
        return HttpResponse(status=204)
