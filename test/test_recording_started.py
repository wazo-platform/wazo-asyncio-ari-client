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
from wazo_appgateway_client.models.recording_started import RecordingStarted  # noqa: E501
from wazo_appgateway_client.rest import ApiException

class TestRecordingStarted(unittest.TestCase):
    """RecordingStarted unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RecordingStarted
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = wazo_appgateway_client.models.recording_started.RecordingStarted()  # noqa: E501
        if include_optional :
            return RecordingStarted(
                recording = wazo_appgateway_client.models.live_recording.LiveRecording(
                    cause = '0', 
                    duration = 56, 
                    format = '0', 
                    name = '0', 
                    silence_duration = 56, 
                    state = '0', 
                    talking_duration = 56, 
                    target_uri = '0', )
            )
        else :
            return RecordingStarted(
                recording = wazo_appgateway_client.models.live_recording.LiveRecording(
                    cause = '0', 
                    duration = 56, 
                    format = '0', 
                    name = '0', 
                    silence_duration = 56, 
                    state = '0', 
                    talking_duration = 56, 
                    target_uri = '0', ),
        )

    def testRecordingStarted(self):
        """Test RecordingStarted"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()