def open_file():
    with open("Daylight.txt",'r') as f:
        data = f.read()
        print(data)

if __name__ == '__main__':
    open_file()
