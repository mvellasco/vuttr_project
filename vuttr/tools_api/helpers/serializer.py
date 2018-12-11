from collections import Iterable
import json

def serialize(tools):
    if isinstance(tools, Iterable):
        data = []
        for tool in tools:
            data.append({
                'id': tool.id,
                'title': tool.title,
                'link': tool.link,
                'description': tool.description,
                'tags': [tag for tag in tool.tags.values_list('name', flat=True)]
            })
        return json.dumps(data)
    else:
        data = []
        data.append({
            'id': tools.id,
            'title': tools.title,
            'link': tools.link,
            'description': tools.description,
            'tags': [tag for tag in tools.tags.values_list('name', flat=True)]
        })
        return json.dumps(data)
