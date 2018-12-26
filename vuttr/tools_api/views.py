from django.http import HttpResponse, HttpResponseNotFound
from django.views import View
from vuttr.core.models import Tools, Tags
from .utils.serializer import serialize
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
        try:
            resp = json.loads(request.body)
            tool = Tools.objects.create(
                title = resp['title'],
                link = resp['link'],
                description = resp['description'],
            )
            for tag_name in resp['tags']:
                tag = Tags.objects.get_or_create(name=tag_name)
                tool.tags.add(tag[0])
            return HttpResponse(serialize(tool), status=201, content_type="application/json")
        except json.decoder.JSONDecodeError:
            return HttpResponse(status=400)
        except KeyError:
            return HttpResponse(status=400)

    def patch(self, request, id):
        try:
            tool = Tools.objects.get(pk=id)
            data = json.loads(request.body)
            if data:
                tags_list = []
                for key, value in data.items():
                    if key == 'tags':
                        for tag_name in value:
                            tag = Tags.objects.get_or_create(name=tag_name)
                            tags_list.append(tag[0])
                        tool.tags.set(tags_list)
                    else:
                        setattr(tool, key, value)
                tool.save()
            else:
                return HttpResponse(status=400)
        except Tools.DoesNotExist:
            return HttpResponseNotFound()
        except json.decoder.JSONDecodeError:
            return HttpResponse(status=400)
        return HttpResponse(serialize(tool))

    def delete(self, request, id):
        if not request.body:
            try:
                tool = Tools.objects.get(pk=id)
                tool.delete()
                return HttpResponse(status=204)
            except Tools.DoesNotExist:
                return HttpResponseNotFound()
        else:
            return HttpResponse(status=400)
