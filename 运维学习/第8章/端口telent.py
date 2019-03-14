#!/usr/bin/python
from __future__ import print_function
import telnetlib

def conn_scan(host, port):
    t = telnetlib.Telnet()
    try:
        t.open(host, port, timeout=1)
        print(host, port, 'is avaliable')
    except Exception as e:
        pass
    finally:
        t.close()

def main():
    host = '210.14.152.1'
    for port in range(80, 5000):
        conn_scan(host, port)

if __name__ == '__main__':
    main()