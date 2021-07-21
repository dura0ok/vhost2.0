import argparse
import sys

from systems_selector.select import select_handler

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--server', help="'apache' or 'nginx'")
    parser.add_argument("-show", help="show", action='store_true')
    args = parser.parse_args()

    if args.server not in ["apache", "nginx"]:
        print("server args must be apache or nginx")
        sys.exit(1)

    try:
        handler = select_handler()
        handler.set_server(args.server)

        if args.show:
            handler.show_hosts()

    except Exception as e:
        print(e)
