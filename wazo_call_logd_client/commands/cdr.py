# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_call_logd_client.command import CallLogdCommand


class CDRCommand(CallLogdCommand):
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
