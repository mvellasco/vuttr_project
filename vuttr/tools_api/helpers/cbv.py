from django.utils.decorators import classonlymethod
from django.http import HttpResponse, HttpResponseNotAllowed


class MyCBV():
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

    def options(self, request):
        response = HttpResponse()
        response['Allow'] = ', '.join(self._allowed_methods())
        response['Content-Length'] = '0'
        return response
