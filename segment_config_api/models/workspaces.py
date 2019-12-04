from segment_config_api.models.base_model import BaseModel
from segment_config_api.models.sources import SourcesModel
from segment_config_api.models.tracking_plans import TrackingPlansModel
from segment_config_api.models.deletion_and_suppression import RegulationsModel, \
    SuppressedUsersModel
from segment_config_api.models.iam import RolesModel, InvitesModel
from segment_config_api.models.event_delivery_metrics import WorkSpaceEventDeliveryMetricsModel

class WorkspacesModel(BaseModel):
    def __init__(self, api):
        super().__init__(api, f'workspaces')

    def workspace(self, name):
        return WorkspaceModel(self, name)

    def list(self):
        return self.send_request('GET')


class WorkspaceModel(BaseModel):
    def __init__(self, workspaces, name):
        super().__init__(workspaces.api, f'{workspaces.model_path}/{name}')

    @property
    def sources(self):
        return SourcesModel(self)

    def source(self, name):
        return self.sources.source(name)

    @property
    def tracking_plans(self):
        return TrackingPlansModel(self)

    def tracking_plan(self, plan_id):
        return self.tracking_plans.tracking_plan(plan_id)

    @property
    def regulations(self):
        return RegulationsModel(self)

    def regulation(self, regulation_id):
        return self.regulations().regulation(regulation_id)

    @property
    def roles(self):
        return RolesModel(self)

    @property
    def invites(self):
        return InvitesModel(self)

    def invite(self, invite_id):
        self.invites.invite(invite_id)

    def batch_get_summary_metrics(self, source_destination_pairs):
        return WorkSpaceEventDeliveryMetricsModel(self) \
            .batch_get_summary(source_destination_pairs)

    @property
    def suppressed_users(self):
        return SuppressedUsersModel(self)

    def get(self):
        return self.send_request('GET')