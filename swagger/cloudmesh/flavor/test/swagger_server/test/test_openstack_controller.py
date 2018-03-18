# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response500 import InlineResponse500  # noqa: E501
from swagger_server.test import BaseTestCase


class TestOpenstackController(BaseTestCase):
    """OpenstackController integration test stubs"""

    def test_get_openstack_compute_flavor(self):
        """Test case for get_openstack_compute_flavor

        Get flavor
        """
        query_string = [('subscriptionId', 'subscriptionId_example')]
        response = self.client.open(
            '/cloudmesh/flavor/flavor'.format(flavor_id='flavor_id_example'),
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
