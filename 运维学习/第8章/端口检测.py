from __future__ import print_function
from socket import *

def conn_scan(host, port):
    conn = socket(AF_INET, SOCK_STREAM)
    try:
        conn.connect((host, port))
        print(host, port, 'is available')
    except Exception as e:
        pass
    finally:
        conn.close()

def main():
    host = "210.14.152.1"
    for port in range(20, 300):
        conn_scan(host, port)

if __name__ == '__main__':
    main()