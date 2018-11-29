#!/usr/bin/env python3
"""Program description.

Usage: program [options] <input> <output>

Options:
  --debug       print debug information
  --profile     print profile information
  <input>       input
  <output>      output
"""


import logging
import sys


def main(args):
    logging.debug(args)

    input_fn = args['input'] if args['input'] != '-' else '/dev/stdin'
    output_fn = args['output'] if args['output'] != '-' else '/dev/stdout'

    with open(input_fn, mode='r') as in_fh, open(output_fn, mode='w') as out_fh:
        n = 0
        for line in in_fh:
            print(line, end='', file=out_fh)
            n += 1
    logging.debug('read and write {} lines'.format(n))
    return 0


if __name__ == '__main__':
    from docopt import docopt
    args = docopt(__doc__)
    args = {k.lstrip('-<').rstrip('>'):args[k] for k in args}
    try:
        if args.get('debug'):
            logLevel = logging.DEBUG
        else:
            logLevel = logging.WARN
        logging.basicConfig(
            level=logLevel,
            format='%(asctime)s; %(levelname)s; %(funcName)s; %(message)s',
            datefmt='%y-%m-%d %H:%M:%S')
        if args.get('profile'):
            import cProfile
            cProfile.run('main(args)')
        else:
            main(args)
    except KeyboardInterrupt:
        logging.warning('Interrupted')
        sys.exit(1)
