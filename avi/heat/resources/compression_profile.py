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
from common import *


class CompressionFilter(object):
    # all schemas
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    index_schema = properties.Schema(
        properties.Schema.NUMBER,
        _(""),
        required=True,
        update_allowed=True,
    )
    match_schema = properties.Schema(
        properties.Schema.STRING,
        _("Whether to apply Filter when group criteria is matched or not"),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['IS_NOT_IN', 'IS_IN']),
        ],
    )
    ip_addrs_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _(" You can either provide UUID or provide a name with the prefix 'get_avi_uuid_for_name:', e.g., 'get_avi_uuid_for_name:my_obj_name'."),
        required=False,
        update_allowed=True,
    )
    ip_addrs_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IpAddr.properties_schema,
        required=True,
        update_allowed=False,
    )
    ip_addrs_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=ip_addrs_item_schema,
        required=False,
        update_allowed=True,
    )
    ip_addr_ranges_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IpAddrRange.properties_schema,
        required=True,
        update_allowed=False,
    )
    ip_addr_ranges_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=ip_addr_ranges_item_schema,
        required=False,
        update_allowed=True,
    )
    ip_addr_prefixes_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IpAddrPrefix.properties_schema,
        required=True,
        update_allowed=False,
    )
    ip_addr_prefixes_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=ip_addr_prefixes_item_schema,
        required=False,
        update_allowed=True,
    )
    devices_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _(" You can either provide UUID or provide a name with the prefix 'get_avi_uuid_for_name:', e.g., 'get_avi_uuid_for_name:my_obj_name'."),
        required=False,
        update_allowed=True,
    )
    user_agent_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    user_agent_schema = properties.Schema(
        properties.Schema.LIST,
        _(""),
        schema=user_agent_item_schema,
        required=False,
        update_allowed=True,
    )
    level_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['NORMAL_COMPRESSION', 'AGGRESSIVE_COMPRESSION', 'NO_COMPRESSION']),
        ],
    )

    # properties list
    PROPERTIES = (
        'name',
        'index',
        'match',
        'ip_addrs_uuid',
        'ip_addrs',
        'ip_addr_ranges',
        'ip_addr_prefixes',
        'devices_uuid',
        'user_agent',
        'level',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'name': name_schema,
        'index': index_schema,
        'match': match_schema,
        'ip_addrs_uuid': ip_addrs_uuid_schema,
        'ip_addrs': ip_addrs_schema,
        'ip_addr_ranges': ip_addr_ranges_schema,
        'ip_addr_prefixes': ip_addr_prefixes_schema,
        'devices_uuid': devices_uuid_schema,
        'user_agent': user_agent_schema,
        'level': level_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'ip_addr_ranges': getattr(IpAddrRange, 'field_references', {}),
        'devices_uuid': 'stringgroup',
        'ip_addrs': getattr(IpAddr, 'field_references', {}),
        'ip_addrs_uuid': 'ipaddrgroup',
        'ip_addr_prefixes': getattr(IpAddrPrefix, 'field_references', {}),
    }



class CompressionProfile(object):
    # all schemas
    compression_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Compress HTTP response content if it wasn't already compressed."),
        required=True,
        update_allowed=True,
    )
    remove_accept_encoding_header_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Offload compression from the servers to AVI. Saves compute cycles on the servers."),
        required=True,
        update_allowed=True,
    )
    compressible_content_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _("Compress only content types listed in this string group. Content types not present in this list are not compressed. You can either provide UUID or provide a name with the prefix 'get_avi_uuid_for_name:', e.g., 'get_avi_uuid_for_name:my_obj_name'."),
        required=False,
        update_allowed=True,
    )
    type_schema = properties.Schema(
        properties.Schema.STRING,
        _("Compress content automatically or add custom filters to define compressible content and compression levels."),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['CUSTOM_COMPRESSION', 'AUTO_COMPRESSION']),
        ],
    )
    filter_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=CompressionFilter.properties_schema,
        required=True,
        update_allowed=False,
    )
    filter_schema = properties.Schema(
        properties.Schema.LIST,
        _("Custom filters used when auto compression is not selected."),
        schema=filter_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'compression',
        'remove_accept_encoding_header',
        'compressible_content_uuid',
        'type',
        'filter',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'compression': compression_schema,
        'remove_accept_encoding_header': remove_accept_encoding_header_schema,
        'compressible_content_uuid': compressible_content_uuid_schema,
        'type': type_schema,
        'filter': filter_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'filter': getattr(CompressionFilter, 'field_references', {}),
        'compressible_content_uuid': 'stringgroup',
    }

