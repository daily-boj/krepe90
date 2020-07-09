def p5397():
    with open("P5397_2.txt", "w") as f:
        f.write("<a" * 500000)


def p15565():
    with open("testcase/P15565_1.txt", "w") as f:
        f.write("100000 10000\n")
        f.write(" ".join("1" for n in range(100000)))


def p5015():
    with open("testcase/P5015_1.txt", "w") as f:
        f.write("a*" * 50 + "\n100\n")
        [f.write("a" * 100 + "\n") for n in range(100)]


if __name__ == "__main__":
    # p15565()
    p5015()
