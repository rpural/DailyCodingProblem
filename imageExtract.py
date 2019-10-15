#! /usr/bin/env python3

import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse

def is_absolute(url):
    '''
    Determines if a URL is absolute
    '''
    return bool(urlparse(url).netloc)


def is_valid(url):
    '''
    Determines if a URL is valid
    '''
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def get_all_images(url):
    '''
    Returns all the image URLs on a single URL
    '''
    urls = list()
    soup = bs(requests.get(url).content, "html.parser")
    for img in tqdm(soup.find_all("img"), "Extracting images"):
        img_url = img.attrs.get("src")

        if not img_url:
            # if img does not contain a src attribute, skip it
            continue
        if not is_absolute(img_url):
            # if img has a relative URL, make it absolute
            img_url = urljoin(url, img_url)

        try:
            pos = img_url.index("?")
            img_url = img_url[:pos]
        except ValueError:
            pass

        # finally, if the url is valid, keep it
        if is_valid(img_url):
            urls.append(img_url)

    return urls


def download(url, pathname):
    '''
    Download a file given a URL and put it in the folder 'pathname'
    '''

    # if path doesn't exist, create it
    if not os.path.isdir(pathname):
        os.makedirs(pathname)

    # download the body of response by chunk, not immediately
    response = requests.get(url, stream=True)
    # get the total file size
    file_size = int(response.headers.get("Content-Length", 0))
    # get the filename
    filename = os.path.join(pathname, url.split("/")[-1])

    # progress bar, change the unit to bytes instead of iteration
    progress = tqdm(response.iter_content(1024), f"Downloading {filename}", 
            total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress:
            # write dataa read to the file
            f.write(data)
            # update the progress bar manually
            progress.update(len(data))


def main(url, path):
    # get all the images
    imgs = get_all_images(url)
    for img in imgs:
        # for each image, fetch the file
        download(img, path)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='This script downloads all images from a web page')
    parser.add_argument("url", help="The URL of the web page from which to capture images")
    parser.add_argument("-p", "--path", help="The directory in which to store the images.")

    args = parser.parse_args()
    url = args.url
    path = args.path

    if not path:
        # if the path wasn't specified, use the domain name of the url as the folder name
        path = urlparse(url).netloc

    main(url, path)
