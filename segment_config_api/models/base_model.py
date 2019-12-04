class BaseModel():
    def __init__(self, api, model_path):
        self.api = api
        self.model_path = model_path

    def send_request(self, method: str, path='', path_suffix='', **kwargs):
        if path_suffix:
            path = f'{self.model_path}{path_suffix}'
        else:
            path = f'{self.model_path}/{path}'
        return self.api.send_request(method, path, **kwargs)