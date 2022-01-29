from enum import Enum, unique


@unique
class ForecastType(Enum):
    TODAY = 'today'
    FIVEDAY = '5day'
    TENDAYS = '10day'
    WEEKEND = 'weekend'