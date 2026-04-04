#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    # İlk arqumenti (fayl adını) ötürürük, yerdə qalanları siyahıya alırıq
    arguments = sys.argv[1:]
    total = 0

    for arg in arguments:
        total += int(arg)

    print("{:d}".format(total))
