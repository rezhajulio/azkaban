#!/usr/bin/python3

import socket
import time
import sys

def wait_for_port_ready(port, retry_count):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', port))

    ready = False
    retries = 0
    while not ready:
        if result == 0:
            print('Port ' + str(port) + ' is open')
            ready = True
        else:
            print('Port ' + str(port) + ' is not open')
            retries += 1
            if retries > retry_count:
                raise Exception('Port ' + str(port) + ' is not open')
            print('waiting for 1 seconds...')
            time.sleep(1)
            result = sock.connect_ex(('127.0.0.1', port))

if __name__ == "__main__":
    port = int(sys.argv[1])
    retry_count = int(sys.argv[2])
    wait_for_port_ready(port, retry_count)