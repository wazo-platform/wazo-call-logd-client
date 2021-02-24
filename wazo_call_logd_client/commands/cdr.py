# -*- coding: utf-8 -*-
# Copyright 2017-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_call_logd_client.command import CallLogdCommand


class CDRCommand(CallLogdCommand):

    def get_by_id(self, cdr_id):
        r = self.session.get(self._client.url('cdr', cdr_id))
        self.raise_from_response(r)
        return r.json()

    def get_by_id_csv(self, cdr_id):
        r = self.session.get(self._client.url('cdr', cdr_id), headers={'Accept': 'text/csv; charset=utf-8'})
        self.raise_from_response(r)
        return r.text

    def list(self, **params):
        if 'from_' in params:
            params['from'] = params.pop('from_')

        r = self.session.get(self._client.url('cdr'), params=params)
        self.raise_from_response(r)
        return r.json()

    def list_csv(self, **params):
        if 'from_' in params:
            params['from'] = params.pop('from_')

        r = self.session.get(self._client.url('cdr'), params=params, headers={'Accept': 'text/csv; charset=utf-8'})
        self.raise_from_response(r)
        return r.text

    def list_for_user(self, user_uuid, **params):
        if 'from_' in params:
            params['from'] = params.pop('from_')

        r = self.session.get(self._client.url('users', user_uuid, 'cdr'), params=params)
        self.raise_from_response(r)
        return r.json()

    def list_for_user_csv(self, user_uuid, **params):
        if 'from_' in params:
            params['from'] = params.pop('from_')

        r = self.session.get(self._client.url('users', user_uuid, 'cdr'), params=params, headers={'Accept': 'text/csv; charset=utf-8'})
        self.raise_from_response(r)
        return r.text

    def list_from_user(self, **params):
        if 'from_' in params:
            params['from'] = params.pop('from_')

        r = self.session.get(self._client.url('users', 'me', 'cdr'), params=params)
        self.raise_from_response(r)
        return r.json()

    def list_from_user_csv(self, **params):
        if 'from_' in params:
            params['from'] = params.pop('from_')

        r = self.session.get(self._client.url('users', 'me', 'cdr'), params=params, headers={'Accept': 'text/csv; charset=utf-8'})
        self.raise_from_response(r)
        return r.text

    def delete_cdrs_recording_media(self, cdr_ids, **kwargs):
        tenant_uuid = kwargs.pop('tenant_uuid', None) or self._client.tenant()
        headers = {}
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid
        url = self._client.url('cdr', 'recordings', 'media')
        body = {'cdr_ids': cdr_ids}
        r = self.session.delete(url, json=body, headers=headers)
        self.raise_from_response(r)

    def get_recording_media(self, cdr_id, recording_uuid, **kwargs):
        tenant_uuid = kwargs.pop('tenant_uuid', None) or self._client.tenant()
        headers = {'Accept': '*/*'}
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid
        url = self._client.url('cdr', cdr_id, 'recordings', recording_uuid, 'media')
        r = self.session.get(url, headers=headers)
        self.raise_from_response(r)
        return r

    def delete_recording_media(self, cdr_id, recording_uuid, **kwargs):
        tenant_uuid = kwargs.pop('tenant_uuid', None) or self._client.tenant()
        headers = {}
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid
        url = self._client.url('cdr', cdr_id, 'recordings', recording_uuid, 'media')
        r = self.session.delete(url, headers=headers)
        self.raise_from_response(r)
