#! /bin/env python
# coding: utf-8

import sqlite3
import pprint
import json
from datetime import datetime, timezone, timedelta

class MappingModel(object):

  def __init__(self):
    None

  def createListMapDict(self, data):
  
    # pprint.pprint(data)
    ret_s = list()
    dict_data = dict()
    JST = timezone(timedelta(hours=+9), 'JST')
    for  i in data:
      # initialize
      dict_data = dict()
      dict_data["id"] = i[0]
      dict_data["codeId"] = i[1]
      dict_data["expiryDate"] = i[2]
      dict_data["expiryJstDate"] = datetime.fromtimestamp(int(i[2]), JST)
      dict_data["merchantPaymentId"] = i[3]
      dict_data["amount"] = i[4]
      dict_data["terminalId"] = i[5]
      dict_data["storeInfo"] = i[6]
      dict_data["storeId"] = i[7]
      dict_data["orderItems"] = i[8]
      dict_data["orderDescription"] = i[9]
      dict_data["requestedAt"] = i[10]
      dict_data["requestedAtJst"] = datetime.fromtimestamp(int(i[10]), JST)
      dict_data["paymentStatus"] = i[11]

      ret_s.append(dict_data)

    return ret_s

