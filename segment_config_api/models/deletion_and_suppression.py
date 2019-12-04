from segment_config_api.models.base_model import BaseModel

class RegulationsModel(BaseModel):
    def __init__(self, workspace):
        super().__init__(workspace.api, f'{workspace.model_path}/regulations')

    def regulation(self, regulation_id):
        return RegulationModel(self, regulation_id)

    def create(self, payload):
        return self.send_request('POST', payload=payload)

    def list(self, status=None, regulation_types=None):
        return self.send_request('GET', params={'status': status,
            'regulation_types': regulation_types})

class RegulationModel(BaseModel):
    def __init__(self, regulations, regulation_id):
        super().__init__(regulations.api, f'{regulations.model_path}/{regulation_id}')

    def get(self):
        return self.send_request('GET')

    def delete(self):
        return self.send_request('DELETE')

class SourceRegulationsModel(BaseModel):
    def __init__(self, source):
        super().__init__(source.api, f'{source.model_path}/regulations')

    def create(self):
        return self.send_request('POST')

    def delete(self):
        return self.send_request('DELETE')

class SuppressedUsersModel(BaseModel):
    def __init__(self, workspace):
        super().__init__(workspace.api, f'{workspace.model_path}/suppressed-users')

    def list(self):
        return self.send_request('GET')