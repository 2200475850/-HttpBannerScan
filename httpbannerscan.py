#coding:utf8
#code by Aedoo

import threading,Queue
from argparse import ArgumentParser
import netaddr
import sys
import re,base64
import requests

header = {
    'Connection': 'close',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language': 'zh-CN,zh;q=0.8',

}

class HttpBannerScan(threading.Thread):

    def __init__(self,queue):
        threading.Thread.__init__(self)
        self._queue = queue

    def run(self):
        while not self._queue.empty():
            ip = self._queue.get(timeout=0.5)
            url = 'http://' + ip
            try:
                r = requests.Session().get(url=url, headers=header, timeout=5)
                content = r.text
                status = r.status_code
                title = re.search(r'<title>(.*)</title>', content)
                if title:
                    title = title.group(1).strip().strip("\r").strip("\n")[:30]
                else:
                    title = "None"

                banner = 'Not Found'
                try:
                    banner = r.headers['Server'][:20]
                except:
                    pass

                sys.stdout.write("|%-16s %-6s %-26s %-30s\n" % (ip, status, banner, title))

            except:
                pass

def main():
    logo_code = 'IF8gICBfIF8gICBfICAgICAgICAgX19fXyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIF9fX18gICAgICAgICAgICAgICAgICAKfCB8IHwgfCB8X3wgfF8gXyBfXyB8IF9fICkgIF9fIF8gXyBfXyAgXyBfXyAgIF9fXyBfIF9fLyBfX198ICBfX18gX18gXyBfIF9fICAKfCB8X3wgfCBfX3wgX198ICdfIFx8ICBfIFwgLyBfYCB8ICdfIFx8ICdfIFwgLyBfIFwgJ19fXF9fXyBcIC8gX18vIF9gIHwgJ18gXCAKfCAgXyAgfCB8X3wgfF98IHxfKSB8IHxfKSB8IChffCB8IHwgfCB8IHwgfCB8ICBfXy8gfCAgIF9fXykgfCAoX3wgKF98IHwgfCB8IHwKfF98IHxffFxfX3xcX198IC5fXy98X19fXy8gXF9fLF98X3wgfF98X3wgfF98XF9fX3xffCAgfF9fX18vIFxfX19cX18sX3xffCB8X3wgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCg=='
    logo = base64.b64decode(logo_code)
    print logo
    parser = ArgumentParser()
    parser.add_argument("-i", dest="cidr_ip", default="192.168.1.1/16", help="The CIDR IP Like 192.168.1.1/24")
    parser.add_argument("-t", dest="thread_count", type=int, default=100, help="The Thread Number")
    args = parser.parse_args()
    parser.print_help()
    print ''
    print 'The Mission Started Successfully::'
    print ''
    threads = []
    queue = Queue.Queue()
    IPduan = str(args.cidr_ip)
    thread_count = int(args.thread_count)
    IPs = netaddr.IPNetwork(IPduan)
    for ip in IPs:
        queue.put(str(ip))

    for i in xrange(thread_count):
        threads.append(HttpBannerScan(queue))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

if __name__ == '__main__':
    main()
    print ''
    print '::The Mission is Over'