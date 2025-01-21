# run_calculator.py

import argparse
from calculator import add

def main():
    parser = argparse.ArgumentParser(description="String Calculator")
    parser.add_argument('numbers', type=str, help="Comma-separated numbers or a string with custom delimiters")
    args = parser.parse_args()
    
    try:
        result = add(args.numbers)
        print(f"Result: {result}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
