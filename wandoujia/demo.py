#!/usr/bin/env python

import sys
import urllib
import mechanize
from mechanize._form import HTMLForm


SITE_NAME = 'wandoujia'


cookie = mechanize.CookieJar()

def crteate_seesion():
    request = mechanize.Request( 'http://open.wandoujia.com/app/add')
    response = mechanize.urlopen(request)
    cookie.extract_cookies(response, request)
    print '\n\n %s -------------------' % 'crteate_seesion'
    print response.read()
    response.close()

def auth():
    """
    auth wandoujia
    """

    raw_data = {
        'username': '616508150@qq.com',
        'password': 'b4496451'
    }
    data = urllib.urlencode(raw_data)
    request = mechanize.Request( 'https://account.wandoujia.com/v4/api/login', data)
    cookie.add_cookie_header(request)
    response = mechanize.urlopen(request)
    print '\n\n %s -------------------' % 'auth'
    print response.read()
    response.close()

def first_setp():
    form_template = """
         <form action=""
         method="POST" enctype="multipart/form-data">

         <input name="file" type="file"></input>
        </form>
                    """
    form = HTMLForm('http://open.wandoujia.com/api/upload/apk', 'POST', 'multipart/form-data')
    #form = mechanize.ParseString(form_template, 'http://open.wandoujia.com/api/upload/apk')[0]
    form.new_control('file', 'file', {})
    print form
    form.add_file(open('e:\\demo.apk'), name='file', filename='demo.apk')
    request = form.click()
    cookie.add_cookie_header(request)
    response = mechanize.urlopen(request)
    print '\n\n %s -------------------' % 'first_setp'
    print response.read()
    response.close()

if __name__ == '__main__':
    crteate_seesion()
    auth()
    first_setp()