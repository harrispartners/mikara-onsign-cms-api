import json


def from_json(x, _type):
    return x if type(x) in [None, _type] else _type(**(json.loads(x) if type(x) is not dict else x))
    
def create_graphql_request(request_string,
                           is_request_query,
                           operation_name=None,
                           variables={}):
    request_type = 'query' if is_request_query else 'mutation'
    
    return {"operationName": operation_name, "variables": variables, request_type: request_string}