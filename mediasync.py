import argparse
import os
from collections import deque


def main():
    parser = argparse.ArgumentParser(description='Generating and comparing \
                                                  multimedia file lists')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-g', '--generate',
                       help='Lists all leaf directories under a specific root \
                       directory and saves a file.')
    group.add_argument('-c', '--compare', nargs=2,
                       help='Takes two multimedia list paths and compares \
                             them.')
    args = parser.parse_args()
    for arg, parameters in vars(args).items():
        if not parameters:
            continue
        func = eval(arg)
        try:
            func(*parameters)
        except TypeError:
            func(parameters)


def compare(first, second):
    pass


def generate(root):
    queue = deque(_build_paths(root))
    leafs = []
    while queue:
        current = queue.popleft()
        subdirs = _build_paths(current)
        if not subdirs:
            leafs.append(current.split('/')[-1])
            continue
        queue.extend(subdirs)
    with open('multimedia.txt', 'w') as f:
        f.write('\n'.join(leafs))


def _build_paths(prefix):
    return [os.path.join(prefix, x) for x in next(os.walk(prefix))[1]]


if __name__ == '__main__':
    main()
