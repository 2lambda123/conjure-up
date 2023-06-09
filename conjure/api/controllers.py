""" Interfaces to Juju Controllers """

from conjure.juju import Juju


def cloud_type(controller):
    """ Gets the cloud type for controller

    Arguments:
    controller: Specify controller

    Returns:
    String of the cloud-type
    """
    info = Juju.controller_info(controller)
    bootstrap_config = info.get('bootstrap-config', {})
    cloud_type = bootstrap_config.get('cloud-type', None)
    return cloud_type
