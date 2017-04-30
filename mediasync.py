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
    first_set = _read_list(first)
    second_set = _read_list(second)
    second_need = first_set - second_set
    first_need = second_set - first_set
    with open('needs.txt', 'w') as f:
        _write_section('first needs:', first_need, f)
        _write_section('second needs:', second_need, f)


def generate(root):
    queue = deque(_build_paths(root))
    leafs = []
    while queue:
        current = queue.popleft()
        subdirs = _build_paths(current)
        if not subdirs:
            leafs.append(current.split(os.sep)[-1])
            continue
        queue.extend(subdirs)
    with open('multimedia.txt', 'w') as f:
        f.write('\n'.join(leafs))


def _build_paths(prefix):
    return [os.path.join(prefix, x) for x in next(os.walk(prefix))[1]]


def _read_list(multimedia_file):
    with open(multimedia_file, 'r') as f:
        return set([x.strip() for x in f.readlines()])


def _write_section(head, needs, handle):
    handle.write(head + '\n')
    handle.write('\n'.join(needs) + '\n')

if __name__ == '__main__':
    main()
