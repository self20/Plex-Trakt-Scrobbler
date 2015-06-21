from plugin.preferences.options.constants import ACTIVITY_BY_KEY, ActivityMode, ACTIVITY_BY_LABEL
from plugin.preferences.options.core.base import Option

import logging

log = logging.getLogger(__name__)


class Activity(Option):
    key = 'activity.mode'
    type = 'enum'

    choices = ACTIVITY_BY_KEY
    default = ActivityMode.Automatic
    scope = 'server'

    group = ('Activity',)
    label = 'Mode'

    preference = 'activity_mode'

    def on_plex_changed(self, value, account=None):
        if value not in ACTIVITY_BY_LABEL:
            log.warn('Unknown value: %r', value)
            return

        # Map plex `value`
        value = ACTIVITY_BY_LABEL[value]

        # Update database
        self.update(value, emit=False)
        return value
