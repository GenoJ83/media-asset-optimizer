from concurrent.futures import ProcessPoolExecutor
def optimize_in_parallel(paths, fn, workers=4):
    with ProcessPoolExecutor(max_workers=workers) as ex:
        return list(ex.map(fn, paths))
