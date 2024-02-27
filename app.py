import data

def main():
    # CH1_score = 0
    # CH3_score = 0
    # CH2_score = 0
    # CH4_score = 0
    # CH5_score = 0
    # CH6_score = 0
    CH7_score = 0
    # CH8_score = 0

    # Prompts Chapter 1 Questions
    # for x in range(len(data.CH1_Q)):

    #     if data.CH1_A[x] == data.CH1_Q[x]:
    #         print()
    #         print(data.CH1_Q[x])
    #         print("Correct\n\n")
    #         # Increases score for chapter
    #         CH1_score += 1
    #     else:
    #         print()
    #         print(data.CH1_Q[x])
    #         print("Incorrect\n\n")

    # Prompts Chapter 3 Questions
    # for x in range(len(data.CH3_Q)):
    #     if data.CH3_A[x] == data.CH3_Q[x]:
    #         print()
    #         print(data.CH3_Q[x])
    #         print("Correct\n\n")
    #         # Increases score for chapter
    #         CH3_score += 1
    #     else:
    #         print()
    #         print(data.CH3_Q[x])
    #         print("Incorrect\n\n")

    # Prompts Chapter 2 Questions
    # for x in range(len(data.CH2_Q)):
    #     if data.CH2_A[x] == data.CH2_Q[x]:
    #         print()
    #         print(data.CH2_Q[x])
    #         print("Correct\n\n")
    #         # Increases score for chapter
    #         CH2_score += 1
    #     else:
    #         print()
    #         print(data.CH2_Q[x])
    #         print("Incorrect\n\n")
    for x in range(len(data.CH7_Q)):
        if data.CH7_A[x] == data.CH7_Q[x]:
            print()
            print(data.CH7_Q[x])
            print("Correct\n\n")
            # Increases score for chapter
            CH7_score += 1
        else:
            print()
            print(data.CH7_Q[x])
            print("Incorrect\n\n")

    # Prints final score of each chapter
    # print(f"Chapter 1 Final Score: {CH1_score}/{len(data.CH1_Q)}\n")
    # print(f"Chapter 3 Final Score: {CH3_score}/{len(data.CH3_Q)}\n")
    # print(f"Chapter 2 Final Score: {CH2_score}/{len(data.CH2_Q)}\n")
    # print(f"Chapter 4 Final Score: {CH4_score}/{len(data.CH4_Q)}\n")
    # print(f"Chapter 5 Final Score: {CH5_score}/{len(data.CH5_Q)}\n")
    # print(f"Chapter 6 Final Score: {CH6_score}/{len(data.CH6_Q)}\n")
    print(f"Chapter 7 Final Score: {CH7_score}/{len(data.CH7_Q)}\n")
    # print(f"Chapter 8 Final Score: {CH8_score}/{len(data.CH8_Q)}\n")


main()
