import json
import logging
import pdb

import falcon
import utils
import datetime
import dbutils


class TransRawHanlder(object):
    def on_post(self, req, resp):

        # body = req.stream.read()
        # pdb.set_trace()

        # req.context = json.loads(body.decode('utf-8'))
        doc = req.context['doc']
        sigg = doc['sigg']

        if sigg != utils.getSignature(req):
            raise falcon.HTTPError(falcon.HTTP_753, 'BAD SIGNATURE', 'SIG INVALID')

        try:
            rawUrl = doc['raw']
            last_update = datetime.datetime.now()
            short = utils.get_hash_key(rawUrl)

            short_path = 's.edyd.cn/' + short

            if not dbutils.find_update_short(short=short_path, raw=rawUrl, update_time=last_update):
                dbutils.save_short(short=short_path, raw=rawUrl, update_time=last_update)
        except Exception as e:
            raise falcon.HTTPError(falcon.HTTP_400, repr(e))

        returndata = {'raw': rawUrl, 'short': short_path, 'last_update': last_update}
        resp.body = json.dumps(returndata, cls=utils.DatetimeEncoder)


class allHandler(object):
    def on_get(self, req, resp, shorturl):
        short = 's.edyd.cn/' + shorturl
        if shorturl:
            data = dbutils.redirect(short)
            raw = str(data['raw'])
            resp.status = falcon.HTTP_301
            raise falcon.HTTPMovedPermanently(raw)


class IndexPhp(object):
    def on_get(self, req, resp):
        raise falcon.HTTPError(falcon.HTTP_400, 'fuck off')

