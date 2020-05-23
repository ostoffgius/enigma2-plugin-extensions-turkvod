#Embedded file name: /usr/lib/enigma2/python/Plugins/Extensions/TURKvod/TURKvodPrsr.py
import re, urllib, urllib2, os, cookielib, base64, sys, random
from urlparse import parse_qs
import time

VER = '00.00'
UA = 'Mozilla/5.0'
FF_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'

def mydebug():
    pass


def versiyon(parser_ver = '<h1>(.*?)</h1></td>\\W*</tr>\\W*<tr>\\W*<td align="right"><h3>(.*?)</h3></td>\\W*<td align="left"><h2>(.*?)</h2></td>\\W*</tr>\\W*<tr>\\W*<td align="right"><h3>(.*?)</h3></td>\\W*<td align="left"><h2>(.*?)</h2>'):
    return parser_ver


class turkvod_parsers:

    def __init__(self):
        self.quality = ''
        mydebug()

    def get_parsed_link(self, url):
        if url.startswith('//www.'):
            url = 'http:' + url
        elif url.startswith('www.'):
            url = 'http://' + url
        elif url.startswith('//'):
            url = 'http:' + url
        son_url = ''
        film_quality = []
        video_tulpe = []
        error = None
        try:
            if error:
                return (error, video_tulpe, film_quality)
            if film_quality:
                return (error, video_tulpe, film_quality)
            return son_url
        except Exception as ex:
            print ex
            print 'html_parser ERROR'
			
				
class modules():

    def __init__(self):
        self.video_liste = []
        self.next_page_url = ''
        self.next_page_text = ''
        self.prev_page_url = ''
        self.prev_page_text = ''
        self.search_text = ''
        self.playlistname = ''
        self.error = ''
				
    def reset_buttons(self):
        self.next_page_url = None
        self.next_page_text = ''
        self.prev_page_url = None
        self.prev_page_text = ''
        self.search_text = ''
        self.search_on = None
				
    def get_list(self, url):
        try:
            self.reset_buttons()
        except Exception as ex:
            print ex
            print 'Module ERROR'
