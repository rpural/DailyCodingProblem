#! /usr/bin/env python3

from concurrent import futures

from flags import save_flag, get_flag, show, main

max_workers = 20

def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc

def download_many(cc_list):
    with futures.ThreadPoolExecutor(max_workers=min(max_workers, len(cc_list))) as executor:
        to_do = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            to_do.append(future)
            print("Scheduled for {} : {}".format(cc, future))

        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            print("{} result: {!r}".format(future, res))
            results.append(res)

        return len(results)

if __name__ == "__main__":
    main(download_many)
