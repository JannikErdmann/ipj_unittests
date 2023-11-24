from data_manager.data_manager import TestCase, TestCaseResult
from data_manager.data_manager import Collection

import datetime as dt

"""
category: production, power, consumption
"""

#Schaltjahre
test_cases = [
    TestCase(
        description='Production pv',
        timestamp=dt.datetime(year=2016, month=2, day=29, hour=9, minute=45),
        collection=self.smard,
        category='production',
        value_field='pv',
        expected_value=1126.75 * 1_000_000
    ),
    TestCase(
        description='Production Biomass',
        timestamp=dt.datetime(year=2020, month=2, day=29, hour=9, minute=45),
        collection=self.smard,
        category='production',
        value_field='biomass',
        expected_value=1241.75 * 1_000_000
    ),
]


#DST Timestamp for 2015/03/29/2:00-3:00 doesnt exist
test_cases = [
    TestCase(
        description='Power lignite DST',
        timestamp=dt.datetime(year=2015, month=3, day=29, hour=4, minute=0),
        collection=self.smard,
        category='power',
        value_field='lignite',
        expected_value=21160 * 1_000_000
    ),
 

    #DST 2 values -> fail ( timechange 3 -> 2)
    TestCase(
        description='Production hydro DST 25.10',
        timestamp=dt.datetime(year=2015, month=10, day=25, hour=2, minute=0),
        collection=self.smard,
        category='production',
        value_field='hydro',
        expected_value=311.75 * 1_000_000
    ),

      TestCase(
        description='Production hydro DST 25.10',
        timestamp=dt.datetime(year=2015, month=10, day=25, hour=2, minute=0),
        collection=self.smard,
        category='production',
        value_field='hydro',
        expected_value=321.25 * 1_000_000
    ),

    TestCase(
        description='Production gas DST 27.03.16',
        timestamp=dt.datetime(year=2016, month=3, day=27, hour=6, minute=30),
        collection=self.smard,
        category='production',
        value_field='gas',
        expected_value=267.5 * 1_000_000
    ),

      TestCase(
        description='Power offshore DST 30.10.16',
        timestamp=dt.datetime(year=2016, month=10, day=30, hour=6, minute=30),
        collection=self.smard,
        category='power',
        value_field='wind_offshore',
        expected_value=3283 * 1_000_000
    ),

       TestCase(
        description='Production onshore DST 27.03.17',
        timestamp=dt.datetime(year=2017, month=3, day=26, hour=16, minute=45),
        collection=self.smard,
        category='production',
        value_field='wind_onshore',
        expected_value=543.75 * 1_000_000
    ),

      TestCase(
        description='Power nuclear DST 29.10.17',
        timestamp=dt.datetime(year=2017, month=10, day=29, hour=16, minute=45),
        collection=self.smard,
        category='power',
        value_field='nuclear',
        expected_value=2338.25 * 1_000_000
    ),


          TestCase(
        description='Production onshore DST 28.10.18',
        timestamp=dt.datetime(year=2018, month=10, day=28, hour=23, minute=00),
        collection=self.smard,
        category='production',
        value_field='solar',
        expected_value=0 * 1_000_000
    ),

      TestCase(
        description='Power other_conventionals DST 25.3.18',
        timestamp=dt.datetime(year=2018, month=3, day=25, hour=23, minute=0),
        collection=self.smard,
        category='power',
        value_field='other_conventionals',
        expected_value=2338.25 * 1_000_000
    ),

        TestCase(
        description='Production onshore DST 31.3.19',
        timestamp=dt.datetime(year=2019, month=3, day=31, hour=15, minute=15),
        collection=self.smard,
        category='production',
        value_field='biomass',
        expected_value=1206.5 * 1_000_000
    ),

      TestCase(
        description='Power hydro DST 27.10.19',
        timestamp=dt.datetime(year=2019, month=10, day=27, hour=15, minute=15),
        collection=self.smard,
        category='power',
        value_field='hydro',
        expected_value=5281 * 1_000_000
    ),

            TestCase(
        description='Production other_renewables DST 29.3.2020',
        timestamp=dt.datetime(year=2010, month=3, day=29, hour=8, minute=0),
        collection=self.smard,
        category='production',
        value_field='other_renewables',
        expected_value=42.5 * 1_000_000
    ),

      TestCase(
        description='Power other_renewables DST 25.10.20',
        timestamp=dt.datetime(year=2020, month=10, day=25, hour=8, minute=0),
        collection=self.smard,
        category='power',
        value_field='other_renewables',
        expected_value=454 * 1_000_000
    ),

             TestCase(
        description='Production other_renewables DST 29.3.2020',
        timestamp=dt.datetime(year=2020, month=3, day=29, hour=8, minute=0),
        collection=self.smard,
        category='production',
        value_field='other_renewables',
        expected_value=42.5 * 1_000_000
    ),

      TestCase(
        description='Power other_renewables DST 25.10.20',
        timestamp=dt.datetime(year=2020, month=10, day=25, hour=8, minute=0),
        collection=self.smard,
        category='power',
        value_field='other_renewables',
        expected_value=454 * 1_000_000
    ),

          TestCase(
        description='Production onshore DST 28.3.2021',
        timestamp=dt.datetime(year=2021, month=3, day=28, hour=1, minute=30),
        collection=self.smard,
        category='production',
        value_field='wind_onshore',
        expected_value=4247.5 * 1_000_000
    ),

      TestCase(
        description='Power biomass DST 31.10.2021',
        timestamp=dt.datetime(year=2021, month=10, day=31, hour=1, minute=30),
        collection=self.smard,
        category='power',
        value_field='biomass',
        expected_value=8400 * 1_000_000
    ),

        TestCase(
        description='Production  other_conventionals DST 27.3.2022',
        timestamp=dt.datetime(year=2022, month=3, day=27, hour=0, minute=0),
        collection=self.smard,
        category='production',
        value_field='other_conventionals',
        expected_value=337.25 * 1_000_000
    ),

      TestCase(
        description='Power lignite DST 30.10.2022',
        timestamp=dt.datetime(year=2022, month=10, day=30, hour=0, minute=0),
        collection=self.smard,
        category='power',
        value_field='lignite',
        expected_value=18544 * 1_000_000
    ),

            TestCase(
        description='Production  coal DST 26.3.2023',
        timestamp=dt.datetime(year=2023, month=3, day=26, hour=18, minute=45),
        collection=self.smard,
        category='production',
        value_field='coal',
        expected_value=415 * 1_000_000
    ),

      TestCase(
        description='Power gas DST 29.10.2023',
        timestamp=dt.datetime(year=2023, month=10, day=29, hour=18, minute=45),
        collection=self.smard,
        category='power',
        value_field='gas',
        expected_value=30553 * 1_000_000
    ),
]


#new year

test_cases = [
    TestCase(
        description='Production wind onshore new year',
        timestamp=dt.datetime(year=2021, month=12, day=31, hour=23, minute=45),
        collection=self.smard,
        category='production',
        value_field='wind_onshore',
        expected_value=6424.75 * 1_000_000
    ),
    TestCase(
        description='Production wind_onshore new year',
        timestamp=dt.datetime(year=2022, month=1, day=1, hour=0, minute=0),
        collection=self.smard,
        category='production',
        value_field='wind_onshore',
        expected_value=6433.75 * 1_000_000
    ),
]