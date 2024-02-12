import sys

def main():
    mas = list(map(int, input().split()))
    mas.sort()
    print(mas[1])

if __name__ == '__main__':
    main()