#!/usr/bin/env python3
# Copyright 2017-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from setuptools import find_packages, setup

setup(
    name='wazo_call_logd_client',
    version='1.0',
    description='a simple client library for the wazo-call-logd HTTP interface',
    author='Wazo Authors',
    author_email='dev@wazo.community',
    url='http://wazo.community',
    packages=find_packages(),
    entry_points={
        'wazo_call_logd_client.commands': [
            'agent_statistics = wazo_call_logd_client.commands.agent_statistics:AgentStatisticsCommand',  # noqa
            'cdr = wazo_call_logd_client.commands.cdr:CDRCommand',
            'config = wazo_call_logd_client.commands.config:ConfigCommand',
            'export = wazo_call_logd_client.commands.export:ExportCommand',
            'queue_statistics = wazo_call_logd_client.commands.queue_statistics:QueueStatisticsCommand',  # noqa
            'retention = wazo_call_logd_client.commands.retention:RetentionCommand',
            'status = wazo_call_logd_client.commands.status:StatusCommand',
        ],
    },
)
