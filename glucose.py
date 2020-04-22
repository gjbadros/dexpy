import datetime
import re

NightscoutTrendStrings = ['None', 'DoubleUp', 'SingleUp', 'FortyFiveUp', 'Flat', 'FortyFiveDown', 'SingleDown', 'DoubleDown', 'NotComputable', 'OutOfRange']

def parseDateTime(val):
    res = re.search("Date\\((\\d*)", val)
    epoch = float(res.group(1)) / 1000
    return datetime.datetime.utcfromtimestamp(epoch)

class GlucoseValue():
    def __init__(self, dt, wt, st, value, trend):
        self.dt = dt
        self.wt = wt
        self.st = st
        self.value = value
        self.trend = trend
        self.trendString = self.trendAsString(trend)
        self.trackingId = None

    def trendAsString(self, trend):
        return NightscoutTrendStrings[trend]

    @staticmethod
    def fromJson(jsonResponse, timeoffset):
        dt = parseDateTime(jsonResponse["DT"]) + timeoffset
        wt = parseDateTime(jsonResponse["WT"]) + timeoffset
        st = parseDateTime(jsonResponse["ST"]) + timeoffset
        value = float(jsonResponse["Value"])
        trend = int(jsonResponse["Trend"])
        return GlucoseValue(dt, wt, st, value, trend)

    def __cmp__(self, other):
        secondDifference = (self.st - other.st).total_seconds()
        if abs(secondDifference) < 240 and \
            self.trend == other.trend and \
            int(round(self.value)) != int(round(other.value)):
            return 0
        return secondDifference if secondDifference != 0 else 1

    def equals(self, other):
        secondDifference = abs((self.st - other.st).total_seconds())
        if secondDifference >= 240:
            return False
        if self.trend != other.trend:
            return False
        if int(round(self.value)) != int(round(other.value)):
            return False

        return True

    def __str__(self):
        return "DT: %s WT: %s ST: %s Trend: %s Value: %f" % (self.dt, self.wt, self.st, self.trendString, self.value)