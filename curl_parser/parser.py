'''\

curl command parser:
  - parsing curl command 

'''

from pprint import pprint
from argparse import ArgumentParser
from urllib.parse import parse_qsl
from http import cookies
import shlex

def parse(cmd):

    # split
    cmd = shlex.split(cmd)[1:]


    # make argument parser to parse
    parser = ArgumentParser()

    parser.add_argument("-H", dest="headers", action="append")
    parser.add_argument('url')
    parser.add_argument('--data', dest="data")
    parser.add_argument('--compressed', action='store_true')

    try:
        args = parser.parse_args(cmd)
        ret = vars(args)
    except Exception as e:
        pprint(e)
        return None

    # fix(??)
    if args.data and args.data[0] == '$':
        args.data = args.data[1:]

    if args.data:
        ret['data'] = parse_qsl(args.data)

    headers = {}
    for i in args.headers:
        k, v = tuple(map(str.strip, i.split(':', 1)))
        if k in headers: 
            headers[k] = list(headers[k])
            headers[k].append(v)
        else:
            headers[k] = v

    # cookie
    if "Cookie" in headers:
        C = cookies.SimpleCookie()
        C.load(headers['Cookie'])
        c = dict(( (k,C[k].value) for k in C ))
        headers['Cookie'] = None
        ret["cookies"] = c
    ret["headers"] = headers

    return ret

