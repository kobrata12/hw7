import sys
if __name__ == "__main__":
    print(f"arguments count: {len (sys.argv)}")
    for i ,arg in enumerate(sys.argv):
        print(f"argument {i:>0}: {arg}")