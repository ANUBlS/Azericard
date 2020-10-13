from django.db import transaction
import requests
import json
import binascii
from datetime import datetime
import time
import hashlib
import random
from random import randrange
from hashlib import sha1
import hmac
from binascii import hexlify
import codecs
from .utils import gmdate,substr


class AzeriCardClass(type):
    def __new__(cls, clsname, bases, attrs, **kwargs):
        newclass= super().__new__(cls, clsname, bases, attrs, **kwargs)

        if newclass.order is not None:
            newclass.register()


        return newclass


class AzeriCard(object, metaclass=AzeriCardClass):
    terminal = None
    merch_name = None
    merch_url = None
    key = None
    order = None
    email = None
    desc = None
    amount = None
    rrn = None # Bank reference number 
    int_ref = None # Internal reference number     


    @classmethod
    def register(cls):
        cls.get_data(cls)
        
  

    @classmethod
    def hex2bin(cls,hexdata):
        bindata = ''
        i = 0
        while i < len(hexdata):
            i += 2
            try:
                string = substr(hexdata,i,2)
                hexdec = int(bin(int(string,16)),2)
                bindata += chr(hexdec)
            except ValueError:
                pass
        return bindata


    @classmethod
    def get_data(cls, *args, **kwargs):
        irand = random.randint(1, 10000000)
        nonce= substr(hashlib.md5(str(irand).encode('utf-8')).hexdigest(),0,16)
        
        AMOUNT = cls.amount
        CURRENCY = 'AZN'
        ORDER = cls.order
        DESC = cls.desc
        RRN = cls.rrn
        MERCH_NAME = cls.merch_name
        MERCH_URL = cls.merch_url
        TERMINAL = cls.terminal
        EMAIL = cls.email
        TRTYPE = '21'
        COUNTRY = 'AZ'
        MERCH_GMT = '+4'
        NONCE = nonce
        INT_REF = cls.int_ref
        BACKREF = cls.merch_url
        key_for_sign=cls.key
        oper_time = gmdate("%Y%m%d%H%i%s")
        TIMESTAMP = oper_time
        to_sign = ORDER + AMOUNT + CURRENCY + RRN + INT_REF + TRTYPE + TERMINAL + str(oper_time) + str(nonce)
        res = cls.hex2bin(key_for_sign)
        p_sign = hmac.new(to_sign.encode(), res.encode(), hashlib.sha1).hexdigest()
        post_data = {}
        post_data["P_SIGN"] = p_sign
        get = cls.send_data(cls,
        AMOUNT = cls.amount,
        CURRENCY = 'AZN',
        ORDER = cls.order,
        DESC = cls.desc,
        RRN = cls.rrn,
        MERCH_NAME = cls.merch_name,
        MERCH_URL = cls.merch_url,
        TERMINAL = cls.terminal,
        EMAIL = cls.email,
        TRTYPE = '21',
        COUNTRY = 'AZ',
        MERCH_GMT = '+4',
        NONCE = nonce,
        INT_REF = cls.int_ref,
        BACKREF = cls.merch_url,
        key_for_sign=cls.key,
        oper_time = gmdate("%Y%m%d%H%i%s"),
        TIMESTAMP = oper_time,
        P_SIGN=p_sign,
        )
        return get

    def send_data(self,*args, **kwargs):
        url = 'https://testmpi.3dsecure.az/cgi-bin/cgi_link'
        r = requests.post(url, data=kwargs)
        return r.content
        

 

