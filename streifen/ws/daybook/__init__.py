import os
import time
import json

_base_dir = "/var/daybook/data/"

def remove_lock(lock):
    os.remove(lock)

def get_lock(userId = -1):
    count = 0

    if userId > 0:
        filename = get_directory() + "item.lock"
    else:
        filename = get_directory() + "user.lock"

    while count < 5:
        try:
            file = os.open(filename, os.O_CREAT | os.O_EXCL)
            os.close(file)
            break
        except FileExistsError:
            count += 1
            time.sleep(.1)

    return filename

def get_directory(user_id = -1, ensure_present = False):
    if user_id > 0:
        path = _base_dir + "user-" + str(user_id) + "/"
    else:
        path = _base_dir

    if ensure_present:
        try:
            os.makedirs(path)
        except FileExistsError:
            pass # common occurance 

    return path

def get_next_user_id():
    file_lock = get_lock()
    path = get_directory() + "/user.id"

    try: 
        file = open(path, "r")
        raw = json.load(file)
        file.close()
        id = raw['next_id']
        raw = { 'next_id': id + 1 }
    except FileNotFoundError:
        raw = { 'next_id': 2 }
        id = 1

    file = open(path, "w")
    json.dump(raw, file)
    file.close()
    remove_lock(file_lock)

    return id

def get_next_item_id(userId):
    file_lock = get_lock(userId)
    path = get_directory() + "item.id"

    try: 
        file = open(path, "r")
        raw = json.load(file)
        file.close()
        id = raw['next_id']
        raw = { 'next_id': id + 1 }
    except FileNotFoundError:
        raw = { 'next_id': 2 }
        id = 1

    file = open(path, "w")
    json.dump(raw, file)
    file.close()
    remove_lock(file_lock)
    return id
