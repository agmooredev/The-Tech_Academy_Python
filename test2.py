import os

def writeData():
    data = '\nHello World'
    with open('new_file.txt', 'a') as f:
       f.write(data)
       f.close()


def openFile():
    with open('new_file.txt', 'r') as f:
        data = f.read()
        print(data)
        f.close()



if __name__ == "__main__":
    writeData()
    openFile()