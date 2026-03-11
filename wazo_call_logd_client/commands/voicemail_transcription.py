# Copyright 2026 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from .helpers.base import BaseCommand


class VoicemailTranscriptionCommand(BaseCommand):
    def list_transcriptions(self, **params):
        if 'from_' in params:
            params['from'] = params.pop('from_')

        headers = self._get_headers()
        url = self._client.url('voicemails', 'transcriptions')
        r = self.session.get(url, params=params, headers=headers)
        self.raise_from_response(r)
        return r.json()
