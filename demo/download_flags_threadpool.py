from concurrent import futures

from demo.download_flags_requests import download_flag_cc, main


def download_flags(country_codes):
    with futures.ThreadPoolExecutor(len(country_codes)) as executor:
        res = executor.map(download_flag_cc, country_codes)

    return len(list(res))

if __name__ == '__main__':
    main(download_flags)
