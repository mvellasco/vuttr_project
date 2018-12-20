from django.http import HttpResponse, HttpResponseNotFound, HttpResponseNotAllowed
from django.utils.decorators import classonlymethod
from vuttr.core.models import Tools, Tags
from .helpers.serializer import serialize
import json


class ToolsView():

    http_method_names = ['get', 'post', 'patch', 'delete', 'options']

    @classonlymethod
    def as_view(cls):
        def view(request, *args, **kwargs):
            self = cls()
            self.request = request
            self.args = args
            self.kwargs = kwargs
            return self.dispatch(request, *args, **kwargs)
        view.view_class = cls
        return view

    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(self._allowed_methods())

    def _allowed_methods(self):
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]

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

    def options(self, request):
        response = HttpResponse()
        response['Allow'] = ', '.join(self._allowed_methods())
        response['Content-Length'] = '0'
        return response
