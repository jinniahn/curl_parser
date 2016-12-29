import sys
sys.path.insert(0, "..")
from curl_parser import parse
import unittest
from pprint import pprint

class TestParser(unittest.TestCase):

    def test_parsing(self):
        cmd="""\
        curl 'http://www.naver.com/' -H 'Pragma: no-cache' -H 'Accept-Encoding: gzip, deflate, sdch' -H 'Accept-Language: en-US,en;q=0.8,ko;q=0.6' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Cache-Control: no-cache' -H 'Cookie: npic=0' -H 'Connection: keep-alive' --compressed
        """
        cmd = parse(cmd)
        print(cmd)

        self.assertIn('Pragma', cmd['headers'])
        self.assertEqual('no-cache', cmd['headers']['Pragma'])
        

if __name__ == '__main__':
    unittest.main()
