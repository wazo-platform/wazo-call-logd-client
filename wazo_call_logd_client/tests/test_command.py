# Copyright 2017-2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from hamcrest import assert_that, calling, raises
from unittest.mock import Mock, patch
from unittest import TestCase

from ..command import CallLogdCommand
from ..exceptions import CallLogdServiceUnavailable, CallLogdError

SOME_ERROR_BODY = {
    'message': 'some message',
    'error_id': 'some-error-id',
    'details': {},
    'timestamp': 'some-date',
}


class TestCallLogdCommand(TestCase):
    @patch('wazo_call_logd_client.command.HTTPCommand.raise_from_response')
    def test_raise_from_response_no_error(self, parent_raise):
        response = Mock(status_code=200)
        response.json.return_value = {}

        CallLogdCommand.raise_from_response(response)

        parent_raise.assert_called_once_with(response)

    def test_raise_from_response_503(self):
        response = Mock(status_code=503)
        response.json.return_value = SOME_ERROR_BODY

        assert_that(
            calling(CallLogdCommand.raise_from_response).with_args(response),
            raises(CallLogdServiceUnavailable),
        )

    def test_raise_from_response_default_error(self):
        response = Mock(status_code=999)
        response.json.return_value = SOME_ERROR_BODY

        assert_that(
            calling(CallLogdCommand.raise_from_response).with_args(response),
            raises(CallLogdError),
        )
