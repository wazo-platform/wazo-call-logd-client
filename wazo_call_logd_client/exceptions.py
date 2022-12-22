# Copyright 2017-2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from requests import HTTPError


class CallLogdError(HTTPError):
    def __init__(self, response):
        try:
            body = response.json()
        except ValueError:
            raise InvalidCallLogdError()

        self.status_code = response.status_code
        try:
            self.message = body['message']
            self.error_id = body['error_id']
            self.details = body['details']
            self.timestamp = body['timestamp']
        except KeyError:
            raise InvalidCallLogdError()

        exception_message = f'{self.message}: {self.details}'
        super().__init__(exception_message, response=response)


class CallLogdServiceUnavailable(CallLogdError):
    pass


class InvalidCallLogdError(Exception):
    pass
