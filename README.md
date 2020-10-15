# wazo-asyncio-ari-client

This library is for connecting to Asterisk ARI with asyncio.

- API version: 5.1.1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import wazo_appgateway_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import wazo_appgateway_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import wazo_appgateway_client
from wazo_appgateway_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8088/ari
# See configuration.py for a list of all supported configuration parameters.
configuration = wazo_appgateway_client.Configuration(
    host = "http://localhost:8088/ari"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = wazo_appgateway_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)


# Enter a context with an instance of the API client
with wazo_appgateway_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wazo_appgateway_client.ApplicationsApi(api_client)
    application_name = 'application_name_example' # str | Application's name
x_asterisk_id = 'x_asterisk_id_example' # str |  (optional)
body = None # object | Specify which event types to allow/disallow (optional)

    try:
        # Filter application events types.
        api_response = api_instance.applications_application_name_event_filter_put(application_name, x_asterisk_id=x_asterisk_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationsApi->applications_application_name_event_filter_put: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:8088/ari*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApplicationsApi* | [**applications_application_name_event_filter_put**](docs/ApplicationsApi.md#applications_application_name_event_filter_put) | **PUT** /applications/{applicationName}/eventFilter | Filter application events types.
*ApplicationsApi* | [**applications_application_name_get**](docs/ApplicationsApi.md#applications_application_name_get) | **GET** /applications/{applicationName} | Get details of an application.
*ApplicationsApi* | [**applications_application_name_subscription_delete**](docs/ApplicationsApi.md#applications_application_name_subscription_delete) | **DELETE** /applications/{applicationName}/subscription | Unsubscribe an application from an event source.
*ApplicationsApi* | [**applications_application_name_subscription_post**](docs/ApplicationsApi.md#applications_application_name_subscription_post) | **POST** /applications/{applicationName}/subscription | Subscribe an application to a event source.
*ApplicationsApi* | [**applications_get**](docs/ApplicationsApi.md#applications_get) | **GET** /applications | List all applications.
*AsteriskApi* | [**asterisk_config_dynamic_config_class_object_type_id_delete**](docs/AsteriskApi.md#asterisk_config_dynamic_config_class_object_type_id_delete) | **DELETE** /asterisk/config/dynamic/{configClass}/{objectType}/{id} | Delete a dynamic configuration object.
*AsteriskApi* | [**asterisk_config_dynamic_config_class_object_type_id_get**](docs/AsteriskApi.md#asterisk_config_dynamic_config_class_object_type_id_get) | **GET** /asterisk/config/dynamic/{configClass}/{objectType}/{id} | Retrieve a dynamic configuration object.
*AsteriskApi* | [**asterisk_config_dynamic_config_class_object_type_id_put**](docs/AsteriskApi.md#asterisk_config_dynamic_config_class_object_type_id_put) | **PUT** /asterisk/config/dynamic/{configClass}/{objectType}/{id} | Create or update a dynamic configuration object.
*AsteriskApi* | [**asterisk_info_get**](docs/AsteriskApi.md#asterisk_info_get) | **GET** /asterisk/info | Gets Asterisk system information.
*AsteriskApi* | [**asterisk_logging_get**](docs/AsteriskApi.md#asterisk_logging_get) | **GET** /asterisk/logging | Gets Asterisk log channel information.
*AsteriskApi* | [**asterisk_logging_log_channel_name_delete**](docs/AsteriskApi.md#asterisk_logging_log_channel_name_delete) | **DELETE** /asterisk/logging/{logChannelName} | Deletes a log channel.
*AsteriskApi* | [**asterisk_logging_log_channel_name_post**](docs/AsteriskApi.md#asterisk_logging_log_channel_name_post) | **POST** /asterisk/logging/{logChannelName} | Adds a log channel.
*AsteriskApi* | [**asterisk_logging_log_channel_name_rotate_put**](docs/AsteriskApi.md#asterisk_logging_log_channel_name_rotate_put) | **PUT** /asterisk/logging/{logChannelName}/rotate | Rotates a log channel.
*AsteriskApi* | [**asterisk_modules_get**](docs/AsteriskApi.md#asterisk_modules_get) | **GET** /asterisk/modules | List Asterisk modules.
*AsteriskApi* | [**asterisk_modules_module_name_delete**](docs/AsteriskApi.md#asterisk_modules_module_name_delete) | **DELETE** /asterisk/modules/{moduleName} | Unload an Asterisk module.
*AsteriskApi* | [**asterisk_modules_module_name_get**](docs/AsteriskApi.md#asterisk_modules_module_name_get) | **GET** /asterisk/modules/{moduleName} | Get Asterisk module information.
*AsteriskApi* | [**asterisk_modules_module_name_post**](docs/AsteriskApi.md#asterisk_modules_module_name_post) | **POST** /asterisk/modules/{moduleName} | Load an Asterisk module.
*AsteriskApi* | [**asterisk_modules_module_name_put**](docs/AsteriskApi.md#asterisk_modules_module_name_put) | **PUT** /asterisk/modules/{moduleName} | Reload an Asterisk module.
*AsteriskApi* | [**asterisk_ping_get**](docs/AsteriskApi.md#asterisk_ping_get) | **GET** /asterisk/ping | Response pong message.
*AsteriskApi* | [**asterisk_variable_get**](docs/AsteriskApi.md#asterisk_variable_get) | **GET** /asterisk/variable | Get the value of a global variable.
*AsteriskApi* | [**asterisk_variable_post**](docs/AsteriskApi.md#asterisk_variable_post) | **POST** /asterisk/variable | Set the value of a global variable.
*BridgesApi* | [**bridges_bridge_id_add_channel_post**](docs/BridgesApi.md#bridges_bridge_id_add_channel_post) | **POST** /bridges/{bridgeId}/addChannel | Add a channel to a bridge.
*BridgesApi* | [**bridges_bridge_id_delete**](docs/BridgesApi.md#bridges_bridge_id_delete) | **DELETE** /bridges/{bridgeId} | Shut down a bridge.
*BridgesApi* | [**bridges_bridge_id_get**](docs/BridgesApi.md#bridges_bridge_id_get) | **GET** /bridges/{bridgeId} | Get bridge details.
*BridgesApi* | [**bridges_bridge_id_moh_delete**](docs/BridgesApi.md#bridges_bridge_id_moh_delete) | **DELETE** /bridges/{bridgeId}/moh | Stop playing music on hold to a bridge.
*BridgesApi* | [**bridges_bridge_id_moh_post**](docs/BridgesApi.md#bridges_bridge_id_moh_post) | **POST** /bridges/{bridgeId}/moh | Play music on hold to a bridge or change the MOH class that is playing.
*BridgesApi* | [**bridges_bridge_id_play_playback_id_post**](docs/BridgesApi.md#bridges_bridge_id_play_playback_id_post) | **POST** /bridges/{bridgeId}/play/{playbackId} | Start playback of media on a bridge.
*BridgesApi* | [**bridges_bridge_id_play_post**](docs/BridgesApi.md#bridges_bridge_id_play_post) | **POST** /bridges/{bridgeId}/play | Start playback of media on a bridge.
*BridgesApi* | [**bridges_bridge_id_post**](docs/BridgesApi.md#bridges_bridge_id_post) | **POST** /bridges/{bridgeId} | Create a new bridge or updates an existing one.
*BridgesApi* | [**bridges_bridge_id_record_post**](docs/BridgesApi.md#bridges_bridge_id_record_post) | **POST** /bridges/{bridgeId}/record | Start a recording.
*BridgesApi* | [**bridges_bridge_id_remove_channel_post**](docs/BridgesApi.md#bridges_bridge_id_remove_channel_post) | **POST** /bridges/{bridgeId}/removeChannel | Remove a channel from a bridge.
*BridgesApi* | [**bridges_bridge_id_video_source_channel_id_post**](docs/BridgesApi.md#bridges_bridge_id_video_source_channel_id_post) | **POST** /bridges/{bridgeId}/videoSource/{channelId} | Set a channel as the video source in a multi-party mixing bridge. This operation has no effect on bridges with two or fewer participants.
*BridgesApi* | [**bridges_bridge_id_video_source_delete**](docs/BridgesApi.md#bridges_bridge_id_video_source_delete) | **DELETE** /bridges/{bridgeId}/videoSource | Removes any explicit video source in a multi-party mixing bridge. This operation has no effect on bridges with two or fewer participants. When no explicit video source is set, talk detection will be used to determine the active video stream.
*BridgesApi* | [**bridges_get**](docs/BridgesApi.md#bridges_get) | **GET** /bridges | List all active bridges in Asterisk.
*BridgesApi* | [**bridges_post**](docs/BridgesApi.md#bridges_post) | **POST** /bridges | Create a new bridge.
*ChannelsApi* | [**channels_channel_id_answer_post**](docs/ChannelsApi.md#channels_channel_id_answer_post) | **POST** /channels/{channelId}/answer | Answer a channel.
*ChannelsApi* | [**channels_channel_id_continue_post**](docs/ChannelsApi.md#channels_channel_id_continue_post) | **POST** /channels/{channelId}/continue | Exit application; continue execution in the dialplan.
*ChannelsApi* | [**channels_channel_id_delete**](docs/ChannelsApi.md#channels_channel_id_delete) | **DELETE** /channels/{channelId} | Delete (i.e. hangup) a channel.
*ChannelsApi* | [**channels_channel_id_dial_post**](docs/ChannelsApi.md#channels_channel_id_dial_post) | **POST** /channels/{channelId}/dial | Dial a created channel.
*ChannelsApi* | [**channels_channel_id_dtmf_post**](docs/ChannelsApi.md#channels_channel_id_dtmf_post) | **POST** /channels/{channelId}/dtmf | Send provided DTMF to a given channel.
*ChannelsApi* | [**channels_channel_id_get**](docs/ChannelsApi.md#channels_channel_id_get) | **GET** /channels/{channelId} | Channel details.
*ChannelsApi* | [**channels_channel_id_hold_delete**](docs/ChannelsApi.md#channels_channel_id_hold_delete) | **DELETE** /channels/{channelId}/hold | Remove a channel from hold.
*ChannelsApi* | [**channels_channel_id_hold_post**](docs/ChannelsApi.md#channels_channel_id_hold_post) | **POST** /channels/{channelId}/hold | Hold a channel.
*ChannelsApi* | [**channels_channel_id_moh_delete**](docs/ChannelsApi.md#channels_channel_id_moh_delete) | **DELETE** /channels/{channelId}/moh | Stop playing music on hold to a channel.
*ChannelsApi* | [**channels_channel_id_moh_post**](docs/ChannelsApi.md#channels_channel_id_moh_post) | **POST** /channels/{channelId}/moh | Play music on hold to a channel.
*ChannelsApi* | [**channels_channel_id_move_post**](docs/ChannelsApi.md#channels_channel_id_move_post) | **POST** /channels/{channelId}/move | Move the channel from one Stasis application to another.
*ChannelsApi* | [**channels_channel_id_mute_delete**](docs/ChannelsApi.md#channels_channel_id_mute_delete) | **DELETE** /channels/{channelId}/mute | Unmute a channel.
*ChannelsApi* | [**channels_channel_id_mute_post**](docs/ChannelsApi.md#channels_channel_id_mute_post) | **POST** /channels/{channelId}/mute | Mute a channel.
*ChannelsApi* | [**channels_channel_id_play_playback_id_post**](docs/ChannelsApi.md#channels_channel_id_play_playback_id_post) | **POST** /channels/{channelId}/play/{playbackId} | Start playback of media and specify the playbackId.
*ChannelsApi* | [**channels_channel_id_play_post**](docs/ChannelsApi.md#channels_channel_id_play_post) | **POST** /channels/{channelId}/play | Start playback of media.
*ChannelsApi* | [**channels_channel_id_post**](docs/ChannelsApi.md#channels_channel_id_post) | **POST** /channels/{channelId} | Create a new channel (originate with id).
*ChannelsApi* | [**channels_channel_id_record_post**](docs/ChannelsApi.md#channels_channel_id_record_post) | **POST** /channels/{channelId}/record | Start a recording.
*ChannelsApi* | [**channels_channel_id_redirect_post**](docs/ChannelsApi.md#channels_channel_id_redirect_post) | **POST** /channels/{channelId}/redirect | Redirect the channel to a different location.
*ChannelsApi* | [**channels_channel_id_ring_delete**](docs/ChannelsApi.md#channels_channel_id_ring_delete) | **DELETE** /channels/{channelId}/ring | Stop ringing indication on a channel if locally generated.
*ChannelsApi* | [**channels_channel_id_ring_post**](docs/ChannelsApi.md#channels_channel_id_ring_post) | **POST** /channels/{channelId}/ring | Indicate ringing to a channel.
*ChannelsApi* | [**channels_channel_id_rtp_statistics_get**](docs/ChannelsApi.md#channels_channel_id_rtp_statistics_get) | **GET** /channels/{channelId}/rtp_statistics | RTP stats on a channel.
*ChannelsApi* | [**channels_channel_id_silence_delete**](docs/ChannelsApi.md#channels_channel_id_silence_delete) | **DELETE** /channels/{channelId}/silence | Stop playing silence to a channel.
*ChannelsApi* | [**channels_channel_id_silence_post**](docs/ChannelsApi.md#channels_channel_id_silence_post) | **POST** /channels/{channelId}/silence | Play silence to a channel.
*ChannelsApi* | [**channels_channel_id_snoop_post**](docs/ChannelsApi.md#channels_channel_id_snoop_post) | **POST** /channels/{channelId}/snoop | Start snooping.
*ChannelsApi* | [**channels_channel_id_snoop_snoop_id_post**](docs/ChannelsApi.md#channels_channel_id_snoop_snoop_id_post) | **POST** /channels/{channelId}/snoop/{snoopId} | Start snooping.
*ChannelsApi* | [**channels_channel_id_variable_get**](docs/ChannelsApi.md#channels_channel_id_variable_get) | **GET** /channels/{channelId}/variable | Get the value of a channel variable or function.
*ChannelsApi* | [**channels_channel_id_variable_post**](docs/ChannelsApi.md#channels_channel_id_variable_post) | **POST** /channels/{channelId}/variable | Set the value of a channel variable or function.
*ChannelsApi* | [**channels_create_post**](docs/ChannelsApi.md#channels_create_post) | **POST** /channels/create | Create channel.
*ChannelsApi* | [**channels_external_media_post**](docs/ChannelsApi.md#channels_external_media_post) | **POST** /channels/externalMedia | Start an External Media session.
*ChannelsApi* | [**channels_get**](docs/ChannelsApi.md#channels_get) | **GET** /channels | List all active channels in Asterisk.
*ChannelsApi* | [**channels_post**](docs/ChannelsApi.md#channels_post) | **POST** /channels | Create a new channel (originate).
*DeviceStatesApi* | [**device_states_device_name_delete**](docs/DeviceStatesApi.md#device_states_device_name_delete) | **DELETE** /deviceStates/{deviceName} | Destroy a device-state controlled by ARI.
*DeviceStatesApi* | [**device_states_device_name_get**](docs/DeviceStatesApi.md#device_states_device_name_get) | **GET** /deviceStates/{deviceName} | Retrieve the current state of a device.
*DeviceStatesApi* | [**device_states_device_name_put**](docs/DeviceStatesApi.md#device_states_device_name_put) | **PUT** /deviceStates/{deviceName} | Change the state of a device controlled by ARI. (Note - implicitly creates the device state).
*DeviceStatesApi* | [**device_states_get**](docs/DeviceStatesApi.md#device_states_get) | **GET** /deviceStates | List all ARI controlled device states.
*EndpointsApi* | [**endpoints_get**](docs/EndpointsApi.md#endpoints_get) | **GET** /endpoints | List all endpoints.
*EndpointsApi* | [**endpoints_send_message_put**](docs/EndpointsApi.md#endpoints_send_message_put) | **PUT** /endpoints/sendMessage | Send a message to some technology URI or endpoint.
*EndpointsApi* | [**endpoints_tech_get**](docs/EndpointsApi.md#endpoints_tech_get) | **GET** /endpoints/{tech} | List available endoints for a given endpoint technology.
*EndpointsApi* | [**endpoints_tech_resource_get**](docs/EndpointsApi.md#endpoints_tech_resource_get) | **GET** /endpoints/{tech}/{resource} | Details for an endpoint.
*EndpointsApi* | [**endpoints_tech_resource_send_message_put**](docs/EndpointsApi.md#endpoints_tech_resource_send_message_put) | **PUT** /endpoints/{tech}/{resource}/sendMessage | Send a message to some endpoint in a technology.
*EventsApi* | [**events_get**](docs/EventsApi.md#events_get) | **GET** /events | WebSocket connection for events.
*EventsApi* | [**events_user_event_name_post**](docs/EventsApi.md#events_user_event_name_post) | **POST** /events/user/{eventName} | Generate a user event.
*MailboxesApi* | [**mailboxes_get**](docs/MailboxesApi.md#mailboxes_get) | **GET** /mailboxes | List all mailboxes.
*MailboxesApi* | [**mailboxes_mailbox_name_delete**](docs/MailboxesApi.md#mailboxes_mailbox_name_delete) | **DELETE** /mailboxes/{mailboxName} | Destroy a mailbox.
*MailboxesApi* | [**mailboxes_mailbox_name_get**](docs/MailboxesApi.md#mailboxes_mailbox_name_get) | **GET** /mailboxes/{mailboxName} | Retrieve the current state of a mailbox.
*MailboxesApi* | [**mailboxes_mailbox_name_put**](docs/MailboxesApi.md#mailboxes_mailbox_name_put) | **PUT** /mailboxes/{mailboxName} | Change the state of a mailbox. (Note - implicitly creates the mailbox).
*PlaybacksApi* | [**playbacks_playback_id_control_post**](docs/PlaybacksApi.md#playbacks_playback_id_control_post) | **POST** /playbacks/{playbackId}/control | Control a playback.
*PlaybacksApi* | [**playbacks_playback_id_delete**](docs/PlaybacksApi.md#playbacks_playback_id_delete) | **DELETE** /playbacks/{playbackId} | Stop a playback.
*PlaybacksApi* | [**playbacks_playback_id_get**](docs/PlaybacksApi.md#playbacks_playback_id_get) | **GET** /playbacks/{playbackId} | Get a playback&#39;s details.
*RecordingsApi* | [**recordings_live_recording_name_delete**](docs/RecordingsApi.md#recordings_live_recording_name_delete) | **DELETE** /recordings/live/{recordingName} | Stop a live recording and discard it.
*RecordingsApi* | [**recordings_live_recording_name_get**](docs/RecordingsApi.md#recordings_live_recording_name_get) | **GET** /recordings/live/{recordingName} | List live recordings.
*RecordingsApi* | [**recordings_live_recording_name_mute_delete**](docs/RecordingsApi.md#recordings_live_recording_name_mute_delete) | **DELETE** /recordings/live/{recordingName}/mute | Unmute a live recording.
*RecordingsApi* | [**recordings_live_recording_name_mute_post**](docs/RecordingsApi.md#recordings_live_recording_name_mute_post) | **POST** /recordings/live/{recordingName}/mute | Mute a live recording.
*RecordingsApi* | [**recordings_live_recording_name_pause_delete**](docs/RecordingsApi.md#recordings_live_recording_name_pause_delete) | **DELETE** /recordings/live/{recordingName}/pause | Unpause a live recording.
*RecordingsApi* | [**recordings_live_recording_name_pause_post**](docs/RecordingsApi.md#recordings_live_recording_name_pause_post) | **POST** /recordings/live/{recordingName}/pause | Pause a live recording.
*RecordingsApi* | [**recordings_live_recording_name_stop_post**](docs/RecordingsApi.md#recordings_live_recording_name_stop_post) | **POST** /recordings/live/{recordingName}/stop | Stop a live recording and store it.
*RecordingsApi* | [**recordings_stored_get**](docs/RecordingsApi.md#recordings_stored_get) | **GET** /recordings/stored | List recordings that are complete.
*RecordingsApi* | [**recordings_stored_recording_name_copy_post**](docs/RecordingsApi.md#recordings_stored_recording_name_copy_post) | **POST** /recordings/stored/{recordingName}/copy | Copy a stored recording.
*RecordingsApi* | [**recordings_stored_recording_name_delete**](docs/RecordingsApi.md#recordings_stored_recording_name_delete) | **DELETE** /recordings/stored/{recordingName} | Delete a stored recording.
*RecordingsApi* | [**recordings_stored_recording_name_file_get**](docs/RecordingsApi.md#recordings_stored_recording_name_file_get) | **GET** /recordings/stored/{recordingName}/file | Get the file associated with the stored recording.
*RecordingsApi* | [**recordings_stored_recording_name_get**](docs/RecordingsApi.md#recordings_stored_recording_name_get) | **GET** /recordings/stored/{recordingName} | Get a stored recording&#39;s details.
*SoundsApi* | [**sounds_get**](docs/SoundsApi.md#sounds_get) | **GET** /sounds | List all sounds.
*SoundsApi* | [**sounds_sound_id_get**](docs/SoundsApi.md#sounds_sound_id_get) | **GET** /sounds/{soundId} | Get a sound&#39;s details.


## Documentation For Models

 - [Application](docs/Application.md)
 - [ApplicationMoveFailed](docs/ApplicationMoveFailed.md)
 - [ApplicationMoveFailedAllOf](docs/ApplicationMoveFailedAllOf.md)
 - [ApplicationReplaced](docs/ApplicationReplaced.md)
 - [AsteriskInfo](docs/AsteriskInfo.md)
 - [AsteriskPing](docs/AsteriskPing.md)
 - [Bridge](docs/Bridge.md)
 - [BridgeAttendedTransfer](docs/BridgeAttendedTransfer.md)
 - [BridgeAttendedTransferAllOf](docs/BridgeAttendedTransferAllOf.md)
 - [BridgeBlindTransfer](docs/BridgeBlindTransfer.md)
 - [BridgeBlindTransferAllOf](docs/BridgeBlindTransferAllOf.md)
 - [BridgeCreated](docs/BridgeCreated.md)
 - [BridgeCreatedAllOf](docs/BridgeCreatedAllOf.md)
 - [BridgeDestroyed](docs/BridgeDestroyed.md)
 - [BridgeDestroyedAllOf](docs/BridgeDestroyedAllOf.md)
 - [BridgeMerged](docs/BridgeMerged.md)
 - [BridgeMergedAllOf](docs/BridgeMergedAllOf.md)
 - [BridgeVideoSourceChanged](docs/BridgeVideoSourceChanged.md)
 - [BridgeVideoSourceChangedAllOf](docs/BridgeVideoSourceChangedAllOf.md)
 - [BuildInfo](docs/BuildInfo.md)
 - [CallerID](docs/CallerID.md)
 - [Channel](docs/Channel.md)
 - [ChannelCallerId](docs/ChannelCallerId.md)
 - [ChannelCallerIdAllOf](docs/ChannelCallerIdAllOf.md)
 - [ChannelConnectedLine](docs/ChannelConnectedLine.md)
 - [ChannelConnectedLineAllOf](docs/ChannelConnectedLineAllOf.md)
 - [ChannelCreated](docs/ChannelCreated.md)
 - [ChannelCreatedAllOf](docs/ChannelCreatedAllOf.md)
 - [ChannelDestroyed](docs/ChannelDestroyed.md)
 - [ChannelDestroyedAllOf](docs/ChannelDestroyedAllOf.md)
 - [ChannelDialplan](docs/ChannelDialplan.md)
 - [ChannelDialplanAllOf](docs/ChannelDialplanAllOf.md)
 - [ChannelDtmfReceived](docs/ChannelDtmfReceived.md)
 - [ChannelDtmfReceivedAllOf](docs/ChannelDtmfReceivedAllOf.md)
 - [ChannelEnteredBridge](docs/ChannelEnteredBridge.md)
 - [ChannelEnteredBridgeAllOf](docs/ChannelEnteredBridgeAllOf.md)
 - [ChannelHangupRequest](docs/ChannelHangupRequest.md)
 - [ChannelHangupRequestAllOf](docs/ChannelHangupRequestAllOf.md)
 - [ChannelHold](docs/ChannelHold.md)
 - [ChannelHoldAllOf](docs/ChannelHoldAllOf.md)
 - [ChannelLeftBridge](docs/ChannelLeftBridge.md)
 - [ChannelLeftBridgeAllOf](docs/ChannelLeftBridgeAllOf.md)
 - [ChannelStateChange](docs/ChannelStateChange.md)
 - [ChannelStateChangeAllOf](docs/ChannelStateChangeAllOf.md)
 - [ChannelTalkingFinished](docs/ChannelTalkingFinished.md)
 - [ChannelTalkingFinishedAllOf](docs/ChannelTalkingFinishedAllOf.md)
 - [ChannelTalkingStarted](docs/ChannelTalkingStarted.md)
 - [ChannelTalkingStartedAllOf](docs/ChannelTalkingStartedAllOf.md)
 - [ChannelUnhold](docs/ChannelUnhold.md)
 - [ChannelUnholdAllOf](docs/ChannelUnholdAllOf.md)
 - [ChannelUserevent](docs/ChannelUserevent.md)
 - [ChannelUsereventAllOf](docs/ChannelUsereventAllOf.md)
 - [ChannelVarset](docs/ChannelVarset.md)
 - [ChannelVarsetAllOf](docs/ChannelVarsetAllOf.md)
 - [ConfigInfo](docs/ConfigInfo.md)
 - [ConfigTuple](docs/ConfigTuple.md)
 - [ContactInfo](docs/ContactInfo.md)
 - [ContactStatusChange](docs/ContactStatusChange.md)
 - [ContactStatusChangeAllOf](docs/ContactStatusChangeAllOf.md)
 - [Containers](docs/Containers.md)
 - [DeviceState](docs/DeviceState.md)
 - [DeviceStateChanged](docs/DeviceStateChanged.md)
 - [DeviceStateChangedAllOf](docs/DeviceStateChangedAllOf.md)
 - [Dial](docs/Dial.md)
 - [DialAllOf](docs/DialAllOf.md)
 - [DialplanCEP](docs/DialplanCEP.md)
 - [Endpoint](docs/Endpoint.md)
 - [EndpointStateChange](docs/EndpointStateChange.md)
 - [EndpointStateChangeAllOf](docs/EndpointStateChangeAllOf.md)
 - [Event](docs/Event.md)
 - [EventAllOf](docs/EventAllOf.md)
 - [FormatLangPair](docs/FormatLangPair.md)
 - [LiveRecording](docs/LiveRecording.md)
 - [LogChannel](docs/LogChannel.md)
 - [Mailbox](docs/Mailbox.md)
 - [Message](docs/Message.md)
 - [MissingParams](docs/MissingParams.md)
 - [MissingParamsAllOf](docs/MissingParamsAllOf.md)
 - [Module](docs/Module.md)
 - [Peer](docs/Peer.md)
 - [PeerStatusChange](docs/PeerStatusChange.md)
 - [PeerStatusChangeAllOf](docs/PeerStatusChangeAllOf.md)
 - [Playback](docs/Playback.md)
 - [PlaybackContinuing](docs/PlaybackContinuing.md)
 - [PlaybackContinuingAllOf](docs/PlaybackContinuingAllOf.md)
 - [PlaybackFinished](docs/PlaybackFinished.md)
 - [PlaybackFinishedAllOf](docs/PlaybackFinishedAllOf.md)
 - [PlaybackStarted](docs/PlaybackStarted.md)
 - [PlaybackStartedAllOf](docs/PlaybackStartedAllOf.md)
 - [RTPstat](docs/RTPstat.md)
 - [RecordingFailed](docs/RecordingFailed.md)
 - [RecordingFailedAllOf](docs/RecordingFailedAllOf.md)
 - [RecordingFinished](docs/RecordingFinished.md)
 - [RecordingFinishedAllOf](docs/RecordingFinishedAllOf.md)
 - [RecordingStarted](docs/RecordingStarted.md)
 - [RecordingStartedAllOf](docs/RecordingStartedAllOf.md)
 - [SetId](docs/SetId.md)
 - [Sound](docs/Sound.md)
 - [StasisEnd](docs/StasisEnd.md)
 - [StasisEndAllOf](docs/StasisEndAllOf.md)
 - [StasisStart](docs/StasisStart.md)
 - [StasisStartAllOf](docs/StasisStartAllOf.md)
 - [StatusInfo](docs/StatusInfo.md)
 - [StoredRecording](docs/StoredRecording.md)
 - [SystemInfo](docs/SystemInfo.md)
 - [TextMessage](docs/TextMessage.md)
 - [TextMessageReceived](docs/TextMessageReceived.md)
 - [TextMessageReceivedAllOf](docs/TextMessageReceivedAllOf.md)
 - [Variable](docs/Variable.md)


## Documentation For Authorization


## basicAuth

- **Type**: HTTP basic authentication


## Author




