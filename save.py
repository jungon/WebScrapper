# -*- coding:utf-8 -*-

import csv


def save_to_file(jobs):
    file = open('jobs.csv', mode='w', encoding='utf-8', newline='')
    writer = csv.writer(file)
    writer.writerow(["type", "value"])
    for job in jobs:
        writer.writerow(list(job.values()))
