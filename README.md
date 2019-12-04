# A Python wrapper for [Segment's Config API](https://segment.com/docs/config-api/)

A minimal wrapper for Segment's config API.

The library is designed as a [Fluent interface](https://en.wikipedia.org/wiki/Fluent_interface) around the REST API. It consists of models that are designed execute API calls within the scope of parent models.


## Usage

```python
import os
from segment_config_api.api import SegmentConfigApi

access_token = os.getenv('SEGMENT_CONFIG_API_ACCESS_TOKEN') # Or hard-coded or whichever way you want to access it
api = SegmentConfigApi(access_token)
```

### Workspaces

```python
# List all workspaces
api.workspaces.list()

# Get a workspace
api.workspace('myworkspace').get()
```

More API details [here](https://reference.segmentapis.com/?version=latest#7a63ac88-43af-43db-a987-7ed7d677a8c8)


### Integrations Catalog

```python
# List all sources
catalog = api.integrations_catalog

catalog.sources.list()

# Get a specific source
catalog.source('customerio').get()

# List all destinations
catalog = api.integrations_catalog

catalog.destinations.list()

# Get a specific destination
catalog.destination('customerio').get()
```

More API details [here](https://reference.segmentapis.com/?version=latest#7a63ac88-43af-43db-a987-7ed7d677a8c8)

### Sources

```python
# Sources are scoped on a workspace level.
workspace = api.workspace('myworkspace')
sources = workspace.sources

# List all sources
sources.list()

# Create a new source
payload = {...}
sources.create(payload)

# Get a specific source by name
workspace.source('js').get()

# Get schema config
sc = workspace.source('js').get_schema_config

#Update schema config
payload = {...}
workspace.source('js').update_schema_config(payload)

# Delete a source
workspace.source('js').delete()
```

More API details [here](https://reference.segmentapis.com/?version=latest#5a852761-54d5-46da-8437-6e14e63449f3)

### Destinations

```python
# Destinations are scoped on the source level
workspace = api.workspace('myworkspace')
destinations = api.source('js').destinations

# List all destinations at this source
destinations.list()

# Create a new destination for this source
payload = {}
destinations.create(payload)

# Get a specific destination by name
ga = workspace.source('js').destination('google-analytics')
ga.get()

# Update a destination
payload = {...}
ga.update(payload)

# Delete a destination
ga.delete()
```

More API details [here](https://reference.segmentapis.com/?version=latest#39ce0439-0969-48c3-ba49-b22a46c41060)

### Tracking Plans

```python
# Tracking plans are scoped on the workspace level
workspace = api.workspace('myworkspace')
tracking_plans = workspace.tracking_plans

# List all the tracking plans
tracking_plans.list()

# Create a tracking plan
payload = {...}
tracking_plans.create(payload)

# Get a specific tracking plan by plan_id
plan = workspace.tracking_plan('rs_123')
plan.get()

# Update a tracking plan
payload = {...}
plan.update(payload)

# Create tracking plan source connection
plan.create_source_connection('workspaces/myworkspace/sources/js')

# Batch create source connections
source_names = [...]
plan.batch_create_source_connection(source_names)

# List source connections
plan.list_source_connections()

# Delete source connection
plan.delete_source_connection('workspaces/myworkspace/sources/js')

# Delete a tracking plan
plan.delete()
```

More API details [here](https://reference.segmentapis.com/?version=latest#c4647e3c-fe1b-4e2f-88b9-6634841eb4e5)


### Event Delivery Metrics

```python
# Event delivery metrics are scoped on a destination level
ga = api.workspace('myworkspace').source('js').destination('google-analytics')

metrics = ga.event_delivery_metrics

# List all the timeseries metrics
payload = {...}
metrics.list_timeseries(payload=payload) #payload is optional


# Get a timeseries metric
metrics.get_timeseries('time_to_success_p95')

# Batch get a timeseries metric, no need to add the full path prefix to metrics names, we'll do it for you
metrics.batch_get_timeseries(['successes', 'retried_502'])

# Get summary metrics
metrics.get_summary()

# Batch get summary metrics (on a workspace level)
ws = api.workspace('myworkspace')
pairs = ['workspaces/myworkspace/sources/js/destinations/google-analytics']
# Or let the api wrapper build your path
pairs = [ws.source('js').destination('google-analytics').model_path]

ws.batch_get_summary_metrics(pairs)
```

More API details [here](https://reference.segmentapis.com/?version=latest#51d89077-efd7-429b-85d4-155ac2cd07aa)

### Destination Filters

```python
# Destination Filters are scoped on a destination level
ga = api.workspace('myworkspace').source('js').destination('google-analytics')
destination_filters = ga.destination_filters

# List all filters for a destination
destination_filters.list()

# Create a destination filter
payload = {...}
destination_filters.create(payload)

# Get a specific filter
filter = ga.destination_filter('df_123')
filter.get()

# Update a filter
payload = {...}
filter.update(payload)

# Delete a filter
filter.delete()

# Preview a filter - This is scoped on the api level
payload = {
    "filter": {
        "if": "all",
            "actions": [
                {
                    "type": "blacklist_fields",
                    "fields": {
                        "properties": {
                            "fields": ["name", "age"]
                        }
                    }
                }
            ],
            "enabled": True
        },
        "input": "{ \"userId\": \"6592\", \"properties\": { \"name\": \"Bob Smith\", \"age\": \"40\", \"order\": \"129\" } }"
}
api.destination_filters.preview(payload)
```

More API details [here](https://reference.segmentapis.com/?version=latest#6c12fbe8-9f84-4a6c-848e-76a2325cb3c5)


### Deletion and Surpression

```python
# Regulations are scoped on a workspace level
ws = api.workspace('myworkspace')
regulations = ws.regulations

# List all regulations for a workspace
regulations.list()

#List regulations based on status
regulations.list(regulation_types='Suppress_With_Delete')

# Create a regulation
payload = {...}
regulations.create(payload)

# Get a specific regulation on it's regulation_id
regulation = ws.regulation('1KQVncbOPeRGjRcpuOHdnhDwPn7')
regulation.get()

# Delete a regulation (It has to be in an `initialized` state)
regulation.delete()

# Create a regulation on a source
payload = {...}
ws.source('js').regulations.create(payload)

# Delete an Object from a cloud source
payload = {...}
ws.source('js').regulations.delete(payload)

# List suppressed users on a workspace level
ws.suppressed_users.list()
```

More API details [here](https://reference.segmentapis.com/?version=latest#57a69434-76cc-43cc-a547-98c319182247)

### IAM

```python
# Roles are scoped on a workspace level
ws = api.workspace('myworkspace')
roles = ws.roles

# List all roles for a workspace
roles.list()

# List role policies
roles.policies.list()

# Get a specific regulation on it's regulation_id
regulation = ws.regulation('1KQVncbOPeRGjRcpuOHdnhDwPn7')
regulation.get()

# Delete a regulation (It has to be in an `initialized` state)
regulation.delete()

# Create a role policy (scoped on the api level)
payload = {...}
api.role_policies(role_name).create(payload)

# Delete role policy
api.role_policy(policy_name).delete()

# Invites are scoped on the workspace level
invites = ws.invites

# List all invites
invites.list()

# Create an invite
payload = {...}
invites.create(payload)

# Delete an invite
ws.invite('123').delete()
```

More API details [here](https://reference.segmentapis.com/?version=latest#57a69434-76cc-43cc-a547-98c319182247)

## What's missing

- Unit/Integration tests. The library hasn't been fully tested end-to-end. If you find any bugs, please file an issue!
- Pagination helpers. Right now you still have to manually retrieve and pass through the `page_token` to do pagination. Ideally there would be a set of nice iteratort functions to automatically do that for you.