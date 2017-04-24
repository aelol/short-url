import os

import falcon
from handler import TransRawHanlder, allHandler, IndexPhp
from middleware import RequireJson, JSONTranslator, ResponseLogger

requireJson = RequireJson()
jsonTanslator = JSONTranslator()
logHandler = ResponseLogger()

api = falcon.API(middleware=[
    requireJson,
    jsonTanslator,
    logHandler,
])

rawhandle = TransRawHanlder()
allh = allHandler()
php = IndexPhp()

api.add_route('/raw', rawhandle)
api.add_route('/{shorturl}', allh)
api.add_route('/index.php', php)
api.add_route('/', php)
api.add_route('/echo.php', php)
