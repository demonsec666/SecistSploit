#!/usr/bin/env python3
#Copyright 2018, The RouterSploit Framework (RSF) by Threat9 All rights reserved.

from __future__ import print_function
import logging.handlers
import sys
if sys.version_info.major < 3:
    print("secistsploit supports only Python3. Rerun application in Python3 environment.")
    exit(0)

from secistsploit.main import secistsploitInterpreter

log_handler = logging.handlers.RotatingFileHandler(filename="secistsploit_attack.log", maxBytes=500000)
log_formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s       %(message)s")
log_handler.setFormatter(log_formatter)
LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)
LOGGER.addHandler(log_handler)


def secistsploit():
    ssf = secistsploitInterpreter()
    ssf.start()


if __name__ == "__main__":
    secistsploit()
