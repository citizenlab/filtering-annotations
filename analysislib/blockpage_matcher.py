"""
Blockpage Matching Classes

SimpleBlockPagePattern - defines what a single entry in a known block looks like
BlockPatternMatcher - a group of BlockPagePatterns that can generate matching dictionaries to use against headers/body text
"""

import re

class SimpleBlockPagePattern:
    def __init__(self, name, pattern, location_found, common_name="", source="", exp_url="",confidence_no_fp=10, scope="nat", expected_countries=None, notes=""):

        self.name = name                                                    # name of the fingerprint to tag identified entries with (should be unique)
        self.common_name = common_name                                             # friendly name of the detection (can be shared)
        self.pattern = pattern                                              # actual pattern to match against
        self.location_found = location_found.lower()                        # either "body", or "header" currently
        self.exp_url = exp_url                                              # an example OONI explorer URL
        self.confidence_no_fp = confidence_no_fp                            # confidence 1-10 of how likely there will be no false positives
                                                                            # we should probably define this more:
                                                                                # 1 - very likely to be a false positive
                                                                                # 5 - somewhat likely to be a false positive
                                                                                # 10 - very unlikely to be a false positive
        self.scope = scope                                                  # likely scope of this detection
                                                                                # "nat" national level blockpage
                                                                                # "isp" ISP level blockpage
                                                                                # "prod" text pattern related to a middlebox product
                                                                                # "inst" text pattern related to a voluntary instition blockpage (school, office)
                                                                                # "vbw" vague blocking word
        self.source = source                                                # where we found the pattern from (informational)
        if isinstance(expected_countries, str):                             # list of countries we expect to find this pattern
            expected_countries = [expected_countries]
        elif expected_countries is None:
            expected_countries = []
        self.expected_countries =[x.upper() for x in expected_countries]    # two letter country code where we expect to find it
        self.notes = notes                                                  # extra text if needed

    def __repr__(self):
        return "%s:%s:%s" % (self.name, self.common_name, self.pattern)

class BlockPatternMatcher:

    all_blocks_known = None

    import analysislib.known_blockpages as kb
    known_blocks = kb.known_blocks

    def __init__(self, given_blocks=None):
        if given_blocks is None:
            self.all_blocks_known = self.known_blocks
        else:
            self.all_blocks_known = given_blocks

        self.all_blocks_known = sorted(self.all_blocks_known, key=lambda i: i.name)

    def pattern_to_common_name(self, given_detection_name):
        for this_block in self.all_blocks_known:
            if this_block.name == given_detection_name:
                return this_block.common_name
        return ""

    def get_info_for_detection(self, given_detection_name):
        for this_block in self.all_blocks_known:
            if this_block.name == given_detection_name:

                cleaned_notes = str(this_block.notes).replace("\n","")
                _RE_COMBINE_WHITESPACE = re.compile(r"\s+")
                cleaned_notes = _RE_COMBINE_WHITESPACE.sub(" ", cleaned_notes).strip()

                return {
                    "name": this_block.name,
                    "common_name": this_block.common_name,
                    "pattern": this_block.pattern,
                    "location_found": this_block.location_found,
                    "exp_url": this_block.exp_url,
                    "confidence_no_fp": this_block.confidence_no_fp,
                    "source": this_block.source,
                    "scope": this_block.scope,
                    "expected_countries": this_block.expected_countries,
                    "notes": cleaned_notes
                }
        return {}

    def as_dict_list(self):
        final_list = list()

        for this_sig in self.all_blocks_known:
            this_sig_as_dict = self.get_info_for_detection(this_sig.name)
            final_list.append(this_sig_as_dict)

        return final_list

    def generate_comparison_dicts(self, confidence_thresh=1, limit_to_countries=None, limit_to_scope=None):

        headers_compare_dict = dict()
        body_compare_dict = dict()

        if isinstance(limit_to_countries, str):
            limit_to_countries = [limit_to_countries]

        if isinstance(limit_to_scope, str):
            limit_to_scope = [limit_to_scope]

        for this_pattern in self.all_blocks_known:
            passes_confidence = this_pattern.confidence_no_fp >= confidence_thresh
            passes_country = False
            passes_scope = False

            if limit_to_scope is None:
                passes_scope = True
            else:
                for this_scope in limit_to_scope:
                    if this_scope == this_pattern.scope:
                        passes_scope = True

            if limit_to_countries is None:
                passes_country = True
            else:
                for this_country in limit_to_countries:
                    if this_country.upper() in this_pattern.expected_countries:
                        passes_country = True

            if passes_confidence and passes_country and passes_scope:
                if this_pattern.location_found == "header":
                    headers_compare_dict[this_pattern.name] = this_pattern.pattern
                elif this_pattern.location_found == "body":
                    body_compare_dict[this_pattern.name] = this_pattern.pattern

        return headers_compare_dict, body_compare_dict
