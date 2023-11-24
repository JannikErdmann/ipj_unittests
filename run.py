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
        description='Production PV',
        timestamp=dt.datetime(year=2021, month=3, day=12, hour=14, minute=15),
        collection=self.smard,
        category='production',
        value_field='pv',
        expected_value=3727.75 * 1_000_000
    ),
    TestCase(
        description='Production Other Renewables',
        timestamp=dt.datetime(year=2018, month=11, day=23, hour=22, minute=30),
        collection=self.smard,
        category='production',
        value_field='other_renewables',
        expected_value=38.25 * 1_000_000
    ),
    TestCase(
        description='Production On-Shore',
        timestamp=dt.datetime(year=2017, month=2, day=8, hour=9, minute=0),
        collection=self.smard,
        category='production',
        value_field='wind_onshore',
        expected_value=1836.5 * 1_000_000
    ),
    TestCase(
        description='Poduction Gas',
        timestamp=dt.datetime(year=2020, month=7, day=27, hour=3, minute=15),
        collection=self.smard,
        category='production',
        value_field='gas',
        expected_value=2108.25 * 1_000_000
    ),
    TestCase(
        description='Consumption Load',
        timestamp=dt.datetime(year=2020, month=9, day=15, hour=16, minute=0),
        collection=self.smard,
        category='consumption',
        value_field='load',
        expected_value=15560.5 * 1_000_000
    ),
    TestCase(
        description='Consumption Load',
        timestamp=dt.datetime(year=2019, month=2, day=25, hour=14, minute=45),
        collection=self.smard,
        category='consumption',
        value_field='load',
        expected_value=16548.75 * 1_000_000
    ),
    TestCase(
        description='Consumption Load',
        timestamp=dt.datetime(year=2016, month=5, day=3, hour=12, minute=30),
        collection=self.smard,
        category='consumption',
        value_field='load',
        expected_value=17392.75 * 1_000_000
    ),
]