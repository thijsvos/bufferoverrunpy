import requests
import json
import argparse

argument_parser = argparse.ArgumentParser(description='Script to parse subdomains from the "bufferover.run" website.')
argument_parser.add_argument('domain', help='Domain to enumerate subdomains for.')
argument_parser.add_argument('-v', dest='verbose', action='store_true', help='Print verbose output.')
argument_parser.add_argument('-o', dest='output_file', help='Output file to write subdomains to.')
arguments = argument_parser.parse_args()


r = requests.get(f"https://dns.bufferover.run/dns?q=.{arguments.domain}")
data = json.loads(r.text)

subdomain_list = []
subdomain_list.extend(subdomain.split(',')[1] for subdomain in data['FDNS_A'])
subdomain_list.extend(subdomain.split(',')[1] for subdomain in data['RDNS'])

if arguments.verbose:
    print('\n'.join(subdomain_list))

if arguments.output_file:
    with open(arguments.output_file, 'w') as f:
        f.writelines(subdomain + '\n' for subdomain in subdomain_list)
