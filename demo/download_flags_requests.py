import os
import sys
import time
import urllib.request


COUNTRY_CODES = {'CN', 'IN', 'US', 'ID', 'BR', 'PK', 'NG', 'BD', 'RU', 'JP',
                 'MX', 'PH', 'VN', 'ET', 'EG', 'DE', 'IR', 'TR', 'CD', 'FR'}

BASE_URL = 'http://flupy.org/data/flags/'

DOWNLOAD_DIR = 'downloads/'


def print_progress(cc):
    print(cc, end=' ')  # 使用空格作为间隔
    sys.stdout.flush()  # python中只有换行才立即输出到控制台


def download_flag(url, filename):
    response = urllib.request.urlopen(url)
    img = response.read()
    path = os.path.join(DOWNLOAD_DIR, filename)
    with open(path, 'wb') as f:
        f.write(img)


def download_flags(country_codes):
    for cc in country_codes:
        cc = cc.lower()
        url = '{}{cc}/{cc}.gif'.format(BASE_URL, cc=cc)
        filename = '{}.gif'.format(cc)
        print_progress(cc)
        download_flag(url, filename)


def main(download_flags):
    if not os.path.exists(DOWNLOAD_DIR):
        os.mkdir(DOWNLOAD_DIR)

    begin_time = time.time()
    download_flags(COUNTRY_CODES)
    end_time = time.time()

    print('{} flags downloaded in {:.2f}s'.format(len(COUNTRY_CODES), end_time-begin_time))

if __name__ == '__main__':
    main(download_flags)