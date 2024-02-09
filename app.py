import data

print("Chapter 1 Questions\n")

def main():
    CH1_score = 0
    # CH3_score = 0
    # CH2_score = 0
    # CH4_score = 0

    for x in range(len(data.CH1_Q)):

        if data.CH1_A[x] == data.CH1_Q[x]:
            print()
            print(data.CH1_Q[x])
            print("Correct\n\n")
            CH1_score += 1
        else:
            print()
            print(data.CH1_Q[x])
            print("Incorrect\n\n")

    print(f"Final Score: {CH1_score}/{len(data.CH1_Q)}")


main()