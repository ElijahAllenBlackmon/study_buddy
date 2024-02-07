print("Chapter 1 Questions\n")

CH1_Q = [
    input("Provides connectivity and ensures data flow across the network:\n"),
    input("A computer that functions both as the client and the server on a network:\n"),
    input("Media in which data is encoded into electrical impulses that travel through metal wires within cables:\n"),
    input("Use dest. end device address in conjunction with info. about the network interconnection to determine msg. paths through a network:\n"),
    input("Provides the channel over which the message travels from source to destination:\n"),
    input("Data encoded via modulation of specific frequencies of electromagnetic waves:\n"),
    input("A device on a network identified by an IP Address:\n"),
    input("What devices connect the individual end devices to the network?\n"),
    input("Glass or plastic fibers within cables:\n"),
    input("What is either the source or destination of a message transmitted over the network?\n"),
    input("Physically connects end devices to the network:\n"),
    input("Specialized ports on networking devices that connect individual networks:\n"),
    input("Connector, outlet on a networking device where the media connects either to an end device, or another networking device.")
    ]
CH1_A = [
    "Intermediary Device",
    "Copper",
    "Peer-to-Peer",
    "Intermediary Device",
    "Media",
    "Wireless",
    "End Device",
    "Intermediary Device",
    "Fiber-Optic",
    "End Device",
    "NIC",
    "Interface",
    "Port"
]


def main():
    score = 0

    for x in range(len(CH1_Q)):

        if CH1_A[x] == CH1_Q[x]:
            print()
            print(CH1_Q[x])
            print("Correct\n")
            score += 1
        else:
            print()
            print(CH1_Q[x])
            print("Incorrect\n")

    print(f"Final Score: {score}/{len(CH1_Q)}")


main()
