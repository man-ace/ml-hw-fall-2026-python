from module5_mod import NumbersProcessor

def main():
    n = int(input("Enter a positive integer N: "))

    processor = NumbersProcessor()
    
    print(f"Enter {n} numbers:")
    for i in range(n):
        processor.input(i)

    x = int(input("Enter integer X to search: "))

    result = processor.search(x)
    print(result)

if __name__ == "__main__":
    main()