from typing import *
from datetime import datetime
from itertools import tee


def get_avg_cost_per_person_short_rides(filename: str) -> float:
    start_date_idx = 1
    end_date_idx = 2
    passengers_no_idx = 3
    total_amount_idx = -2
    date_format = "%Y-%m-%d %H:%M:%S"
    with open(filename) as f:
        f.readline()
        trips_1 = (line.split(',') for line in f)
        trips_2 = (line for line in trips_1 if line[passengers_no_idx] not in ('0', ''))
        trips_3 = (line
                   for line in trips_2
                   if ((datetime.strptime(line[end_date_idx], date_format) -
                        datetime.strptime(line[start_date_idx], date_format)).total_seconds() / 60) <= 15
                   )

        trips_4 = map(lambda line: float(line[total_amount_idx]) / int(line[passengers_no_idx]), trips_3)
        trips_5, trips_6 = tee(trips_4)
        sum_x = sum(trips_5)
        leng = sum(1 for _ in trips_6)
        return sum_x / leng


if __name__ == '__main__':
    a = get_avg_cost_per_person_short_rides('yellow_tripdata_2021-01.csv')
    print(a)
