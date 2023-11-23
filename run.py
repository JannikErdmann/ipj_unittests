from data_manager.data_manager import TestCase, TestCaseResult
from data_manager.data_manager import Collection

import datetime as dt

"""
category: production, power, consumption
"""


test_cases = [
    TestCase(
        description='Production lignite',
        timestamp=dt.datetime(year=2022, month=12, day=13, hour=12, minute=0),
        collection=self.smard,
        category='production',
        value_field='lignite',
        expected_value=3931.75 * 1_000_000
    ),
    TestCase(
        description='',
        timestamp=dt.datetime(year=2022, month=12, day=13, hour=12, minute=0),
        collection=self.smard,
        category='production',
        value_field='lignite',
        expected_value=3931.75 * 1_000_000
    ),
]