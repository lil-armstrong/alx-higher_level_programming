#!/usr/bin/python3
import json
"""Create object from JSON file"""


def load_from_json_file(filename):
    """Create an object from a JSON file"""
    with open(filename, "r") as f:
        return (json.load(f))
