#!/usr/bin/env python

#
#
#

import os, inspect, sys
import argparse

if __name__ == "__main__":

    # Get the path of the current directory
    path = os.path.dirname(
        os.path.abspath(inspect.getfile(inspect.currentframe())))

    # Get the arguments from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("statusfile",   help="The status output file to be processed."  )
    args = parser.parse_args()

    print("* File being processed: '%s'" % (args.statusfile))

    f = open(args.statusfile, "r")

    ls = f.readlines()

    print("*--> Contains %d lines..." % (len(ls)))

    n_jobs    = 0
    n_success = 0
    n_aborted = 0
    n_waiting = 0
    n_ready   = 0

    for l in ls:
        if "Current Status:" in l:
            n_jobs += 1
            if "Done(Success)" in l: n_success += 1
            if "Aborted"       in l: n_aborted += 1
            if "Waiting"       in l: n_waiting += 1
            if "Ready"         in l: n_ready   += 1

    print("*--> % 5d jobs were submitted......" % (n_jobs))
    print("*----> Of which % 5d succeeded....." % (n_success))
    print("*----> Of which % 5d aborted......." % (n_aborted))
    print("*----> Of which % 5d are waiting..." % (n_waiting))
    print("*----> Of which % 5d are ready....." % (n_ready  ))
    print("*====>    TOTAL:% 5d <=============" % \
        (n_success + n_aborted + n_waiting + n_ready))
