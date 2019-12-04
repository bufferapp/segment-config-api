from segment_config_api.models.base_model import BaseModel

class RolesModel(BaseModel):
    def __init__(self, workspace):
        super().__init__(workspace.api, f'{workspace.model_path}/roles')

    @property
    def policies(self):
        return PoliciesModel(self)

    def list(self):
        return self.send_request('GET')

class PoliciesModel(BaseModel):
    def __init__(self, roles):
        super().__init__(roles.api, f'{roles.model_path}/-/policies')

    def list(self):
        return self.send_request('GET')

class RolePoliciesModel(BaseModel):
    def __init__(self, api, role_name):
        super().__init__(api, f'{role_name}/policies')

    def create(self, payload):
        return self.send_request('POST', payload)

class RolePolicyModel(BaseModel):
    def __init__(self, api, policy_name):
        super().__init__(api, f'{policy_name}')

    def delete(self):
        return self.send_request('DELETE')

class InvitesModel(BaseModel):
    def __init__(self, workspace):
        super().__init__(workspace.api, f'{workspace.model_path}/invites')

    def invite(self, invite_id):
        return InviteModel(self, invite_id)

    def list(self):
        return self.send_request('GET')

    def create(self, payload):
        return self.send_request('POST', payload)

class InviteModel(BaseModel):
    def __init__(self, invites, name):
         super().__init__(invites.api, f'{invites.model_path}/{name}')

    def delete(self):
        return self.send_request('DELETE')