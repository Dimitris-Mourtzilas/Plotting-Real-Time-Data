


"""
This is program is designed to provide real-time generated data printed
into a csv file.

Further features will include operations on a json file.

"""

from time import *
from random import randint
import csv


class File:
    _csv_reader = None
    _csv_writer = None
    _count = 0
    _file = None

    def __init__(self):
        pass

    def openFile(self,filename):
        if filename.__eq__("") or not(filename.__contains__(".csv")):
            print("File is either empty or not .csv")
            exit(1)
        self._file= open(filename,"w+")

    def readFile(self):
        if self._file is None:
            print("The file is empty")
            return
        self.csv_reader = csv.reader(self._file,delimiter=',')
        for value in self.csv_file:
            print(f"Data:\n{value}")

    def writeFile(self,el):
        if self._file is None:
            print("File either corrupted or empty")
            return
        self._csv_writer=csv.writer(self._file,delimiter=',')
        self._csv_writer.writerow(str(el))

    def closeFile(self):
        self._file.close()


if __name__ == "__main__":

    filename = input("Give the name of the file")
    new_csv_file = File()
    new_csv_file.openFile(filename)
    size = randint(0,100)
    size_count =0
    while size_count < size:
        num= randint(0,100)
        print(f"Wrinting {num} to file\n")
        sleep(0.35)
        new_csv_file.writeFile(num)
        size_count+=1

    new_csv_file.closeFile()
