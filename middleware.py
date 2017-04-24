import json
import logging
import traceback
import datetime
import falcon
import pdb

logger = logging.getLogger(__name__)
logger.addHandler(logging.FileHandler('nlog.log'))
logger.setLevel(logging.INFO)


class ResponseLogger(object):
    def process_response(self, req, resp, resouce):
        tfe = traceback.format_exc()
        logger.info('{0} {1} {2} {3} {4} {5}'.format(datetime.datetime.now(), req.method, req.relative_uri, resp.status[:3], tfe, '\n_________________________'))
        # logger.info("1")


class RequireJson(object):
    def process_request(self, req, resp):
        if not req.client_accepts_json:
            raise falcon.HTTPNotAcceptable('This API only supports responses encoded as JSON.')
        if req.method in ('POST', 'PUT'):
            if 'application/json' not in req.content_type:
                raise falcon.HTTPUnsupportedMediaType('This API only supports requests encoded as JSON.')


class JSONTranslator(object):
    def process_request(self, req, resp):
        if req.content_length in (None, 0):
            return
        body = req.stream.read()
        if not body:
            raise falcon.HTTPBadRequest('Empty request body',
                                        'A valid JSON document is required.')
        try:
            req.context['doc'] = json.loads(body.decode('utf-8'))

        except(ValueError, UnicodeDecodeError):
            raise falcon.HTTPError(falcon.HTTP_753, 'Malformed JSON',
                                   'Could not decode the request body. The '
                                   'JSON was incorrect or not encoded as '
                                   'UTF-8.')

class ignor404(object):
    def process_response(self, req, resp, resource):
        if falcon.HTTP_404():
            return 'yep i totally found the page:'+req.url

