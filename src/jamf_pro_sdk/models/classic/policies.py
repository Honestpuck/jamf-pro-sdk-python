from typing import Optional, Union

from pydantic import Extra

from .. import BaseModel
from . import ClassicApiModel

_XML_ARRAY_ITEM_NAMES = {
    # general
    "id": "id",
    "name": "name",
    "enabled": "enabled",
    "trigger": "trigger",
    "trigger_checkin": "trigger_checkin",
    "trigger_enrolment_complete": "trigger_enrolment_complete",
    "trigger_login": "trigger_login",
    "trigger_network_state_changed": "trigger_network_state_changed",
    "trigger_startup": "trigger_startup",
    "trigger_other": "trigger_other",
    "frequency": "frequency",
    "retry_event": "retry_event",
    "retry_attempts": "retry_attempts",
    "notify_on_each_failed_retry": "notify_on_each_failed_retry",
    "location_user_only": "location_user_only",
    "target_drive": "target_drive",
    "offline": "offline",
    
}