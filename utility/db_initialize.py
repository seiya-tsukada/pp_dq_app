#! /bin/env python
# coding: utf-8

import sys
import pprint
sys.path.append("/pp/model")
pprint.pprint(sys.path)

from database import DatabaseModel

if __name__ == "__main__":

  dbm = DatabaseModel()  
  dbm.createDb()