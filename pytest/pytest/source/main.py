import os, sys

if __name__ == '__main__':
    print("Python Version: " + sys.version)
    print("Python Executable: " + sys.executable)
    print("Env var TEST_NAME: " + os.getenv('TEST_NAME', None))