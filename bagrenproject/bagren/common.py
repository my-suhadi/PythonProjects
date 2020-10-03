import hashlib
import time


def generate_uuid():
    time_string = str(time.time())
    sh = hashlib.sha1(time_string.encode())
    return str(sh.hexdigest())
