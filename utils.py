# coding=utf-8
from datetime import date, datetime
import hashlib
import hmac
import json
import re


# key = '1800cc75b39a99c0258b573f83a92e65'

'''________________________________________short'''


def get_md5(s):
    s = s.encode('utf8') if isinstance(s, str) else s
    m = hashlib.md5()
    m.update(s)
    return m.hexdigest()


code_map = (
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
    'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
    'y', 'z', '0', '1', '2', '3', '4', '5',
    '6', '7', '8', '9', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
)


def get_hash_key(long_url):
    # hkeys = []
    hex = get_md5(long_url)
    for i in range(0, 4):
        n = int(hex[i * 8:(i + 1) * 8], 16)
        v = []
        e = 0
        for j in range(0, 5):
            x = 0x0000003D & n
            e |= ((0x00000002 & n) >> 1) << j
            v.insert(0, code_map[x])
            n = n >> 6
        e |= n << 5
        v.insert(0, code_map[e & 0x0000003D])
        hkeys = ''.join(v)
    return hkeys


'''___________________________________________short'''


def splitUrl(url):
    splited = re.findall(r'(?<=\bcom/).*', url)

    ss = ''.join(splited)
    return ss


def getSignature(req):
    msg = req.url
    signature = hmac.new(b'1800cc75b39a99c0258b573f83a92e65')
    signature.update(msg.encode())
    sigg = signature.hexdigest()
    return sigg


class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)
