import argparse

def _argpaser():
    parser = argparse.ArgumentParser(description="this is description")
    parser.add_argument('--host', action='store', dest='server', default="localhost", help='common to host')
    return parser.parse_args()

def main():
    parser = _argpaser()
    print(parser)
    print('host =', parser.server)

if __name__ == '__main__':
    main()

