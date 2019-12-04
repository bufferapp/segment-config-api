from segment_config_api.models.base_model import BaseModel

class TrackingPlansModel(BaseModel):
    def __init__(self, workspace):
        super().__init__(workspace.api, f'{workspace.model_path}/tracking-plans')

    def tracking_plan(self, plan_id):
        return TrackingPlanModel(self, plan_id)

    def create(self, payload):
        return self.send_request('POST', payload=payload)

    def list(self, page_size=None, page_token=None):
        return self.send_request('GET',
            params={'page_size': page_size, 'page_token': page_token})

class TrackingPlanModel(BaseModel):
    def __init__(self, tracking_plans: TrackingPlansModel, plan_id: str):
        super().__init__(tracking_plans.api,
            f'{tracking_plans.model_path}/{plan_id}')

    def get(self):
        return self.send_request('GET')

    def update(self, payload):
        return self.send_request('PUT', payload=payload)

    def delete(self):
        return self.send_request('DELETE')

    def create_source_connection(self, source_name):
        path = f'source-connections'
        payload = {'source_name' : source_name}
        return self.send_request('POST', path, payload=payload)

    def batch_create_source_connection(self, source_names):
        path = f'source-connections:batchCreateConnections'
        payload = {'source_names' : source_names}
        return self.send_request('POST', path, payload=payload)

    def list_source_connections(self):
        path = f'source-connections'
        return self.send_request('GET', path)

    def delete_source_connection(self, source_slug):
        path = f'source-connections/{source_slug}'
        return self.send_request('DELETE', path)