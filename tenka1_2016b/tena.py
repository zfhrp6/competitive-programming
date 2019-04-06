from math import floor

def f(n):
    return floor((n**2+4.0)/8.0)

def main():
    print(f(f(f(20))))

if __name__ == '__main__':
    main()
