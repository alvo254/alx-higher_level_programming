#!/usr/bin/python3
for number in range(0, 100):
    if number == 99:
        print(f"{number}")
    else:
        print("{:0>2}".format(number), end=", ")
