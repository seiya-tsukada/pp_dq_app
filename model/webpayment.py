#! /bin/env python
# coding: utf-8

import pprint
import datetime
import paypayopa
import json


class WebPaymentModel(object):

  def __init__(self):
    # Read base information
    json_file = open('./baseinfo.json', 'r')
    base_json = json.load(json_file)
    
    API_KEY = base_json['apiKey']
    API_SECRET = base_json['apiKeySecret']
    MERCHANT_ID = base_json['mid']

    #Set True for Production Environment. By Default this is set False for Sandbox Environment.
    client = paypayopa.Client(auth=(API_KEY, API_SECRET), production_mode=False)
    client.set_assume_merchant(MERCHANT_ID)

    self.client = client
    self.redirectUrl = base_json['redirectUrl']
    self.merchantPaymentIdPrefix = base_json['merchantPaymentIdPrefix']

  def createCode(self, data):
  
    pprint.pprint("in model")
    pprint.pprint(data)
    exit

    now = datetime.datetime.now()
    current_time =  now.strftime('%Y%m%d%H%M%S')
    print(current_time)
  
    request = {
      "merchantPaymentId": "{0}-qr-{1}".format(self.merchantPaymentIdPrefix, current_time),
      "codeType": "ORDER_QR",
      "redirectUrl": self.redirectUrl,
      "redirectType": "WEB_LINK",
      "orderDescription": data["orderDescription"],
      "terminalId": data["terminalId"],
      "storeInfo": data["storeInfo"],
      "storeId": data["storeId"],
      "orderItems": [
          {
              "name": data["itemName"],
              "quantity": 1,
              "unitPrice": {
                  "amount": int(data["amount"]),
                  "currency": "JPY"
              }
          }
      ],
      "amount": {
        "amount": int(data["amount"]),
        "currency": "JPY"
      }
    }
  
    # Calling the method to create a qr code
    response = self.client.Code.create_qr_code(request)

    return response