from simple_rest_client.api import API
from simple_rest_client.resource import Resource

# Creates the API
api = API(
     api_root_url='http://localhost:3000/', # base api url
     params={}, # default params
     headers={}, # default headers
     timeout=20, # default timeout in seconds
     append_slash=False, # append slash to final url
     json_encode_body=True, # encode body as json
)

# Creates the user resources
class UserResources(Resource):
    actions = {
        'create_user': {'method': 'POST', 'url': 'accounts/create_user'},
        'login': {'method': 'POST', 'url': 'accounts/login'},
        'logout': {'method': 'POST', 'url': 'accounts/logout'},
        'get_tools': {'method': 'GET', 'url': 'tools'},
        'get_tool_by_id': {'method': 'GET', 'url': 'tool/{}'},
        'get_tool_by_tag': {'method': 'GET', 'url': 'tools?tag={}'},
        'create_tool': {'method': 'POST', 'url': 'tools'},
        'update_tool': {'method': 'PATCH', 'url': 'tool/{}'},
        'delete_tool': {'method': 'DELETE', 'url': 'tool/{}'},
    }

# Adds the user sources to the api to be used
api.add_resource(resource_name='user_actions', resource_class=UserResources)

# Creates a new user
api.user_actions.create_user(body={"username": "johndoe", "email": "john@doe.com", "password": "123456"})

# Logs the user in
api.user_actions.login(body={"username": "johndoe", "password": "123456"})

# Gets all the tools for the authenticated user
print("All the tools: {}\n".format(api.user_actions.get_tools().body))

# Gets a tool by id for the authenticated user
print("Gets tool with id=2: {}\n".format(api.user_actions.get_tool_by_id(2).body))

# Filter tools by tag for the authenticated user
print("Found tools with tag=node: {}\n".format(api.user_actions.get_tool_by_tag('node').body))

# Creates a new tool
data = {
    "title": "hotel",
    "link": "https://github.com/typicode/hotel",
    "description": "Local app manager. Start apps within your browser, developer tool with local .localhost domain and https out of the box.",
    "tags":["node", "organizing", "webapps", "domain", "developer", "https", "proxy"]
}
response = api.user_actions.create_tool(body=data)
print("Created tool: {} with status_code: {}\n".format(response.body, response.status_code))

# Creates a new tool for the authenticated user
data = {
    "title": "manage_hostel",
    "link": "https://anything.com/hostel",
    "description": "A tool for managing hostels",
    "tags": ['manage', 'hostel']
}
response = api.user_actions.update_tool(4, body=data)
print("Updated tool: {}\n".format(response.body))

# Deletes a tool for the authenticated user
response = api.user_actions.delete_tool(4)
print("Deleted tool with id=4 with status code: {}\n".format(response.status_code))

# Logout the user and shows that it's no longer possible to access tools
api.user_actions.logout()
response = api.user_actions.get_tools()
print("After the logout the result for GET tools is: {}".format(response))
