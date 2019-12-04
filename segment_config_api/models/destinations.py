from segment_config_api.models.base_model import BaseModel
from segment_config_api.models.destination_filters import DestinationFiltersModel
from segment_config_api.models.event_delivery_metrics import EventDeliveryMetricsModel

class DestinationsModel(BaseModel):
    def __init__(self, source):
        super().__init__(source.api, f'{source.model_path}/destinations')

    def destination(self, name):
        return DestinationModel(self, name)

    def create(self, payload):
        return self.send_request('POST', payload=payload)

    def list(self,page_size=None, page_token=None):
        return self.send_request('GET',
            params={'page_size': page_size, 'page_token': page_token})

class DestinationModel(BaseModel):
    def __init__(self, destinations, name):
        super().__init__(destinations.api, f'{destinations.model_path}/{name}')

    @property
    def destination_filters(self):
        return DestinationFiltersModel(self)

    def destination_filter(self, name):
        self.destination_filters.destination_filter(name)

    @property
    def event_delivery_metrics(self):
        return EventDeliveryMetricsModel(self)

    def get(self):
        return self.send_request('GET')

    def update(self, payload):
        return self.send_request('PATCH', payload=payload)

    def delete(self,name):
        return self.send_request('DELETE')
