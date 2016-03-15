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
    user_list = {}

    for row in rows:
        user = row[1]
        status = row[3]

        if user not in user_list:
            user_list[user] = {status: 1}

        elif user in user_list:
            if status not in user_list[user]:
                user_list[user][status] = 1
            elif status in user_list[user]:
                user_list[user][status] += 1

    return user_list


def zabbix_data(hostname, data):
    for port in data:
        for user in data[port]:
            for status in data[port][user]:
                value = data[port][user][status]
                print "%s pgbouncer.stats[%s.%s.%s] %s" \
                           % (hostname, port, user, status, value)


def main():
    data = {}

    for port in ports:
        rows = get_query(host, port, "SHOW SERVERS")
        data[port] = get_data(rows)

    zabbix_data(hostname, data)


if __name__ == "__main__":
    main()
