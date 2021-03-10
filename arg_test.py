import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--nargs", nargs="+", type=int)
    opt = parser.parse_args()
    print(opt)
    print(type(opt.nargs))
