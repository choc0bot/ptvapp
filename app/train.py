import ptvapi

import calendar
from datetime import datetime, timedelta

def utc_to_local(utc_dt):
    # get integer timestamp to avoid precision lost
    timestamp = calendar.timegm(utc_dt.timetuple())
    local_dt = datetime.fromtimestamp(timestamp)
    assert utc_dt.resolution >= timedelta(microseconds=1)
    return local_dt.replace(microsecond=utc_dt.microsecond)


def next_upfield():
	mydep = ptvapi.specificNextDepartures(0,15,1155,14,1)
	train_list = mydep[u'values']
	first = train_list[0]
	if len(train_list)>1:
		first = train_list[1]
	mytime = first[u'time_timetable_utc']
	datestr = datetime.strptime( mytime[:-1], "%Y-%m-%dT%H:%M:%S" )
	mytime = utc_to_local(datestr)
	return mytime
