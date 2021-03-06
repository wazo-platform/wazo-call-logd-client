# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from hamcrest import assert_that
from hamcrest import calling
from hamcrest import equal_to
from hamcrest import raises
from mock import Mock
from unittest import TestCase

from ..exceptions import CallLogdError
from ..exceptions import InvalidCallLogdError


class TestCallLogdError(TestCase):

    def test_when_response_has_no_json_then_raise_invalid(self):
        response = Mock()
        response.json.side_effect = ValueError

        assert_that(calling(CallLogdError).with_args(response),
                    raises(InvalidCallLogdError))

    def test_when_response_is_missing_keys_then_raise_invalid(self):
        response = Mock()
        response.json.return_value = {}

        assert_that(calling(CallLogdError).with_args(response),
                    raises(InvalidCallLogdError))

    def test_when_response_is_valid_then_return(self):
        response = Mock()
        response.json.return_value = {
            'message': 'message',
            'error_id': 'error_id',
            'details': 'details',
            'timestamp': 'timestamp',
        }

        error = CallLogdError(response)

        assert_that(error.response, equal_to(response))
