# Copyright 2017-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_lib_rest_client.client import BaseClient


class Client(BaseClient):
    namespace = 'wazo_call_logd_client.commands'

    def __init__(
        self, host, port=443, prefix='/api/call-logd', version='1.0', **kwargs
    ):
        super().__init__(host=host, port=port, prefix=prefix, version=version, **kwargs)
