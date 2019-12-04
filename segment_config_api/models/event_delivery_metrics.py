from typing import Sequence
from segment_config_api.models.base_model import BaseModel

class EventDeliveryMetricsModel(BaseModel):
    def __init__(self, destination):
        super().__init__(destination.api, f'{destination.model_path}/metrics')

    def get_timeseries(self, metric):
        return self.send_request('GET', metric)

    def batch_get_timeseries(self, metrics: Sequence[str]):
        #add model paths to metric names
        metrics = list(map(lambda n: f'{self.model_path}/{n}', metrics))
        payload = {"names": metrics}
        return self.send_request('GET', path_suffix=':batchGet', payload=payload)

    def list_timeseries(self, payload={}):
        return self.send_request('GET', payload=payload)

    def get_summary(self):
        return self.send_request('GET', path_suffix=':getSummary')

class WorkSpaceEventDeliveryMetricsModel(BaseModel):
    def __init__(self, workspace):
        super().__init__(workspace.api, f'{workspace.model_path}/event-delivery-metrics')

    def batch_get_summary(self, source_destination_pairs: Sequence[str]):
        payload = {"names": source_destination_pairs}
        return self.send_request('GET', path_suffix=':batchGetSummary',
            payload=payload)