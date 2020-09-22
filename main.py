#! /usr/bin/env python
# coding: utf-8

from flask import Flask
from flask import render_template, request, url_for, redirect
from model.webpayment import WebPaymentModel
from model.qrcode import QrCodeModel
from model.database import DatabaseModel
from model.mapping import MappingModel
from model.form import qrCodeGenerateForm

from datetime import datetime, timezone, timedelta
import pprint
import requests

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():

  form = qrCodeGenerateForm()

  return render_template("index.html", form = form)

@app.route("/qrcode", methods=["POST"])
def qrcode():

  if request.method == "POST": 

    webpayment = WebPaymentModel()
    dbm = DatabaseModel()
    qrcode = QrCodeModel()
  
    code = webpayment.createCode(request.form)

    # pprint.pprint(code)

    # insert GeneratedPaymentData to DB
    dbm.insertData(code)

    # Generate to Qrcode from PaymentData
    qrcode_image_name = qrcode.generateQrcode(code["data"]["url"], code["data"]["codeId"])

    # epoch to JST
    JST = timezone(timedelta(hours=+9), 'JST')
    expiryDate = datetime.fromtimestamp(code["data"]["expiryDate"], JST)
    requestedAt = datetime.fromtimestamp(code["data"]["requestedAt"], JST)

    return render_template("qrcode.html",
      code = code,
      qrcode_image_name = qrcode_image_name,
      expiryDate = expiryDate,
      requestedAt = requestedAt
    )

@app.route("/list")
def list():

  dbm = DatabaseModel()
  mm = MappingModel()

  qr_list_s_src = dbm.selectData()

  # create dict from list
  qr_list_s = mm.createListMapDict(qr_list_s_src)

  # pprint.pprint(qr_list_s)

  return render_template("list.html", qr_list_s = qr_list_s)

if __name__ == "__main__":
    app.run(host="0.0.0.0")