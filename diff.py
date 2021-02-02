import pandas
import sys

def findDiff(file1, file2):
    #Read Sheet
    file1Sheet = pandas.read_excel(file1)
    file2Sheet = pandas.read_excel(file2)

    #Read headers
    HeaderList1 = file1.column.rivel()


if len(sys.argv) != 3:
    raise ValueError ('Invalid input')

findDiff(sys.argv[1], sys.argv[2])