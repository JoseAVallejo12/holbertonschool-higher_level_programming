#!/usr/bin/python3
if __name__ == "__main__":
    import sys
result = 0
ac_len = len(sys.argv)
if ac_len > 1:
    for n in range(1, ac_len):
        result += int(sys.argv[n])
    print("{}".format(result))
else:
    print("0")
