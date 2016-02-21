import sys
def read():
    return sys.stdin.readline()

def readstrip():
    return read().strip()

def main():
    line = ""
    for i in range(4):
        line += "".join(readstrip().split(" "))
    print("{0} {1} {2} {3}".format(line[15],line[14],line[13],line[12]))
    print("{0} {1} {2} {3}".format(line[11],line[10],line[9],line[8]))
    print("{0} {1} {2} {3}".format(line[7],line[6],line[5],line[4]))
    print("{0} {1} {2} {3}".format(line[3],line[2],line[1],line[0]))


if __name__ == '__main__':
    main()
