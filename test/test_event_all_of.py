# coding: utf-8

"""
    localhost:8088

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 5.1.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import wazo_appgateway_client
from wazo_appgateway_client.models.event_all_of import EventAllOf  # noqa: E501
from wazo_appgateway_client.rest import ApiException

class TestEventAllOf(unittest.TestCase):
    """EventAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EventAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = wazo_appgateway_client.models.event_all_of.EventAllOf()  # noqa: E501
        if include_optional :
            return EventAllOf(
                application = '0', 
                timestamp = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date()
            )
        else :
            return EventAllOf(
                application = '0',
                timestamp = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
        )

    def testEventAllOf(self):
        """Test EventAllOf"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
