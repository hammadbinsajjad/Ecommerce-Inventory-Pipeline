from argparse import ArgumentParser

from ingestion.utils.loader_map import loader_map
from ingestion.utils.missing_loader import missing_loader
from ingestion.utils.normalize_env_vars import normalize_environment_variables


def main():
    argument_parser = init_argument_parser()
    arguments = argument_parser.parse_args()

    for loader_key in arguments.l:
        loader = loader_map.get(loader_key) or (lambda: missing_loader(loader_key))
        print(loader())


def init_argument_parser():
    parser = ArgumentParser()
    parser.add_argument("-l", "-loaders", nargs="+")

    return parser


if __name__ == "__main__":
    normalize_environment_variables()
    main()
