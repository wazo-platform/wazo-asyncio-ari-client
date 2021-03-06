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
from wazo_appgateway_client.models.recording_failed import RecordingFailed  # noqa: E501
from wazo_appgateway_client.rest import ApiException

class TestRecordingFailed(unittest.TestCase):
    """RecordingFailed unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RecordingFailed
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = wazo_appgateway_client.models.recording_failed.RecordingFailed()  # noqa: E501
        if include_optional :
            return RecordingFailed(
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
            return RecordingFailed(
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

    def testRecordingFailed(self):
        """Test RecordingFailed"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
