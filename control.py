#!/usr/bin/env python
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

        print("This is a test.")
        pid = os.getpid()
        platform = sys.platform
        if platform == 'win32':
            clear = 'cls'
        else:
            clear = 'clear'
        os.system(clear)
        print("Process running on PID: {}".format(pid))
        print("Currently Running on System: {}".format(platform))
        print("Running pexpect Tests...")
        #pgm.expect('07/07/2017')
        #days = pgm.match.groups()
        #print("Testing days: {}".format(days))
        #for i in pgm.__dict__:
        #    print("{}: {}".format(i, pgm.__dict__[i]))
        print("All tests Successfully completed.")

    except KeyboardInterrupt:
        os.system(clear)
        print("@Ruckusist... Failed Safely.")
        pass

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("and thats okay too. See here:")
        print("Errors:\n{}".format(e))
