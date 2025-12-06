from aocd import get_data

YEAR, DAY = 2025, 3
puzzle = get_data(day=DAY, year=YEAR)

TEST_1 = """
987654321111111
811111111111119
234234234234278
818181911112111
"""


def parse(data: str) -> list:
    banks = []
    for row in data.strip().splitlines():
        banks.append([int(x) for x in row])

    return banks


def part_1(banks: list) -> int:
    vals = []

    for bank in banks:
        max_val = max(bank[:-1])
        max_pos = [i for i, x in enumerate(bank[:-1]) if x == max_val]

        pos_vals = []
        for pos in max_pos:
            max_val_2 = max(bank[pos + 1 :])
            pos_vals.append(max_val * 10 + max_val_2)

        vals.append(max(pos_vals))

    return sum(vals)


def part_2(banks: list) -> int:
    vals = []
    for bank in banks:
        val_1 = max(bank[:-11])
        pos_1 = [i for i, x in enumerate(bank[:-11]) if x == val_1]
        # print(pos_1)

        pos_vals = []
        for p_1 in pos_1:
            val_2 = max(bank[p_1 + 1 : -10])
            pos_2 = [i for i, x in enumerate(bank[:-10]) if x == val_2 and i > p_1]
            # print(pos_2)

            for p_2 in pos_2:
                val_3 = max(bank[p_2 + 1 : -9])
                pos_3 = [i for i, x in enumerate(bank[:-9]) if x == val_3 and i > p_2]

                for p_3 in pos_3:
                    val_4 = max(bank[p_3 + 1 : -8])
                    pos_4 = [i for i, x in enumerate(bank[:-8]) if x == val_4 and i > p_3]

                    for p_4 in pos_4:
                        val_5 = max(bank[p_4 + 1 : -7])
                        pos_5 = [i for i, x in enumerate(bank[:-7]) if x == val_5 and i > p_4]

                        for p_5 in pos_5:
                            val_6 = max(bank[p_5 + 1 : -6])
                            pos_6 = [i for i, x in enumerate(bank[:-6]) if x == val_6 and i > p_5]

                            for p_6 in pos_6:
                                val_7 = max(bank[p_6 + 1 : -5])
                                pos_7 = [i for i, x in enumerate(bank[:-5]) if x == val_7 and i > p_6]

                                for p_7 in pos_7:
                                    val_8 = max(bank[p_7 + 1 : -4])
                                    pos_8 = [i for i, x in enumerate(bank[:-4]) if x == val_8 and i > p_7]

                                    for p_8 in pos_8:
                                        val_9 = max(bank[p_8 + 1 : -3])
                                        pos_9 = [i for i, x in enumerate(bank[:-3]) if x == val_9 and i > p_8]

                                        for p_9 in pos_9:
                                            val_10 = max(bank[p_9 + 1 : -2])
                                            pos_10 = [i for i, x in enumerate(bank[:-2]) if x == val_10 and i > p_9]

                                            for p_10 in pos_10:
                                                val_11 = max(bank[p_10 + 1 : -1])
                                                pos_11 = [
                                                    i for i, x in enumerate(bank[:-1]) if x == val_11 and i > p_10
                                                ]

                                                for p_11 in pos_11:
                                                    val_12 = max(bank[p_11 + 1 :])
                                                    # pos_12 = [i for i, x in enumerate(bank) if x == val_12 and i > p_11]

                                                    pos_vals.append(
                                                        int(
                                                            str(val_1)
                                                            + str(val_2)
                                                            + str(val_3)
                                                            + str(val_4)
                                                            + str(val_5)
                                                            + str(val_6)
                                                            + str(val_7)
                                                            + str(val_8)
                                                            + str(val_9)
                                                            + str(val_10)
                                                            + str(val_11)
                                                            + str(val_12)
                                                        )
                                                    )
        vals.append(max(pos_vals))

    return sum(vals)


def part_2_test(banks: list) -> int:
    vals = []
    for bank in banks:
        val_1 = max(bank[:-11])
        pos_1 = [i for i, x in enumerate(bank[:-11]) if x == val_1][0]

        val_2 = max(bank[pos_1 + 1 : -10])
        pos_2 = [i for i, x in enumerate(bank[:-10]) if x == val_2 and i > pos_1][0]

        val_3 = max(bank[pos_2 + 1 : -9])
        pos_3 = [i for i, x in enumerate(bank[:-9]) if x == val_3 and i > pos_2][0]

        val_4 = max(bank[pos_3 + 1 : -8])
        pos_4 = [i for i, x in enumerate(bank[:-8]) if x == val_4 and i > pos_3][0]

        val_5 = max(bank[pos_4 + 1 : -7])
        pos_5 = [i for i, x in enumerate(bank[:-7]) if x == val_5 and i > pos_4][0]

        val_6 = max(bank[pos_5 + 1 : -6])
        pos_6 = [i for i, x in enumerate(bank[:-6]) if x == val_6 and i > pos_5][0]

        val_7 = max(bank[pos_6 + 1 : -5])
        pos_7 = [i for i, x in enumerate(bank[:-5]) if x == val_7 and i > pos_6][0]

        val_8 = max(bank[pos_7 + 1 : -4])
        pos_8 = [i for i, x in enumerate(bank[:-4]) if x == val_8 and i > pos_7][0]

        val_9 = max(bank[pos_8 + 1 : -3])
        pos_9 = [i for i, x in enumerate(bank[:-3]) if x == val_9 and i > pos_8][0]

        val_10 = max(bank[pos_9 + 1 : -2])
        pos_10 = [i for i, x in enumerate(bank[:-2]) if x == val_10 and i > pos_9][0]

        val_11 = max(bank[pos_10 + 1 : -1])
        pos_11 = [i for i, x in enumerate(bank[:-1]) if x == val_11 and i > pos_10][0]

        val_12 = max(bank[pos_11 + 1 :])

        vals.append(
            int(
                str(val_1)
                + str(val_2)
                + str(val_3)
                + str(val_4)
                + str(val_5)
                + str(val_6)
                + str(val_7)
                + str(val_8)
                + str(val_9)
                + str(val_10)
                + str(val_11)
                + str(val_12)
            )
        )

    return sum(vals)


banks = parse(puzzle)
print("part 1: ", part_1(banks))
print("part 2: ", part_2_test(banks))
