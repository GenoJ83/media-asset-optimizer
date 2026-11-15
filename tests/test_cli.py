from src.cli.args import get_parser
def test_cli():
    p = get_parser()
    args = p.parse_args(['./assets', '--quality', '85'])
    assert args.quality == 85
