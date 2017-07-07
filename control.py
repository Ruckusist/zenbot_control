#!/usr/bin/env python3
"""Python Power of Zenbot js.

Give python control over the execution of zenbot,
for variable control and management.
"""

import os
import time
import getpass
import pexpect as pex

def main():
    try:
        pid = os.getpid()
        username = getpass.getuser()
        os.system('clear')
        print("Process running on PID: {}".format(pid))
        program_path = 'zenbot sim '
        flags = '--period=2d'
        conf = "--conf=/home/{}/zenbot_control/conf.js ".format(username)
        full_spawn = program_path + conf + flags
        print("Running this command: {}".format(full_spawn))
        time.sleep(.5)
        pgm = pex.spawnu(full_spawn)
        catch = '{'
        caught = False
        buffed = []
        for line in pgm:
            if caught:
                print(line)
                if not line == '':
                    buffed.append(line)
            else:
                if catch in line:
                    print("caught: {}".format(line))
                    caught = True

        for i in buffed:
            print(i)
        
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
