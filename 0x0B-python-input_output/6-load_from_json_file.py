#!/usr/bin/python3
'''Moddule for load_to_json_file method.'''
import json


def load_from_json_file(filename):
    '''Method for loading from json file.'''
    with open(filename, "r", encoding="utf-8") as fl:
        return json.load(fl)
