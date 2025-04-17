from Imports.add import Add
from Imports.divide import Divide

def main():
    x = 4
    y = 6
    divide_answer = Divide(x, y)
    print(Add(x, y))
    print(f"\n{divide_answer}")

if __name__ == '__main__':
    main()
