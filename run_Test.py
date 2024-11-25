from configTest import *
import sys

# Main function to run the tests
def main():
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        pytest.main(["-vv", "-n", "1", file_name])
    else:
        print("file name needed")

if __name__ == "__main__":
    main()
