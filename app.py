print("Chapter 1 Questions\n")

CH1_Q = [
    input("Provides connectivity and ensures data flow across the network:\n"),
    input("Runs over telephone line:\n"),
    input("Media in which data is encoded into electrical impulses that travel through metal wires within cables:\n"),
    input("A computer that functions both as the client and the server on a network:\n"),
    input("ICANN:\n"),
    input("Internet access for areas with no internet:\n"),
    input("Use dest. end device address in conjunction with info. about the network interconnection to determine msg. paths through a network:\n"),
    input("Provides the channel over which the message travels from source to destination:\n"),
    input("Data encoded via modulation of specific frequencies of electromagnetic waves:\n"),
    input("High bandwidth, high availability, always-on connection to the internet:\n"),
    input("Low bandwidth; any phone line + modem:\n"),
    input("Illustrates devices, ports, and the addressing scheme of the network:\n"),
    input("A device on a network identified by an IP Address:\n"),
    input("What devices connect the individual end devices to the network?\n"),
    input("Worldwide collection of interconnected networks:\n"),
    input("IAB:\n"),
    input("Glass or plastic fibers within cables:\n"),
    input("What is either the source or destination of a message transmitted over the network?\n"),
    input("IETF:\n"),
    input("Mandatory documentation for a network. Visual map of networks:\n"),
    input("DSL:\n"),
    input("Physically connects end devices to the network:\n"),
    input("Specialized ports on networking devices that connect individual networks:\n"),
    input("Safe/secure access to outsiders from organizations; suppliers,contractors:\n"),
    input("Connector, outlet on a networking device where the media connects either to an end device, or another networking device:\n"),
    input("Illustrates the physical topolgy of intermediary devices:\n"),
    input("Private connection of LANs and WANs; belongs to an organization:\n"),
    input("In context, refers to the technologies that support the infrastructure & programmed services/rules/protocols, that move data across the network:\n"),
    input("Limits the number of affected devices during network failure.\n"),
    input("Built for quick recovery; multi-path dependence between destination and source:\n"),
    input("Data traveling through different paths but to the same destination:\n"),
    input("Bandwidth demand exceeds available amount; bps:\n"),
    input("Assures safe information transmission from source to destination:\n"),
    input("Timely reliable data access:\n"),
    input("Only intended and authorized recipients can access data:\n"),
    input("CCNA:\n"),
    input("NAT:\n"),
    ]
CH1_A = [
    "Intermediary Device",
    "DSL",
    "Copper",
    "Peer-to-Peer",
    "Internet Corporation for Assigned Names and Numbers",
    "Satellite",
    "Intermediary Device",
    "Media",
    "Wireless",
    "DSL",
    "Dial-Up Telephone",
    "Logical Topology Diagram",
    "End Device",
    "Intermediary Device",
    "The Internet",
    "Internet Architecture Board",
    "Fiber-Optic",
    "End Device",
    "Internet Engineering Task Force",
    "Topology Diagram",
    "Digital Subscriber Line",
    "NIC",
    "Interface",
    "Extranet",
    "Port",
    "Physical Topology Diagram",
    "Intranet",
    "Network Architecture",
    "Fault Tolerance",
    "Redundancy",
    "Packet Switching",
    "Congestion",
    "Integrity",
    "Availability",
    "Confidentiality",
    "Cisco Certified Network Administration",
    "Network Administration Type"
]


def main():
    CH1_score = 0

    for x in range(len(CH1_Q)):

        if CH1_A[x] == CH1_Q[x]:
            print()
            print(CH1_Q[x])
            print("Correct\n\n")
            CH1_score += 1
        else:
            print()
            print(CH1_Q[x])
            print("Incorrect\n\n")

    print(f"Final Score: {CH1_score}/{len(CH1_Q)}")


main()
