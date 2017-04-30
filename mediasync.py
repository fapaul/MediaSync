import argparse


def main():
    parser = argparse.ArgumentParser(description='Generating and comparing \
                                                  multimedia file lists')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-g', '--generate',
                       help='List all leaf directories under a specific root \
                       directory.')
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
    pass

if __name__ == '__main__':
    main()
