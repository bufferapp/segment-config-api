from segment_config_api.models.base_model import BaseModel

class IntegrationsCatalogModel(BaseModel):
    def __init__(self, api):
        super().__init__(api, '/catalog')

    @property
    def sources(self):
        return IntegrationsCatalogSourcesModel(self)

    def source(self, name):
        return self.sources.source(name)

    @property
    def destinations(self):
        return IntegrationsCatalogDestinationsModel(self)

    def destination(self, name):
        return self.destinations.destination(name)


class IntegrationsCatalogSourcesModel(BaseModel):
    def __init__(self, catalog: IntegrationsCatalogModel):
        super().__init__(catalog.api, f'{catalog.model_path}/sources')

    def source(self, name):
        return IntegrationsCatalogSourceModel(self, name)

    def list(self, page_size=None, page_token=None):
        return self.send_request('GET',
            params={'page_size': page_size, 'page_token': page_token})

class IntegrationsCatalogSourceModel(BaseModel):
    def __init__(self, sources: IntegrationsCatalogSourcesModel, name):
        super().__init__(sources.api, f'{sources.model_path}/{name}')

    def get(self):
        return self.send_request('GET')

class IntegrationsCatalogDestinationsModel(BaseModel):
    def __init__(self, catalog: IntegrationsCatalogModel):
        super().__init__(catalog.api, f'{catalog.model_path}/destinations')

    def destination(self, name):
        return IntegrationsCatalogDestinationModel(self, name)

    def list(self, page_size=None, page_token=None):
        return self.send_request('GET',
            params={'page_size': page_size, 'page_token': page_token})

class IntegrationsCatalogDestinationModel(BaseModel):
    def __init__(self, sources: IntegrationsCatalogDestinationsModel, name):
        super().__init__(sources.api, f'{sources.model_path}/{name}')

    def get(self):
        return self.send_request('GET')
