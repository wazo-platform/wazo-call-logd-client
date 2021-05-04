# -*- coding: utf-8 -*-
# Copyright 2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later


from .helpers.base import BaseCommand


class ConfigCommand(BaseCommand):

    def get(self):
        headers = self._get_headers()
        url = self._client.url('config')
        r = self.session.get(url, headers=headers)
        self.raise_from_response(r)
        return r.json()
