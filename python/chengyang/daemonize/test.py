from pykit import daemonize
import time


def run():
    for i in range(100):
        print i
        time.sleep(1)


if __name__ == '__main__':
    daemonize.daemonize_cli(run, '/home/cheng/d.py')
