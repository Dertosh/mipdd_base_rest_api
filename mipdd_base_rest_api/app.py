#!/usr/bin/env
#!/usr/bin/pytho
# -*- coding: utf-8 -*-

from eve import Eve
from eve.auth import HMACAuth
from flask import current_app
from hashlib import sha1
import hmac

from werkzeug.contrib.fixers import ProxyFix

app = Eve()

with app.app_context():
    # within this block, current_app points to app.
    print(current_app.name)

app.wsgi_app = ProxyFix(app.wsgi_app)


class HMACAuth(HMACAuth):
    def check_auth(self, userid, hmac_hash, headers, data, allowed_roles,resource, method):
        # use Eve's own db driver; no additional connections/resources are
        # used
        accounts = app.data.driver.db['accounts']
        user = accounts.find_one({'userid': userid})
        if user:
            secret_key = user['secret_key']
        # in this implementation we only hash request data, ignoring the
        # headers.
        return user and \
            hmac.new(str(secret_key), str(data), sha1).hexdigest() == hmac_hash

if __name__ == '__main__':
    #app = Eve(auth=HMACAuth)
    app.run()