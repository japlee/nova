# Copyright 2013 NEC Corporation.  All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import copy

from nova.api.validation import parameter_types

create = {
    'type': 'object',
    'properties': {
        'agent': {
            'type': 'object',
            'properties': {
                'hypervisor': {
                    'type': 'string', 'minLength': 0, 'maxLength': 255,
                    'pattern': '^[a-zA-Z0-9-._ ]*$'
                },
                'os': {
                    'type': 'string', 'minLength': 0, 'maxLength': 255,
                    'pattern': '^[a-zA-Z0-9-._ ]*$'
                },
                'architecture': {
                    'type': 'string', 'minLength': 0, 'maxLength': 255,
                    'pattern': '^[a-zA-Z0-9-._ ]*$'
                },
                'version': {
                    'type': 'string', 'minLength': 0, 'maxLength': 255,
                    'pattern': '^[a-zA-Z0-9-._ ]*$'
                },
                'url': {
                    'type': 'string', 'minLength': 0, 'maxLength': 255,
                    'format': 'uri'
                },
                'md5hash': {
                    'type': 'string', 'minLength': 0, 'maxLength': 255,
                    'pattern': '^[a-fA-F0-9]*$'
                },
            },
            'required': ['hypervisor', 'os', 'architecture', 'version',
                         'url', 'md5hash'],
            'additionalProperties': False,
        },
    },
    'required': ['agent'],
    'additionalProperties': False,
}


update = {
    'type': 'object',
    'properties': {
        'para': {
            'type': 'object',
            'properties': {
                'version': {
                    'type': 'string', 'minLength': 0, 'maxLength': 255,
                    'pattern': '^[a-zA-Z0-9-._ ]*$'
                },
                'url': {
                    'type': 'string', 'minLength': 0, 'maxLength': 255,
                    'format': 'uri'
                },
                'md5hash': {
                    'type': 'string', 'minLength': 0, 'maxLength': 255,
                    'pattern': '^[a-fA-F0-9]*$'
                },
            },
            'required': ['version', 'url', 'md5hash'],
            'additionalProperties': False,
        },
    },
    'required': ['para'],
    'additionalProperties': False,
}

index_query = {
    'type': 'object',
    'properties': {
        'hypervisor': parameter_types.common_query_param
    },
    # NOTE(gmann): This is kept True to keep backward compatibility.
    # As of now Schema validation stripped out the additional parameters and
    # does not raise 400. In microversion 2.75, we have blocked the additional
    # parameters.
    'additionalProperties': True
}

index_query_275 = copy.deepcopy(index_query)
index_query_275['additionalProperties'] = False
