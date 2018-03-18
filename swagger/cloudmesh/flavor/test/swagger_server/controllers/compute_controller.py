import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response500 import InlineResponse500  # noqa: E501
from swagger_server import util


def get_openstack_compute_flavor(subscriptionId, flavor_id):  # noqa: E501
    """Get flavor

    Get specific flavor by id # noqa: E501

    :param subscriptionId: subscription id
    :type subscriptionId: str
    :param flavor_id: Flavor id
    :type flavor_id: str

    :rtype: InlineResponse200
    """
    return 'do some magic!'
