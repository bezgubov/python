#!/usr/bin/env python

'''
Dependencies in Ubuntu: sudo apt-get install python-psycopg2
'''

import psycopg2
import sys
import os

hostname = os.uname()[1]
host = 'localhost'
ports = (5432, 5433, 5434, 5435)


def get_query(host, port, query):
    con = None
    result = []

    try:
        con = psycopg2.connect(database='pgbouncer',
                               user='postgres',
                               port=port)
        con.set_isolation_level(0)
        cur = con.cursor()
        cur.execute(query)

        for row in cur.fetchall():
            result.append(row)

    except psycopg2.DatabaseError, e:
        if con:
            con.rollback()
        pass

    finally:
        if con:
            con.close()

    return result


def get_data(rows):
    sum_status = {"idle": 0, "active": 0, "used": 0}
    status_by_user = {}

    for row in rows:
        user = row[1]
        status = row[3]

        if user not in status_by_user:
            status_by_user[user] = {status: 1}
            sum_status[status] += 1

        elif user in status_by_user:
            if status not in status_by_user[user]:
                status_by_user[user][status] = 1
                sum_status[status] = 1
            elif status in status_by_user[user]:
                status_by_user[user][status] += 1
                sum_status[status] += 1

    return status_by_user, sum_status


def zabbix_data_by_user(hostname, data):
    for port in data:
        for user in data[port]:
            for status in data[port][user]:
                value = data[port][user][status]
                print "%s pgbouncer.stats[%s.%s.%s] %s" \
                       % (hostname, port, user, status, value)


def zabbix_data_sum(hostname, data):
    for port in data:
        for status in data[port]:
            value = data[port][status]
            print "%s pgbouncer.stats[%s.%s] %s" \
                   % (hostname, port, status, value)


def main():
    data_by_user = {}
    data_sum = {}

    for port in ports:
        rows = get_query(host, port, "SHOW SERVERS")
        data_by_user[port], data_sum[port] = get_data(rows)

    if "--by-user" in sys.argv:
        zabbix_data_by_user(hostname, data_by_user)
    elif "--sum" in sys.argv:
        zabbix_data_sum(hostname, data_sum)
    else:
        print "Need arguments"
        print "     --by-user"
        print "     --sum"

if __name__ == "__main__":
    main()
