import argparse
import ipaddress


def parse_arguments():
    """
    Parses command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Subnet Calculator")
    parser.add_argument(
        "ip_address", type=str, help="IP address in dotted decimal notation"
    )
    parser.add_argument(
        "--cidr", type=int, help="CIDR notation (optional if subnet mask is given)"
    )
    parser.add_argument(
        "--subnets", type=int, help="Number of desired subnets (optional)"
    )
    args = parser.parse_args()
    return args


def validate_input(ip_address, cidr=None, subnets=None):
    """
    Validates the input parameters for correctness.
    - Ensures the IP address and CIDR notation are valid.
    - Checks if the requested number of subnets is feasible.
    """
    try:
        if cidr is not None:
            ip_network = ipaddress.ip_network(f"{ip_address}/{cidr}", strict=False)
        else:
            ip_network = ipaddress.ip_network(ip_address, strict=False)

        if cidr is None:
            cidr = ip_network.prefixlen

        if subnets:
            max_subnets = 2 ** (32 - cidr)
            if subnets > max_subnets:
                raise ValueError(
                    f"Requested number of subnets ({subnets}) exceeds the maximum possible ({max_subnets}) with CIDR {cidr}."
                )
    except ValueError as e:
        print(f"Input validation error: {e}")
        exit(1)


def calculate_subnet_details(ip_address, cidr):
    """
    Calculates subnet details based on the given IP address and CIDR notation.
    - Subnet Mask
    - Network Address
    - Broadcast Address
    - Range of Usable IP Addresses
    """
    ip_network = ipaddress.ip_network(f"{ip_address}/{cidr}", strict=False)
    subnet_mask = ip_network.netmask
    network_address = ip_network.network_address
    broadcast_address = ip_network.broadcast_address
    usable_ips = list(ip_network.hosts())

    results = {
        "Subnet Mask": str(subnet_mask),
        "Network Address": str(network_address),
        "Broadcast Address": str(broadcast_address),
        "Usable IP Range": f"{usable_ips[0]} - {usable_ips[-1]}"
        if usable_ips
        else "N/A",
    }

    return results


def calculate_multiple_subnets(ip_address, cidr, subnets):
    """
    Calculates details for multiple subnets if the number of desired subnets is provided.
    - Determines the new CIDR notation to split the network into the desired number of subnets.
    - Calculates the subnet details for each split.
    """
    new_cidr = cidr
    while 2 ** (new_cidr - cidr) < subnets:
        new_cidr += 1

    ip_network = ipaddress.ip_network(f"{ip_address}/{cidr}", strict=False)
    subnet_list = list(ip_network.subnets(new_prefix=new_cidr))

    results = []
    for subnet in subnet_list:
        details = {
            "Subnet": str(subnet),
            "Subnet Mask": str(subnet.netmask),
            "Network Address": str(subnet.network_address),
            "Broadcast Address": str(subnet.broadcast_address),
            "Usable IP Range": f"{list(subnet.hosts())[0]} - {list(subnet.hosts())[-1]}",
        }
        results.append(details)

    return results


def display_results(results):
    """
    Displays the calculation results in a user-friendly manner.
    - For a single subnet, it displays the subnet details directly.
    - For multiple subnets, it iterates through the list of subnet details and displays each.
    """
    if isinstance(results, list):
        for i, subnet in enumerate(results, start=1):
            print(f"Subnet {i}:")

            for key, value in subnet.items():
                print(f"  {key}: {value}")

            print()
    else:
        for key, value in results.items():
            print(f"{key}: {value}")


def main():
    """
    The main entry point of the script.
    """
    args = parse_arguments()
    validate_input(args.ip_address, args.cidr, args.subnets)
    if args.subnets:
        results = calculate_multiple_subnets(args.ip_address, args.cidr, args.subnets)
    else:
        results = calculate_subnet_details(args.ip_address, args.cidr)
    display_results(results)


if __name__ == "__main__":
    main()
