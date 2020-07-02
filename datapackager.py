from analysislib import BlockPatternMatcher, DNSMatcher
import json
import csv
import os

output_dir = "data"
current_version = "v1"

# json output
def blocks_to_json(given_fn):
    bpm = BlockPatternMatcher()
    all_http_sigs = bpm.as_dict_list()
    dict_to_json(given_fn, all_http_sigs)

def dns_to_json(given_fn):
    dnsm = DNSMatcher()
    all_dns_sigs = dnsm.as_dict_list()
    dict_to_json(given_fn, all_dns_sigs)

def dict_to_json(given_fn, given_dict):
    with open(given_fn, 'w') as fout:
        json.dump(given_dict, fout, indent=2)

# csv output
def blocks_to_csv(given_fn):
    bpm = BlockPatternMatcher()
    all_http_sigs = bpm.as_dict_list()
    http_fields = ["name", "common_name", "pattern", "location_found", "exp_url", "confidence_no_fp", "source", "scope", "expected_countries", "notes"]
    dict_to_csv(given_fn, all_http_sigs, http_fields)

def dns_to_csv(given_fn):
    dnsm = DNSMatcher()
    all_dns_sigs = dnsm.as_dict_list()
    dns_fields = ["name", "response", "confidence_no_fp", "exp_url", "source", "scope", "expected_countries", "notes"]
    dict_to_csv(given_fn, all_dns_sigs, dns_fields)

def dict_to_csv(given_fn, given_dict, given_fields):
    with open(given_fn, "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=given_fields)
        writer.writeheader()
        for this_entry in given_dict:
            writer.writerow(this_entry)


# json
blocks_to_json(os.path.join(output_dir, current_version, "http.json"))
dns_to_json(os.path.join(output_dir, current_version, "dns.json"))

# csv
blocks_to_csv(os.path.join(output_dir, current_version, "http.csv"))
dns_to_csv(os.path.join(output_dir, current_version, "dns.csv"))
