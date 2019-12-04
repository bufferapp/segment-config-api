import json
import requests

from segment_config_api.models.integrations_catalog import IntegrationsCatalogModel
from segment_config_api.models.workspaces import WorkspacesModel
from segment_config_api.models.destination_filters import GlobalDestinationFiltersModel
from segment_config_api.models.iam import RolePoliciesModel, RolePolicyModel

class SegmentConfigApi:

    def __init__(self, access_token):
        self.access_token = access_token
        self.base_url = 'https://platform.segmentapis.com/v1beta/'

    def send_request(self, verb, path, payload={}, params={}):
        #remove params that have null values (these are optional)
        params = {k: v for k, v in params.items() if v is not None}

        url = f'{self.base_url}{path}'
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }
        response = requests.request(verb, url,
            headers=headers,
            data=json.dumps(payload),
            params=params)

        response.raise_for_status()
        return response.json()

    @property
    def integrations_catalog(self):
        return IntegrationsCatalogModel(self)

    @property
    def workspaces(self):
        return WorkspacesModel(self)

    def workspace(self, name):
        return self.workspaces.workspace(name)

    @property
    def destination_filters(self):
        return GlobalDestinationFiltersModel(self)

    def role_policies(self, role_name):
        return RolePoliciesModel(role_name)

    def role_policy(self, policy_name):
        return RolePolicyModel(policy_name)