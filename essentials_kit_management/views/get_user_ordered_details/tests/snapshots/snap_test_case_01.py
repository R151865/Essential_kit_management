# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetUserOrderedDetailsAPITestCase::test_case status'] = 200

snapshots['TestCase01GetUserOrderedDetailsAPITestCase::test_case body'] = [
    {
        'cost_incurred': 1,
        'item_id': 1,
        'item_name': 'string',
        'items_added': 1,
        'items_recived': 1,
        'out_of_stock': 1
    }
]

snapshots['TestCase01GetUserOrderedDetailsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '105',
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
