#! /bin/env python
# coding: utf-8

from flask_wtf import FlaskForm
from wtforms import Form, StringField, TextAreaField, validators, SubmitField

class qrCodeGenerateForm(Form):

  itemName = StringField("itemName", render_kw={"placeholder": u"商品名を入力してください"})
  amount = StringField("amount", render_kw={"placeholder": u"金額を入力してください"})
  terminalId = StringField("terminalId", render_kw={"placeholder": u"terminalIdを入力してください"})
  storeInfo = StringField("storeInfo", render_kw={"placeholder": u"store情報を入力してください"})
  storeId = StringField("storeId", render_kw={"placeholder": u"storeIdを数字で入力してください"})
  orderDescription = StringField("orderDescription", render_kw={"placeholder": u"商品詳細を入力してください"})

  submit = SubmitField("submit")