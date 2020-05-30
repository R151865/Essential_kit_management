# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01CreateTransactionRequestAPITestCase::test_case status'] = 200

snapshots['TestCase01CreateTransactionRequestAPITestCase::test_case body'] = {
    'QR_code': 'string',
    'account_holder': 'string',
    'account_number': 'string',
    'phone_number': 1
}

snapshots['TestCase01CreateTransactionRequestAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '89',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'application/json'
    ],
    'vary': [
        'Accept-Language, Origin',
        'Vary'
    ],
    'x-frame-options': [
        'DENY',
        'X-Frame-Options'
    ]
}
