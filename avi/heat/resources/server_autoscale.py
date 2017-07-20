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


class ServerAutoScalePolicy(AviResource):
    resource_name = "serverautoscalepolicy"
    # all schemas
    avi_version_schema = properties.Schema(
        properties.Schema.STRING,
        _("Avi Version to use for the object. Default is 16.4.2. If you plan to use any fields introduced after 16.4.2, then this needs to be explicitly set."),
        required=False,
        update_allowed=True,
    )
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    intelligent_autoscale_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Use Avi intelligent autoscale algorithm where autoscale is performed by comparing load on the pool against estimated capacity of all the servers. (Default: False)"),
        required=False,
        update_allowed=True,
    )
    intelligent_scaleout_margin_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Minimum extra capacity as percentage of load used by the intelligent scheme. Scaleout is triggered when available capacity is less than this margin. (Default: 20)"),
        required=False,
        update_allowed=True,
    )
    intelligent_scalein_margin_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum extra capacity as percentage of load used by the intelligent scheme. Scalein is triggered when available capacity is more than this margin. (Default: 40)"),
        required=False,
        update_allowed=True,
    )
    min_size_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("No scale-in happens once number of operationally up servers reach min_servers."),
        required=False,
        update_allowed=True,
    )
    max_size_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum number of servers after scaleout."),
        required=False,
        update_allowed=True,
    )
    max_scaleout_adjustment_step_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum number of servers to scaleout simultaneously. The actual number of servers to scaleout is chosen such that target number of servers is always less than or equal to the max_size. (Default: 1)"),
        required=False,
        update_allowed=True,
    )
    max_scalein_adjustment_step_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Maximum number of servers to scalein simultaneously. The actual number of servers to scalein is chosen such that target number of servers is always more than or equal to the min_size. (Default: 1)"),
        required=False,
        update_allowed=True,
    )
    scaleout_cooldown_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Cooldown period during which no new scaleout is triggered to allow previous scaleout to successfully complete. (Units: SEC) (Default: 300)"),
        required=False,
        update_allowed=True,
    )
    scalein_cooldown_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Cooldown period during which no new scalein is triggered to allow previous scalein to successfully complete. (Units: SEC) (Default: 300)"),
        required=False,
        update_allowed=True,
    )
    scaleout_alertconfig_uuids_item_schema = properties.Schema(
        properties.Schema.STRING,
        _("Trigger scaleout when alerts due to any of these Alert configurations are raised."),
        required=True,
        update_allowed=False,
    )
    scaleout_alertconfig_uuids_schema = properties.Schema(
        properties.Schema.LIST,
        _("Trigger scaleout when alerts due to any of these Alert configurations are raised. You can either provide UUID or provide a name with the prefix 'get_avi_uuid_by_name:', e.g., 'get_avi_uuid_by_name:my_obj_name'."),
        schema=scaleout_alertconfig_uuids_item_schema,
        required=False,
        update_allowed=True,
    )
    scalein_alertconfig_uuids_item_schema = properties.Schema(
        properties.Schema.STRING,
        _("Trigger scalein when alerts due to any of these Alert configurations are raised."),
        required=True,
        update_allowed=False,
    )
    scalein_alertconfig_uuids_schema = properties.Schema(
        properties.Schema.LIST,
        _("Trigger scalein when alerts due to any of these Alert configurations are raised. You can either provide UUID or provide a name with the prefix 'get_avi_uuid_by_name:', e.g., 'get_avi_uuid_by_name:my_obj_name'."),
        schema=scalein_alertconfig_uuids_item_schema,
        required=False,
        update_allowed=True,
    )
    use_predicted_load_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Use predicted load rather than current load. (Default: False)"),
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
        'avi_version',
        'name',
        'intelligent_autoscale',
        'intelligent_scaleout_margin',
        'intelligent_scalein_margin',
        'min_size',
        'max_size',
        'max_scaleout_adjustment_step',
        'max_scalein_adjustment_step',
        'scaleout_cooldown',
        'scalein_cooldown',
        'scaleout_alertconfig_uuids',
        'scalein_alertconfig_uuids',
        'use_predicted_load',
        'description',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'avi_version': avi_version_schema,
        'name': name_schema,
        'intelligent_autoscale': intelligent_autoscale_schema,
        'intelligent_scaleout_margin': intelligent_scaleout_margin_schema,
        'intelligent_scalein_margin': intelligent_scalein_margin_schema,
        'min_size': min_size_schema,
        'max_size': max_size_schema,
        'max_scaleout_adjustment_step': max_scaleout_adjustment_step_schema,
        'max_scalein_adjustment_step': max_scalein_adjustment_step_schema,
        'scaleout_cooldown': scaleout_cooldown_schema,
        'scalein_cooldown': scalein_cooldown_schema,
        'scaleout_alertconfig_uuids': scaleout_alertconfig_uuids_schema,
        'scalein_alertconfig_uuids': scalein_alertconfig_uuids_schema,
        'use_predicted_load': use_predicted_load_schema,
        'description': description_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'scaleout_alertconfig_uuids': 'alertconfig',
        'scalein_alertconfig_uuids': 'alertconfig',
    }



class AutoScaleMesosSettings(object):
    # all schemas
    force_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Apply scaleout even when there are deployments inprogress. (Default: True)"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'force',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'force': force_schema,
    }



class AutoScaleOpenStackSettings(object):
    # all schemas
    heat_scale_up_url_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.1) Avi Controller will use this URL to scale upthe pool. Cloud connector will automatically update the membership. This is an alpha feature."),
        required=False,
        update_allowed=True,
    )
    heat_scale_down_url_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.1) Avi Controller will use this URL to scale downthe pool. Cloud connector will automatically update the membership. This is an alpha feature."),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'heat_scale_up_url',
        'heat_scale_down_url',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'heat_scale_up_url': heat_scale_up_url_schema,
        'heat_scale_down_url': heat_scale_down_url_schema,
    }



class AutoScaleAWSSettings(object):
    # all schemas
    autoscaling_group_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("(Introduced in: 17.1.1) Name of the AWS autoscaling group. The AWS autoscaling group should not be set up with scaling policies as it would result in unpredictable behavior when used together with Avi autoscaling policies."),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'autoscaling_group_name',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'autoscaling_group_name': autoscaling_group_name_schema,
    }



class AutoScaleLaunchConfig(AviResource):
    resource_name = "autoscalelaunchconfig"
    # all schemas
    avi_version_schema = properties.Schema(
        properties.Schema.STRING,
        _("Avi Version to use for the object. Default is 16.4.2. If you plan to use any fields introduced after 16.4.2, then this needs to be explicitly set."),
        required=False,
        update_allowed=True,
    )
    name_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=True,
    )
    image_id_schema = properties.Schema(
        properties.Schema.STRING,
        _("Unique ID of the Amazon Machine Image (AMI)  or OpenStack VM ID."),
        required=False,
        update_allowed=True,
    )
    openstack_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=AutoScaleOpenStackSettings.properties_schema,
        required=False,
        update_allowed=True,
    )
    aws_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=AutoScaleAWSSettings.properties_schema,
        required=False,
        update_allowed=True,
    )
    mesos_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=AutoScaleMesosSettings.properties_schema,
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
        'avi_version',
        'name',
        'image_id',
        'openstack',
        'aws',
        'mesos',
        'description',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'avi_version': avi_version_schema,
        'name': name_schema,
        'image_id': image_id_schema,
        'openstack': openstack_schema,
        'aws': aws_schema,
        'mesos': mesos_schema,
        'description': description_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'openstack': getattr(AutoScaleOpenStackSettings, 'field_references', {}),
        'aws': getattr(AutoScaleAWSSettings, 'field_references', {}),
        'mesos': getattr(AutoScaleMesosSettings, 'field_references', {}),
    }

    unique_keys = {
        'openstack': getattr(AutoScaleOpenStackSettings, 'unique_keys', {}),
        'aws': getattr(AutoScaleAWSSettings, 'unique_keys', {}),
        'mesos': getattr(AutoScaleMesosSettings, 'unique_keys', {}),
    }



def resource_mapping():
    return {
        'Avi::LBaaS::ServerAutoScalePolicy': ServerAutoScalePolicy,
        'Avi::LBaaS::AutoScaleLaunchConfig': AutoScaleLaunchConfig,
    }

