# Filtering Annotations

Filtering annotations is a collection of descriptive names to text patterns that are meant to 
be matched against network measurements in platforms such as [OONI](https://ooni.org/), 
[CensoredPlanet](https://censoredplanet.org/), or [ICLab](https://iclab.org/).  These
are intended to describe facets of observed filtering infrastructure such as network
middle boxes, deep packet devices, and ISP blockpages among others. This collection is 
distributed as a Python library: analysislib that includes dns/blockpage signatures as
well as some code to create dictionaries to match against.

There are two types of signatures:

* HTTP(s) signatures
    * contained in: `known_blockpages.py`
    * screenshots in `blockpage_meta`
    * meant to be matched against either HTTP header/body responses
* DNS signatures
    * signatures contained in: `known_dns_sigs.py`
    * screenshots in `dns_meta`
    * meant to be be matched against DNS replies.    

Where possible samples of both screenshots and HTML are contained in the `meta` directories.

# Data

The data is stored in the `data` directory and currently in version 1.  It is available
in both JSON and CSV format.  If you are hoping to contribute annotations it is best
to edit the `.py` files in a pull request or add an issue with an associated example.

# Schema

## HTTP(s) Signatures

* name 
    * Name of the fingerprint to tag identified entries with (should be unique)
* common_name
    * A friendly name of the detection.  Unlike "name" field this can be shared.
* pattern
    * The actual text pattern to match against.
* location_found
    * Where the pattern is located either "body", or "header" currently.
* exp_url
    *  An example OONI explorer URL containing the behaviour.
* confidence_no_fp
    * How likely (by self-assessment) the signature is to cause a false positive. 
    Shorter or more vague text patterns which may be likely to match against are given lower numbers.
* scope
    * What is the network scope of the device/behaviour
    * Current allowed values:
        * "nat" National level filtering
        * "isp" ISP level filtering
        * "prod" text pattern related to a middlebox product such as a default blockpage.
        * "inst" text pattern related to a voluntary institution blockpage (school, office)
        * "vbw" a vague blocking word such as "web site blocked"
* source
    * URLs or citations related to the behaviour seen in the annotation.
* expected_countries
    * The two letter country code for where we would expect to find the annotations.
* notes
    * Extra field for any additional information


## DNS Signatures

* name 
    * Name of the fingerprint to tag identified entries with (should be unique)
* response
    * DNS reply to match against.
* confidence_no_fp
    * How likely (by self-assessment) the signature is to cause a false positive. 
    Shorter or more vague text patterns which may be likely to match against are given lower numbers.
* exp_url
    *  An example OONI explorer URL containing the behaviour.
* source
    * URLs or citations related to the behaviour seen in the annotation.
* scope
    * What is the network scope of the device/behaviour
    * Current allowed values:
        * "nat" National level filtering
        * "isp" ISP level filtering
        * "prod" text pattern related to a middlebox product such as a default blockpage.
        * "inst" text pattern related to a voluntary institution blockpage (school, office)
        * "vbw" a vague blocking word such as "web site blocked"
* notes
    * Extra field for any additional information


# License

[Code under MIT 3-Clause](LICENSE.md)