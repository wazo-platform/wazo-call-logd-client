# -*- coding: utf-8 -*-
# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_call_logd_client.command import CallLogdCommand


class StatusCommand(CallLogdCommand):

    def get(self):
        r = self.session.get(self._client.url('status'))
        self.raise_from_response(r)
        return r.json()
