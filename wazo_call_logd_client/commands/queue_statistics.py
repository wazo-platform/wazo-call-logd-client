# -*- coding: utf-8 -*-
# Copyright 2020 The Wazo Authors  (see AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_call_logd_client.command import CallLogdCommand


class QueueStatisticsCommand(CallLogdCommand):

    def get_by_id(self, queue_id, **params):
        if 'from_' in params:
            params['from'] = params.pop('from_')

        r = self.session.get(self._client.url('queues', queue_id, 'statistics'), params=params)
        self.raise_from_response(r)
        return r.json()

    def list(self, **params):
        if 'from_' in params:
            params['from'] = params.pop('from_')

        r = self.session.get(self._client.url('queues', 'statistics'), params=params)
        self.raise_from_response(r)
        return r.json()

    def get_qos_by_id(self, queue_id, **params):
        if 'from_' in params:
            params['from'] = params.pop('from_')

        r = self.session.get(
            self._client.url('queues', queue_id, 'statistics', 'qos'), params=params
        )
        self.raise_from_response(r)
        return r.json()
