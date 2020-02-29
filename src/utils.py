import json
import dateutil.parser


def parseDateTimeString(x):
    if x is None:
        return None
        
    return dateutil.parser.parse(x)

def parseTimeString(x):
    if parseDateTimeString(x) is None:
        return None
        
    return dateutil.parser.parse(x).time()
    
    
def from_json(data, _type, _subtype=None):
    if type(data) in [type(None), _type]:
        return data
        
    if type(data) is not dict:
        data = json.loads(data)
        
    if _subtype is not None:
        data['_subtype'] = _subtype.__name__
        
    return _type(**data)

    
def from_json_list(data, _type):
    if data is None:
        return None
    
    return [from_json(x, _type) for x in data]
    
    
def create_graphql_request(request_string,
                           is_request_query,
                           operation_name=None,
                           variables={}):
    request_type = 'query' if is_request_query else 'mutation'
    
    return {"operationName": operation_name, "variables": variables, request_type: request_string}