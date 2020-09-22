#! /bin/env python
# coding: utf-8

import pprint
import qrcode

class QrCodeModel(object):

  def __init__(self):

    app_dir = "/pp"
    self.store_dir = "{0}/static/qrcodes".format(app_dir)

  def generateQrcode(self, url, codeId):

    file_name = "{0}.png".format(codeId)
    img_path = "{0}/{1}".format(self.store_dir, file_name)

    img = qrcode.make(url)
    img.save(img_path)

    return file_name