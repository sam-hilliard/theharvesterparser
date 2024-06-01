#!/usr/bin/python3

import json
import argparse

def parse_theharvester_output(input_file, target, only_hostname=False):
    with open(input_file, 'r') as file:
        data = json.load(file)

    if target in data:
        result = data[target]
        if target == 'hosts' and only_hostname:
            result = [item.split(':')[0].rstrip('.') for item in result]
        return result
    else:
        raise ValueError(f"Target '{target}' not found in the JSON file")

def main():
    parser = argparse.ArgumentParser(
        description="Parse TheHarvester JSON output.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-i', '--input', required=True, help="Input JSON file from TheHarvester.")
    parser.add_argument('-t', '--target', required=True, choices=['hosts', 'emails', 'ips', 'urls', 'asns'],
                        help="Target section to extract. Supported targets: hosts, emails, ips, urls, asns")
    parser.add_argument('--only-hostname', action='store_true', help="Only extract the hostname (without trailing IP, ':', or trailing '.') when target is 'hosts'")

    args = parser.parse_args()

    try:
        result = parse_theharvester_output(args.input, args.target, args.only_hostname)
        if isinstance(result, list):
            for item in result:
                print(item)
        else:
            print(result)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
