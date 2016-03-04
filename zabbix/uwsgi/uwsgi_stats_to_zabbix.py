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


def workers_status(data, port):
    statuses = {"name": "workers.status"}
    for worker in data["workers"]:
        if worker["status"] in statuses:
            statuses[worker["status"]] += 1
        else:
            statuses[worker["status"]] = 1
    return statuses


def workers_cores_in_request(data, port):
    in_requests = {"name": "worker_cores.status",
                   "idle_cores": 0,
                   "busy_cores": 0}
    for worker in data["workers"]:
        for core in worker["cores"]:
            if core["in_request"] == 0:
                in_requests["idle_cores"] += 1
            elif core["in_request"] == 1:
                in_requests["busy_cores"] += 1
    return in_requests


def zabbix_data(hostname, port, metric):
    metric_name = metric.pop("name")
    for key, value in metric.iteritems():
        print "%s uwsgi.stats[%s.%s.%s] %s" \
               % (hostname, port, metric_name, key, value)


def main():
    for port in services.keys():
        try:
            data = json.loads(get_json(host, services[port]))
        except:
            continue

        zabbix_data(hostname, port, workers_status(data, port))
        zabbix_data(hostname, port, workers_cores_in_request(data, port))


if __name__ == "__main__":
    main()
