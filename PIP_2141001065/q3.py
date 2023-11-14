import pdb
pdb.set_trace()
def main():
    totalmarks = 0
    i = 0
    while True:
        marks = input("Enter Marks for subject " + str(i + 1) + ":")
        if marks == '':
            break
        marks = int(marks)
        if marks < 0 or marks > 100:
            print("Invalid Marks")
            continue
        i += 1
        totalmarks += marks
    percentage = totalmarks // i
    print("Total marks", int(totalmarks))
    print("Percentage", round(percentage, 2))

if __name__ == '__main__':
    main()
