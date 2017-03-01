# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from xivo_lib_rest_client.client import BaseClient


class Client(BaseClient):

    namespace = 'call_logs_client.commands'

    def __init__(self,
                 host,
                 port=9298,
                 version='1.0',
                 **kwargs):
        super(Client, self).__init__(
            host=host,
            port=port,
            version=version,
            **kwargs)
