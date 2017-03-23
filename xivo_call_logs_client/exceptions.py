# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from requests import HTTPError


class CallLogdError(HTTPError):

    def __init__(self, response):
        body = response.json()
        self.status_code = response.status_code
        try:
            self.message = body['message']
            self.error_id = body['error_id']
            self.details = body['details']
            self.timestamp = body['timestamp']
        except KeyError:
            raise InvalidCallLogdError()

        exception_message = '{e.message}: {e.details}'.format(e=self)
        super(CallLogdError, self).__init__(exception_message, response=response)


class CallLogdServiceUnavailable(CallLogdError):
    pass


class InvalidCallLogdError(Exception):
    pass
