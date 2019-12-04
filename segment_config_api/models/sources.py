from segment_config_api.models.base_model import BaseModel
from segment_config_api.models.destinations import DestinationsModel, \
    DestinationModel
from segment_config_api.models.deletion_and_suppression import SourceRegulationsModel

class SourcesModel(BaseModel):
    def __init__(self, workspace):
        super().__init__(workspace.api, f'{workspace.model_path}/sources')

    def source(self, name):
        return SourceModel(self, name)

    def create(self, payload):
        return self.send_request('POST', payload=payload)

    def list(self, page_size=None, page_token=None):
        return self.send_request('GET',
            params={'page_size': page_size, 'page_token': page_token})

class SourceModel(BaseModel):
    def __init__(self, sources, name):
        super().__init__(sources.api, f'{sources.model_path}/{name}')

    @property
    def destinations(self):
        return DestinationsModel(self)

    def destination(self, name):
        return self.destinations.destination(name)

    @property
    def regulations(self):
        return SourceRegulationsModel(self)

    def get(self):
        return self.send_request('GET')

    def delete(self, name):
        return self.send_request('DELETE')

    def get_schema_config(self):
        path = f'schema-config'
        return self.send_request('GET', path)

    def update_schema_config(self, payload):
        path = f'schema-config'
        return self.send_request('PATCH', path, payload=payload)

