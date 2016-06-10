# GENERATED FILE - DO NOT EDIT THIS FILE UNLESS YOU ARE A WIZZARD
#pylint:  skip-file
from heat.engine import properties
from heat.engine import constraints
from heat.engine import attributes
from heat.common.i18n import _
from avi.heat.avi_resource import AviResource
from avi.heat.avi_resource import AviNestedResource
from options import *

from options import *


class MicroServiceContainer(object):
    # all schemas
    ip_schema = properties.Schema(
        properties.Schema.MAP,
        _("IP Address of the container."),
        schema=IpAddr.properties_schema,
        required=True,
        update_allowed=True,
    )
    port_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Port nunber of the instance"),
        required=False,
        update_allowed=True,
    )
    container_id_schema = properties.Schema(
        properties.Schema.STRING,
        _("ID of the container."),
        required=False,
        update_allowed=True,
    )
    host_schema = properties.Schema(
        properties.Schema.STRING,
        _("ID or name of the host where the container is."),
        required=False,
        update_allowed=True,
    )
    task_id_schema = properties.Schema(
        properties.Schema.STRING,
        _("Marathon Task ID of the instance"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'ip',
        'port',
        'container_id',
        'host',
        'task_id',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'ip': ip_schema,
        'port': port_schema,
        'container_id': container_id_schema,
        'host': host_schema,
        'task_id': task_id_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'ip': getattr(IpAddr, 'field_references', {}),
    }



class MicroService(AviResource):
    resource_name = "microservice"
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    orchestrator_name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    application_name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    ip_list_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Flag to indicate if container IP list is provided by cloud connectorThis is applicable for overlay cases."),
        required=False,
        update_allowed=True,
    )
    containers_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=MicroServiceContainer.properties_schema,
        required=True,
        update_allowed=False,
    )
    containers_schema = properties.Schema(
        properties.Schema.LIST,
        _("The list of containers for this microservice"),
        schema=containers_item_schema,
        required=False,
        update_allowed=True,
    )
    created_by_schema = properties.Schema(
        properties.Schema.STRING,
        _("Creator name"),
        required=False,
        update_allowed=True,
    )
    description_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'name',
        'orchestrator_name',
        'application_name',
        'ip_list',
        'containers',
        'created_by',
        'description',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'orchestrator_name': orchestrator_name_schema,
        'application_name': application_name_schema,
        'ip_list': ip_list_schema,
        'containers': containers_schema,
        'created_by': created_by_schema,
        'description': description_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'containers': getattr(MicroServiceContainer, 'field_references', {}),
    }



class MicroServiceContainers(AviNestedResource, MicroServiceContainer):
    resource_name = "microservice"
    nested_property_name = "containers"

    parent_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("UUID of microservice."
          " You can also provide a name"
          " with the prefix 'get_avi_uuid_for_name:', e.g.,"
          " 'get_avi_uuid_for_name:my_obj_name'."),
        required=True,
        update_allowed=False,
    )

    # properties list
    PROPERTIES = MicroServiceContainer.PROPERTIES + ('microservice_uuid',)

    # mapping of properties to their schemas
    properties_schema = {
        'microservice_uuid': parent_uuid_schema,
    }
    properties_schema.update(MicroServiceContainer.properties_schema)

    # field references
    field_references = {
        'microservice_uuid': 'microservice',
    }
    field_references.update(getattr(MicroServiceContainer, 'field_references', {}))


def resource_mapping():
    return {
        'Avi::MicroService': MicroService,
        'Avi::MicroService::Container': MicroServiceContainers,
    }

