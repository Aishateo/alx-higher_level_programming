#!/usr/bin/python3
'''
reads stdin line by line and computes metrics
'''
import sys

file_size = 0
status_tally = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
x = 0
try:
    for _line in sys.stdin:
        tokens = _line.split()
        if len(tokens) >= 2:
            a = x
            if tokens[-2] in status_tally:
                status_tally[tokens[-2]] += 1
                x += 1
            try:
                file_size += int(tokens[-1])
                if a == x:
                    x += 1
            except FileNotFoundError:
                if a == x:
                    continue
        if x % 10 == 0:
            print("File size: {:d}".format(file_size))
            for key, value in sorted(status_tally.items()):
                if value:
                    print("{:s}: {:d}".format(key, value))
    print("File size: {:d}".format(file_size))
    for key, value in sorted(status_tally.items()):
        if value:
            print("{:s}: {:d}".format(key, value))

except KeyboardInterrupt:
    print("File size: {:d}".format(file_size))
    for key, value in sorted(status_tally.items()):
        if value:
            print("{:s}: {:d}".format(key, value))
