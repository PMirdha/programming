def take_input():
    instr = raw_input()
    a = list(map(int, instr.strip().split(" ")))


def get_input():
    n = int(take_input()[0])
    for i in range(n):
        solve(take_input()[0])


if __name__ == "__main__":
    pass