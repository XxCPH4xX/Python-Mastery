def hello(name):
    return f"Hello, {name}!"

def main():
    print('(banner) running directly - __name__ is __main__')
    print(hello("Sarah"))

if __name__ == '__main__':
    main()
