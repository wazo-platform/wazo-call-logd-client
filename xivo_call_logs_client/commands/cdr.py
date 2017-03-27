# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from xivo_call_logs_client.command import CallLogdCommand


class CDRCommand(CallLogdCommand):
    def list(self):
        r = self.session.get(self._client.url('cdr'))
        self.raise_from_response(r)
        return r.json()
