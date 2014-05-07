import argparse
import urllib2
import httplib
import re
import sys

def translate(word, src, tgt):

    host = src + '.wiktionary.org'
    path = '/wiki/' + urllib2.quote(word)
    table_regex = re.compile('<table class="translations".*?>(.*?)</table>')
    regex = re.compile('lang="' + tgt + '">.*?title="(.*?)"')

    translations = set()

    connection = httplib.HTTPConnection(host, 80)
    connection.request('HEAD', path)
    response = connection.getresponse()
    if response.status == 200:

        url = 'http://' + host + path

        request = urllib2.Request(url)
        request.add_header('User-Agent', 'Mozilla/5.0')
    
        response = urllib2.urlopen(request)
        html = response.read()
        html = re.sub('\r|\n', '', html)

        for table_match in table_regex.finditer(html):
            table = table_match.group(1)
            # take out any gender links
            table = re.sub('<span class="gender">.*?</span>', '', table)
            for match in regex.finditer(table):
                translation = match.group(1)
                translation = re.sub(" \(.*?\)", "", translation)
                translations.add(translation)

    return translations

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('word', help='Word to translate')
    parser.add_argument('src', help='Source language')
    parser.add_argument('tgt', help='Target language')
    args = parser.parse_args()
    translations = translate(args.word, args.src, args.tgt)
    for t in translations:
        print t
