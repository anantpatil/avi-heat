# GENERATED FILE - DO NOT EDIT THIS FILE UNLESS YOU ARE A WIZZARD
#pylint:  skip-file
from heat.engine import properties
from heat.engine import constraints
from heat.engine import attributes
from heat.common.i18n import _
from avi.heat.avi_resource import AviResource
from avi.heat.avi_resource import AviNestedResource
from options import *

from common import *
from options import *
from snmp import *
from auth import *
from match import *


class DNSConfiguration(object):
    # all schemas
    server_list_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IpAddr.properties_schema,
        required=True,
        update_allowed=False,
    )
    server_list_schema = properties.Schema(
        properties.Schema.LIST,
        _("List of DNS Server IP addresses"),
        schema=server_list_item_schema,
        required=False,
        update_allowed=True,
    )
    search_domain_schema = properties.Schema(
        properties.Schema.STRING,
        _("Search domain to use in DNS lookup"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'server_list',
        'search_domain',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'server_list': server_list_schema,
        'search_domain': search_domain_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'server_list': getattr(IpAddr, 'field_references', {}),
    }



class NTPAuthenticationKey(object):
    # all schemas
    key_number_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Key number to be assigned to the authentication-key."),
        required=True,
        update_allowed=True,
    )
    algorithm_schema = properties.Schema(
        properties.Schema.STRING,
        _("Message Digest Algorithm used for NTP authentication. Default is NTP_AUTH_ALGORITHM_MD5"),
        required=False,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['NTP_AUTH_ALGORITHM_SHA1', 'NTP_AUTH_ALGORITHM_MD5']),
        ],
    )
    key_schema = properties.Schema(
        properties.Schema.STRING,
        _("NTP Authentication key"),
        required=True,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'key_number',
        'algorithm',
        'key',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'key_number': key_number_schema,
        'algorithm': algorithm_schema,
        'key': key_schema,
    }




class AdminAuthConfiguration(object):
    # all schemas
    auth_profile_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _(" You can either provide UUID or provide a name with the prefix 'get_avi_uuid_for_name:', e.g., 'get_avi_uuid_for_name:my_obj_name'."),
        required=False,
        update_allowed=True,
    )
    mapping_rules_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=AuthMappingRule.properties_schema,
        required=True,
        update_allowed=False,
    )
    mapping_rules_schema = properties.Schema(
        properties.Schema.LIST,
        _("Rules list for tenant or role mapping"),
        schema=mapping_rules_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'auth_profile_uuid',
        'mapping_rules',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'auth_profile_uuid': auth_profile_uuid_schema,
        'mapping_rules': mapping_rules_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'mapping_rules': getattr(AuthMappingRule, 'field_references', {}),
        'auth_profile_uuid': 'authprofile',
    }



class NTPServer(object):
    # all schemas
    server_schema = properties.Schema(
        properties.Schema.MAP,
        _("IP Address of the NTP Server"),
        schema=IpAddr.properties_schema,
        required=True,
        update_allowed=True,
    )
    key_number_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Key number from the list of trusted keys used to authenticate this server"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'server',
        'key_number',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'server': server_schema,
        'key_number': key_number_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'server': getattr(IpAddr, 'field_references', {}),
    }



class TechSupportUploaderConfiguration(object):
    # all schemas
    auto_upload_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'auto_upload',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'auto_upload': auto_upload_schema,
    }




class EmailConfiguration(object):
    # all schemas
    smtp_type_schema = properties.Schema(
        properties.Schema.STRING,
        _("Type of SMTP Mail Service"),
        required=True,
        update_allowed=True,
        constraints=[
            constraints.AllowedValues(['SMTP_NONE', 'SMTP_LOCAL_HOST', 'SMTP_SERVER', 'SMTP_ANONYMOUS_SERVER']),
        ],
    )
    from_email_schema = properties.Schema(
        properties.Schema.STRING,
        _("Email address in From field"),
        required=False,
        update_allowed=True,
    )
    mail_server_name_schema = properties.Schema(
        properties.Schema.STRING,
        _("Mail server host"),
        required=False,
        update_allowed=True,
    )
    mail_server_port_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Mail server port"),
        required=False,
        update_allowed=True,
    )
    auth_username_schema = properties.Schema(
        properties.Schema.STRING,
        _("Username for mail server"),
        required=False,
        update_allowed=True,
    )
    auth_password_schema = properties.Schema(
        properties.Schema.STRING,
        _("Password for mail server"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'smtp_type',
        'from_email',
        'mail_server_name',
        'mail_server_port',
        'auth_username',
        'auth_password',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'smtp_type': smtp_type_schema,
        'from_email': from_email_schema,
        'mail_server_name': mail_server_name_schema,
        'mail_server_port': mail_server_port_schema,
        'auth_username': auth_username_schema,
        'auth_password': auth_password_schema,
    }




class ProxyConfiguration(object):
    # all schemas
    host_schema = properties.Schema(
        properties.Schema.STRING,
        _("Proxy hostname or IP address"),
        required=True,
        update_allowed=True,
    )
    port_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("Proxy port"),
        required=True,
        update_allowed=True,
    )
    username_schema = properties.Schema(
        properties.Schema.STRING,
        _("Username for proxy"),
        required=False,
        update_allowed=True,
    )
    password_schema = properties.Schema(
        properties.Schema.STRING,
        _("Password for proxy"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'host',
        'port',
        'username',
        'password',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'host': host_schema,
        'port': port_schema,
        'username': username_schema,
        'password': password_schema,
    }




class LinuxConfiguration(object):
    # all schemas
    motd_schema = properties.Schema(
        properties.Schema.STRING,
        _("Message of the day, shown to users on login via the command line interface, web interface, or ssh."),
        required=False,
        update_allowed=True,
    )
    banner_schema = properties.Schema(
        properties.Schema.STRING,
        _("Banner displayed before login to ssh, and UI"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'motd',
        'banner',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'motd': motd_schema,
        'banner': banner_schema,
    }




class PortalConfiguration(object):
    # all schemas
    enable_https_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    redirect_to_https_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    enable_http_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _(""),
        required=False,
        update_allowed=True,
    )
    sslkeyandcertificate_uuids_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    sslkeyandcertificate_uuids_schema = properties.Schema(
        properties.Schema.LIST,
        _("Certificates for system portal. Maximum 2 allowed. Leave list empty to use system default certs You can either provide UUID or provide a name with the prefix 'get_avi_uuid_for_name:', e.g., 'get_avi_uuid_for_name:my_obj_name'."),
        schema=sslkeyandcertificate_uuids_item_schema,
        required=False,
        update_allowed=True,
    )
    use_uuid_from_input_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Use UUID in POST object data as UUID of the new object, instead of a generated UUID."),
        required=False,
        update_allowed=True,
    )
    sslprofile_uuid_schema = properties.Schema(
        properties.Schema.STRING,
        _(" You can either provide UUID or provide a name with the prefix 'get_avi_uuid_for_name:', e.g., 'get_avi_uuid_for_name:my_obj_name'."),
        required=False,
        update_allowed=True,
    )
    enable_clickjacking_protection_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Enable/Disable Clickjacking protection"),
        required=False,
        update_allowed=True,
    )
    allow_basic_authentication_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Enable/Disable HTTP basic authentication"),
        required=False,
        update_allowed=True,
    )
    http_port_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("HTTP port"),
        required=False,
        update_allowed=True,
    )
    https_port_schema = properties.Schema(
        properties.Schema.NUMBER,
        _("HTTPS port"),
        required=False,
        update_allowed=True,
    )
    password_strength_check_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Strict checking of password strength for user accounts"),
        required=False,
        update_allowed=True,
    )
    disable_remote_cli_shell_schema = properties.Schema(
        properties.Schema.BOOLEAN,
        _("Disable Remote CLI Shell Client access"),
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'enable_https',
        'redirect_to_https',
        'enable_http',
        'sslkeyandcertificate_uuids',
        'use_uuid_from_input',
        'sslprofile_uuid',
        'enable_clickjacking_protection',
        'allow_basic_authentication',
        'http_port',
        'https_port',
        'password_strength_check',
        'disable_remote_cli_shell',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'enable_https': enable_https_schema,
        'redirect_to_https': redirect_to_https_schema,
        'enable_http': enable_http_schema,
        'sslkeyandcertificate_uuids': sslkeyandcertificate_uuids_schema,
        'use_uuid_from_input': use_uuid_from_input_schema,
        'sslprofile_uuid': sslprofile_uuid_schema,
        'enable_clickjacking_protection': enable_clickjacking_protection_schema,
        'allow_basic_authentication': allow_basic_authentication_schema,
        'http_port': http_port_schema,
        'https_port': https_port_schema,
        'password_strength_check': password_strength_check_schema,
        'disable_remote_cli_shell': disable_remote_cli_shell_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'sslprofile_uuid': 'sslprofile',
        'sslkeyandcertificate_uuids': 'sslkeyandcertificate',
    }



class NTPConfiguration(object):
    # all schemas
    ntp_server_list_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=IpAddr.properties_schema,
        required=True,
        update_allowed=False,
    )
    ntp_server_list_schema = properties.Schema(
        properties.Schema.LIST,
        _("List of NTP server hostnames or IP addresses"),
        schema=ntp_server_list_item_schema,
        required=False,
        update_allowed=True,
    )
    ntp_authentication_keys_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=NTPAuthenticationKey.properties_schema,
        required=True,
        update_allowed=False,
    )
    ntp_authentication_keys_schema = properties.Schema(
        properties.Schema.LIST,
        _("NTP Authentication keys"),
        schema=ntp_authentication_keys_item_schema,
        required=False,
        update_allowed=True,
    )
    ntp_servers_item_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=NTPServer.properties_schema,
        required=True,
        update_allowed=False,
    )
    ntp_servers_schema = properties.Schema(
        properties.Schema.LIST,
        _("List of NTP Servers"),
        schema=ntp_servers_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'ntp_server_list',
        'ntp_authentication_keys',
        'ntp_servers',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'ntp_server_list': ntp_server_list_schema,
        'ntp_authentication_keys': ntp_authentication_keys_schema,
        'ntp_servers': ntp_servers_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'ntp_servers': getattr(NTPServer, 'field_references', {}),
        'ntp_authentication_keys': getattr(NTPAuthenticationKey, 'field_references', {}),
        'ntp_server_list': getattr(IpAddr, 'field_references', {}),
    }



class MgmtIpAccessControl(object):
    # all schemas
    ssh_access_schema = properties.Schema(
        properties.Schema.MAP,
        _("Configure IP addresses to access controller using SSH"),
        schema=IpAddrMatch.properties_schema,
        required=False,
        update_allowed=True,
    )
    api_access_schema = properties.Schema(
        properties.Schema.MAP,
        _("Configure IP addresses to access controller using API"),
        schema=IpAddrMatch.properties_schema,
        required=False,
        update_allowed=True,
    )
    shell_server_access_schema = properties.Schema(
        properties.Schema.MAP,
        _("Configure IP addresses to access controller using CLI Shell"),
        schema=IpAddrMatch.properties_schema,
        required=False,
        update_allowed=True,
    )
    snmp_access_schema = properties.Schema(
        properties.Schema.MAP,
        _("Configure IP addresses to access controller using SNMP"),
        schema=IpAddrMatch.properties_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'ssh_access',
        'api_access',
        'shell_server_access',
        'snmp_access',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'ssh_access': ssh_access_schema,
        'api_access': api_access_schema,
        'shell_server_access': shell_server_access_schema,
        'snmp_access': snmp_access_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'snmp_access': getattr(IpAddrMatch, 'field_references', {}),
        'api_access': getattr(IpAddrMatch, 'field_references', {}),
        'ssh_access': getattr(IpAddrMatch, 'field_references', {}),
        'shell_server_access': getattr(IpAddrMatch, 'field_references', {}),
    }



class SystemConfiguration(AviResource):
    resource_name = "systemconfiguration"
    # all schemas
    dns_configuration_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=DNSConfiguration.properties_schema,
        required=False,
        update_allowed=True,
    )
    ntp_configuration_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=NTPConfiguration.properties_schema,
        required=False,
        update_allowed=True,
    )
    tech_support_uploader_configuration_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=TechSupportUploaderConfiguration.properties_schema,
        required=False,
        update_allowed=True,
    )
    portal_configuration_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=PortalConfiguration.properties_schema,
        required=False,
        update_allowed=True,
    )
    global_tenant_config_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=TenantConfiguration.properties_schema,
        required=False,
        update_allowed=True,
    )
    email_configuration_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=EmailConfiguration.properties_schema,
        required=False,
        update_allowed=True,
    )
    admin_auth_configuration_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=AdminAuthConfiguration.properties_schema,
        required=False,
        update_allowed=True,
    )
    snmp_configuration_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=SnmpConfiguration.properties_schema,
        required=False,
        update_allowed=True,
    )
    linux_configuration_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=LinuxConfiguration.properties_schema,
        required=False,
        update_allowed=True,
    )
    proxy_configuration_schema = properties.Schema(
        properties.Schema.MAP,
        _(""),
        schema=ProxyConfiguration.properties_schema,
        required=False,
        update_allowed=True,
    )
    mgmt_ip_access_control_schema = properties.Schema(
        properties.Schema.MAP,
        _("Configure Ip Access control for controller to restrict open access."),
        schema=MgmtIpAccessControl.properties_schema,
        required=False,
        update_allowed=True,
    )
    ssh_ciphers_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    ssh_ciphers_schema = properties.Schema(
        properties.Schema.LIST,
        _("Allowed Ciphers list for SSH to the management interface on the Controller and Service Engines. If this is not specified, all the default ciphers are allowed. ssh -Q cipher provides the list of default ciphers supported."),
        schema=ssh_ciphers_item_schema,
        required=False,
        update_allowed=True,
    )
    ssh_hmacs_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    ssh_hmacs_schema = properties.Schema(
        properties.Schema.LIST,
        _("Allowed HMAC list for SSH to the management interface on the Controller and Service Engines. If this is not specified, all the default HMACs are allowed. ssh -Q mac provides the list of default HMACs supported."),
        schema=ssh_hmacs_item_schema,
        required=False,
        update_allowed=True,
    )
    dns_virtualservice_uuids_item_schema = properties.Schema(
        properties.Schema.STRING,
        _(""),
        required=True,
        update_allowed=False,
    )
    dns_virtualservice_uuids_schema = properties.Schema(
        properties.Schema.LIST,
        _("DNS virtualservices hosting FQDN records for applications across Avi Vantage. If no virtualservices are provided, Avi Vantage will provide DNS services for configured applications. Switching back to Avi Vantage from DNS virtualservices is not allowed."),
        schema=dns_virtualservice_uuids_item_schema,
        required=False,
        update_allowed=True,
    )

    # properties list
    PROPERTIES = (
        'dns_configuration',
        'ntp_configuration',
        'tech_support_uploader_configuration',
        'portal_configuration',
        'global_tenant_config',
        'email_configuration',
        'admin_auth_configuration',
        'snmp_configuration',
        'linux_configuration',
        'proxy_configuration',
        'mgmt_ip_access_control',
        'ssh_ciphers',
        'ssh_hmacs',
        'dns_virtualservice_uuids',
    )

    # mapping of properties to their schemas
    properties_schema = {
        'dns_configuration': dns_configuration_schema,
        'ntp_configuration': ntp_configuration_schema,
        'tech_support_uploader_configuration': tech_support_uploader_configuration_schema,
        'portal_configuration': portal_configuration_schema,
        'global_tenant_config': global_tenant_config_schema,
        'email_configuration': email_configuration_schema,
        'admin_auth_configuration': admin_auth_configuration_schema,
        'snmp_configuration': snmp_configuration_schema,
        'linux_configuration': linux_configuration_schema,
        'proxy_configuration': proxy_configuration_schema,
        'mgmt_ip_access_control': mgmt_ip_access_control_schema,
        'ssh_ciphers': ssh_ciphers_schema,
        'ssh_hmacs': ssh_hmacs_schema,
        'dns_virtualservice_uuids': dns_virtualservice_uuids_schema,
    }

    # for supporting get_avi_uuid_by_name functionality
    field_references = {
        'email_configuration': getattr(EmailConfiguration, 'field_references', {}),
        'global_tenant_config': getattr(TenantConfiguration, 'field_references', {}),
        'dns_configuration': getattr(DNSConfiguration, 'field_references', {}),
        'proxy_configuration': getattr(ProxyConfiguration, 'field_references', {}),
        'tech_support_uploader_configuration': getattr(TechSupportUploaderConfiguration, 'field_references', {}),
        'snmp_configuration': getattr(SnmpConfiguration, 'field_references', {}),
        'linux_configuration': getattr(LinuxConfiguration, 'field_references', {}),
        'portal_configuration': getattr(PortalConfiguration, 'field_references', {}),
        'ntp_configuration': getattr(NTPConfiguration, 'field_references', {}),
        'admin_auth_configuration': getattr(AdminAuthConfiguration, 'field_references', {}),
        'mgmt_ip_access_control': getattr(MgmtIpAccessControl, 'field_references', {}),
    }



def resource_mapping():
    return {
        'Avi::LBaaS::SystemConfiguration': SystemConfiguration,
    }

