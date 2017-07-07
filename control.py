#!/usr/bin/env python3
"""Python Power of Zenbot js.

Give python control over the execution of zenbot,
for variable control and management.
"""

import os
import sys
import pexpect as pex

def main():
    # TODO: this is still missing a command line arg parser!
    try:
        pid = os.getpid()
        os.system('clear')
        print("Process running on PID: {}".format(pid))
        print("Running pexpect Tests...")
        flags = ''
        pgm = pex.spawnu('zenbot {}'.format(flags))
        for line in pgm:
            if not line == '':
                print(line)

        print("All tests Successfully completed.")

    except KeyboardInterrupt:
        os.system('clear')
        print("@Ruckusist... Failed Safely.")
        pass

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("and thats okay too. See here:")
        print("Errors:\n{}".format(e))
