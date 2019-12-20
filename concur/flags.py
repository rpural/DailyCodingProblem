#! /usr/bin/env python3

import os
import time
import sys

import requests

pop20_cc = ( 'CN IN US ID BR PK NG BD RU JP '
             'MX PH VN ET EG DE IR TR CD FR').split()

base_url = "http://flupy.org/data/flags"

dest_dir = 'downloads/'

def save_flag(img, filename):
    path = os.path.join(dest_dir, filename)
    with open(path, 'wb') as fp:
        fp.write(img)

def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(base_url, cc=cc.lower())
    resp = requests.get(url)
    return resp.content

def show(text):
    print(text, end=' ')
    sys.stdout.flush()

def download_many(cc_list):
    for cc in sorted(cc_list):
        image = get_flag(cc)
        show(cc)
        save_flag(image, cc.lower() + ".gif")

    return len(cc_list)

def main(download_many):
    t0 = time.time()
    count = download_many(pop20_cc)
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(count, elapsed))


if __name__ == "__main__":
    main(download_many)
