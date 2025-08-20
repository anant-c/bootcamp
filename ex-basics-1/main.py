import sys

def main():
    # Check if a name argument is passed
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "world"
    print(f"Hello {name}")

if __name__ == "__main__":
    main()
