# Copyright 2021-2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from .helpers.base import BaseCommand


class ExportCommand(BaseCommand):
    def get(self, export_uuid, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        url = self._client.url('exports', export_uuid)
        r = self.session.get(url, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def download(self, export_uuid, tenant_uuid=None):
        headers = self._get_headers(write=True, tenant_uuid=tenant_uuid)
        url = self._client.url('exports', export_uuid, 'download')
        r = self.session.get(url, headers=headers)
        self.raise_from_response(r)
        return r
