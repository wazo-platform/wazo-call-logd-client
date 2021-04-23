# -*- coding: utf-8 -*-
# Copyright 2021 The Wazo Authors  (see AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_call_logd_client.command import CallLogdCommand


class RetentionCommand(CallLogdCommand):

    headers = {'Accept': 'application/json'}

    def get(self, tenant_uuid=None):
        tenant_uuid = tenant_uuid or self._client.tenant()
        headers = self.headers.copy()
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid

        url = self._client.url('retention')
        r = self.session.get(url, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def update(self, tenant_uuid=None, **body):
        tenant_uuid = tenant_uuid or self._client.tenant()
        headers = self.headers.copy()
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid

        url = self._client.url('retention')
        r = self.session.put(url, json=body, headers=headers)
        self.raise_from_response(r)
