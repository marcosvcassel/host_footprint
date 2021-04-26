import sys
import requests
import dns.resolver
from bs4 import BeautifulSoup
import reg
import json

# Caso eu queira aceitar outro resolv.conf, posso iniciar um resolver com
# novoResolver = dns.resolver.Resolver("<caminho do novo resolv.conf")




def version():
    print("host_footprint.py - 0.0.1")

# def help():


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
domain_name = "sgnh.com.br"
dns_recon_report_file = "dns_registers.txt"
dns_findings = []

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

if "-d" in opts:
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
else:
    raise SystemExit(f"Usage: {sys.argv[0]} (-d)")








