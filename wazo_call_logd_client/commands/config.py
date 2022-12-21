# Copyright 2021-2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from .helpers.base import BaseCommand


class ConfigCommand(BaseCommand):

    def get(self):
        headers = self._get_headers()
        url = self._client.url('config')
        r = self.session.get(url, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def patch(self, config_patch):
        headers = self._get_headers()
        url = self._client.url('config')
        r = self.session.patch(url, headers=headers, json=config_patch)
        self.raise_from_response(r)
        return r.json()
