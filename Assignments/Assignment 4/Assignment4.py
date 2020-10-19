def Sum(num):
    return sum(range(1,num+1))

def main():
    num = input("Please enter your number to sum: ")
    print(Sum(int(num)))

if __name__ == "__main__":
    main()