#!/usr/bin/env python3


def first_last(data):
    new_list = data[:]
    new_list[0] = data[-1]
    new_list[-1] = data[0]
    return new_list


def every_other(data):
    new_list = data[::2]
    return new_list


def fourth_fourth(data):
    new_list = data[0:4] + data[-4:]
    return new_list


def reversed(data):
    return data[::-1]


def thirds(data):
    first_third = int(len(data) / 3)
    middle_third = int((len(data) / 3) * 2)
    last_third = data[-1]
    return [data[middle_third], last_third, first_third]


assert first_last(['first', 'second', 'third', 'fourth', 'last']) == [
    'last', 'second', 'third', 'fourth', 'first']
assert every_other(['first', 'second', 'third', 'fourth', 'last']) == [
    'first', 'third', 'last']
assert fourth_fourth(
    [
        'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
        'eighth', 'nineth', 'tenth']) == [
            'first', 'second', 'third', 'fourth',
            'seventh', 'eighth', 'nineth', 'tenth']
assert reversed(['first', 'second', 'third']) == [
    'third', 'second', 'first']
assert thirds((range(1, 22))) == [15, 21, 7]
