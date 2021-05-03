import sys
import requests
import dns.resolver
from bs4 import BeautifulSoup
import reg
import json
import argparse


# Caso eu queira aceitar outro resolv.conf, posso iniciar um resolver com
# novoResolver = dns.resolver.Resolver("<caminho do novo resolv.conf")

def resolve_dns(domain_name, query_type="A", verbose=True):
    try:
        dns_request = dns.resolver.resolve(domain_name, query_type, raise_on_no_answer=verbose)
        response = dns_request.response.answer

        return response[0].__str__()

    except dns.resolver.NoAnswer as response:
        print(response.__str__())
        # return response.__str__()
    except dns.exception.Timeout as response:
        print(response.__str__())
        # return response.__str__()
    except dns.resolver.NXDOMAIN as response:
        print(response.__str__())
        # return response.__str__()
    except dns.resolver.YXDOMAIN as response:
        print(response.__str__())
        # return response.__str__()
    except dns.resolver.NoNameservers as response:
        print(response.__str__())
        # return response.__str__()

##### General configuration
# Keep this as TRUE while we do not finish its implementation otherwise it will crash
verbose = True
query_types = ["A", 'MX', 'CNAME', 'NS', 'TXT', 'AAAA']
dns_recon_report_file = "dns_registers.txt"
dns_findings = []


args_parser = argparse.ArgumentParser(
    usage='%(prog)s [options] <domain_name>',
    description="This is a learning project "
                "created to help me on my python learning journey, "
                "mixing security and python programming. "
                "The intention of this tool, when finished is to provide a "
                "complete footprint of a given domain or IP",
    allow_abbrev=False)

args_parser.add_argument('-d',
                         '--dns',
                         action='store_true',
                         help='search all types of dns records for the informed dns_name')
args_parser.add_argument('--output_file',
                         action='store',
                         nargs=1,
                         default='footprint_report.txt',
                         help='inform the name of the output file used to record the footprint findings')
args_parser.add_argument('domain_name',
                         metavar='domain_name',
                         action='store')


args = args_parser.parse_args()
domain_name = args.domain_name
report_file = args.output_file
if args.dns:
    for type in query_types:
            dns_answer = resolve_dns(domain_name, type, verbose)
            if dns_answer is None:
                continue
            else:
                dns_findings.append(dns_answer)

    with open(dns_recon_report_file, 'w') as dns_file_writer:
        for dns_register in dns_findings:
            dns_file_writer.writelines(dns_register.__str__())
            dns_file_writer.write('\n')


print(args)
# if "-d" in opts:
#     for type in query_types:
#         dns_answer = resolve_dns(domain_name, type, verbose)
#         if dns_answer is None:
#             continue
#         else:
#             dns_findings.append(dns_answer)
#
#     with open(dns_recon_report_file, 'w') as dns_file_writer:
#         for dns_register in dns_findings:
#             dns_file_writer.writelines(dns_register.__str__())
#             dns_file_writer.write('\n')
# else:
#     raise SystemExit(help())
#







