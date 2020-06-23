import re

class SimpleDNSReplyPattern:
    def __init__(self, name, response, confidence_no_fp=10, exp_url="", source="", scope="", expected_countries=None,
                 notes=""):
        self.name = name
        self.response = response
        self.confidence_no_fp = confidence_no_fp
        self.exp_url = exp_url
        self.source = source
        self.scope = scope
        self.notes = notes

        if isinstance(expected_countries, str):  # list of countries we expect to find this pattern
            expected_countries = [expected_countries]
        elif expected_countries is None:
            expected_countries = []
        self.expected_countries = [x.upper() for x in
                                   expected_countries]  # two letter country code where we expect to find it

    def __repr__(self):
        return "%s:%s" % (self.name, self.response)


class DNSMatcher:
    from analysislib.known_dns_sigs import known_dns_sigs as kds

    knowns_dns_sigs = kds

    def __init__(self, given_sigs=None):
        if given_sigs is None:
            self.sigs = self.knowns_dns_sigs
        else:
            self.sigs = given_sigs

        self.sigs = sorted(self.sigs, key=lambda i: i.name)

    def get_info_for_detection(self, given_detection_name):
        for this_block in self.sigs:
            if this_block.name == given_detection_name:
                cleaned_notes = str(this_block.notes).replace("\n","")
                _RE_COMBINE_WHITESPACE = re.compile(r"\s+")
                cleaned_notes = _RE_COMBINE_WHITESPACE.sub(" ", cleaned_notes).strip()

                return {
                    "name": this_block.name,
                    "response": this_block.response,
                    "confidence_no_fp": this_block.confidence_no_fp,
                    "exp_url": this_block.exp_url,
                    "source": this_block.source,
                    "scope": this_block.scope,
                    "expected_countries": this_block.expected_countries,
                    "notes": cleaned_notes,
                }
        return {}

    def as_dict_list(self):
        final_list = list()

        for this_sig in self.sigs:
            this_sig_as_dict = self.get_info_for_detection(this_sig.name)
            final_list.append(this_sig_as_dict)

        return final_list

    def generate_comparison_dict(self, limit_to_countries=None, confidence_thresh=1):

        compare_dict = dict()

        if isinstance(limit_to_countries, str):
            limit_to_countries = [limit_to_countries]

        for this_sig in self.sigs:
            passes_confidence = this_sig.confidence_no_fp >= confidence_thresh
            passes_country = False

            if limit_to_countries is None:
                passes_country = True
            else:
                for this_country in limit_to_countries:
                    if this_country.upper() in this_sig.expected_countires:
                        passes_country = True

            if passes_country and passes_confidence:
                compare_dict[this_sig.name] = this_sig.response

        return compare_dict
