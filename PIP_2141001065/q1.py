import pdb
pdb.set_trace()

def summation(n):
    total=0
    for count in range(1,n):
        total += count
    return total
def main():
    n = int(input("Enter Number of terms: "))
    total = summation(n)
    print("Sum of first",n, "Positive Integers: ", total)
if __name__== "__main__":
    main()
