import pdb
pdb.set_trace()

def findhcf(num1, num2):
    if num1 < num2:
        minNum = num1
    else:
        minNum = num2
    
    for i in range(minNum, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            HCF = i
            return HCF

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = findhcf(num1, num2)
    print(f"The HCF of {num1} and {num2} is: {result}")

if __name__ == '__main__':
    main()
