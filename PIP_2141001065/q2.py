import pdb
pdb.set_trace()

def invertedRightTriangle(nRows):
    for i in range(nRows,0,-1):
        print("*"*i)

def main():
    nRows = int(input("Enter Number Of Rows: "))
    invertedRightTriangle(nRows)

if __name__ == '__main__':
    main()
