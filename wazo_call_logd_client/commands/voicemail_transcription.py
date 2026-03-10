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

    def list_from_user(self, **params):
        if 'from_' in params:
            params['from'] = params.pop('from_')

        headers = self._get_headers()
        url = self._client.url('users', 'me', 'voicemails', 'transcriptions')
        r = self.session.get(url, params=params, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def get_from_user(self, voicemail_message_id):
        headers = self._get_headers()
        url = self._client.url(
            'users', 'me', 'voicemails', voicemail_message_id, 'transcription'
        )
        r = self.session.get(url, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def list_for_user(self, user_uuid, **params):
        if 'from_' in params:
            params['from'] = params.pop('from_')

        headers = self._get_headers()
        url = self._client.url(
            'users', user_uuid, 'voicemails', 'transcriptions'
        )
        r = self.session.get(url, params=params, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def get_for_user(self, user_uuid, voicemail_message_id):
        headers = self._get_headers()
        url = self._client.url(
            'users', user_uuid, 'voicemails', voicemail_message_id, 'transcription'
        )
        r = self.session.get(url, headers=headers)
        self.raise_from_response(r)
        return r.json()
