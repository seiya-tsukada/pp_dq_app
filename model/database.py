#! /bin/env python
# coding: utf-8

import sqlite3
import pprint
import json

class DatabaseModel(object):

  def __init__(self):
    self.dbpath = "qrcode.sqlite"

  def createDb(self):

    conn = sqlite3.connect(self.dbpath)

    c = conn.cursor()
    sql = 'create table qr_list(id integer, codeId text, expiryDate text, merchantPaymentId text, amount text, terminalId text, storeInfo text, storeId text, orderItems text, orderDescription text, requestedAt text, paymentStatus text)'
    c.execute(sql)

    conn.commit()
    conn.close()

    return 

  def selectData(self):
  
    conn = sqlite3.connect(self.dbpath)

    c = conn.cursor()
    sql = 'select * from qr_list order by id desc'
    c.execute(sql)
    ret = c.fetchall()
    pprint.pprint(len(ret))
    pprint.pprint(ret)

    return ret

  def insertData(self, code):
  
    print("model")
    pprint.pprint(code)

    conn = sqlite3.connect(self.dbpath)
    c = conn.cursor()

    sql = 'select * from qr_list'
    c.execute(sql)
    ret = c.fetchall()
    pprint.pprint(len(ret))
    pprint.pprint(ret)

    qrcode_info = (len(ret) + 1, code["data"]["codeId"], code["data"]["expiryDate"], code["data"]["merchantPaymentId"], code["data"]["amount"]["amount"], code["data"]["terminalId"], code["data"]["storeInfo"], code["data"]["storeId"], json.dumps(code["data"]["orderItems"][0], ensure_ascii=False), code["data"]["orderDescription"], code["data"]["requestedAt"], "CREATED")

    sql = 'insert into qr_list (id, codeId, expiryDate, merchantPaymentId, amount, terminalId, storeInfo, storeId, orderItems, orderDescription, requestedAt, paymentStatus) values (?,?,?,?,?,?,?,?,?,?,?,?)'
    pprint.pprint(sql)
    pprint.pprint(qrcode_info)
    c.execute(sql, qrcode_info)
    
    conn.commit()
    conn.close()

    return 