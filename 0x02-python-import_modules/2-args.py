#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    index = len(sys.argv) - 1
    if index == 0:
        print("0 arguments.")
    elif index == 1:
        print(index, "argument:")
        print("{:d}:".format(index), sys.argv[index], end='\n')

    else:
        print(index, "arguments:")
        for name in range(index):

            print("{:d}:".format(name + 1), sys.argv[name + 1], end='\n')
