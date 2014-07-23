import ptvapi

import calendar
from datetime import datetime, timedelta

work_train = (1155,14)
home_train = (1014,0)


def utc_to_local(utc_dt):
    # get integer timestamp to avoid precision lost
    timestamp = calendar.timegm(utc_dt.timetuple())
    local_dt = datetime.fromtimestamp(timestamp)
    assert utc_dt.resolution >= timedelta(microseconds=1)
    return local_dt.replace(microsecond=utc_dt.microsecond)

def timestring(mytime):
	mytimestr = mytime.strftime('%H:%M')
	return mytimestr

def get_train_time(train_tuple):
	mydep = ptvapi.specificNextDepartures(0,15,train_tuple[0],train_tuple[1],1)
	train_list = mydep[u'values']
	first = train_list[0]
	if len(train_list)>1:
		first = train_list[1]
	mytime = first[u'time_timetable_utc']
	datestr = datetime.strptime( mytime[:-1], "%Y-%m-%dT%H:%M:%S" )
	mytime = utc_to_local(datestr)
	return timestring(mytime)

"""
def next_upfield():
	mydep = ptvapi.specificNextDepartures(0,15,1155,14,1)
	train_list = mydep[u'values']
	first = train_list[0]
	if len(train_list)>1:
		first = train_list[1]
	mytime = first[u'time_timetable_utc']
	datestr = datetime.strptime( mytime[:-1], "%Y-%m-%dT%H:%M:%S" )
	mytime = utc_to_local(datestr)
	return timestring(mytime)

def next_batman():
	mydep = ptvapi.specificNextDepartures(0,15,1014,0,1)
	train_list = mydep[u'values']
	first = train_list[0]
	if len(train_list)>1:
		first = train_list[1]
	mytime = first[u'time_timetable_utc']
	datestr = datetime.strptime( mytime[:-1], "%Y-%m-%dT%H:%M:%S" )
	mytime = utc_to_local(datestr)
	return timestring(mytime)

"""

def c_time():
	#curtime = datetime.now().time()
	curtime = datetime.now().strftime('%H:%M')
	return curtime


#print c_time()

#print get_train_time(work_train)

#print get_train_time(home_train)