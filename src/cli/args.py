import argparse
def get_parser():
    p = argparse.ArgumentParser(prog='media-opt')
    p.add_argument('input_dir')
    p.add_argument('--quality', type=int, default=80)
    p.add_argument('--webp', action='store_true')
    return p
