#!/usr/bin/env python

import telnetlib
import json
import os

hostname = os.uname()[1]
host = "localhost"
services = {"service1": 5050,
            "service2": 5051,
            "service3": 5052,
            "service4": 5053}


def get_json(host, port):
    tn = telnetlib.Telnet(host, port=port)
    json = tn.read_all()
    tn.close()
    return json


def main():
    for port in services.keys():
        try:
            data = json.loads(get_json(host, services[port]))
        except:
            continue
        statuses = {}
        for worker in data["workers"]:
            if worker["status"] in statuses:
                statuses[worker["status"]] += 1
            else:
                statuses[worker["status"]] = 1
        for status in statuses:
            value = str(statuses[status])
            print "%s uwsgi.stats[%s.workers.status.%s] %s" \
                   % (hostname, port, status, value)


if __name__ == "__main__":
    main()
