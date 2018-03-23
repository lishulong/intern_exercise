from pykit import timeutil


if __name__ == '__main__':
    time_utc = 'Tue, 24 Jan 2017 07:51:59 UTC'
    dt = timeutil.parse(time_utc, 'default')
    print dt
    dt = timeutil.parse(time_utc, 'utc')
    print dt
    print 

    time_mysql = '2018-12-1 11:20:30'
    dt = timeutil.parse(time_mysql, 'mysql')
    print dt
    print 

    print timeutil.format(dt, 'utc')
    print timeutil.format(dt, 'iso')
    print timeutil.format(dt, 'daily')
    print

    ts = timeutil.utc_datetime_to_ts(dt)
    print ts
    print

    time_mysql = timeutil.format_ts(ts, 'mysql')
    print time_mysql
    time_iso = timeutil.format_ts(ts, 'iso')
    print time_iso
    print

    ts = timeutil.ts()
    print ts
    time_mysql = timeutil.format_ts(ts, 'mysql')
    print time_mysql
    print

    ms = timeutil.ms()
    us = timeutil.us()
    ns = timeutil.ns()
    print ms
    print us
    print ns
    print

    print timeutil.to_sec(ms)
    print timeutil.to_sec(us)
    print timeutil.to_sec(ns)
