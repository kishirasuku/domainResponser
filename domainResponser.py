import requests
from argparse import ArgumentParser

def get_option():
    argparser = ArgumentParser()

    argparser.add_argument('-f','--file',type=str,help='file of urls to investigate',required=True)

    return argparser.parse_args()

def getResponseCode(url):
    r = requests.get(url)

    return str(r.status_code)


if __name__ == '__main__':
    args = get_option()

    with open(args.file) as f:
        lines = f.read()
        for url in lines.split("\n"):
            print(url + " : " +getResponseCode("https://"+url))
