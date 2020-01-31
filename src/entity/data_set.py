from oauthlib.oauth2.rfc6749.errors import TokenExpiredError
from src.entity.base_entity import BaseEntity


class DataSet(BaseEntity):
    def __init__(self, xibo):
        super(DataSet, self).__init__(xibo, '/dataset')

    def copy(self, id=0, data={}):
        self.url = self.url + '/copy/' + str(id)
        return self.post(data=data)

    def import_csv(self, id=0, data={}):
        self.url = self.url + '/import/' + str(id)
        return self.post(data=data)

    def import_json(self, id=0, data={}):
        self.url = self.url + '/importjson/' + str(id)
        return self.post(data=data)

    def get_column(self, id=0, data={}):
        self.url = self.url + '/' + str(id) + '/column'
        return self.get(data)

    def add_column(self, id=0, data={}):
        self.url = self.url + '/' + str(id) + '/column'
        return self.post(data=data)

    def edit_column(self, id=0, column_id=0, data={}):
        try:
            url = self.url + '/' + str(id) + '/column/' + str(column_id)
            response = self.client.put(url, data=data)
            response = self._process_response(response)
        
        except TokenExpiredError:
            self._renew_token()
            response = self.edit_column(id, column_id, data)
        
        return response

    def delete_column(self, id=0, column_id=0):
        try:
            url = self.url + '/' + str(id) + '/column/' + str(column_id)
            response = self.client.delete(url)
            response = self._process_response(response)
        
        except TokenExpiredError:
            self._renew_token()
            response = self.delete_column(id, column_id)
        
        return response

    def get_data(self, id=0):
        self.url = self.url + '/data/' + str(id)
        return self.get()

    def add_row(self, id=0, data={}):
        self.url = self.url + '/data/' + str(id)
        return self.post(data=data)

    def edit_row(self, id=0, row_id=0, data={}):
        try:
            url = self.url + '/data/' + str(id) + '/' + str(row_id)
            response = self.client.put(url, data=data)
            response = self._process_response(response)
        
        except TokenExpiredError:
            self._renew_token()
            response = self.edit_row(id, row_id, data)
        
        return response

    def delete_row(self, id=0, row_id=0):
        try:
            url = self.url + '/data/' + str(id) + '/' + str(row_id)
            response = self.client.delete(url)
            response = self._process_response(response)
        
        except TokenExpiredError:
            self._renew_token()
            response = self.delete_row(id, row_id)
        
        return response
