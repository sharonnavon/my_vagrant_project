#!/usr/bin/env python3

import os
import sys
import time
import random
import datetime
import multiprocessing

# If the script is already running it will exit with an error message
scpipt_pid = str(os.getpid())
pidfile = '/tmp/myscript.pid'

if os.path.isfile(pidfile):
    print('ERROR: This script is already running...\nExiting!')
    sys.exit()

# Create a PID file
open(pidfile, 'w').write(scpipt_pid)

# Function for wait up to 20 sec, print PID and timestamp
def print_pid_and_time():
    time.sleep(random.randint(1, 20))
    print('Timestamp:', str(datetime.datetime.now()), 'PID:', os.getpid())

try:
    # Check if the first argument is an integer
    N = int(sys.argv[1])

    # Prepare procs list and counts
    procs = []
    successed_procs = 0
    failed_procs = 0

    # Run N processes in parallel
    for i in range(0, N):
        procs.append(multiprocessing.Process(target=print_pid_and_time))
        procs[i].start()

    # Check exit code + count success and fail
    for i in range(0, N):
        # Wait the process to be completeted
        procs[i].join()

        if procs[i].exitcode == 0:
            successed_procs += 1

        else:
            failed_procs += 1

    print(successed_procs, 'processes have completed successfully')
    print(failed_procs, 'processes have failed')

except ValueError:
    print('ERROR: This script accepts only integer as an argument...\nExiting!')
    sys.exit()

finally:
    # Remove the PID file
    os.unlink(pidfile)

