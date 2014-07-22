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
	test = mydep[u'values']
	first = test[0]
	mytime = first[u'time_timetable_utc']
	datestr = datetime.strptime( mytime[:-1], "%Y-%m-%dT%H:%M:%S" )
	mytime = utc_to_local(datestr)
	return mytime


"""
#print ptvapi.search("parliment railway station")

#ptvapi.healthCheck()

#print ptvapi.search('batman')

#print ptvapi.stopsNearby(-38, 145)

#print ptvapi.broadNextDepartures(0,1014,2)

#next train upfield train from Batman
#mydep = ptvapi.specificNextDepartures(0,15,1014,0,1)
#def specificNextDepartures(mode, line, stop, directionid, limit, for_utc=nownomicro()):

mydep_broad = ptvapi.broadNextDepartures('train', 1155, 10)
#next train, upfield line, from Parliment, direction to city, limit 1

#print mydep
print "*****************"


print first
print "*****************"
mytime = first[u'time_timetable_utc']

second = test[1]
print second
mytime_two = second[u'time_timetable_utc']
datestr_two = datetime.strptime( mytime_two[:-1], "%Y-%m-%dT%H:%M:%S" )

datestr = datetime.strptime( mytime[:-1], "%Y-%m-%dT%H:%M:%S" )

print "+++++++++++++++++++++++++++++"
print utc_to_local(datestr)
print "-------------------"
#print utc_to_local(datestr_two)
"""