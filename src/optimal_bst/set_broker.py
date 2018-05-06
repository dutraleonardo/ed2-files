#!/usr/bin/env python
# -*- coding: utf-8 -*-


def set_broker():
    s = [(21, 2), (32, 4), (22, 7), (35, 11), (29, 2), (43, 3), (37, 5),
              (99, 8), (10, 19), (45, 12), (2, 1), (27, 1), (19, 14), (51, 21)]
    first_set = [x[0] for x in s]
    second_set = [x[1] for x in s]
    print("Set of indexes: ", first_set)
    print("Set of frequencies: ", second_set)


if __name__ == "__main__":
    set_broker()