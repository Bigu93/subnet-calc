# Subnet Calculator

This Python script is designed to calculate subnet details based on provided IP addresses and CIDR notation. It supports calculating details for a single subnet or multiple subnets, making it a versatile tool for network administrators and enthusiasts.

## Features

- Calculate subnet mask, network address, broadcast address, and the range of usable IP addresses for a given IP address and CIDR notation.
- Support for calculating details for multiple subnets if the number of desired subnets is provided.
- Input validation to ensure correct IP address format and feasible subnet requests.

## Requirements

This script requires Python 3.6 or later. All necessary libraries are part of the Python Standard Library, so no additional installations are required.

## Installation

No installation is necessary. Simply clone or download the repository to your local machine.

```bash
git clone https://github.com/Bigu93/subnet-calc.git
cd subnet-calc
```

## Usage

Run the script from the command line, providing the IP address and optionally the CIDR notation and the number of desired subnets.

```bash
python subnet.py 192.168.1.0 --cidr 24
python subnet.py 192.168.1.0 --cidr 24 --subnets 4
```

## Input arguments

- *ip_address*: The IP address in dotted decimal notation (mandatory).
- *--cidr* CIDR notation (optional if subnet mask is given).
- *--subnets*: Number of desired subnets (optional).

## Output

The script outputs the following details:

- Subnet Mask
- Network Address
- Broadcast Address
- Usable IP Range

For multiple subnets, these details are provided for each calculated subnet.
