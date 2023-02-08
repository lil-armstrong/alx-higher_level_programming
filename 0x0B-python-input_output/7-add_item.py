#!/usr/bin/python3
import sys
"""Load, add, save"""

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


if __name__ == "__main__":
    filename = "add_item.json"
    list = sys.argv[1:]
    existing_list = []

    try:
        existing_list = load_from_json_file(filename)

    except Exception as err:
        # print("Exception {}", err)
        pass
    finally:
        existing_list += list
        save_to_json_file(existing_list, filename)
