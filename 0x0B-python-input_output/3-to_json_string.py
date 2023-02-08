#!/usr/bin/python3

"""To JSON string"""

import json


def to_json_string(my_obj):
    """Return the json representation of an object (string)

    Args:
    my_obj: Python Object

    Returns:
        json string representation of my_obj
    """
    return (json.dumps(my_obj))
