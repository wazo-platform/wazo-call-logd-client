# Copyright 2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_call_logd_client.command import CallLogdCommand


class BaseCommand(CallLogdCommand):

    _headers = {'Accept': 'application/json'}

    def _get_headers(self, **kwargs):
        headers = dict(self._headers)
        # The requests session will use self.tenant_uuid by default
        tenant_uuid = kwargs.pop('tenant_uuid', None)
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid
        return headers
