from analysislib.blockpage_matcher import SimpleBlockPagePattern

"""
These are all our known blockpage patterns thus far.  Ideally this should be stored in some kind of yml 
or similar but I am storing here because we get some error highlighting from an IDE as well because the
schema changes frequently.
"""

known_blocks = [

    # National Level Blockpage Patterns

    SimpleBlockPagePattern(
        name="nat_ir_iframe_forward_ipv4",
        common_name="National Iran Block",
        pattern="""iframe src="http://10.10.""",
        location_found="body",
        source=[
            "https://censorbib.nymity.ch/pdf/Aryan2013a.pdf"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200119T191016Z_AS49100_ISzGfWT9eaRxyQF58bRh1B0BUkDQYDXAgSixr0f9ZV2hFjVNsI?input=http://www.gayhealth.com/",
        confidence_no_fp=10,
        scope="nat",
        expected_countries=[ "IR" ],
        notes="Well known iframe to http://10.10.34.34 (or .33) Iranian national blockpage",
    ),

    SimpleBlockPagePattern(
        name="nat_ir_iframe_forward_ipv6",
        common_name="National Iran Block",
        pattern="""</title></head><body><iframe src="http://[d0:0:0:0:0:0:0:11:80]" style="width: 100%; height: 100%" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" vspace="0" hspace="0"></iframe></body></html>""",
        location_found="body",
        source=[
            "https://censorbib.nymity.ch/pdf/Aryan2013a.pdf"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20180627T180515Z_AS44244_Z8V0i4Cr6PoJHByQQ89uN3meAmQbvdUrBli1NqYU8786BLquMk?input=http://alone-persian-man.blogspot.com",
        confidence_no_fp=10,
        scope="nat",
        expected_countries=[ "IR" ],
        notes="IPv6 variant of the known 10.10.34.34/35 blockpage iframe forward.",
    ),

    SimpleBlockPagePattern(
        name="nat_ir_block_internetir",
        common_name="National Iran Block",
        pattern="""internet.ir/1-2""",
        location_found="body",
        source=[
            "https://censorbib.nymity.ch/pdf/Aryan2013a.pdf"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180820T042050Z_AS61173_FPMTdrQeLtEbtLwBjDarQzBlhKVOLhwMbYXGvn9RRcazAFRzRM?input=http://www.wmmh.blogspot.com",
        confidence_no_fp=10,
        scope="nat",
        expected_countries=["IR"],
        notes="Destination block page of iran (from 10.10.34.34 and 10.10.34.33 within country)",
    ),

    SimpleBlockPagePattern(
        name="nat_ir_block_peyvandha",
        common_name="National Iran Block",
        pattern="""peyvandha.ir/1-2""",
        location_found="body",
        source=[
            "https://censorbib.nymity.ch/pdf/Aryan2013a.pdf"
        ],
        exp_url="https://explorer.ooni.org/measurement/20190409T200524Z_AS58224_rPCEFPueXMqioaKnlJnCxocixIQntBMYRps14Iabf3FYimDuRd?input=http://www.wmmh.blogspot.com/",
        confidence_no_fp=10,
        scope="nat",
        expected_countries=["IR"],
        notes="Destination block page of iran (from 10.10.34.34 and 10.10.34.33 within country)",
    ),

    SimpleBlockPagePattern(
        name="nat_sa",
        common_name="National Saudi Block",
        pattern="""لمزيد من المعلومات عن خدمة الإنترنت في المملكة العربية السعودية، يمكنك زيارة الموقع التالي""",
        location_found="body",
        source=[
            ""
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190901T044136Z_AS35819_7HmiWOJ6eNRSV5sGcKUd165APHOYJgaYheRtn5PSRRerkdjDk7?input=http://www.gay.com/",
        confidence_no_fp=9,
        scope="nat",
        expected_countries=["SA"],
        notes="National Green Saudi Blocked URL Page",
    ),

    SimpleBlockPagePattern(
        name="nat_th_deb_blockpage",
        common_name="National Thai Digital Economy Block",
        pattern="""Sorry. Access to this website has been disabled because the Ministry of Digital Economic""",
        location_found="body",
        source=[
            "https://www.voanews.com/east-asia/thai-lawmakers-approve-tighter-control-internet"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190904T062730Z_AS7470_IqwbYni159FTGxsg003mQv3LKQZAW5MefvhKkBNcfvz9Ff5FBx?input=http://www.gboysiam.com/",
        confidence_no_fp=10,
        scope="nat",
        expected_countries=["TH"],
        notes="",
    ),

    SimpleBlockPagePattern(
        name="nat_th_deb_forward_2",
        common_name="National Thai Digital Economy Block",
        pattern="""Location: http://103.86.50.16""",
        location_found="header",
        source=[
            "https://www.voanews.com/east-asia/thai-lawmakers-approve-tighter-control-internet"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190911T075509Z_AS9931_nxPKYSoZ3cDyjEkfs8kHGRW4DpctE8wJfgXMKoMOWFwER1YTD7?input=http://www.gboysiam.com/",
        confidence_no_fp=7,
        scope="nat",
        expected_countries=["TH"],
        notes="This is the IP the national Thai blockpage was in 2019",
    ),

    SimpleBlockPagePattern(
        name="nat_th_deb_forward_1",
        common_name="National Thai Digital Economy Block",
        pattern="""Location: http://103.208.24.21""",
        location_found="header",
        source=[
            "https://www.voanews.com/east-asia/thai-lawmakers-approve-tighter-control-internet"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190101T072530Z_AS7470_TWZ0f5svDKrU2gYh3tmmboIGn8iTDkRaLaZD4oZq3iuSZbBTUm?input=http://www.gboysiam.com",
        confidence_no_fp=7,
        scope="nat",
        expected_countries=["TH"],
        notes="This is the IP the national Thai blockpage was in ~2016 according to link",
    ),

    SimpleBlockPagePattern(
        name="nat_th_forward_1",
        common_name="National Thai Digital Economy Block",
        pattern="""Location: http://103.208.24.21""",
        location_found="header",
        source=[
            "https://www.voanews.com/east-asia/thai-lawmakers-approve-tighter-control-internet"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190101T072530Z_AS7470_TWZ0f5svDKrU2gYh3tmmboIGn8iTDkRaLaZD4oZq3iuSZbBTUm?input=http://www.gboysiam.com",
        confidence_no_fp=7,
        scope="nat",
        expected_countries=["TH"],
        notes="This is the IP the national Thai blockpage was in ~2016 according to link",
    ),

    SimpleBlockPagePattern(
        name="nat_th_ictprohibit_forward",
        common_name="National Thai ICT Block",
        pattern="""prohibit.ais-idc.com""",
        location_found="header",
        source=[
            "https://twitter.com/marcodavids/status/803985421516570625"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200214T212342Z_AS133481_bLNPUx39hgpO75VcUdF2V6pPXdiKoyug5hCio1HCMntxh7VaW7?input=http://www.gboysiam.com/",
        confidence_no_fp=7,
        scope="nat",
        expected_countries=["TH"],
        notes="""This is the IP the national Thai blockpage used by IDC/ICT as seen with a 30x
              to http://prohibit.ais-idc.com/prohibit.html""",
    ),

    SimpleBlockPagePattern(
        name="nat_th_ictprohibit_block",
        common_name="National Thai Digital Economy Blockpage",
        pattern="""pPGh0bWwgeG1sbnM6dj0idXJuOnNjaGVtYXMtbWljcm9zb2Z0LWNvbTp2bWwiDQp4bWxuczpvPSJ1cm46c""",
        location_found="body",
        source=[
            "https://twitter.com/marcodavids/status/803985421516570625"
        ],
        exp_url ="",
        confidence_no_fp=7,
        scope="nat",
        expected_countries=["TH"],
        notes="""This is the IP the national Thai blockpage used by IDC/ICT it has mixed encodings/base64
        so this should only match on OONI""",
    ),

    SimpleBlockPagePattern(
        name="nat_id_trustpositif_forward",
        common_name="ID TrustPositif Block",
        pattern="""internetpositif.uzone.id""",
        location_found="header",
        source=[
            "https://trustpositif.kominfo.go.id/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20180528T130640Z_AS7713_A2RVHOGPmVoYQ5U9Fe3WNCMkJcH7D2kCmPboBZDEfgt6XjE8OM?input=http://www.samesexmarriage.ca",
        confidence_no_fp=10,
        scope="nat",
        expected_countries=["ID"],
        notes="Trust/Internet Positif is a DNS blacklist distributed by the Telecom regulator in Indonesia as a part of the Internet Sehat program",
    ),

    SimpleBlockPagePattern(
        name="nat_id_trustpositif_forward_2",
        common_name="ID TrustPositif Block",
        pattern="""window.location.replace("http://internetpositif.uzone.id/""",
        location_found="body",
        source=[
            "https://trustpositif.kominfo.go.id/",
            "https://explorer.ooni.org/measurement/20171025T095349Z_AS131709_vvCnDreaVjMN1MQ2imNyl4ynBG4EhIZRdWHJIBKgOexJSnaWcb?input=http://www.ifge.org"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20180528T130640Z_AS7713_A2RVHOGPmVoYQ5U9Fe3WNCMkJcH7D2kCmPboBZDEfgt6XjE8OM?input=http://www.samesexmarriage.ca",
        confidence_no_fp=10,
        scope="nat",
        expected_countries=["ID"],
        notes="""Trust/Internet Positif is a DNS blacklist distributed by the Telecom regulator in Indonesia as a part of the Internet Sehat program
        This catches the variant that does a window.replace in the data returned to get to the block page.
        """,
    ),

    SimpleBlockPagePattern(
        name="nat_id_trustpositif_forward_3",
        common_name="ID TrustPositif Block",
        pattern="""mercusuar.uzone.id""",
        location_found="header",
        source=[
            "https://trustpositif.kominfo.go.id/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20200312T024737Z_AS45292_QGO96hC1JiPt1T30OH3q4EXyCDfE8D3c4cjGqalbffrgJCrbe9?input=http://ilga.org/",
        confidence_no_fp=10,
        scope="nat",
        expected_countries=["ID"],
        notes="""Trust/Internet Positif is a DNS blacklist distributed by the Telecom regulator in Indonesia as a part of the Internet Sehat program.
        Mercusuar is a branding put of this under the Telkom brand.""",
    ),

    SimpleBlockPagePattern(
        name="nat_id_trustpositif_block_1",
        common_name="ID TrustPositif Block",
        pattern="""http://block.uzone.id""",
        location_found="body",
        source=[
            "https://trustpositif.kominfo.go.id/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200213T053902Z_AS17974_igK3SmCYSdqnVjV2OxZ1VCUnsaECgo8Dh7S6CfU0AQgWg5nPQU?input=http://www.queernet.org/",
        confidence_no_fp=10,
        scope="nat",
        expected_countries=["ID"],
        notes="Trust/Internet Positif is a DNS blacklist distributed by the Telecom regulator in Indonesia as a part of the Internet Sehat program",
    ),

    SimpleBlockPagePattern(
        name="nat_id_trustpositif_block_2",
        common_name="ID TrustPositif Block",
        pattern=""".uzone.id/assets/internetpositif""",
        location_found="body",
        source=[
            "https://trustpositif.kominfo.go.id/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20170414T032645Z_AS17974_Qho7Y39z1oG2s1ylGbQvoFuQh8aDDnY2OwhXMVkqmyBPwQjmT5?input=http://www.bglad.com",
        confidence_no_fp=10,
        scope="nat",
        expected_countries=["ID"],
        notes="Trust/Internet Positif is a DNS blacklist distributed by the Telecom regulator in Indonesia as a part of the Internet Sehat program.",
    ),

    SimpleBlockPagePattern(
        name="nat_id_trustpositif_block_3",
        common_name="ID TrustPositif Block",
        pattern="""positif.uzone.id""",
        location_found="body",
        source=[
            "https://trustpositif.kominfo.go.id/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20171121T103829Z_AS17974_QgZkCjksBNucHe11XDLxKXIC3MTW32OamXngJCJrLaoouWNoEM?input=http://www.ifge.org",
        confidence_no_fp=10,
        scope="nat",
        expected_countries=["ID"],
        notes="Trust/Internet Positif is a DNS blacklist distributed by the Telecom regulator in Indonesia as a part of the Internet Sehat program.",
    ),

    SimpleBlockPagePattern(
        name="nat_id_trustpositif_block_4",
        common_name="ID TrustPositif Block",
        pattern="""UA-16251743-3""",
        location_found="body",
        source=[
            "https://trustpositif.kominfo.go.id/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20181005T025940Z_AS0_j9Q9C7qnBZAdAtoiStJMgBFCSjmGxSNkXU6UNjfx2xeIxoIVtd?input=http://www.gayscape.com",
        confidence_no_fp=10,
        scope="nat",
        expected_countries=["ID"],
        notes="""Trust/Internet Positif is a DNS blacklist distributed by the Telecom regulator in Indonesia as a part of the Internet Sehat program.
        This is based on the analytics code used on the page as observed in 2018.""",
    ),

    SimpleBlockPagePattern(
        name="nat_id_trustpositif_block_5",
        common_name="ID TrustPositif Block",
        pattern="""This page is blocked by <a href=http://trustpositif.kominfo.go.id""",
        location_found="body",
        source=[
            "https://trustpositif.kominfo.go.id/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20190314T214950Z_AS17658_kybYxwcXIxWZYnX32z36B1ZprSLxFT3WpxY0g7sfuy0Uy7MLAo?input=http://www.samesexmarriage.ca/",
        confidence_no_fp=10,
        scope="nat",
        expected_countries=["ID"],
        notes="""Trust/Internet Positif is a DNS blacklist distributed by the Telecom regulator in Indonesia as a part of the Internet Sehat program.
        This is based on the block message.""",
    ),

    SimpleBlockPagePattern(
        name="nat_id_trustpositif_block_6",
        common_name="ID TrustPositif Block",
        pattern="""<title>Mercusuar</title>""",
        location_found="body",
        source=[
            "https://trustpositif.kominfo.go.id/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20200312T024737Z_AS45292_QGO96hC1JiPt1T30OH3q4EXyCDfE8D3c4cjGqalbffrgJCrbe9?input=http://ilga.org/",
        confidence_no_fp=10,
        scope="nat",
        expected_countries=["ID"],
        notes="""Trust/Internet Positif is a DNS blacklist distributed by the Telecom regulator in Indonesia as a part of the Internet Sehat program.
        Mercusuar is a branding put of this under the Telkom brand.""",
    ),

    SimpleBlockPagePattern(
        name="nat_id_idnic_block",
        common_name="ID NIC Block",
        pattern="""di.og.ofnimok@netnoknauda""",
        location_found="body",
        source=[
            "https://www.idnic.id/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20200130T121354Z_AS18103_6roxhkcpVP4ML3VyjL75G28deYvsJgocbDyeV8Ud6WBHAFTwy4?input=http://www.grindr.com/",
        confidence_no_fp=10,
        scope="nat",
        expected_countries=["ID"],
        notes="""Indonesian NIC block. Based on weird localnet email used in the HTML.""",
    ),

    SimpleBlockPagePattern(
        name="nat_qa_block_forward_accessurl",
        common_name="National Qatari Blockpage",
        pattern="""censor.qa/?accessurl=""",
        location_found="body",
        source=[
            ""
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200101T185215Z_AS42298_Si7iYR3b37Ai654IPgzQUSdRE2HnLKbi8ubdiwvzvGQ0mnWDDF?input=http://www.grindr.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["QA"],
        notes="""National Qatari Blockapge (censor.qa) typically seen as a 200 that has an iframe, this matches
        the access url device.
        """,
    ),

    SimpleBlockPagePattern(
        name="nat_qa_block_forward_netsweeper",
        common_name="National Qatari Blockpage",
        pattern="""censor.qa/?dpid=""",
        location_found="body",
        source=[
            ""
        ],
        exp_url ="https://explorer.ooni.org/measurement/20170215T050956Z_AS8781_ArhSFkwQmwTTc46EA5E5GVIK0a85TdbngwJJ3B3wRZ9kZVy060?input=http://gayromeo.com",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["QA"],
        notes="""National Qatari Blockapge (censor.qa) typically seen as a 200 that has an iframe, this matches the
              Netsweeper variant""",
    ),

    SimpleBlockPagePattern(
        name="nat_om_block_blockom_forward",
        common_name="National Omani Blockpage",
        pattern="""block.om/newrequestform.aspx?accessurl=""",
        location_found="body",
        source=[
            ""
        ],
        exp_url ="https://explorer.ooni.org/measurement/20171008T164257Z_AS28885_x73TSE1uoiU8cTEo0NxxBkjRfV1tHOYoQplxDvNTGzxi9vkKIY?input=http://www.gayscape.com",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["OM"],
        notes="""
            National Omani Blockapge typically seen as a 200 that has an iframe.  This is for block.om variant
        """,
    ),

    SimpleBlockPagePattern(
        name="nat_om_block_siteblockedom_forward",
        common_name="National Omani Blockpage",
        pattern="""http://siteblocked.om/?accessurl=""",
        location_found="body",
        source=[
            ""
        ],
        exp_url ="https://explorer.ooni.org/measurement/20170215T210727Z_AS50010_aOkarIhF1xmYR53lpC4iy45St2E0yB25zVr7rpqi39tNNHgKnL?input=http://www.scruff.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["OM"],
        notes="""
            National Omani Blockapge typically seen as a 200 that has an iframe.  This is for siteblocked.om variant
        """,
    ),

    # This website is not available in Malaysia as it violate(s)

    SimpleBlockPagePattern(
        name="nat_my_violates",
        common_name="National Malaysian Blockpage",
        pattern="""This website is not available in Malaysia as it violate(s)""",
        location_found="body",
        source=[
            ""
        ],
        exp_url="https://explorer.ooni.org/measurement/20190510T024428Z_AS4788_39J7OiJ5VtjhP2aZ9tYooWikE9aI5pTQvCdRVwA6KiBazotDUw?input=http://www.gaystarnews.com/",
        confidence_no_fp=10,
        scope="nat",
        expected_countries=["MY"],
        notes="""
        National Malaysian legal block
        """,
    ),

    #   http://siteblocked.om/?accessurl=

    # Product Identifying Patterns

    SimpleBlockPagePattern(
        name="prod_wirefilter",
        common_name="WireFilter",
        pattern="Protected by WireFilter",
        location_found="header",
        source=[
            ""
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200214T180921Z_AS35819_INXiu6FqyTRS0cTO8wF5nLUHtCZZIw35rfGmsrSBnD7CeNDodJ?input=http://www.samesexmarriage.ca/",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=["SA", "AE"],
        notes="Saudi Product WireFilter commonly adds this to headers.",
    ),

    SimpleBlockPagePattern(
        name="prod_nawala",
        common_name="Nawala",
        pattern="UA-36449470-1",
        location_found="body",
        source=[
            "https://nawala.id/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20170214T023529Z_AS17974_1hVbJGBPLdOsxQvNgIawwvABxfZuLNeVK5VaY1XWajguEt0yK3?input=http://www.lesbian.org",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=["ID"],
        notes="DNS filtering blacklist promoted by government of Indonesia. This is for the blockpage and matches on analytics code used.",
    ),

    SimpleBlockPagePattern(
        name="prod_netsweeper_inject",
        common_name="Netsweeper",
        pattern="?dpid=",
        location_found="header",
        source=[
            ""
        ],
        exp_url ="https://explorer.ooni.org/measurement/20191118T063541Z_AS15802_ocKS0RbSg8GE1oLahQKYeAozvsxM3HglG8f3xMRkrWVOd4ajtN?input=http://gayguide.net/",
        confidence_no_fp=6,
        scope="prod",
        expected_countries=[],
        notes="Netsweeper Injections typically encode deny pages as ?dpid= followed by num ",
    ),

    SimpleBlockPagePattern(
        name="prod_netsweeper_inject_2",
        common_name="Netsweeper",
        pattern="/webadmin/deny/",
        location_found="body",
        source=[
            ""
        ],
        exp_url ="https://explorer.ooni.org/measurement/20181208T133424Z_AS42961_V48ENKhCXwvMW9BsnGKb4mC2p8PoOJRBI9kbF3t4lC5puLcXE2?input=http://www.gayegypt.com",
        confidence_no_fp=6,
        scope="prod",
        expected_countries=[],
        notes="Netsweeper Injections can also be done via an inject of an HTTP 200 response with an iframe this has the format of http[s]://IP/webadmin/deny/ ",
    ),

    SimpleBlockPagePattern(
        name="prod_netsweeper_inject_3",
        common_name="Netsweeper",
        pattern="&dpruleid=",
        location_found="body",
        source=[
            ""
        ],
        exp_url ="https://explorer.ooni.org/measurement/20191110T160527Z_AS5416_pFas5trZrCCcqh7gCCLDMWpQyeO69lz7MvuHOUgvD3GyRxrU9P?input=http://gaytoday.com/",
        confidence_no_fp=6,
        scope="prod",
        expected_countries=[],
        notes="""Netsweeper Injections can also be done via an inject of an HTTP 200 response with an iframe this has the format of http[s]://IP/webadmin/deny/
              This matches the common dprulid param. """,
    ),

    SimpleBlockPagePattern(
        name="prod_netsweeper_blockpage",
        common_name="Netsweeper",
        pattern="poweredbynetsweeper.com",
        location_found="body",
        source=[
            ""
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190408T151922Z_AS2572_zYBghMNvqHWjkWVXx7dPjjiB3pXaJC4Je8SThdzF5zTEUZT7Lr?input=http://www.bglad.com/",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=[],
        notes="Netsweeper Powered By URL",
    ),

    SimpleBlockPagePattern(
        name="prod_fortiguard_webfilter_blocktext",
        common_name="Fortinet Fortiguard",
        pattern="You have tried to access a web page which is in violation of your internet usage policy.",
        location_found="body",
        source=[
            "https://forum.fortinet.com/tm.aspx?m=107704"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200213T165957Z_AS31242_dOxoMkg9lZqvXsFm9088Fywi7WcFyRSGpq8fHB3PYfDo1FUFtD?input=http://www.amnestyusa.org/the-state-of-lgbt-rights-worldwide/",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=[],
        notes="Fortguard is a web filtering middlebox commonly used in the institutional space, this matches the common block text",
    ),

    SimpleBlockPagePattern(
        name="prod_fortiguard_webfilter_poweredby",
        common_name="Fortinet Fortiguard",
        pattern="Powered By FortiGuard",
        location_found="body",
        source=[
            "https://forum.fortinet.com/tm.aspx?m=107704"
        ],
        exp_url ="prod_fortiguard_webfilter_poweredby",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=[],
        notes="Fortguard is a web filtering middlebox commonly used in the institutional space, this matches the power by fortiguard text",
    ),

    SimpleBlockPagePattern(
        name="prod_fortiguard_webfilter_blockurl",
        common_name="Fortinet Fortiguard",
        pattern=":8008/XX/YY/ZZ/CI/MGPGHGPGPFGHCDPFGGOGFGEH",
        location_found="body",
        source=[
            "https://forum.fortinet.com/tm.aspx?m=107704"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200213T073834Z_AS24863_yfzKDaLHODIsPqFCit6OJvwpGEBKF7HzG1zv2DWuDHJ7DK5XBw?input=http://www.well.com/",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=[],
        notes="Fortguard is a web filtering middlebox commonly used in the institutional space, this matches the pass through url",
    ),

    SimpleBlockPagePattern(
        name="prod_paloaltonetworks_forward",
        common_name="Palo Alto Networks Filtering",
        pattern="/php/urlblock.php?args=",
        location_found="header",
        source=[
            "https://knowledgebase.paloaltonetworks.com/KCSArticleDetail?id=kA10g000000ClsQCAS",
            "https://knowledgebase.paloaltonetworks.com/KCSArticleDetail?id=kA10g000000ClXtCAK"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20191104T185520Z_AS2381_aXMx8fZVBM5t27IvVAQGscDgnoJZyhesum6rKk2zqfj25oks4m?input=http://www.gay.com/",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=[],
        notes="Palo Alto Networks typically forwards to url: http(s)://IP/php/urlblock.php?args=",
    ),

    SimpleBlockPagePattern(
        name="prod_paloaltonetworks_block",
        common_name="Palo Alto Networks Filtering",
        pattern="Access to the web page you were trying to visit has been blocked in accordance with company policy.",
        location_found="body",
        source=[
            "https://knowledgebase.paloaltonetworks.com/KCSArticleDetail?id=kA10g000000ClsQCAS",
            "https://knowledgebase.paloaltonetworks.com/KCSArticleDetail?id=kA10g000000ClXtCAK"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20191104T140958Z_AS8551_3ClYxxNcVYkL21ReDyEXSXYWJzjZgVSGcpycmucSI1MIBq3uDp?input=http://gaytoday.com/",
        confidence_no_fp=8,
        scope="prod",
        expected_countries=[],
        notes="Palo Alto Networks default blockpage text - common filtering middlebox used in institutions",
    ),

    SimpleBlockPagePattern(
        name="prod_netspark_familyfilter",
        common_name="Netspark",
        pattern="http://mobile.netsparkmobile.com/?a=block",
        location_found="body",
        source=[
            "https://www.netsparkmobile.com/en/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190820T203403Z_AS199391_BKc62QxMlSz5esuRV2hHpMsUArF7fTeaeRAc8eN0Eb2uE4NVtV?input=http://www.ifge.org/",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=["IL"],
        notes="Family oriented blocking service sold to companies, used by Israeli schools",
    ),

    SimpleBlockPagePattern(
        name="prod_contentkeeper",
        common_name="ContentKeeper",
        pattern="Blocked by ContentKeeper",
        location_found="body",
        source=[
            "https://www.contentkeeper.com/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190727T072541Z_AS132909_MpSZSKk7KLUGwYzXlP6Q1BTllFuPXmFxAZjvUyZrOYjJa6RlVD?input=http://gaytoday.com/",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=["IL"],
        notes="Blocking service used in schools",
    ),

    SimpleBlockPagePattern(
        name="prod_ciscomeraki_filter_block",
        common_name="Cisco Meraki",
        pattern="This website is blocked by your network operator.",
        location_found="body",
        source=[
            "https://community.meraki.com/t5/Security-SD-WAN/Content-Filtering-Categories-with-exclusions/td-p/6543"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200113T170919Z_AS7992_Vsui789aT1BOO3UARTvMcsAdnipGL8ywQQ10GD5iW9COO7QwQw?input=http://www.gayscape.com/",
        confidence_no_fp=7,
        scope="prod",
        expected_countries=[""],
        notes="Cisco Meraki Content Filter The Blockpage",
    ),

    SimpleBlockPagePattern(
        name="prod_ciscomeraki_filter_forward",
        common_name="Cisco Meraki",
        pattern="http://wired.meraki.com:8090/blocked.cgi",
        location_found="header",
        source=[
            "https://community.meraki.com/t5/Security-SD-WAN/Content-Filtering-Categories-with-exclusions/td-p/6543"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20191207T201222Z_AS701_g1N8na12mnYVLDYH7o0fxRvHhOmRKyqU1QInZvOSp0P7Xiv7gB?input=http://www.gayscape.com/",
        confidence_no_fp=8,
        scope="prod",
        expected_countries=[""],
        notes="Cisco Meraki Content Filter Forward",
    ),

    SimpleBlockPagePattern(
        name="prod_cisco_opendns_forward",
        common_name="Cisco OpenDNS/Umbrella",
        pattern=".opendns.com/",
        location_found="header",
        source=[
            "https://support.opendns.com/hc/en-us/community/posts/220031687-Torrents-and-OpenDNS"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20180729T214053Z_AS22773_Mdk9rhM8xnJULGR1IR0yleS5X8xJfKYwLdJFrs2MxCIsSLwkeJ?input=http://www.gayscape.com",
        confidence_no_fp=8,
        scope="prod",
        expected_countries=[""],
        notes="Cisco OpenDNS Content Filter Forward (subdomain can be customized)",
    ),

    SimpleBlockPagePattern(
        name="prod_cisco_opendns_forward_2",
        common_name="Cisco OpenDNS/Umbrella",
        pattern="https://block.opendns.com/?url=",
        location_found="body",
        source=[
            "https://support.opendns.com/hc/en-us/community/posts/220031687-Torrents-and-OpenDNS"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200212T140553Z_AS25180_vR9Si2WPkIOLANW08uIay7ikEhrMEZQOYsrlcbfdoyqSQdhgDw?input=http://www.glil.org/",
        confidence_no_fp=8,
        scope="prod",
        expected_countries=[""],
        notes="Cisco OpenDNS Content Filter Blockpage (also Cisco Umbrella). This captures the window.replace forward",
    ),

    SimpleBlockPagePattern(
        name="prod_cisco_opendns_block_1",
        common_name="Cisco OpenDNS/Umbrella",
        pattern="This site is blocked due to content filtering.",
        location_found="body",
        source=[
            "https://support.opendns.com/hc/en-us/community/posts/220031687-Torrents-and-OpenDNS"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20191007T155258Z_AS20115_DS8uyNobQ0CH9o9fls70ftC1ItOJ7dK5OlMG3YBs7NYrIXQ2Ty?input=http://transsexual.org/",
        confidence_no_fp=8,
        scope="prod",
        expected_countries=[""],
        notes="Cisco OpenDNS Content Filter Blockpage (also Cisco Umbrella)",
    ),

    SimpleBlockPagePattern(
        name="prod_opendns_block_2",
        common_name="Cisco OpenDNS/Umbrella",
        pattern="""This domain is blocked due to content filtering.""",
        location_found="body",
        source=[
            "https://support.opendns.com/hc/en-us/community/posts/220047187-OpenDNS-suddenly-blocks-sites-after-a-few-days-of-use"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180401T092328Z_AS25019_Fwt7OWzgSX5bgt4fU2uwLnIfAlQrSkXHIrgk0NaMktVUkMsJCC?input=http://www.gayegypt.com",
        confidence_no_fp=8,
        scope="prod",
        expected_countries=[""],
        notes="Matches default block page text for an OpenDNS blockpage. Lower fp value due to wording based pattern.",
    ),

    SimpleBlockPagePattern(
        name="prod_juniper_webfilter",
        common_name="Juniper Web Filtering",
        pattern="Juniper Web Filtering",
        location_found="body",
        source=[
            "https://www.juniper.net/documentation/en_US/src4.9/information-products/topic-collections/services-policies/book-services-policies.pdf"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20191128T071619Z_AS30844_j5az7WIvAuc0VHR60QoTNWGVAqciBLQKuzbzodGeFWn6McCt6N?input=http://www.planetromeo.com/",
        confidence_no_fp=8,
        scope="prod",
        expected_countries=[""],
        notes="Juniper Web Filter",
    ),

    SimpleBlockPagePattern(
        name="prod_forcepoint_websense_forward",
        common_name="Forcepoint Websense",
        pattern=":15871/cgi-bin/blockpage.cgi",
        location_found="header",
        source=[
            "https://www.websense.com/content/support/library/web/v77/ws_faq/wsfaq_blockpages.aspx"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190913T145843Z_AS786_MVKkIkzY2jFPMlH7ZCG093OubMBNJwKxJq4OAek0kdw0Z2p2oy?input=http://www.grindr.com/",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=[""],
        notes="This matches on Forcepoint Websense filtering forward, the block page is usually customized",
    ),

    SimpleBlockPagePattern(
        name="prod_forcepoint_websense_blockpage",
        common_name="Forcepoint Websense",
        pattern=":15871/cgi-bin/blockpage.cgi",
        location_found="body",
        source=[
            "https://www.websense.com/content/support/library/web/v77/ws_faq/wsfaq_blockpages.aspx"
        ],
        exp_url ="",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=[""],
        notes="This matches on Forcepoint Websense filtering block page, as it has an anload of this 15871 port cgi",
    ),

    SimpleBlockPagePattern(
        name="prod_forcepoint_websense_blockpage_2",
        common_name="Forcepoint Websense",
        pattern=":15871/cgi-bin/block_message.cgi",
        location_found="body",
        source=[
            "https://www.websense.com/content/support/library/web/v77/ws_faq/wsfaq_blockpages.aspx"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200204T114540Z_AS5619_LcwP0ODKUovrjaf3xYK8i2VnBx9XSNHa6Jdo1Em2g5NUcKmNDv?input=http://www.gayegypt.com/",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=[""],
        notes="This matches on Forcepoint Websense filtering block page, it is a variant that is observed block_message.cgi vs blockpage.cgi",
    ),

    SimpleBlockPagePattern(
        name="prod_checkpoint_urlfilter_forward",
        common_name="CheckPoint URL Filtering",
        pattern="/UserCheck/PortalMain?IID=",
        location_found="header",
        source=[
            "https://www.checkpoint.com/products/url-filtering-software-blade/",
            "https://sc1.checkpoint.com/documents/R76/CP_R76_AppControl_WebAdmin/83287.htm"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20180818T200128Z_AS4760_TDbPbBLoW8PxHn3FBNwwWBvR37pnyiJF99qrbqE50tLSgigSQl?input=http://www.bglad.com",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=[""],
        notes="CheckPoint URL filtering typically fowards to http://<IP>/UserCheck/PortalMain?IID=<something>&origUrl=<something>",
    ),

    SimpleBlockPagePattern(
        name="prod_checkpoint_urlfilter_blockpage",
        common_name="CheckPoint URL Filtering",
        pattern="Check Point UserCheck",
        location_found="body",
        source=[
            "https://www.checkpoint.com/products/url-filtering-software-blade/",
            "https://sc1.checkpoint.com/documents/R76/CP_R76_AppControl_WebAdmin/83287.htm"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190103T083125Z_AS378_YGjxy3hs0CJ7KNbCqT28ZyNH7IHFuHEEyJ9kdfdQz2vemBJBLZ?input=http://www.gayegypt.com",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=[""],
        notes="CheckPoint URL Filtering features are typically under the UserCheck Brand",
    ),

    SimpleBlockPagePattern(
        name="prod_lightspeed_filter_blockpage",
        common_name="Lightspeed Systems Filter",
        pattern="<title>Lightspeed System - Web Access</title>",
        location_found="body",
        source=[
            "https://www.lightspeedsystems.com/filter/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20191002T174831Z_AS26670_EWuOb35WpxA8HL2UGPAqCD6UPl0BnOhvwgeU87jmQVPsWSZljC?input=http://www.gay.com/",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=[""],
        notes="Web filtering device marketed for the education market.",
    ),

    SimpleBlockPagePattern(
        name="prod_lightspeed_filter_forward",
        common_name="Lightspeed Systems Filter",
        pattern="/access?",
        location_found="header",
        source=[
            "https://www.lightspeedsystems.com/filter/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190910T184643Z_AS22773_zEshEFJWXK5mZcHhPlocyCVNe8uD8cWjO3Gske60DErR3N7azq?input=http://instinctmagazine.com/",
        confidence_no_fp=5,
        scope="prod",
        expected_countries=[""],
        notes="""Web filtering device marketed for the education market. This matches headers forwards in the format:
                 https://<DOMAIN>/access?<randomkey>
                 Be careful because this has a higher likilihood of a false positive given the short match pattern.
              """,
    ),

    SimpleBlockPagePattern(
        name="prod_comodo_securedns_forward",
        common_name="Comodo SecureDNS Service",
        pattern="warn.recursive.dnsbycomodo.com",
        location_found="header",
        source=[
            "https://securedns.dnsbycomodo.com/",
        ],
        exp_url="https://explorer.ooni.org/measurement/20190924T211601Z_AS6856_p2XyAY2gncrEiK23Ac5zqFDfYHF83J94NEp4fyxbKWNrGTdXBk?input=http://www.deti-404.com/",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=[""],
        notes="""
        Comodo SecureDNS is a security focused DNS filtering system.  This matches the forward where you are forwarded
        to a url in this format: http://warn.recursive.dnsbycomodo.com/?host={{url}}
        """,
    ),

    SimpleBlockPagePattern(
        name="prod_comodo_securedns_warning",
        common_name="Comodo SecureDNS Service",
        pattern="://www.comodo.com/home/internet-security/submit.php?",
        location_found="body",
        source=[
            "https://securedns.dnsbycomodo.com/",
        ],
        exp_url="https://explorer.ooni.org/measurement/20190924T211601Z_AS6856_p2XyAY2gncrEiK23Ac5zqFDfYHF83J94NEp4fyxbKWNrGTdXBk?input=http://www.deti-404.com/",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=[""],
        notes="""
        Comodo SecureDNS is a security focused DNS filtering system.  This matches the submission for recategorization 
        script call.
        """,
    ),


    SimpleBlockPagePattern(
        name="prod_bluecoat_notify_forward",
        common_name="Symantec Bluecoat User Notification",
        pattern="notify.bluecoat.com",
        location_found="header",
        source=[
            "http://notify.bluecoat.com/",
            "https://knowledge.broadcom.com/external/article/169743/notifybluecoatcom-unexpectedly-shows-up.html",
        ],
        exp_url="https://explorer.ooni.org/measurement/20181014T082454Z_AS15505_UlzScz9IQ0QBGrAg6CscMDzF2FeTJhqWXiOvcQYZGj2uFI9BD0?input=http://www.glil.org",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=[""],
        notes="""
        Symantec Bluecoat product line notifications are done via a foward to the notify.bluecoat.com domain with the 
        following parameters as an HTTP 302 to URL:
        http://notify.bluecoat.com/notify-Notify?{{requested_url}}{{url_as_base64}}
        """,
    ),

    SimpleBlockPagePattern(
        name="prod_bluecoat_notify_notification",
        common_name="Symantec Bluecoat User Notification",
        pattern="://notify.bluecoat.com",
        location_found="body",
        source=[
            "http://notify.bluecoat.com/",
            "https://knowledge.broadcom.com/external/article/169743/notifybluecoatcom-unexpectedly-shows-up.html",
        ],
        exp_url="https://explorer.ooni.org/measurement/20181014T082454Z_AS15505_UlzScz9IQ0QBGrAg6CscMDzF2FeTJhqWXiOvcQYZGj2uFI9BD0?input=http://www.glil.org",
        confidence_no_fp=8,
        scope="prod",
        expected_countries=[""],
        notes="""
        Symantec Bluecoat product line notifications are done via a foward to the notify.bluecoat.com domain with the 
        following parameters as an HTTP 302 to URL:
        http://notify.bluecoat.com/notify-Notify?{{requested_url}}{{url_as_base64}}
    """,
    ),

    SimpleBlockPagePattern(
        name="prod_squid_error_page",
        common_name="Squid Proxy",
        pattern="Stylesheet for Squid Error pages",
        location_found="body",
        source=[
            "http://www.squid-cache.org/Doc/config/err_page_stylesheet/",
            "https://github.com/sullo/nikto/issues/603",
        ],
        exp_url ="https://explorer.ooni.org/measurement/20191222T110018Z_AS8452_iDqrGOsuG3oZgbSax3PPtuzTGSPUmFtQab5L0Gizvr7nZqJZ8F?input=http://www.thegailygrind.com/",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=[""],
        notes="""
            Squid is hard to write a pattern for, as it is a common reverse and in-path proxy. Cases where an inpath
            squid proxy returns errors is a clear case of inaccessible content that should be flagged however.
        """,
    ),

    SimpleBlockPagePattern(
        name="prod_squid_error_forward",
        common_name="Squid Proxy",
        pattern="/sgerror.php?url=",
        location_found="header",
        source=[
            "http://www.squid-cache.org/Doc/config/err_page_stylesheet/",
            "https://github.com/sullo/nikto/issues/603",
        ],
        exp_url ="https://explorer.ooni.org/measurement/20191014T112153Z_AS766_i7LuwpPrUtwgjjjCNCFwsnvNv8yih3PLXE7lvAF8MyDaSC4abw?input=https://bisexual.org/",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=[""],
        notes="""
            Squid is hard to write a pattern for, as it is a common reverse and in-path proxy. Cases where an inpath
            squid proxy returns errors is a clear case of inaccessible content that should be flagged however.
        """,
    ),

    SimpleBlockPagePattern(
        name="prod_squidguard_forward",
        common_name="Squid Proxy",
        pattern="squidGuard.cgi?clientaddr=",
        location_found="header",
        source=[
            "http://www.squidguard.org/",
            "https://github.com/Distrotech/squidGuard/blob/master/samples/squidGuard.cgi.in"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190904T065601Z_AS6720_FJDttShzEsIa3mATRsC6n9K9KbJkC22VEawXxyA7BKOlVx76TR?input=http://www.gayegypt.com/",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=[""],
        notes="""
        Squid is hard to write a pattern for, as it is a common reverse and in-path proxy. SquidGuard however 
        is made for blacklist implementation and the redirector performs block requests like so :
        http://{{domain}}/squidGuard.cgi?clientaddr={{clients ip}}&clientname=&clientuser=&clientgroup=wlan&targetgroup=porn&url=http://transsexual.org/
        
        The block page can be and typically is customized from the default here:
        https://github.com/Distrotech/squidGuard/blob/master/samples/squidGuard-simple.cgi.in
    """,
    ),

    SimpleBlockPagePattern(
        name="prod_rmedufilter_forward",
        common_name="RM Education Filter",
        pattern=".ifl.net/filterpages/",
        location_found="header",
        source=[
            "https://www.rm.com/security-and-safeguarding/online-safety"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190924T111147Z_AS5503_tbltX9RU8fCAkZoJf6fhR3wC8TEukKjHbBm6pT54GZnYbFLTiL?input=http://www.glil.org/",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=[""],
        notes="""
        RM is a consultancy that provides a filtering product for schools.  This matches on a forward in the headers
        that is done into their DNS space {X}.{Y}.ifl.net/filterpages/ when we saw it it looked like this:
        http://fp.sn.ifl.net/filterpages/3390-59870.htm#f=1&c=59870&d=1&p=3396&t=145722002&u=http://www.glil.org/&ip={ip}
        """,
    ),

    SimpleBlockPagePattern(
        name="prod_rmedufilter_blockpage",
        common_name="RM Education Filter",
        pattern="www.rm.com/filteringpolicy/",
        location_found="body",
        source=[
            "https://www.rm.com/security-and-safeguarding/online-safety"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190924T111147Z_AS5503_tbltX9RU8fCAkZoJf6fhR3wC8TEukKjHbBm6pT54GZnYbFLTiL?input=http://www.glil.org/",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=[""],
        notes="""
        RM is a consultancy that provides a filtering product for schools.  This matches on the URL to re-categorize URls
        """,
    ),

    SimpleBlockPagePattern(
        name="prod_vasexperts_forward",
        common_name="VAS Experts SKAT DPI",
        pattern="vasexperts.ru",
        location_found="header",
        source=[
            "https://vasexperts.ru",
            "https://vasexperts.ru/products/skat/",
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190618T124754Z_AS31261_OrJwUWO1xCLKQWLvmRjNuRB64rxBxnjln9jPQbRP5GL5WtNbAs?input=http://www.deti-404.com/",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=["RU"],
        notes="""
            VAS Experts is a vendor of filtering gear such as SKAT DPI engine for blocking, and SORM devices for
            the Russian market.  This matches on their domain in the header.  One configuration of SKAT is to 30x
            to URL: http://vasexperts.ru/test/blocked.php
        """,
    ),

    SimpleBlockPagePattern(
        name="prod_vasexperts_blockpage_1",
        common_name="VAS Experts SKAT DPI",
        pattern="www.rm.com/filteringpolicy/",
        location_found="body",
        source=[
            "https://vasexperts.ru",
            "https://vasexperts.ru/products/skat/",
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190924T111147Z_AS5503_tbltX9RU8fCAkZoJf6fhR3wC8TEukKjHbBm6pT54GZnYbFLTiL?input=http://www.glil.org/",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=["RU"],
        notes="""
            VAS Experts is a vendor of filtering gear such as SKAT DPI engine for blocking, and SORM devices for
            the Russian market.  
        """,
    ),

    SimpleBlockPagePattern(
        name="prod_vasexperts_blockpage_2",
        common_name="VAS Experts SKAT DPI",
        pattern="mc.yandex.ru/watch/21144079",
        location_found="body",
        source=[
            "https://vasexperts.ru",
            "https://vasexperts.ru/products/skat/",
        ],
        exp_url="https://explorer.ooni.org/measurement/20180317T120401Z_AS58042_yJMJTpz2i5Qbl8JH3UfBICOMoLFILAZpNrZUxGWdDqvjKFluPF?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=["RU"],
        notes="""
            VAS Experts is a vendor of filtering gear such as SKAT DPI engine for blocking, and SORM devices for
            the Russian market.  This matches the Metrika ID embedded on the blockpage.
        """,
    ),

    SimpleBlockPagePattern(
        name="prod_iserv_blockpage",
        common_name="IServ Education Filter",
        pattern="title>IServ",
        location_found="body",
        source=[
            "https://iserv.eu/portal/zielgruppen#admin"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20191129T093025Z_AS31334_QLJPBWGVj5ZqNmPb7C3R4KQkEatrbGCQu9nVQQwgkNH4SnWxpZ?input=http://www.newnownext.com/",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=["DE"],
        notes="Web filtering product focused on German schools",
    ),

    SimpleBlockPagePattern(
        name="prod_iserv_forward",
        common_name="IServ Education Filter",
        pattern="/idesk/inet/block.php?",
        location_found="header",
        source=[
            "https://iserv.eu/portal/zielgruppen#admin"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200109T094904Z_AS31334_JILxtOIrBF8JOwG6MVY9ZGzR6hzqTAsjIjRaf4ULM4LEDVKZ6q?input=http://www.queernet.org/",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=["DE"],
        notes=""" Web filtering product focused on German schools, matches 
        forward which looks like : http://<DOMAIN>/idesk/inet/block.php?grp=<CAT>&url=<URL>""",
    ),

    SimpleBlockPagePattern(
        name="prod_olfeo",
        common_name="Olfeo Web Filter",
        pattern="Server: Olfeo",
        location_found="header",
        source=[
            "https://en.olfeo.com/en"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20181013T160011Z_AS3215_IRIYlWDvBY8FTKrWmI3C6GrvGXVEeHwibS9J9AeorEPZbKp62j?input=http://gaytoday.com",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=["FR"],
        notes="""French Web Filtering/Secure Gateway product makes itself generally known in headers""",
    ),

    SimpleBlockPagePattern(
        name="prod_gfi_kerio",
        common_name="GFI Kerio Control Firewall",
        pattern="This page has been blocked by Kerio Control",
        location_found="body",
        source=[
            "https://www.gfi.com/sites/keriocontrol/network-firewall-security"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20191104T031908Z_AS17974_a3tPUBwPAnNTdi3CZQLHiLFOVN0Uq8kPSdpPSibdW9KCgtdvkw?input=http://www.gmhc.org/",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=[""],
        notes="""Common security firewall that has a filtering function.""",
    ),

    SimpleBlockPagePattern(
        name="prod_iboss_forwardtoblock_1",
        common_name="iBoss Network Security",
        pattern="""/ibreports/ibp/bp.html""",
        location_found="header",
        source=[
            "https://www.iboss.com/",
            "https://cdn.ymaws.com/oshean.site-ym.com/resource/resmgr/Docs/ChromebookSSOSetup.pdf",
        ],
        exp_url ="https://explorer.ooni.org/measurement/20171213T191554Z_AS7018_oxpfkYyeFYy6Nem6NSDwf0MAZcVSzKHwcepGBu7k0mcMWr0wXr?input=http://www.exgay.com",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=[""],
        notes="""Filtering product common in US schools and instititions. Matches forwards to ibreport (iboss reports)
                ex : http<s>://<IP<:8080/ibreports/ibp/bp.html?<vars such as url and block text etc> 
              """
    ),

    SimpleBlockPagePattern(
        name="prod_iboss_forwardtoblock_2",
        common_name="iBoss Network Security",
        pattern="""/block/restricted.html?fn=""",
        location_found="header",
        source=[
            "https://www.iboss.com/",
            "https://cdn.ymaws.com/oshean.site-ym.com/resource/resmgr/Docs/ChromebookSSOSetup.pdf",
        ],
        exp_url ="https://explorer.ooni.org/measurement/20171215T185429Z_AS393581_Oc1mYR1Bb4Y5lucLnjaHx8IWSGQKaoXS8ZkjAllz2edhoi1Ws9?input=http://www.grindr.com/",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=[""],
        notes="""Filtering product common in US schools and instititions. Matches forwards to iphantom blockpages (typically cloud hosted installs)
                ex : http://cb.iphantom.com/block/restricted.html?fn=<rest of vars>
              """
    ),

    SimpleBlockPagePattern(
        name="prod_iboss_forwardtoblock_3",
        common_name="iBoss Network Security",
        pattern="""/iboss/restricted.html?fn=""",
        location_found="header",
        source=[
            "https://www.iboss.com/",
            "https://cdn.ymaws.com/oshean.site-ym.com/resource/resmgr/Docs/ChromebookSSOSetup.pdf",
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190918T230042Z_AS21708_5wdGu7Cip7EyLbtj04ib7AKskc55eMULSHHIataglrzFskaXw0?input=http://www.bglad.com/",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=[""],
        notes="""Filtering product common in US schools and instititions. Matches forwards to blockpages of this format:
            ex : http://<IP OR DOMAIN>/iboss/restricted.html?<rest of vars>
          """
    ),

    SimpleBlockPagePattern(
        name="prod_iboss_iphantom_block",
        common_name="iBoss Network Security",
        pattern="""Access to the requested site has been restricted due to its contents.""",
        location_found="body",
        source=[
            "https://www.iboss.com/",
            "https://cdn.ymaws.com/oshean.site-ym.com/resource/resmgr/Docs/ChromebookSSOSetup.pdf",
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190425T101718Z_AS4755_lTV8BFhpJGAOPCGQhytFAufitQEalqKY3A0opg4R48vtk9JSSv?input=http://www.queernet.org/",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=[""],
        notes="""Filtering product common in US schools and instititions. Matches forwards to iphantom blockpages (typically cloud hosted installs)
            matches text on block page
          """
    ),

    SimpleBlockPagePattern(
        name="prod_sonicwall_cfc",
        common_name="Sonicwall Client Filter",
        pattern="""://cfssupport.sonicwall.com""",
        location_found="body",
        source=[
            "https://www.sonicwall.com/products/firewalls/security-services/content-filtering-client/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190530T060325Z_AS9930_aFIp6ijOM0HCyMp1Zo0BA01CHkisHlohZcn9WmB3R43ijK8LYt?input=http://www.gayrice.com/",
        confidence_no_fp=8,
        scope="prod",
        expected_countries=[""],
        notes="Sonicwall Client Filter Blockpage",
    ),


    SimpleBlockPagePattern(
        name="prod_zscaler_forward_1",
        common_name="ZScaler Internet Security",
        pattern="""://gateway.zscaler.net""",
        location_found="header",
        source=[
            "https://www.zscaler.com/solutions/web-security"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20180122T201538Z_AS22616_uLviWLsbTKGig4oiZFlS9Xz7VeSaMX2G4Tggg9MU7yflA1WQDt?input=http://lgbt.foundation/",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=[""],
        notes="ZScaler Internet Security Filtering, matches forward to cloud hosted block page at gateway.zscaler.net",
    ),

    SimpleBlockPagePattern(
        name="prod_zscaler_forward_2",
        common_name="ZScaler Internet Security",
        pattern="""://gateway.zscalertwo.net""",
        location_found="header",
        source=[
            "https://www.zscaler.com/solutions/web-security"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20180309T161700Z_AS22616_Ezy0LpcYa4OKlZeXQlAFLnoK0TR9Ezj6tqXXN86cCiJvytE2rf?input=http://www.gayscape.com",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=[""],
        notes="ZScaler Internet Security Filtering, matches forward to cloud hosted block page at gateway.zscalertwo.net",
    ),

    SimpleBlockPagePattern(
        name="prod_zscaler_block",
        common_name="ZScaler Internet Security",
        pattern="""Internet Security by Zscaler""",
        location_found="body",
        source=[
            "https://www.zscaler.com/solutions/web-security"
        ],
        exp_url ="",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=[""],
        notes="ZScaler Internet Security Filtering, matches blockpage title",
    ),

    SimpleBlockPagePattern(
        name="prod_untangle_forward",
        common_name="Untangle Web Filter",
        pattern="""web-filter/blockpage?""",
        location_found="header",
        source=[
            "https://forums.untangle.com/tips-tricks/40122-customise-untangle-block-messages-users.html",
            "https://forums.untangle.com/web-monitor/29591-problems-web-filter.html",
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200105T111900Z_AS60045_yvYmENVuUcOj3ihDAatweKpOZp8aFhloYnrM8XRr9xUgHafPhH?input=http://www.bglad.com/",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=[""],
        notes="Forward is typically a 307 to IP: http(s)://IP/web-filter/blockpage?nonce=",
    ),

    SimpleBlockPagePattern(
        name="prod_untangle_block",
        common_name="Untangle Web Filter",
        pattern="""This web page is blocked</b> because it violates network policy.""",
        location_found="body",
        source=[
            "https://forums.untangle.com/tips-tricks/40122-customise-untangle-block-messages-users.html",
            "https://forums.untangle.com/web-monitor/29591-problems-web-filter.html",
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200105T111900Z_AS60045_yvYmENVuUcOj3ihDAatweKpOZp8aFhloYnrM8XRr9xUgHafPhH?input=http://www.gayscape.com/",
        confidence_no_fp=10,
        scope="prod",
        expected_countries=[""],
        notes="Matches default block page text for untangle.",
    ),

    # ISP Level Blockpage Patterns

    SimpleBlockPagePattern(
        name="isp_ae_du_surfsafely_forward_1",
        common_name="UAE ISP du Block",
        pattern="""index2.php?ucat=""",
        location_found="header",
        source=[
            "https://www.du.ae/personal"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20191118T063541Z_AS15802_ocKS0RbSg8GE1oLahQKYeAozvsxM3HglG8f3xMRkrWVOd4ajtN?input=http://gayguide.net/",
        confidence_no_fp=8,
        scope="isp",
        expected_countries=["AE"],
        notes="UAE ISP Du Surf Safely does an intermediate forward to Location: index2.php?ucat=&<something>&uref=<base64 encoded url>=",
    ),

    SimpleBlockPagePattern(
        name="isp_ae_du_surfsafely_forward_2",
        common_name="UAE ISP du Block",
        pattern="""lighthouse.du.ae""",
        location_found="header",
        source=[
            "https://www.du.ae/personal"
        ],
        exp_url="https://explorer.ooni.org/measurement/20171105T032733Z_AS15802_HaY0S8nTvD8xcK50zBOzcdDFCLiqhjVRFAFhPnUowVNv582Tp6?input=http://amygoodloe.com/lesbian-dot-org/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["AE"],
        notes="UAE ISP Du Surf Safely does an intermediate forward to Location: http://lighthouse.du.ae?dpid=X&dpruleid=X&cat=X&dplanguage=-&url=X (netsweeper)",
    ),

    SimpleBlockPagePattern(
        name="isp_ae_du_surfsafely_block_1",
        common_name="UAE ISP du Block",
        pattern="""lighthouse.du.ae""",
        location_found="body",
        source=[
            "https://www.du.ae/personal"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200127T092537Z_AS15802_GvFE8kAEn7C40Sq0vlu5OUmUxAP89DajF7LRzqs51Bl8eztjip?input=http://www.gayscape.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["AE"],
        notes="UAE ISP Du Surf Safely Blockpage matches on lighthouse domain used in body",
    ),

    SimpleBlockPagePattern(
        name="isp_ae_du_surfsafely_block_2",
        common_name="UAE ISP du Block",
        pattern="""UA-102574946-1""",
        location_found="body",
        source=[
            "https://www.du.ae/personal"
        ],
        exp_url="https://explorer.ooni.org/measurement/20171105T032733Z_AS15802_HaY0S8nTvD8xcK50zBOzcdDFCLiqhjVRFAFhPnUowVNv582Tp6?input=http://amygoodloe.com/lesbian-dot-org/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["AE"],
        notes="UAE ISP Du Surf Safely Blockpage matches on analytics code used in blockpage.",
    ),

    SimpleBlockPagePattern(
        name="isp_ae_etisalat_block",
        common_name="UAE ISP Etisalat Block",
        pattern="""iframe src="http://proxy.etisalat.ae/""",
        location_found="body",
        source=[
            ""
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200119T122050Z_AS5384_c3w6BLgePoeH9DLcYiH5MbgwfNujXtBUPNkMzpHmn1tdxZdn4P?input=http://www.helem.net/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["AE"],
        notes="",
    ),

    SimpleBlockPagePattern(
        name="isp_by_mts_forward",
        common_name="BY ISP MTS Block",
        pattern="""internet.mts.by/blocked/""",
        location_found="header",
        source=[
            "https://www.mts.by/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20200808T195507Z_AS25106_hY9xbufjqUKiqPI5LZJ4IqiwfGMNcaOdrtKnwCaXADPRhSOL8J?input=http://intimby.net/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["BY"],
        notes="Belarusian ISP MTS Block forward.",
    ),

    SimpleBlockPagePattern(
        name="isp_by_mts_block",
        common_name="BY ISP MTS Block",
        pattern="""https://help.mts.by/hc/ru/requests/new""",
        location_found="body",
        source=[
            "https://www.mts.by/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20200808T195507Z_AS25106_hY9xbufjqUKiqPI5LZJ4IqiwfGMNcaOdrtKnwCaXADPRhSOL8J?input=http://intimby.net/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["BY"],
        notes="Belarusian ISP MTS Block.",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_orionnet_forward",
        common_name="RU ISP Orion Net Block",
        pattern="""block.orionnet.ru""",
        location_found="header",
        source=[
            "https://orionnet.ru/krk"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180318T024825Z_AS31257_nfyc81ftqzpC3spdlHGM8z5mUCR3fhbcBZP9dTSkdidlB2eLMS?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Orionnet RKN blockpage forwarding.",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_orionnet_block",
        common_name="RU ISP Orion Net Block",
        pattern="""Орион телеком :: ДОСТУП ЗАПРЕЩЕН""",
        location_found="body",
        source=[
            "https://orionnet.ru/krk"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180318T024825Z_AS31257_nfyc81ftqzpC3spdlHGM8z5mUCR3fhbcBZP9dTSkdidlB2eLMS?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Orionnet RKN blockpage forwarding.",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_elight_forward",
        common_name="RU ISP E-Light Telecom Block",
        pattern="""site-blocked.ru""",
        location_found="header",
        source=[
            "https://goodline.info/o-kompanii/rekvizity.html"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180318T022949Z_AS39927_ixezvoybYaEp6uSlk6Ikof2tJYytEeaVyzffuGRioxHuxTJIqw?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="E-Light Telecom blockpage forwarding.",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_elight_block",
        common_name="RU ISP E-Light Telecom Block",
        pattern="""https://mc.yandex.ru/watch/43501029""",
        location_found="body",
        source=[
            "https://goodline.info/o-kompanii/rekvizity.html"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180318T022949Z_AS39927_ixezvoybYaEp6uSlk6Ikof2tJYytEeaVyzffuGRioxHuxTJIqw?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="E-Light Telecom blockpage.",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_sovatelecom_forward",
        common_name="RU ISP Sova Telecom Block",
        pattern="""://sovatelecom.ru/ZAPRET.html""",
        location_found="header",
        source=[
            "https://sovatelecom.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20200116T201205Z_AS35239_m3RIheOFkheUOKXr8r58t2OsdVEZnB54J1ib0Qt4IIqI9Pezxl?input=http://www.deti-404.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Sovatelecoms RKN blockpage",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_sovatelecom_block",
        common_name="RU ISP Sova Telecom Block",
        pattern="""mailto:support@balttelecom.net""",
        location_found="body",
        source=[
            "https://sovatelecom.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20200116T201205Z_AS35239_m3RIheOFkheUOKXr8r58t2OsdVEZnB54J1ib0Qt4IIqI9Pezxl?input=http://www.deti-404.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Sovatelecoms RKN blockpage",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_sochionline_forward",
        common_name="RU ISP Sochi Online Block",
        pattern="""denied.sochi-online.com""",
        location_found="header",
        source=[
            "https://www.sochi-online.com/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20200307T140013Z_AS48498_UUkMRFXpMpgvZ4BCtfBBKZUsh4HSJdS5lwwzktA1xXmHlx9eMI?input=http://bluesystem.info/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Sochi Onlines' RKN blockpage",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_sochionline_block",
        common_name="RU ISP Sochi Online Block",
        pattern="""://www.sochi-online.com/node/2""",
        location_found="body",
        source=[
            "https://www.sochi-online.com/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20200307T140013Z_AS48498_UUkMRFXpMpgvZ4BCtfBBKZUsh4HSJdS5lwwzktA1xXmHlx9eMI?input=http://bluesystem.info/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Sochi Onlines' RKN blockpage",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_convex_intersat_forward",
        common_name="RU ISP Convex Block",
        pattern="""block.intersat.ru""",
        location_found="header",
        source=[
            "https://www.convex.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20200109T111809Z_AS38972_nXN971LWjRPgQi8AkN52iZQwOo8SOV3VkLqvkV6NYSnDGVjWkd?input=http://www.deti-404.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Convex Russias RKN blockpage with Intersat branding",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_convex_intersat_block",
        common_name="RU ISP Convex Block",
        pattern="""Уважаемые пользователи ООО &quot;Сухой Лог Интерсат&quot;!""",
        location_found="body",
        source=[
            "https://www.convex.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20200109T111809Z_AS38972_nXN971LWjRPgQi8AkN52iZQwOo8SOV3VkLqvkV6NYSnDGVjWkd?input=http://www.deti-404.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Convex Russias RKN blockpage with Intersat branding",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_convex_rkn_foward",
        common_name="RU ISP Convex Block",
        pattern="""http://ban.convex.ru/index.html""",
        location_found="header",
        source=[
            ""
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200214T055045Z_AS5563_stIHGHbLS4sYXFhdxetRWMC8MwZ5fkkNFexjCPlCpMT1D6nOmv?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Convex Russias RKN blockpage Ural Region",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_novotelecom_forward",
        common_name="RU ISP Novotelecom Block",
        pattern="""zapret.2090000.ru""",
        location_found="header",
        source=[
            "https://2090000.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180318T070543Z_AS31200_V253RHv9hxMZJA1k3MqyQxreUHCZcXPk5ERo5oe8Dof0klN1iV?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Novotelecom RKN blockpage Forward",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_relline_forward",
        common_name="RU ISP Relline Block",
        pattern="""195.146.65.20/block.html""",
        location_found="header",
        source=[
            "http://relline.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180426T161628Z_AS0_CWEZrmlwar4W96mZVYgWNq3ICGQMGAAb9g3IJeLt1yGoYWcG34?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Relline RKN blockpage Forward",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_relline_block",
        common_name="RU ISP Relline Block",
        pattern="""<a href="http://relline.ru/" style="border:0;" title="Главная страница сайта «Реллайн»">""",
        location_found="body",
        source=[
            "http://relline.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180426T161628Z_AS0_CWEZrmlwar4W96mZVYgWNq3ICGQMGAAb9g3IJeLt1yGoYWcG34?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Relline RKN blockpage Forward",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_profintel_forward",
        common_name="RU ISP Profintel Block",
        pattern="""stat.profintel.ru/block/blacklist/""",
        location_found="header",
        source=[
            "https://www.profintel.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20200215T045010Z_AS28890_zMSKnUXeDyc2AIT0zl1JkHBLyx89vDgeFoXvi3I6iRuBA0XV1Y?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Profintel blacklist Forward",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_postltd_forward",
        common_name="RU ISP Post LTD (formerly KMV) Block",
        pattern="""blockpage.kmv.ru""",
        location_found="header",
        source=[
            "https://www.kmv.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180317T130121Z_AS12494_4BeSmhJhSVlr2II7km6x1bWG3s4UV02F1PI69cbDm85b97kMaS?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Post LTD (formerly KMV) RKN blockpage Forward",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_postltd_block",
        common_name="RU ISP Post LTD (formerly KMV) Block",
        pattern="""<title>POST Ltd &bull; Доступ ограничен</title>""",
        location_found="body",
        source=[
            "https://www.kmv.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180317T130121Z_AS12494_4BeSmhJhSVlr2II7km6x1bWG3s4UV02F1PI69cbDm85b97kMaS?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Post LTD (formerly KMV) RKN blockpage Forward",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_planeta_forward",
        common_name="RU ISP Planeta Block",
        pattern="""blacklist.planeta.tc""",
        location_found="header",
        source=[
            "https://planeta.tc/ekb"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180318T080743Z_AS12668_tteAPafZVumB1iKGUlmJj24vMNIuhsyxoTFqFbtkmxOyUjBoUW?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Planetas RKN blockpage Forward",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_planeta_block",
        common_name="RU ISP Planeta Block",
        pattern="""<h1 class="HeaderTitle">Доступ к данному ресурсу закрыт</h1>""",
        location_found="body",
        source=[
            "https://planeta.tc/ekb"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180318T080743Z_AS12668_tteAPafZVumB1iKGUlmJj24vMNIuhsyxoTFqFbtkmxOyUjBoUW?input=http://bluesystem.ru/",
        confidence_no_fp=6,
        scope="isp",
        expected_countries=["RU"],
        notes="Planetas RKN blockpage matches on a tag that links to the ISPs page.",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_ertelecom_rkn_forward",
        common_name="RU ISP Ertelecom Block",
        pattern="""http://lawfilter.ertelecom.ru""",
        location_found="header",
        source=[
            ""
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200215T045355Z_AS51035_4UK4BURzcK2cudFO8OEEki6wOVsHd8A5Ilx4IKJwITDPOQC7q7?input=http://www.deti-404.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Ertelecom Russias RKN blockpage Forward",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_ertelecom_rkn_blockpage",
        common_name="RU ISP Ertelecom Block",
        pattern="""UA-42895529-7""",
        location_found="body",
        source=[
            ""
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200215T053939Z_AS24588_8y57x6ldbe7mTws5UTFMc8DxpIGAtn65B2hhfSPoNOGC6AhjEH?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Ertelecom Russias RKN blockpage - am matching on the GoogleAnalytics UA they use",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_megamax_rkn_forward_1",
        common_name="RU ISP Megamax Block",
        pattern="""http://89.185.75.227/451/1f50893f80d6830d62765ffad7721742.html""",
        location_found="header",
        source=[
            ""
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200215T065021Z_AS39289_MA6u7UK8b8tD6lDtpsUIEUnjFOcvvQp3QMRStQcJIC4snikqu2?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Forward to Megamax Russias RKN blockpage",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_megamax_rkn_forward_2",
        common_name="RU ISP Megamax Block",
        pattern="""81.163.39.153:8080""",
        location_found="header",
        source=[
            ""
        ],
        exp_url="https://explorer.ooni.org/measurement/20200326T111113Z_AS57227_WihnDCNLJ6CX0NmZejS46ni9PWDk4eUGHCrXzDM7Rh0Wr181pi?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Forward to Megamax Russias RKN blockpage, variant on other IP",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_megamax_rkn_block",
        common_name="RU ISP Megamax Block",
        pattern="""Доступ ограничен  по решению суда или по иным основаниям, установленным законодательством Российской Федерации.""",
        location_found="body",
        source=[
            ""
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200214T055045Z_AS5563_stIHGHbLS4sYXFhdxetRWMC8MwZ5fkkNFexjCPlCpMT1D6nOmv?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Megamax Russias RKN blockpage",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_mgts_rkn_forward_1",
        common_name="RU ISP MGTS Block",
        pattern="""blocked.mgts.ru""",
        location_found="header",
        source=[
            ""
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200204T193749Z_AS25513_9Z7LP2duZHnf1I5bAjLF196Dl6aEzCaBwFXBegie524WzJ4rJj?input=http://www.deti-404.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="MGTS Russias RKN blockpage forward",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_mgts_rkn_forward_2",
        common_name="RU ISP MGTS Block",
        pattern="""block.mgts.ru""",
        location_found="header",
        source=[
            ""
        ],
        exp_url="https://explorer.ooni.org/measurement/20180314T172713Z_AS25513_JKzji9R0aZ8eAUuEplDoPGOZgZS3VxCFlnbFcyfQjTDXefoL7g?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="MGTS Russias RKN blockpage forward.  This is a different domain (block instead blocked) than _1",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_mgts_rkn_forward_3",
        common_name="RU ISP MGTS Block",
        pattern="""62.112.121.68""",
        location_found="header",
        source=[
            ""
        ],
        exp_url="https://explorer.ooni.org/measurement/20180826T070129Z_AS25513_Oc2jCi998XSfV1AccJgCanulDVWpm8PBG7tEZeiOF2nuh8FFIj?input=http://www.deti-404.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="MGTS Russias RKN blockpage forward.  This is a by IP since early versions (circa 2018) do not use the domain.",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_mgts_rkn_forward_4",
        common_name="RU ISP MGTS Block",
        pattern="""block.kf.mgts.ru""",
        location_found="header",
        source=[
            ""
        ],
        exp_url="https://explorer.ooni.org/measurement/20171125T060158Z_AS25513_qFQyEl7yxNubN8DjveszHUl8t8mfzEFKV5M1pAqpwOPoBNxxhN?input=http://www.glil.org",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="MGTS Russias blockpage forward.  This is the block page for the content filter (this might be opt-in)",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_mgts_rkn_blockpage_1",
        common_name="RU ISP MGTS Block",
        pattern="""<p><a id="toggle" href="">Узнать причину <img src="/img/down_mobile.png"></a></p>""",
        location_found="body",
        source=[
            ""
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200206T193832Z_AS48720_SlLIbMHbU6Z7Nb9HY3gISWDS0s9UKgtvS4Ec9dADxjqaPV6hrH?input=http://www.deti-404.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="MGTS Russias RKN blockpage",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_mgts_rkn_blockpage_2",
        common_name="RU ISP MGTS Block",
        pattern="""UA-12816426-25""",
        location_found="body",
        source=[
            ""
        ],
        exp_url="https://explorer.ooni.org/measurement/20180314T172713Z_AS25513_JKzji9R0aZ8eAUuEplDoPGOZgZS3VxCFlnbFcyfQjTDXefoL7g?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="MGTS Russias RKN blockpage.  This is for the block.mgts domain and matches the GA tracker.",
    ),


    SimpleBlockPagePattern(
        name="isp_ru_rinet_forward",
        common_name="RU ISP RiNet Block",
        pattern="""http://rinet.ru/blocked/index.html""",
        location_found="header",
        source=[
            ""
        ],
        exp_url="https://explorer.ooni.org/measurement/20180317T143113Z_AS8331_FwDwX6bHEgagwbGdtlaTJABMU3WwQXJOAJxLRoyvMIVnD8BPve?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP RiNets RKN blockpage forward",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_rinet_block",
        common_name="RU ISP RiNet Block",
        pattern="""http://rinet.ru/blocked/blocked_bg.png""",
        location_found="body",
        source=[
            ""
        ],
        exp_url="https://explorer.ooni.org/measurement/20180317T143113Z_AS8331_FwDwX6bHEgagwbGdtlaTJABMU3WwQXJOAJxLRoyvMIVnD8BPve?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP RiNets RKN blockpage forward",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_naukanet_forward",
        common_name="RU ISP Naukanet Block",
        pattern="""block.naukanet.ru""",
        location_found="header",
        source=[
            "https://www.naukanet.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20200318T090603Z_AS8641_sZfld8WLVRMRZ6Oa6uj23WNddUJ5zFCFLL5JCNBqorFDn1P050?input=http://www.lesbi.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Nauka Net blockpage forward",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_naukanet_block",
        common_name="RU ISP Naukanet Block",
        pattern="""перейти на сайт www.naukanet.ru""",
        location_found="body",
        source=[
            "https://www.naukanet.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20200318T090603Z_AS8641_sZfld8WLVRMRZ6Oa6uj23WNddUJ5zFCFLL5JCNBqorFDn1P050?input=http://www.lesbi.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Nauka Nnet blockpage, matches on the return to nauka net link.",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_teleseti_forward",
        common_name="RU ISP Teleseti Block",
        pattern="""www.teleseti.com/zapret/zapret-new.php""",
        location_found="header",
        source=[
            "http://www.teleseti.com/pskov/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180317T192943Z_AS15673_6rgzZxX5Dk9JVrI1x3DzM10Scuq7qtqaYD8gIatp4ByTDXjYdc?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Teleseti RKN blockpage forward",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_teleseti_block",
        common_name="RU ISP Teleseti Block",
        pattern="""yaCounter43509064""",
        location_found="body",
        source=[
            "http://www.teleseti.com/pskov/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180317T192943Z_AS15673_6rgzZxX5Dk9JVrI1x3DzM10Scuq7qtqaYD8gIatp4ByTDXjYdc?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Teleseti RKN blockpage blockpage, matches on Metrika tracer embedded on blockpage.",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_dialog_forward",
        common_name="RU ISP TIS-Dialog Block",
        pattern="""zapret-info.tis-dialog.ru""",
        location_found="header",
        source=[
            "http://www.tis-dialog.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180320T222703Z_AS31214_pCNLYmthnVmG3G3QPYDFkDkxwUmXiA0kgeNB0T285eQHwIkibU?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP TIS-Dialog RKN blockpage forward",
    ),
    
    SimpleBlockPagePattern(
        name="isp_ru_dialog_block",
        common_name="RU ISP TIS-Dialog Block",
        pattern="""Ресурс по данному адресу заблокирован :: Тис-диалог""",
        location_found="body",
        source=[
            "http://www.tis-dialog.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180320T222703Z_AS31214_pCNLYmthnVmG3G3QPYDFkDkxwUmXiA0kgeNB0T285eQHwIkibU?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP TIS-Dialog RKN blockpage blockpage, matches on title.",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_strela_block",
        common_name="RU ISP Strela Block",
        pattern="""UA-52529175-5""",
        location_found="body",
        source=[
            "https://strelatelecom.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180317T131026Z_AS56969_fW0lpqCHNlnPDeGqeaL7MEBDwiZOwKSzJHnYPs3FoVf84wCKsD?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Strela RKN blockpage",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_comfortel_forward",
        common_name="RU ISP Comfortel Block",
        pattern="""law.filter.comfortel.pro""",
        location_found="header",
        source=[
            "https://strelatelecom.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20190316T015348Z_AS44640_7b4Bz0TeF0gdXnQshAbDuk2jt6pgY4TrX0HPfom6wIZsxG9sWE?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Comfortel RKN blockpage",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_rostelcom_warning_forward",
        common_name="RU ISP Rostelecom Block",
        pattern="""http://warning.rt.ru""",
        location_found="header",
        source=[
            ""
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200214T044208Z_AS3239_1tgg2uJRbQkBKgp8uyG8ImI7Ca8w7YdzRmjI7ujcuPLf8CaTf9?input=http://www.deti-404.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Forward to Rostelcom Warning RKN page.",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_rostelcom_warning_block_1",
        common_name="RU ISP Rostelecom Block",
        pattern="""://mc.yandex.ru/watch/38740850""",
        location_found="body",
        source=[
            ""
        ],
        exp_url="https://explorer.ooni.org/measurement/20200205T210511Z_AS12389_m0Vr9g5NgqSChZXnMdMOyFNWZj3AmUrKMZz26Y8KAwG3eiliaO?input=http://bluesystem.info/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Blockpage on Rostelcom. Matches on the Yandex Metrika Tracker ID",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_rostelcom_warning_block_2",
        common_name="RU ISP Rostelecom Block",
        pattern="""://mc.yandex.ru/watch/25730126""",
        location_found="body",
        source=[
            ""
        ],
        exp_url="https://explorer.ooni.org/measurement/20180318T035416Z_AS8439_0e87NdF0Qx0Wh4gEH25KPSg32sz71XjM6vbRebSkdNMdJzXrZt?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Blockpage on Rostelcom. Matches on the Yandex Metrika Tracker ID, slightly older (2018) tracker than block_1",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_rostelcom_block_forward",
        common_name="RU ISP Rostelecom Block",
        pattern="""http://block.rt.ru""",
        location_found="header",
        source=[
            ""
        ],
        exp_url ="https://explorer.ooni.org/measurement/20191118T092317Z_AS42610_3HH5n7Bwuo8ibohIsM7mKmlnsO0Tv0l6dAdIp1d4wG7AVFCSPe?input=http://transsexual.org/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Forward to Rostelcom Block page.",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_tele2_forward",
        common_name="RU ISP Tele2 Block",
        pattern="""//217.169.82.130/""",
        location_found="header",
        source=[
            "http://tele2.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20190809T191432Z_AS15378_fmsQw7Pl5AMY5uxejuU0d095iyVXnfki55sFBPtu799zPhfi0R?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="RU ISP Tele2 Block page forward.",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_tele2_block",
        common_name="RU ISP Tele2 Block",
        pattern="""//t2rkn.com/""",
        location_found="body",
        source=[
            "http://tele2.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20200130T202021Z_AS12958_HjHGx4wo3WtUxuoElLzjhlNMmEucNTEIftGkafEqn6Ypg9UKDl?input=http://bluesystem.info/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="RU ISP Tele2 Block page based off the custome RKN domain they use and embed in the blockpage.",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_ttk_fz139_forward",
        common_name="RU ISP TTK Block",
        pattern="""http://fz139.ttk.ru""",
        location_found="header",
        source=[
            "https://moskva.ttk.ru/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200215T063712Z_AS8427_cIJNHs6ysaZH1kt9gI7uAVPGmIDcZOn3UTwX2w7wkMj8SFK3VN?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Forward to TTK ISP RKN Block page forward",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_ttk_block",
        common_name="RU ISP TTK Block",
        pattern="""TTK :: Доступ к ресурсу ограничен""",
        location_found="body",
        source=[
            "https://moskva.ttk.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180318T055620Z_AS8427_eLCazBA5rz8M241SW9vuD3Be7ikVb32rpLEk5ys3MuZqodzvwb?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Forward to TTK ISP RKN Block page matches on title.",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_kaspnet_forward",
        common_name="RU ISP Kaspnet Block",
        pattern="""kaspnet.ru/sites/default/files/0.html""",
        location_found="header",
        source=[
            "http://kaspnet.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20190803T010043Z_AS42922_pjHbAidMpZuZp2PN2HzXhXCQZyZlhf0A4hkNqOzB7XbXGzkmHF?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Forward to Kaspnet RKN Block page",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_kaspnet_block",
        common_name="RU ISP Kaspnet Block",
        pattern="""i.imgur.com/KMKuXmA.png""",
        location_found="body",
        source=[
            "http://kaspnet.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20190803T010043Z_AS42922_pjHbAidMpZuZp2PN2HzXhXCQZyZlhf0A4hkNqOzB7XbXGzkmHF?input=http://bluesystem.ru/",
        confidence_no_fp=7,
        scope="isp",
        expected_countries=["RU"],
        notes="Kaspnet RKN Block page matches the TV advert embedded in the blockpage.",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_tscrimea_forward",
        common_name="RU/UA ISP TS Crimea Block",
        pattern="""77.121.14.5""",
        location_found="header",
        source=[
            "https://tscrimea.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180716T134926Z_AS205515_y8sbE1h6ribC4qXeK9b3X9CWdj1tPywgOpxrMxojiCy50Oav5i?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU", "UA"],
        notes="Block for RU/UA ISP TS Crimea reverse DNS for IP is undefined.tscrimea.ru",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_formulasvyaz_forward",
        common_name="RU Formula Svyaz LLC Block",
        pattern="""109.197.24.2""",
        location_found="header",
        source=[
            ""
        ],
        exp_url="https://explorer.ooni.org/measurement/20190320T052333Z_AS50672_uQSuXHki5S8pmwxwMNUaebGb3G1NAl54hrzfxn0eplF3Qi3T5U?input=http://bluesystem.ru/",
        confidence_no_fp=9,
        scope="isp",
        expected_countries=["RU"],
        notes="Not sure what the scope is here, blockpage lives on AS50672, Formula Svyaz",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_westcall_forward_1",
        common_name="RU ISP Westcall Block",
        pattern="""http://195.94.233.66?UrlRedir=""",
        location_found="header",
        source=[
            ""
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190304T004458Z_AS8595_fphvlM2yC2x9Enus1eKlVPrN7kIgEPZ9XCa5WI6I2O6JQAAFcm?input=http://bluesystem.ru/",
        confidence_no_fp=9,
        scope="isp",
        expected_countries=["RU"],
        notes="Forward to Westcall Russias ISP blockpage",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_westcall_forward_2",
        common_name="RU ISP Westcall Block",
        pattern="""http://zapret.westcall.net/""",
        location_found="header",
        source=[
            ""
        ],
        exp_url ="https://explorer.ooni.org/measurement/20191028T010715Z_AS0_LMZN0lqus9a06Ts9jOPsJqLXpRb88J454clYl7OOYeZdd5vQYq?input=http://www.deti-404.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Forward to Westcall Russias ISP blockpage",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_westcall_block",
        common_name="RU ISP Westcall Block",
        pattern="""PEhUTUwgc3R5bGU9ImZvbnQtZmFtaWx5OiBHZW5ldmEsIEhlbHZldGljYSwgc2Fucy1zZXJpZjsiPgoKCTxIRUFEPgoJCTxUSVRMRT5BY2Nlc3MgUmVzdHJpY3RlZCE8L1RJVExFPgoJCTwhLS0gPHRpdGxlPuTP09TV0CDPx9LBzsnexc48L3RpdGxlPiAtLT4KCQkgICAgICAKCQk8TUVUQSBIVFRQLUVRVUlWPSJDb250ZW50LVR5cGUiIENPTlRFTlQ9InRleHQvaHRtbDsgY2hhcnNldD1rb2k4LXIiPgoJPC9IRUFEPgoJCgk8Qk9EWT4KCQoJICAgIDxESVYgc3R5bGU9ImhlaWdodDoxMDAlOyB3aWR0aDoxMDAlOyBwb3NpdGlvbjpmaXhlZDsgdG9wOjA7IGxlZnQ6MDsgZGlzcGxheTpmbGV4OyBhbGlnbi1pdGVtczpjZW50ZXI7IGp1c3RpZnktY29udGVudDogY2VudGVyOyBvdmVyZmxvdzphdXRvOyI""",
        location_found="body",
        source=[
            ""
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190305T005035Z_AS8595_0vVnWfDYWDzSGKMf5K8k0zUt669Cz12fNbyvNCBKMBEsDpyFOY?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Westcall Russias ISP (as base64 wrap)",
    ),

    SimpleBlockPagePattern(
        name="isp_ug_gilat_pornblock",
        common_name="UG ISP Gilat Telecom Block",
        pattern="""According to UCC regulation, Pornography pages are restricted for browsing.""",
        location_found="body",
        source=[
            "https://qz.com/africa/1340505/uganda-is-making-isps-block-pornography-from-its-citizens/",
            "https://www.sautitech.com/telecom/uganda-porn-banned/",
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190603T052310Z_AS12491_gPTKEWF0N9k2UpuLPVm6jl5q0ya6uTYge6iB2b0oXPcFejuhpc?input=http://www.gayhealth.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["UG"],
        notes="Ugandan Anti Porn Blockpage",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_sibset_149_forward",
        common_name="RU ISP Sibset Block",
        pattern="""http://211.ru/149.html""",
        location_found="header",
        source=[
        ],
        exp_url ="https://explorer.ooni.org/measurement/20180318T101233Z_AS34757_dIAMaflYtvY3WlkTT0q8l0iDnP0tzztQeacqAYTniCXQDG2G7F?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Sibsets Federal Law 149 Block Page, this is the forward to the blockpage",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_sibset_149_blockpage",
        common_name="RU ISP Sibset Block",
        pattern="""Роскомнадзор напоминает о вступлении в силу с 01 ноября 2012 года изменений в Федеральный закон 149-ФЗ "Об информации, информационных технологиях и защите информации""",
        location_found="body",
        source=[
        ],
        exp_url ="https://explorer.ooni.org/measurement/20180318T101233Z_AS34757_dIAMaflYtvY3WlkTT0q8l0iDnP0tzztQeacqAYTniCXQDG2G7F?input=http://bluesystem.ru/",
        confidence_no_fp=9,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Sibsets Federal Law 149 Block Page, this is the text on the blockpage",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_rascom_forward",
        common_name="RU ISP Rascom Block",
        pattern="""blocked.as20764.net/blocked.php""",
        location_found="header",
        source=[
            "https://rascom.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20200426T030624Z_AS15378_m3QsGmFgaY0yex11nq2wFgOTNLHiCK0lmShNdYZR6LXBKE1iq5?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Rascom Page, this is the forward to the blockpage",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_rascom_block",
        common_name="RU ISP Rascom Block",
        pattern="""<hr><center><a href="http://www.rascom.ru">""",
        location_found="body",
        source=[
            "https://rascom.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20200426T030624Z_AS15378_m3QsGmFgaY0yex11nq2wFgOTNLHiCK0lmShNdYZR6LXBKE1iq5?input=http://bluesystem.ru/",
        confidence_no_fp=7,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Rascom Page, this is matches on the ISP branding at the end of the blockpage.",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_beeline_blackhole_forward",
        common_name="RU ISP Beeline Block",
        pattern="""blackhole.beeline.ru""",
        location_found="header",
        source=[
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200214T003928Z_AS16345_MspHYIbQka8Krh8T1rYKMv2a2mwRaYQZSVlKwgYpew7x3I1f4x?input=http://www.deti-404.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Beeline Block Page, this is the forward to the blockpage via the DNS blackhole.beeline.ru",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_beeline_blackhole_blockpage",
        common_name="RU ISP Beeline Block",
        pattern="""http://www.beeline.ru/customers/help/safe-beeline/""",
        location_found="body",
        source=[
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200214T003928Z_AS16345_MspHYIbQka8Krh8T1rYKMv2a2mwRaYQZSVlKwgYpew7x3I1f4x?input=http://www.deti-404.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Beeline Federal Law 149 Block Page, this is the text on the blockpage",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_ecotelecom_forward",
        common_name="RU ISP Eco Telecom Block",
        pattern="""block.ecotelecom.ru""",
        location_found="header",
        source=[
            "https://ecotelecom.ru"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190904T071904Z_AS50473_nDaX3gMXRvqiOIIsQasGCrlo1mkiNiDIdRWwEVetB6AyQSlBDM?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Eco Telecom Block Page, this is the forward to the blockpage via the DNS block.ecotelecom.ru",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_ecotelecom_block",
        common_name="RU ISP Eco Telecom Block",
        pattern="""ДОСТУП К ИНФОРМАЦИОННОМУ<br>РЕСУРСУ ОГРАНИЧЕН""",
        location_found="body",
        source=[
            "https://ecotelecom.ru"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190904T071904Z_AS50473_nDaX3gMXRvqiOIIsQasGCrlo1mkiNiDIdRWwEVetB6AyQSlBDM?input=http://bluesystem.ru/",
        confidence_no_fp=8,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Eco Telecom Block Page, this is the text on the blockpage",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_akado_forward",
        common_name="RU ISP Akado Block",
        pattern="""blocked.akado.ru""",
        location_found="header",
        source=[
            "https://akado.ru"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20191123T232848Z_AS15582_SGLjs47pfssBgI4Pmtqe6Q4D8JfPdw5M5i68ofgzUIKRtw7s9M?input=http://www.deti-404.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Akado Block Page, this is the forward to the blockpage via the DNS block.akado.ru",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_akado_block_1",
        common_name="RU ISP Akado Block",
        pattern="""https://www.akado.ru/services/itv/?utm_source=blocked-RKN""",
        location_found="body",
        source=[
            "https://akado.ru"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20191123T232848Z_AS15582_SGLjs47pfssBgI4Pmtqe6Q4D8JfPdw5M5i68ofgzUIKRtw7s9M?input=http://www.deti-404.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Akado Block Page, this is a link on the blockpage unique to the ISP and relating to RKN blocking",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_akado_block_2",
        common_name="RU ISP Akado Block",
        pattern="""UA-2468561-43""",
        location_found="body",
        source=[
            "https://akado.ru"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180318T190102Z_AS15582_AN3pN6fRfLwsONN4y0GEgnGLXlIGPv9QDysJwLhzVv3PZw4Ujz?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Akado Block Page, this is the Google Analytics tracker id embedded in blockpage.",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_akado_block_3",
        common_name="RU ISP Akado Block",
        pattern=""".akado-ural.ru/web/rkn/site_blocked.css""",
        location_found="body",
        source=[
            "https://akado.ru"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180318T035524Z_AS30868_YNRgacl7Q5HcThofYIOQRl0Z0T00uxv1TnvOXqhzsM7165fN8W?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Akado Block Page, this is for their Ural Oblast branding",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_pakt_forward",
        common_name="RU ISP Pakt Block",
        pattern="""rkn.pakt.ru""",
        location_found="header",
        source=[
            "https://pakt.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180317T130438Z_AS39087_UU6okQpeONhX0qrLfLdlKQeculY95MVSW1zY89UcbM4snfJPNN?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian Pakt Block Page, this is the forward to the blockpage",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_pakt_block",
        common_name="RU ISP Pakt Block",
        pattern="""C уважением, П.А.К.Т.""",
        location_found="body",
        source=[
            "https://pakt.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180317T130438Z_AS39087_UU6okQpeONhX0qrLfLdlKQeculY95MVSW1zY89UcbM4snfJPNN?input=http://bluesystem.ru/",
        confidence_no_fp=8,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian Pakt Block Page, this matches the salutation at the end of their announcements.",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_tcentr_forward",
        common_name="RU ISP Telecom Center Block",
        pattern="""185.36.60.2/blocked.html""",
        location_found="header",
        source=[
            "https://www.tcenter.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20190603T211434Z_AS0_kxjMajdYmi5TXQlX4eA3fC0yf9puWMbkCK1QP8TcUSz4CoS0So?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian Telecom Center Block Page, this is the forward to the blockpage",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_tcentr_block",
        common_name="RU ISP Telecom Center Block",
        pattern="""185.36.60.2/icons/logo.png""",
        location_found="body",
        source=[
            "https://www.tcenter.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20190603T211434Z_AS0_kxjMajdYmi5TXQlX4eA3fC0yf9puWMbkCK1QP8TcUSz4CoS0So?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian Telecom Center Block Page",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_mipt_block",
        common_name="RU ISP MIPT Telecom Block",
        pattern="""МФТИ-Телеком&nbsp;&nbsp;</td>""",
        location_found="body",
        source=[
            "http://mipt-telecom.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180317T124213Z_AS5467_jYLepdiccPKELyLYmRNgvZ8KaaeGBz4JArbyfepClYbyg1EHJK?input=http://bluesystem.ru/",
        confidence_no_fp=8,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP MIPT Telecom Block Page.",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_ucanet_block",
        common_name="RU ISP UCA Networks Block",
        pattern="""rkn.ucanet.ru""",
        location_found="body",
        source=[
            "http://www.ucanet.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180318T222011Z_AS43404_jQgcHPhGKPE8KsqFe0Psx5228ciYSdUgH6KCjYMUq5CJk6f6ty?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP UCA Networks Block Page this should match both the iframe forward and the destination block page.",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_lantanet_forward",
        common_name="RU ISP Lanta Net Block",
        pattern="""193.203.61.234""",
        location_found="header",
        source=[
            "https://www.lanta-net.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180317T131247Z_AS41268_VA5OAJGFFPBeOIRJUBeiSu1WdeRjOtw2Z0O5t0FyOKmvQZsuse?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Lanta Net Block Page, this is the forward to the blockpage.",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_lantanet_block",
        common_name="RU ISP Lanta Net Block",
        pattern="""www.lanta-net.ru/zapret/""",
        location_found="body",
        source=[
            "https://www.lanta-net.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180317T131247Z_AS41268_VA5OAJGFFPBeOIRJUBeiSu1WdeRjOtw2Z0O5t0FyOKmvQZsuse?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Lanta Net Block Page, this is the forward to the blockpage.",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_skynetkazan_forward",
        common_name="RU ISP Skynet Kazan Block",
        pattern="""www.skynet-kazan.com/_blocked.htm""",
        location_found="header",
        source=[
            "https://www.skynet-kazan.com/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180318T073159Z_AS31566_N85quRr4romDzcXN4MZPiHCueUqZ0WBQGZdGq7tcJWEh32D7bz?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Skynet Kazan Block Page, this is the forward to the blockpage.",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_linkregion_forward",
        common_name="RU ISP Link Block",
        pattern="""error.link-region.ru:8099""",
        location_found="header",
        source=[
            "https://link-region.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180318T075609Z_AS0_HUKpvO8jhpAAdqfvJAlNqtoJOpDUf0MNDCQGuD1yJU2KsSUzxO?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Link Block Page, this is the forward to the blockpage.",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_linkregion_block",
        common_name="RU ISP Link Block",
        pattern="""<title>Federal block</title>""",
        location_found="body",
        source=[
            "https://link-region.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180318T075609Z_AS0_HUKpvO8jhpAAdqfvJAlNqtoJOpDUf0MNDCQGuD1yJU2KsSUzxO?input=http://bluesystem.ru/",
        confidence_no_fp=6,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Link Block Page, this might be a broad pattern to match against.",
    ),




    SimpleBlockPagePattern(
        name="isp_ru_maximatelecom_forward",
        common_name="RU ISP Maxima Telecom Block",
        pattern="""81.200.123.101""",
        location_found="header",
        source=[
            "https://maximatelecom.ru/en"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180317T175207Z_AS0_QOSBKEtHsKf5hG22JdhEjgZT83erD2VFRZpYuuhLyzWlnBCPQi?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Maxima Telecom Block Page, this is the forward to the blockpage.",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_alliancetelecom_forward",
        common_name="RU ISP Alliance Telecom Block",
        pattern="""blocked.inetvl.ru""",
        location_found="header",
        source=[
            "https://inetvl.ru/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190801T201552Z_AS44724_ELUWsMCtSP26Ihzex0GSPS3hqvRh0GIIrooWg7p45RvZbgUmi3?input=http://www.deti-404.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Alliance Telecom Block Page, this is the forward to the blockpage via blocked.inetvl.ru",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_alliancetelecom_block",
        common_name="RU ISP Alliance Telecom Block",
        pattern="""PCFET0NUWVBFIGh0bWwgUFVCTElDICItLy9XM0MvL0RURCBYSFRNTCAxLjAgVHJhbnNpdGlvbmFsLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL1RSL3hodG1sMS9EVEQveGh0bWwxLXRyYW5zaXRpb25hbC5kdGQiPgo8IS0tIHNhdmVkIGZyb20gdXJsPSgwMDE1KWh0dHA6Ly96ZXJ4LnJ1LyAtLT4KPGh0bWwgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiPjxoZWFkPjxtZXRhIGh0dHAtZXF1aXY9IkNvbnRlbnQtVHlwZSIgY29udGVudD0idGV4dC9odG1sOyBjaGFyc2V0PXdpbmRvd3MtMTI1MSIN""",
        location_found="body",
        source=[
            "https://inetvl.ru/"
        ],
        exp_url ="",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="""Russian ISP Alliance Telecom Block Page, this is a base64 of the blockpage because of mixed encodings so
              will likely only work against ooni data if you don't try to parse the different encodings""",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_infolink_forward",
        common_name="RU ISP Info-Link Block",
        pattern="""85.234.0.61""",
        location_found="header",
        source=[
            "https://new.info-link.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180318T165918Z_AS34892_LhhbkpUslR9YCTt4Nbig5XeUd39rXBk0COnBk5h0js3Wpr1R4D?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Info-Link Block Page, this is the forward to the blockpage via IP",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_infolink_block",
        common_name="RU ISP Info-Link Block",
        pattern="""missing.info-link.ru/""",
        location_found="body",
        source=[
            "https://new.info-link.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180318T165918Z_AS34892_LhhbkpUslR9YCTt4Nbig5XeUd39rXBk0COnBk5h0js3Wpr1R4D?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Info-Link Block Page matches the link to their site on the blockpage.",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_rostelecom_blocksystem",
        common_name="RU ISP Rostelecom Block System",
        pattern="""<title>block-system</title>""",
        location_found="body",
        source=[
            "https://rt.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180318T052642Z_AS31499_2BoIdLV94NnrtvwbVNk89RkG6Wg86FBLjO2lzCH6o8FmebjrQv?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="""
        Russian ISP Rostelecom but the filtering pattern is very different than what
        customers typically see.  This might be a small downstream players RKN
        implementation.
        """,
    ),

    SimpleBlockPagePattern(
        name="isp_ru_rostelecom_ipcenter",
        common_name="RU ISP Rostelecom Block System",
        pattern="""block.ip.center.rt.ru""",
        location_found="header",
        source=[
            "https://rt.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180317T162427Z_AS25515_5VmIHP6K59TMNgwYPVjJMsKM4a87URc7sbuvlZe7yb5a7Y83Rf?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="""
        Russian ISP Rostelecom variant where an HTTP 451 response is given via block.ip.center.rt.ru in the headers.
        """,
    ),

    SimpleBlockPagePattern(
        name="isp_ru_ktelecom_forward",
        common_name="RU ISP K-Telecom Block",
        pattern="""block.k-telecom.org""",
        location_found="header",
        source=[
            "https://k-telecom.org/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20200218T053707Z_AS48642_teIfdu9u5LoU76KCYMwyEQOk2qbfpJPmeSsiYL2KRMgkYxwE9e?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP K-Telecom Block Page, this is the forward to the blockpage",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_ktelecom_block",
        common_name="RU ISP K-Telecom Block",
        pattern="""<p>Техническая поддержка: <a href="mailto:support@k-telecom.org""",
        location_found="body",
        source=[
            "https://k-telecom.org/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20200218T053707Z_AS48642_teIfdu9u5LoU76KCYMwyEQOk2qbfpJPmeSsiYL2KRMgkYxwE9e?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP K-Telecom Block Page, this matches on the support email they append to a standard RKN blockpage",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_kmtn_forward",
        common_name="RU ISP KMTN Block",
        pattern="""block.kmtn.ru""",
        location_found="header",
        source=[
            "https://www.kostroma.net/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20190520T181638Z_AS44507_AXiwWpNivv9uIzC1ESqdSNy3lkqoNDBpgK2ZrFoCUhoj79MymS?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP KMTN Block Page, this is the forward to the blockpage",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_podryad_forward",
        common_name="RU ISP Podryad Block",
        pattern="""forbidden.podryad.tv""",
        location_found="header",
        source=[
            "http://podryad.tv"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180317T133059Z_AS196949_VIOHLwGOwFJGNHcWbbYtxOFTrTftiYhDXtyngllWDEmhgNgED1?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Podryad Block Page, this is the forward to the blockpage via forbidden.podryad.tv",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_podryad_block",
        common_name="RU ISP Podryad Block",
        pattern="""<a href="http://podryad.tv" class="header__logo header__logo__locked"></a>""",
        location_found="body",
        source=[
            "http://podryad.tv"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180317T133059Z_AS196949_VIOHLwGOwFJGNHcWbbYtxOFTrTftiYhDXtyngllWDEmhgNgED1?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Podryad Block Page, this is matching some html referencing the ISP and blockpage",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_miranda_forward",
        common_name="RU ISP Miranda Media Block",
        pattern="""miranda-media.ru/stop_rkn""",
        location_found="header",
        source=[
            "https://www.miranda-media.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20200503T080344Z_AS201776_LcmthstHJJjoU7fd9RIdqC2NvOPIbT48S43epb5mWou5gDdYux?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian/Ukranian ISP Miranda Media (based in Crimea) Block Page, this is the forward to the blockpage via 302 redir",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_miranda_block",
        common_name="RU ISP Miranda Media Block",
        pattern="""109.200.155.73/info.js""",
        location_found="body",
        source=[
            "https://www.miranda-media.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20200503T080344Z_AS201776_LcmthstHJJjoU7fd9RIdqC2NvOPIbT48S43epb5mWou5gDdYux?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian/Ukranian ISP Miranda Media (based in Crimea) Block Page, this matches the custom tracker js they include",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_mts_forward",
        common_name="RU ISP MTS Block",
        pattern="""blocked.mts.ru""",
        location_found="header",
        source=[
            "https://moskva.mts.ru/personal"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200131T005107Z_AS8359_BGPMi8pmHmXvn1vJEpcLafYnnstcjEvZn16varKBY9VQTTkbYu?input=http://www.lesbi.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP MTS Block Page, this is the forward to the blockpage via the DNS blocked.mts.ru",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_mts_block",
        common_name="RU ISP MTS Block",
        pattern="""subblock.mts.ru""",
        location_found="body",
        source=[
            "https://moskva.mts.ru/personal"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200131T005107Z_AS8359_BGPMi8pmHmXvn1vJEpcLafYnnstcjEvZn16varKBY9VQTTkbYu?input=http://www.lesbi.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP MTS Block Page, subdomain that the blockpage uses that should be unique to the blockpage",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_netbynet_forward",
        common_name="RU ISP NetByNet Block",
        pattern="""blocked.netbynet.ru""",
        location_found="header",
        source=[
            "http://www.netbynet.ru/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20191004T205146Z_AS12714_Vh5wOEj1bL4YyQCNz2kUOmL6y3NSnP9DTAvn55eFd93q9YPfxr?input=http://www.thegailygrind.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP NetByNet Block Page, this is the forward to the blockpage via the DNS blocked.netbynet.ru",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_netbynet_block",
        common_name="RU ISP NetByNet Block",
        pattern="""UA-23688716-21""",
        location_found="body",
        source=[
            "http://www.netbynet.ru/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20180317T125006Z_AS12714_EKKezyi1I1R4ccMvYU90GdJ9xf5mwg7qocORQgcQZ1ckX6vVCA?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP NetByNet Block Page, they use Google Analytics so this is the UA being used for this",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_tinkoff_forward",
        common_name="RU ISP Tinkoff Block",
        pattern="""blocked.tinkoff.ru""",
        location_found="header",
        source=[
            "https://www.tinkoff.ru/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190801T112858Z_AS205638_WIDlbpcLq2Wdx6ZuLHvDPyEiOfmcowETD2feCnGdfp4waZKUNa?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Tinkoff Block Page, this is the forward to the blockpage via the DNS blocked.tinkoff.ru",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_tinkoff_block",
        common_name="RU ISP Tinkoff Block",
        pattern="""Тинькофф Мобайл | Страница заблокирована Роскомнадзором""",
        location_found="body",
        source=[
            "http://www.netbynet.ru/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190801T112858Z_AS205638_WIDlbpcLq2Wdx6ZuLHvDPyEiOfmcowETD2feCnGdfp4waZKUNa?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Tinkoff Block Page, this is the title",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_ugmktelecom_forward",
        common_name="RU ISP Tinkoff Block",
        pattern="""blocked.ugmk-telecom.ru""",
        location_found="header",
        source=[
            "https://ugmk-telecom.ru/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20180318T050632Z_AS41560_b7QCibF5I8GA0EwSDSdRmMlISrxgZ4vc98irCf5uGRpC6uoAIm?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP UGMK Telecom Block Page, this is the forward to the blockpage via the DNS blocked.ugmk-telecom.ru",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_ugmktelecom_block",
        common_name="RU ISP UGMK Telecom Block",
        pattern="""ДОСТУП К РЕСУРСУ ЗАБЛОКИРОВАН!""",
        location_found="body",
        source=[
            "https://ugmk-telecom.ru/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20180318T162821Z_AS29124_8hyYyPgC6VptMKiuXkFVGcBEXj3bnAbScN8YrXqd77GijxsDQ5?input=http://bluesystem.ru/",
        confidence_no_fp=8,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP UGMK Telecom Block Page, this is the text in the blockpage but should be unique enough not to catch other RKN blocks",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_avantel_forward",
        common_name="RU ISP Avantel Block",
        pattern="""block.msk.avantel.ru""",
        location_found="header",
        source=[
            "https://avantel.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20190418T064317Z_AS44811_YuHou8TpZoBdfIwW8ZjLp7AJUZjWkLe1j3mJnedRpx3DU5Ge3q?input=http://www.deti-404.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Avantel Block Page, this is the forward to the blockpage",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_avantel_block",
        common_name="RU ISP Avantel Block",
        pattern="""helpdesk@avantel.ru""",
        location_found="body",
        source=[
            "https://avantel.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20190418T064317Z_AS44811_YuHou8TpZoBdfIwW8ZjLp7AJUZjWkLe1j3mJnedRpx3DU5Ge3q?input=http://www.deti-404.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Avantel Block Page, this matches on the helpdesk email embedded in the block page.",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_yaltanet_forward",
        common_name="RU ISP Yaltanet Block",
        pattern="""block.yaltanet.ru""",
        location_found="header",
        source=[
            "http://yaltanet.ru/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190803T194713Z_AS47939_8XZsen8o7UM56nyowpxdQINGWBeWr4soyFi9C31IFEVv24Tg3R?input=http://www.deti-404.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Yaltanet Block Page, this is the forward to the blockpage via the DNS block.yaltanet.ru",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_yaltanet_block",
        common_name="RU ISP Yaltanet Block",
        pattern="""<title>Yaltanet Ltd</title>""",
        location_found="body",
        source=[
            "http://yaltanet.ru/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190803T194713Z_AS47939_8XZsen8o7UM56nyowpxdQINGWBeWr4soyFi9C31IFEVv24Tg3R?input=http://www.deti-404.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Yaltanet Block Page, this is the title",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_primelink_forward",
        common_name="RU ISP Primelink Block",
        pattern="""95.131.176.27""",
        location_found="header",
        source=[
            "http://www.primelink.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180322T162058Z_AS49058_vYrpjxnSyh3GXz3R7EW8zGy4sVAxZ92jcSYvbcgny3uYTixO8B?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Primelink Block Page, this is the forward to the blockpage",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_almatel_forward",
        common_name="RU ISP Almatel Block",
        pattern="""deny.cifra1.ru""",
        location_found="header",
        source=[
            "https://almatel.ru/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20180330T151901Z_AS8905_eVr71AR4JRpJBtXOPRIUqIQmsjKK449XNgqADi6sSfD1pL0uMI?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Almatel Block Page, this is the forward to the blockpage via the DNS deny.cifra1.ru",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_almatel_block",
        common_name="RU ISP Almatel Block",
        pattern="""almatel.ru/ajax/all.php?e=ott_forbidden_reg""",
        location_found="body",
        source=[
            "https://almatel.ru/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200127T101808Z_AS8334_CXzMxCcZGarpjw4h6HZod7C4ktkoXLShemHwxSJ1CptUcnDQqL?input=http://www.lesbi.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Almatel Block Page, this a link that does an AJAX post",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_crelcom_forward",
        common_name="RU/UA/Crimean ISP Crelcom Block",
        pattern="""erblock.crimea.com""",
        location_found="header",
        source=[
            "http://www.crimea.com/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190817T194620Z_AS57093_GyP7oVw2nGeRpf8YINz9YgO7KnrXPONAdWRFHwjTWrk1tzzyRE?input=http://www.lesbi.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian/Crimean ISP Crelcom Block Page, this is the forward to the blockpage via the DNS erblock.crimea.com",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_crelcom_block",
        common_name="RU/UA/Crimean ISP Crelcom Block",
        pattern="""UA-62111225-1""",
        location_found="body",
        source=[
            "http://www.crimea.com/"
        ],
        exp_url ="",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian/Crimean ISP Crelcom Block Page, which uses a Google Analytics script on the blockpage",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_feonet_forward",
        common_name="RU/UA/Crimean ISP Crelcom Block",
        pattern="""erblock.feonet.net""",
        location_found="header",
        source=[
            "https://feonet.net/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20180318T111845Z_AS42975_F8baGa4ov62PxGsyC7PwxTeldI3Ee8VAch7DHXzTCPwFk8VFUU?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="""Russian/Crimean ISP Feonet Block Page, this is the forward to the blockpage via the
              DNS erblock.feonet.net.  This ISP serves the resort town of Feodosia on the Black Sea Coast in Crimea.
              When I checked this fowarded to the same blockpage of crelcom, which seems shared among Crimea""",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_2kom_forward",
        common_name="RU ISP 2kom Block",
        pattern="""forbidden.2kom.ru""",
        location_found="header",
        source=[
            "https://2kom.ru/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200127T101808Z_AS8334_CXzMxCcZGarpjw4h6HZod7C4ktkoXLShemHwxSJ1CptUcnDQqL?input=http://www.lesbi.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="""Russian ISP 2kom Block Page, this is the forward to the blockpage via the
          DNS forbidden.2kom.ru. This forwarded me to the almatel blockpage when I checked""",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_2kom_block",
        common_name="RU ISP 2kom Block",
        pattern="""GTM-NBL6CQ""",
        location_found="body",
        source=[
            "https://2kom.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180430T004143Z_AS8334_w0W0QB8R1vcxsb8GkwBu0vuI5LV4ktuldUTUvI2DLeEulIOxN3?input=http://bluesystem.ru/",
        confidence_no_fp=8,
        scope="isp",
        expected_countries=["RU"],
        notes="""Russian ISP 2kom Block Page, matches based on Google Tag Manager ID so there is a slight chance
        this is used on other 2Kom sites.""",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_virginconnect_forward",
        common_name="RU ISP Virgin Connect Block",
        pattern="""mega.nn.ru/l7.html""",
        location_found="header",
        source=[
            "https://www.virginconnect.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180810T065459Z_AS39289_SM4QfsdBvxi6UYZjn4rwMHvIzgSwDPBxwmfOZUTeIa4YWyg5Ft?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="""Russian ISP Virgin Connect Block Page, this is the forward to the blockpage""",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_yota_forward",
        common_name="RU ISP Yota Block",
        pattern="""forbidden.yota.ru""",
        location_found="header",
        source=[
            "https://www.yota.ru/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200215T074314Z_AS25159_0xrGzNzvnnsXSAVKwYNzwIb7cL2eUxH2Nj1fJ0nclVrYPQJmLO?input=http://www.deti-404.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="Russian ISP Yota Block Page, this is the forward to the blockpage via the DNS forbidden.yota.ru",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_yota_block_1",
        common_name="RU ISP Yota Block",
        pattern="""<h1 class="title title_h1">Доступ ограничен</h1>""",
        location_found="body",
        source=[
            "https://www.yota.ru/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20180321T164414Z_AS47395_zANSZBCvk6wkOGQSCgFy5DVvM0X1akRXBjXkyazUrqFKY3JE53?input=http://bluesystem.ru/",
        confidence_no_fp=7,
        scope="isp",
        expected_countries=["RU"],
        notes="""Russian ISP Yota Block Page, this is the title since it uses these specific h1 class it may be unique
              enough to avoid fps""",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_yota_block_2",
        common_name="RU ISP Yota Block",
        pattern="""UA-16019436-1""",
        location_found="body",
        source=[
            "https://www.yota.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20190221T004849Z_AS47395_EyAG1vxiNO1VkgbiIifh1zdrQ8Olgs4ntIfEeHpkuJozkjwFQZ?input=http://bluesystem.ru/",
        confidence_no_fp=7,
        scope="isp",
        expected_countries=["RU"],
        notes="""Russian ISP Yota Block Page, This is for the blockpage variant where a Google Analytics tracker is used
        on the blockpage.""",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_telincom_forward",
        common_name="RU ISP Telincom Block",
        pattern="""cacti.telincom.ru/blocked.html""",
        location_found="header",
        source=[
            "http://telincom.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20190215T191020Z_AS51077_PgHDPvuTuN4HiRIfg8b6bYw2J3diS2doqaQpqs8NLlPaBsC9XQ?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="""Russian ISP Telincom blockpage forward.""",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_telincom_block",
        common_name="RU ISP Telincom Block",
        pattern="""yaCounter48660917""",
        location_found="body",
        source=[
            "http://telincom.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20190215T191020Z_AS51077_PgHDPvuTuN4HiRIfg8b6bYw2J3diS2doqaQpqs8NLlPaBsC9XQ?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="""Russian ISP Telincom blockpage.""",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_cityline_block",
        common_name="RU ISP City Line Block",
        pattern="""rkn.clkon.net/images/""",
        location_found="body",
        source=[
            "http://clkon.net/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180317T134334Z_AS56476_KFg0mIozfedCjgfrcGis7ZiFKnZn2gMg2BFxMpZMdxuIiVA0Vk?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="""Russian ISP City Line blockpage.""",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_rialink_forward",
        common_name="RU ISP Ria Link Block",
        pattern="""91.215.188.193""",
        location_found="header",
        source=[
            "https://ria-link.ru/uslugi"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180318T062701Z_AS49701_cV0IJIOulrZqBi9yQsD99legkwh7MCgMcrrYBE4un3cukO6HxN?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="""Russian ISP Ria Link blockpage forward via 30x through squid""",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_rialink_block",
        common_name="RU ISP Ria Link Block",
        pattern="""РИА-линк интернет Брянск / ria-link.ru""",
        location_found="body",
        source=[
            "https://ria-link.ru/uslugi"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180318T062701Z_AS49701_cV0IJIOulrZqBi9yQsD99legkwh7MCgMcrrYBE4un3cukO6HxN?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="""Russian ISP Ria Link blockpage forward via 30x through squid""",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_intersvas_forward",
        common_name="RU ISP Intersvas Block",
        pattern="""you-shall-not-pass.is74.ru""",
        location_found="header",
        source=[
            "https://www.is74.ru/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200205T012112Z_AS8369_lz479luPP9r7txwbYi3IxOSC4J2m3eu2xPZbed1O5NTBq2cDQW?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="""Russian ISP Intersvas (is74) Block Page, this is the forward to the blockpage via the DNS
              you-shall-not-pass.is74.ru  I have never actually seen a succeful GET here to the page but 
              it is a clear block page given the name and urls seen.""",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_intersvas_block",
        common_name="RU ISP Intersvas Block",
        pattern="""id=com.intersvyaz.lk&referrer=utm_source%3Dlp_you_shall_not_pass_parking""",
        location_found="body",
        source=[
            "https://www.is74.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20190726T044441Z_AS8369_pt6iOTfKLtNs6vy19VFsbMTvwtRno87AZ601Xdyj4TJkiwumfU?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="""Russian ISP Intersvas (is74) Block Page, this is the forward to the blockpage via the DNS
          you-shall-not-pass.is74.ru  This matches on their referrer links which reference both the blockpage
          and the ISP.""",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_nevalink_forward",
        common_name="RU ISP Nevalink Block",
        pattern="""89.223.47.135""",
        location_found="header",
        source=[
            "https://nevalink.net/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20200201T082946Z_AS42668_gmx6fqwN0k925BbuFXoqKR01sUjq7fsFHbXJT8LpqmAJrWSRDi?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="""Russian ISP Nevalink forward to a blockpage should 302 to GET http://89.223.47.135/index.html
        """,
    ),

    SimpleBlockPagePattern(
        name="isp_ru_svyazenergo_forward",
        common_name="RU ISP Svyaz Energo Block",
        pattern="""http://sv-en.ru/block.php""",
        location_found="header",
        source=[
            "http://sv-en.ru"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180318T095622Z_AS50477_cLI1EK0sH5N5MEKzozCK1pZPygYAOWsfjxXhRB1BBIRGGDMk5J?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="""Russian ISP Svyaz Energo Block Page, a business focused ISP
        """,
    ),

    SimpleBlockPagePattern(
        name="isp_ru_svyazenergo_block",
        common_name="RU ISP Svyaz Energo Block",
        pattern="""http://www.sv-en.ru/block""",
        location_found="body",
        source=[
            "http://sv-en.ru"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180318T095622Z_AS50477_cLI1EK0sH5N5MEKzozCK1pZPygYAOWsfjxXhRB1BBIRGGDMk5J?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="""Russian ISP Svyaz Energo Block Page, a business focused ISP
    """,
    ),

    SimpleBlockPagePattern(
        name="isp_ru_megafon_forward",
        common_name="RU ISP Megafon Block",
        pattern="""m.megafonpro.ru""",
        location_found="header",
        source=[
            "https://megafonpro.ru/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200215T053350Z_AS31208_ilgbksUk8hWR5svFbpJ0oxOkeDWdQqaW2xsDiL13G2VeN7KnVT?input=http://www.lesbi.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="""Russian ISP Megafon Block Page, this is the forward to a few possible domains such as:
        m.megafonpro.ru/rkn, m.megafonpro.ru:81/rkn and m.megafonpro.ru/session?token
        
        These forwards often don't complete and is poorly implemented so seeing infinite redirects situations is
        common
        """,
    ),

    SimpleBlockPagePattern(
        name="isp_ru_megafon_block",
        common_name="RU ISP Megafon Block",
        pattern="""UA-97554836-1""",
        location_found="body",
        source=[
            "https://megafonpro.ru/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20191123T161807Z_AS31195_eBzph7e3WZ0EhpiNDOVYeSjnVpAyR7DA8e5xW3e4U2yGB0LzZr?input=http://www.deti-404.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="""Russian ISP Megafon Block Page, if the redirects ever finish will have a Google Analytics
        code that is unique to the page""",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_megafon_block_tag",
        common_name="RU ISP Megafon Block",
        pattern="""GTM-WBQ8X7M""",
        location_found="body",
        source=[
            "https://megafonpro.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20200118T012925Z_AS31213_HXkdYCWN5qqPLgvSvFam2G3EwubT2qtm6Wrp6e6s7GS8X46mDq?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="""Russian ISP Megafon Block Page, this matches the GTM tag they use on the blockpage.""",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_megafon_block_with_ad",
        common_name="RU ISP Megafon Block",
        pattern="""href="rkn">Отменить</a>""",
        location_found="body",
        source=[
            "https://megafonpro.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20191213T100614Z_AS25159_ZHdmlcy3Gqv7zZKgNCUHU7kdmIRP9wsQ0xnBiRrEo5SUs0O5Zj?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="""Russian ISP Megafon Block Page, this is a variant that has an ad banner above but this matches on the lower
        RKN related block HTML.""",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_obit_forward",
        common_name="RU ISP Obit Block",
        pattern="""notice.obit.ru/censored""",
        location_found="header",
        source=[
            "https://www.obit.ru/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190417T083259Z_AS0_uSpocMEwsEZlkDtgVOumm4liHHCbBA6KhbGbJJFfEkkpFydnVU?input=http://www.deti-404.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="""Russian ISP Obit Block Page via a forward in the headers to notice.obit.ru/censored""",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_obit_block",
        common_name="RU ISP Obit Block",
        pattern="""id:43845029,""",
        location_found="body",
        source=[
            "https://www.obit.ru/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190417T083259Z_AS0_uSpocMEwsEZlkDtgVOumm4liHHCbBA6KhbGbJJFfEkkpFydnVU?input=http://www.deti-404.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="""Russian ISP Obit Block Page, it uses Yandex Metrika for tracking so we can use the unique id""",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_ufanet_forward",
        common_name="RU ISP Ufanet Block",
        pattern="""ufanet.ru/blocking.html""",
        location_found="header",
        source=[
            "https://www.ufanet.ru/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20191014T032243Z_AS24955_PfJea2GTQ0zkg1IMtUmEVa8FnVbDTB8SmPrFc5zHGOr5HyMc1p?input=http://www.deti-404.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="""Russian ISP Ufanet Block Page via a forward in the headers to https://www.ufanet.ru/blocking.html/""",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_ufanet_forward_ipvariant",
        common_name="RU ISP Ufanet Block",
        pattern="""95.213.254.253""",
        location_found="header",
        source=[
            "https://www.ufanet.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20190525T080819Z_AS24955_qQMrVJZWRoIbrZFkqSUgKpO7SVsWXKSfH9ZtiIGPGoIiuaths0?input=http://bluesystem.ru/",
        confidence_no_fp=6,
        scope="isp",
        expected_countries=["RU"],
        notes="""Russian ISP Ufanet Block Page via a forward in the headers to http://95.213.254.253/.  Attribution
        is not clear as the explorer URL places this to Ufanet but the blockpage is hosted on Russian IT provider
        Selectel.""",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_ufanet_block",
        common_name="RU ISP Ufanet Block",
        pattern="""id:41226669,""",
        location_found="body",
        source=[
            "https://www.ufanet.ru/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20191014T032243Z_AS24955_PfJea2GTQ0zkg1IMtUmEVa8FnVbDTB8SmPrFc5zHGOr5HyMc1p?input=http://www.deti-404.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="""Russian ISP Ufanet Block Page, it uses Yandex Metrika for tracking so we can use the unique id""",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_wiland_forward",
        common_name="RU ISP Wiland Block",
        pattern="""blocked.wiland.ru""",
        location_found="header",
        source=[
            "http://wiland.ru/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20181221T095704Z_AS21367_H6haY9cXO9O0I2t86lqWzxgBmqnJOkIyt0NUfD8Rz7XAceiMJw?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="""Russian ISP Wiland Block Page forward.""",
    ),

    SimpleBlockPagePattern(
        name="isp_ru_megion_forward",
        common_name="RU ISP Megion Block",
        pattern="""megion.biz/block.html""",
        location_found="header",
        source=[
            "http://www.megion.biz/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180318T204204Z_AS12714_moZOawAkYEeJxmuAAbfpf9G8DqJOvLSXIg9EFrNRGWztrVM7nn?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["RU"],
        notes="""Russian ISP Megion Block Page forward.""",
    ),

    SimpleBlockPagePattern(
        name="isp_tr_ttnet_secureinternet_forward",
        common_name="TR ISP TTNet OptIn Block",
        pattern="""http://bilgi.turktelekom.com.tr/guvenli_internet_uyari""",
        location_found="header",
        source=[
                "https://www.turktelekomguvenlik.com/destek/guvenli-internet-hizmeti"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200207T075356Z_AS20978_JJ3svMeHEnIrFcIceAHeqrbp6RyDtgBqTtnDmo3mRfMEGFGiXK?input=http://transsexual.org/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["TR"],
        notes="Turkish ISP TTNet (Turk Telecom) block page this is an opt-in filter",
    ),


    SimpleBlockPagePattern(
        name="isp_tr_ttnet_secureinternet_blockpage",
        common_name="TR ISP TTNet OptIn Block",
        pattern="""<title>Güvenli İnternet Uyarı</title>""",
        location_found="body",
        source=[
            "https://www.turktelekomguvenlik.com/destek/guvenli-internet-hizmeti"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200207T075356Z_AS20978_JJ3svMeHEnIrFcIceAHeqrbp6RyDtgBqTtnDmo3mRfMEGFGiXK?input=http://transsexual.org/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["TR"],
        notes="Turkish ISP TTNet (Turk Telecom) block page this is an opt-in filter",
    ),

    SimpleBlockPagePattern(
        name="isp_ie_three_optinporn_forward",
        common_name="IE ISP Three OptIn Block",
        pattern="""m.three.ie/adult-content""",
        location_found="header",
        source=[
            "https://www.three.ie/",
            "https://forum.three.ie/t5/3MadeEasy/Adult-Content-Filter-How-to-Turn-Off/ba-p/191"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190724T152019Z_AS13280_5XchAx4T8ZNmgtqbFSgcjHFB9QKFqviPSJa88PQs4VXCdk1mBo?input=http://www.gayscape.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["IE"],
        notes="Irish ISP Three forward to a block page. This is an opt-in porn filter.",
    ),

    SimpleBlockPagePattern(
        name="isp_ie_three_optinporn_block",
        common_name="IE ISP Three OptIn Block",
        pattern="""To turn this off, you must verify your age - click below to log in to My3""",
        location_found="body",
        source=[
            "https://www.three.ie/",
            "https://forum.three.ie/t5/3MadeEasy/Adult-Content-Filter-How-to-Turn-Off/ba-p/191"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190724T152019Z_AS13280_5XchAx4T8ZNmgtqbFSgcjHFB9QKFqviPSJa88PQs4VXCdk1mBo?input=http://www.gayscape.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["TR"],
        notes="Irish ISP Three forward to a block page. This is an opt-in porn filter.",
    ),

    SimpleBlockPagePattern(
        name="isp_gb_o2_18plusoptin_forward",
        common_name="GB ISP O2 OptIn Block",
        pattern="""assets.o2.co.uk/18plusaccess""",
        location_found="header",
        source=[
            "https://www.o2.co.uk/",
            "https://www.o2.co.uk/help/safety-and-security/age-restricted-content-and-age-verification"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190403T143637Z_AS29180_Rg2EoxvcDr0pcIYCywybM010BYCl8skvqZk7yAQbArxo2lHSJJ?input=http://www.bglad.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["GB"],
        notes="British ISP Three forward to a block page. This is an opt-in porn filter that age gates urls.",
    ),

    SimpleBlockPagePattern(
        name="isp_gb_o2_18plusoptin_block",
        common_name="GB ISP O2 OptIn Block",
        pattern="""You need to be over 18 for this website [O2""",
        location_found="body",
        source=[
            "https://www.o2.co.uk/",
            "https://www.o2.co.uk/help/safety-and-security/age-restricted-content-and-age-verification"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190403T143637Z_AS29180_Rg2EoxvcDr0pcIYCywybM010BYCl8skvqZk7yAQbArxo2lHSJJ?input=http://www.bglad.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["GB"],
        notes="British ISP O2 block page. This is an opt-in porn filter that age gates urls.",
    ),

    SimpleBlockPagePattern(
        name="isp_gb_vodafone_optinporn_forward",
        common_name="GB ISP Vodafone OptIn Block",
        pattern="""vodafone.co.uk/restricted-content""",
        location_found="header",
        source=[
            "https://www.vodafone.co.uk/",
            "https://www.vodafone.co.uk/about-us/code-of-practice/content-control/#:~:targetText=Age%2Drestricted%20content%20bar&targetText=It's%20a%20setting%20we%20provide,or%20crime%20%E2%80%93%20on%20mobile%20devices."
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190704T000814Z_AS25135_mqMcWW8a9uRprR4q1bWdrsOnWMgJnQljybCpd5pJ488dXV3zYw?input=http://www.bglad.com",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["GB"],
        notes="British ISP Vodafone forward to a block page. This is an opt-in porn filter that age gates urls.",
    ),

    SimpleBlockPagePattern(
        name="isp_gb_vodafone_optinporn_block",
        common_name="GB ISP Vodafone OptIn Block",
        pattern="""<strong>Age-restricted content bar</strong>""",
        location_found="body",
        source=[
            "https://www.vodafone.co.uk/",
            "https://www.vodafone.co.uk/about-us/code-of-practice/content-control/#:~:targetText=Age%2Drestricted%20content%20bar&targetText=It's%20a%20setting%20we%20provide,or%20crime%20%E2%80%93%20on%20mobile%20devices."
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190704T000814Z_AS25135_mqMcWW8a9uRprR4q1bWdrsOnWMgJnQljybCpd5pJ488dXV3zYw?input=http://www.bglad.com",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["GB"],
        notes="British ISP Vodafone block page. This is an opt-in porn filter that age gates urls.",
    ),

    SimpleBlockPagePattern(
        name="isp_gb_ee_optinporn_forward",
        common_name="GB ISP EE OptIn Block",
        pattern="""myaccount.ee.co.uk/anonymous-content-lock""",
        location_found="header",
        source=[
            "https://ee.co.uk/",
            "https://ee.co.uk/help/help-new/safety-and-security/content-lock/switching-content-lock-on-or-off"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190706T190225Z_AS12576_mFnAzWvDmH9kePFIPqNM8CRSK29bixzax8yZ6qnclZNehy835d?input=http://www.bglad.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["GB"],
        notes="British ISP EE forward to a block page. This is an opt-in porn filter that age gates urls.",
    ),

    SimpleBlockPagePattern(
        name="isp_gb_ee_optinporn_block",
        common_name="GB ISP Vodafone OptIn Block",
        pattern="""www.internetmatters.org/ee""",
        location_found="body",
        source=[
            "https://ee.co.uk/",
            "https://ee.co.uk/help/help-new/safety-and-security/content-lock/switching-content-lock-on-or-off"
        ],
        exp_url ="",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["GB"],
        notes="British ISP EE block page. This is an opt-in porn filter that age gates urls.",
    ),

    SimpleBlockPagePattern(
        name="isp_gb_three_optinporn_forward",
        common_name="GB ISP Three OptIn Block",
        pattern="""three.co.uk/mobilebroadband_restricted""",
        location_found="header",
        source=[
            "http://www.three.co.uk/",
            "https://support.three.co.uk/SRVS/CGI-BIN/WEBISAPI.DLL?Command=New,Kb=Mobile,Ts=Mobile,T=Article,varset_cat=internetapps,varset_subcat=3582,Case=obj(16080)"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20191231T161856Z_AS60339_TIssjRdOb8ResMnoEVeHpWtovxJg5QxRKsRuYYecfcAmiETc57?input=http://www.bglad.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["GB"],
        notes="British ISP Three forward to a block page. This is an opt-in porn filter that age gates urls.",
    ),

    SimpleBlockPagePattern(
        name="isp_gb_three_optinporn_block",
        common_name="GB ISP Three OptIn Block",
        pattern="""ThreeWeb_C|-->Your adult content filter is on""",
        location_found="body",
        source=[
            "http://www.three.co.uk/",
            "https://support.three.co.uk/SRVS/CGI-BIN/WEBISAPI.DLL?Command=New,Kb=Mobile,Ts=Mobile,T=Article,varset_cat=internetapps,varset_subcat=3582,Case=obj(16080)"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20191231T161856Z_AS60339_TIssjRdOb8ResMnoEVeHpWtovxJg5QxRKsRuYYecfcAmiETc57?input=http://www.bglad.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["GB"],
        notes="British ISP Three block page. This is an opt-in porn filter that age gates urls.",
    ),

    SimpleBlockPagePattern(
        name="isp_gb_giffgaff_optinporn_forward",
        common_name="GB ISP GiffGaff OptIn Block",
        pattern="""www.giffgaff.com/mobile/over18""",
        location_found="header",
        source=[
            "https://www.giffgaff.com/",
            "https://www.giffgaff.com/help/articles/how-do-i-turn-off-the-adult-content-block"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20191009T152456Z_AS35228_2YC8q7bdXWrnOO8NuKvNjS5F0SsVQBHLCyt17C5i684qDQ7DQT?input=http://www.bglad.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["GB"],
        notes="British ISP GiffGaff forward to a block page (part of O2 internet). This is an opt-in porn filter that age gates urls.",
    ),

    SimpleBlockPagePattern(
        name="isp_gb_giffgaff_optinporn_block",
        common_name="GB ISP GiffGaff OptIn Block",
        pattern="""UA-10328417-1""",
        location_found="body",
        source=[
            "https://www.giffgaff.com/",
            "https://www.giffgaff.com/help/articles/how-do-i-turn-off-the-adult-content-block"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20191009T152456Z_AS35228_2YC8q7bdXWrnOO8NuKvNjS5F0SsVQBHLCyt17C5i684qDQ7DQT?input=http://www.bglad.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["GB"],
        notes="British ISP GiffGaff block page (part of O2 internet). This is an opt-in porn filter that age gates urls.",
    ),

    SimpleBlockPagePattern(
        name="isp_gb_skybroadband_optinporn_forward",
        common_name="GB ISP Sky Broadband OptIn Block",
        pattern="""block.cf.sky.com""",
        location_found="header",
        source=[
            "https://www.sky.com/shop/broadband-talk/",
            "https://www.sky.com/shop/broadband-talk/broadband-shield/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190929T145217Z_AS5607_2kkJ5ZcoHY65PnXshBrnVW1SkwHUGBJYgKApmQ82qYQl5U6kkC?input=http://www.grindr.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["GB"],
        notes="British ISP Sky Broadband forward to a block page. This is an opt-in porn filter that age gates urls.",
    ),

    SimpleBlockPagePattern(
        name="isp_gb_skybroadband_optinporn_block",
        common_name="GB ISP Sky Broadband OptIn Block",
        pattern="""http://broadbandshield.sky.com""",
        location_found="body",
        source=[
            "https://www.sky.com/shop/broadband-talk/",
            "https://www.sky.com/shop/broadband-talk/broadband-shield/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190929T145217Z_AS5607_2kkJ5ZcoHY65PnXshBrnVW1SkwHUGBJYgKApmQ82qYQl5U6kkC?input=http://www.grindr.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["GB"],
        notes="British ISP GiffGaff block page. This is an opt-in porn filter that age gates urls.",
    ),

    SimpleBlockPagePattern(
        name="isp_gb_talktalk_optinporn_block",
        common_name="GB ISP TalkTalk OptIn Block",
        pattern="""www.talktalk.co.uk/notices/parental-controls.html?originalURL=""",
        location_found="body",
        source=[
            "https://www.talktalk.co.uk/",
            "https://www.talktalk.co.uk/shop/security/homesafe"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190929T145217Z_AS5607_2kkJ5ZcoHY65PnXshBrnVW1SkwHUGBJYgKApmQ82qYQl5U6kkC?input=http://www.grindr.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["GB"],
        notes="""British ISP TalkTalk block page. This is an opt-in porn filter that age gates urls. They
        have an iframe like this:
         <iframe src="http://www.talktalk.co.uk/notices/parental-controls.html?originalURL=http://www.bglad.com/&list=porn_i>"
        """,
    ),

    SimpleBlockPagePattern(
        name="isp_gb_bt_optin_forward",
        common_name="GB ISP BT Block",
        pattern="""blockpage.bt.com""",
        location_found="header",
        source=[
            "https://bt.custhelp.com/app/answers/detail/a_id/46768/~/how-to-keep-your-family-safe-online-with-bt-parental-controls-and-the-different"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190829T210440Z_AS0_JeFN85k6TtBxasKqtjtJyuNroNql9ZxwtU49GwELCJvY8YdVHu?input=http://www.gayscape.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["GB"],
        notes="GB ISP BT Forward to Block.  This is a parental opt-in porn filter.",
    ),

    SimpleBlockPagePattern(
        name="isp_gb_bt_optin_block",
        common_name="GB ISP BT Block",
        pattern="""blockpage.bt.com/pcstaticpage/internet-matters.png""",
        location_found="body",
        source=[
            "https://bt.custhelp.com/app/answers/detail/a_id/46768/~/how-to-keep-your-family-safe-online-with-bt-parental-controls-and-the-different"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190829T210440Z_AS0_JeFN85k6TtBxasKqtjtJyuNroNql9ZxwtU49GwELCJvY8YdVHu?input=http://www.gayscape.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["GB"],
        notes="GB ISP BT Block. This is a parental opt-in porn filter.",
    ),

    SimpleBlockPagePattern(
        name="isp_id_mncplay_sehat_blockpage",
        common_name="ID ISP MNC Play Media Blockpage",
        pattern="""internetpositif.mncplaymedia.com""",
        location_found="body",
        source=[
            "https://www.mncplay.id/en/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180727T095622Z_AS17670_ryQ3v3ZDI2X8YI7FKTxeG9L5PEmgc0Z5N3bDIU7uusFaaIcuql?input=http://www.bglad.com",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["ID"],
        notes="Indonesian ISP MNC Play Media block page.",
    ),

    SimpleBlockPagePattern(
        name="isp_id_cbn_sehat_blockpage",
        common_name="ID ISP CBN Fibre Blockpage",
        pattern="""please contact our Customer Care at 1500 780 or email us at""",
        location_found="body",
        source=[
            "https://cbn.id/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20190420T092536Z_AS135478_mLOlXUu4n0QwTV10X6nqZYFwh9aQga4i4fPo9fMomwk2IMV6Le?input=http://transsexual.org/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["ID"],
        notes="Indonesian ISP CBN Fibre Blockpage. Matching on the Phone number, was worried that title would be too broad here.",
    ),

    SimpleBlockPagePattern(
        name="isp_id_bolt_sehat_blockpage",
        common_name="ID ISP Bolt! Blockpage",
        pattern="""UA-4293319-7""",
        location_found="body",
        source=[
            "https://www.bolt.id/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20170213T013637Z_AS4832_Y8ct5af944VzPhrMoeoll3Ap7MtHL97R2JBO0lEHto45vPYwFQ?input=http://www.gayscape.com",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["ID"],
        notes="Indonesian ISP Bolt! Blockpage. Matching on the analytics tracker ID the blockpage used in 2017.",
    ),

    SimpleBlockPagePattern(
        name="isp_id_fastnet_sehat_blockpage_1",
        common_name="ID ISP First Media Fastnet Blockpage",
        pattern="""internetsehatdanamanfastnet.html""",
        location_found="body",
        source=[
            "https://www.firstmedia.com/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20161031T235715Z_AS23700_3cxMXOKGRHBMQly8HBD4vFHM3qRsMKtzc5Yl8Dcm8LVeQasRLj?input=http://www.bglad.com",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["ID"],
        notes="Indonesian ISP First Media Fastnet block page.",
    ),

    SimpleBlockPagePattern(
        name="isp_id_fastnet_sehat_blockpage_2",
        common_name="ID ISP First Media Fastnet Blockpage",
        pattern="""var pname='internet-sehat';""",
        location_found="body",
        source=[
            "https://www.firstmedia.com/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20191124T035958Z_AS23700_qdrRmnIMyFi0rfhj3OnrSb94TDyu7uRcw9vRTM1mjghyJGnAJW?input=http://ilga.org/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["ID"],
        notes="Indonesian ISP First Media Fastnet block page. This is a variant based on a different pattern in js",
    ),

    SimpleBlockPagePattern(
        name="isp_id_gmedia_xblock_blockpage",
        common_name="ID ISP First Media Fastnet Blockpage",
        pattern="""xblock.gmedia.net.id""",
        location_found="body",
        source=[
            "https://gmedia.net.id/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20190301T020519Z_AS55666_zcD5kLAL3QHZypge7Kppqp2ysd5p76afVPmvC7XlZ8zol52iEl?input=http://ilga.org/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["ID"],
        notes="Indonesian ISP GMedia blockpage. ",
    ),

    SimpleBlockPagePattern(
        name="isp_id_crypto_negatifkonten_blockpage",
        common_name="ID ISP Crypto Blockpage",
        pattern="""http://crypto.net.id/images/crypto_emblem.png""",
        location_found="body",
        source=[
            "http://crypto.net.id/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20170309T010546Z_AS131755_CXFUVwBIsB3jPdgrbAzOsELHeTsrb92fj97zsHrNrO86it0RA1?input=http://www.bglad.com",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["ID"],
        notes="Indonesian ISP Crypto block page.  This appears to be a business focused ISP.",
    ),

    SimpleBlockPagePattern(
        name="isp_id_jlm_negatifkonten_blockpage",
        common_name="ID ISP JLM Negatif Content Blockpage",
        pattern="""<title>Negatif Konten</title>""",
        location_found="body",
        source=[
            "https://jlm.net.id/",
        ],
        exp_url ="",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["ID"],
        notes="Indonesian ISP JLM  negatif konten block pages",
    ),

    SimpleBlockPagePattern(
        name="isp_id_starnet_sehat_blockpage",
        common_name="ID ISP Megavision/Starnet Sehat Block",
        pattern="""<a href=http://megavision.net.id>StarNet Project</a></strong> - DNS Filter Project.""",
        location_found="body",
        source=[
            "http://megavision.net.id/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190323T072437Z_AS0_pvl7biYGsLZDaHODVWbZ1PHC3iijtVfwM4a7BmBOd3YCg8705w?input=http://www.tsroadmap.com",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["ID"],
        notes="Indonesian ISP Starnet forward to the block page.",
    ),

    SimpleBlockPagePattern(
        name="isp_id_citranet_sehat_forward",
        common_name="ID ISP Citranet Sehat Block",
        pattern="""filter.citra.net.id""",
        location_found="header",
        source=[
            "https://www.citra.net.id/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20170920T165858Z_AS17974_3WOOOvd6aU5LlWGoP1mVIXMiXBDXaJpAwfkjP4IYR52V0nXvDF?input=http://transsexual.org",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["ID"],
        notes="Indonesian ISP Citranet forward to the block page.",
    ),

    SimpleBlockPagePattern(
        name="isp_id_citranet_sehat_block",
        common_name="ID ISP Citranet Sehat Block",
        pattern="""filter.citra.net.id""",
        location_found="body",
        source=[
            "https://www.citra.net.id/"
        ],
        exp_url ="",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["ID"],
        notes="Indonesian ISP Citranet block page.",
    ),

    SimpleBlockPagePattern(
        name="isp_id_citranet_sehat_block_2017",
        common_name="ID ISP Citranet Sehat Block",
        pattern="""UA-18076037-2""",
        location_found="body",
        source=[
            "https://www.citra.net.id/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20171010T001639Z_AS17974_DRF1cmT5lEsJdMlrkJ6xtFk4FW4zwAJHmf0eYBmCzoNFFHSgua?input=http://www.bglad.com",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["ID"],
        notes="Indonesian ISP Citranet block page circa 2017 before it began using the filter.citra.net.id naming.",
    ),

    SimpleBlockPagePattern(
        name="isp_id_indosatooredo_forward1",
        common_name="ID ISP Indosat/Ooredo Block",
        pattern="""114.6.128.7""",
        location_found="header",
        source=[
            "https://indosatooredoo.com/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190602T174828Z_AS4761_YOEBG2rWEL90gfaLLyKNI3kBNU5RjG5ryZ5b3LPd81ayu8oW31?input=http://www.gayegypt.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["ID"],
        notes="Indonesian ISP Indosat/Ooredo forward to the block page. Chain goes 114.6.128.7->netsafe.indosatooredoo.com",
    ),

    SimpleBlockPagePattern(
        name="isp_id_indosatooredo_forward2",
        common_name="ID ISP Indosat/Ooredo Block",
        pattern="""netsafe.indosatooredoo.com""",
        location_found="header",
        source=[
            "https://indosatooredoo.com/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200213T135057Z_AS4761_0VqghBlufZfB6k68FBcGkeU9XAUcCmfXguHZJGBJhaQfurl2do?input=http://www.grindr.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["ID"],
        notes="Indonesian ISP Indosat/Ooredo forward to the block page. Chain goes 114.6.128.7->netsafe.indosatooredoo.com",
    ),

    SimpleBlockPagePattern(
        name="isp_id_indosatooredo_block_1",
        common_name="ID ISP Indosat/Ooredo Block",
        pattern="""<title>Indosatooredoo Netsafe</title>""",
        location_found="body",
        source=[
            "https://indosatooredoo.com/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200213T135057Z_AS4761_0VqghBlufZfB6k68FBcGkeU9XAUcCmfXguHZJGBJhaQfurl2do?input=http://www.grindr.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["ID"],
        notes="Indonesian ISP Indosat/Ooredo block page.",
    ),

    SimpleBlockPagePattern(
        name="isp_id_indosatooredo_block_2",
        common_name="ID ISP Indosat/Ooredo Block",
        pattern="""<title>Netsafe IndosatM2</title>""",
        location_found="body",
        source=[
            "https://indosatooredoo.com/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20170403T000118Z_AS4795_ZGyxgVEVzoRMZpL4QlHyPZtmJOwAO26NUv1Op3Vh6fCv7XIAW3?input=http://www.ifge.org",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["ID"],
        notes="Indonesian ISP Indosat/Ooredo block page. This is a different title to match against compared to the _1 variant."
              "I believe this is before they merged.",
    ),

    SimpleBlockPagePattern(
        name="isp_id_indosatooredo_block_js_variant",
        common_name="ID ISP Indosat/Ooredo Block",
        pattern="""http://netsafe.indosatooredoo.com""",
        location_found="body",
        source=[
            "https://indosatooredoo.com/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200213T135057Z_AS4761_0VqghBlufZfB6k68FBcGkeU9XAUcCmfXguHZJGBJhaQfurl2do?input=http://www.grindr.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["ID"],
        notes="Indonesian ISP Indosat/Ooredo block page. This is made to catch the variant of the blockpage which does a JS forward",
    ),

    SimpleBlockPagePattern(
        name="isp_id_argon_block",
        common_name="ID ISP Argon (Data Centre) Block",
        pattern="""argon_files/stop.jpg""",
        location_found="body",
        source=[
            "http://www.argon.id/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20170501T123218Z_AS17974_TQovh9GvtBR3FlRa5IfIH19tSRfiGUgUzEnGoh5sgdLI1m0OgY?input=http://www.ifge.org",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["ID"],
        notes="Indonesian ISP Argon (Data Centre) Block",
    ),

    SimpleBlockPagePattern(
        name="isp_id_myrepublic_forward",
        common_name="ID ISP MyRepublic Block",
        pattern="""block.myrepublic.co.id""",
        location_found="header",
        source=[
            "https://myrepublic.co.id/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190905T165736Z_AS63859_PeIPMNtOMVuCacZ3pJmR3RySVKbNArcUTaKTPPLgPddZXwN2KC?input=http://www.queernet.org/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["ID"],
        notes="Indonesian ISP MyRepublic forward to the block page.",
    ),

    SimpleBlockPagePattern(
        name="isp_id_myrepublic_block",
        common_name="ID ISP MyRepublic Block",
        pattern="""https://myrepublic.co.id/internet-sehat/""",
        location_found="body",
        source=[
            "https://myrepublic.co.id/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190905T165736Z_AS63859_PeIPMNtOMVuCacZ3pJmR3RySVKbNArcUTaKTPPLgPddZXwN2KC?input=http://www.queernet.org/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["ID"],
        notes="Indonesian ISP MyRepublic block page.",
    ),

    SimpleBlockPagePattern(
        name="isp_id_telkomsel_forward",
        common_name="ID ISP Telkomsel Block",
        pattern="""internetbaik.telkomsel.com/block?""",
        location_found="header",
        source=[
            "https://www.telkomsel.com/en"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200130T135811Z_AS23693_d5uipVzMCxrQlnNCO4cB3ZxZYk4CyYZWr8ipsdgC8Qzp4K2Bl9?input=http://www.bglad.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["ID"],
        notes="Indonesian ISP Telkomsel forward to the block page.",
    ),

    SimpleBlockPagePattern(
        name="isp_id_telkomsel_block_baik_1",
        common_name="ID ISP Telkomsel Block",
        pattern="""internetbaik.telkomsel.com/""",
        location_found="body",
        source=[
            "https://www.telkomsel.com/en"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200130T135811Z_AS23693_d5uipVzMCxrQlnNCO4cB3ZxZYk4CyYZWr8ipsdgC8Qzp4K2Bl9?input=http://www.bglad.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["ID"],
        notes="Indonesian ISP Telkomsel block page.",
    ),

    SimpleBlockPagePattern(
        name="isp_id_telkomsel_block_baik_2",
        common_name="ID ISP Telkomsel Block",
        pattern="""telkomsel|internet sehat|baik|internet baik""",
        location_found="body",
        source=[
            "https://www.telkomsel.com/en"
        ],
        exp_url="https://explorer.ooni.org/measurement/20170316T024318Z_AS23693_CQPxlyILeqGXlHzFqGSCPR6MgtCBfZtbs3h2l37MOyiU77N1xP?input=http://www.bglad.com",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["ID"],
        notes="Indonesian ISP Telkomsel block page. This is for the variant that does not use internetbaik.telkomsel.com subdomain. "
              "Matches based on metacontent",
    ),

    SimpleBlockPagePattern(
        name="isp_id_xl_forward",
        common_name="ID ISP XL Block",
        pattern="""blockpage.xl.co.id""",
        location_found="header",
        source=[
            "https://www.xl.co.id/id"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20180308T104910Z_AS24203_nhfe7SS0mYB7NFo906daTIuBIz5qPAue9LDvWSAw7p2E3hjUna?input=http://www.tsroadmap.com",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["ID"],
        notes="Indonesian ISP XL forward to the block page.",
    ),

    SimpleBlockPagePattern(
        name="isp_id_xl_block",
        common_name="ID ISP XL Block",
        pattern="""www.xl.co.id/xlblockpage""",
        location_found="body",
        source=[
            "https://www.xl.co.id/id"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190307T051144Z_AS131472_7RLBdzGBIF3RPC6UcuV9HJAMkysGP4IR9JkfwfhCSXuieZQtAq?input=http://www.tsroadmap.com",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["ID"],
        notes="Indonesian ISP XL block page.",
    ),

    SimpleBlockPagePattern(
        name="isp_id_xl_block_2",
        common_name="ID ISP XL Block",
        pattern="""blockpage.xl.co.id""",
        location_found="body",
        source=[
            "https://www.xl.co.id/id"
        ],
        exp_url="https://explorer.ooni.org/measurement/20170412T174345Z_AS24203_qlNBUtI6cL4DZGjeNWLOQ5puycMYiMol71agNH5Qvg1WmSAWzL?input=http://www.bglad.com",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["ID"],
        notes="Indonesian ISP XL block page.  Sometimes there is a header forward here (see isp_id_xl_forward) but other "
              "times the forward is done in the body content as http-equiv refresh",
    ),

    SimpleBlockPagePattern(
        name="isp_id_biznet_block",
        common_name="ID ISP Biznet Block",
        pattern="""www.biznetnetworks.com/safesurf/""",
        location_found="body",
        source=[
            "https://www.biznetnetworks.com/id/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190727T045744Z_AS17451_kC7sYnleU6DzAOhrgOf4LXXvtois6M4GnEpgvFCcFP0taBcuIU?input=http://www.gayhealth.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["ID"],
        notes="Indonesian ISP Biznet block page.",
    ),

    SimpleBlockPagePattern(
        name="isp_id_velo_block",
        common_name="ID ISP Velo Networks Block",
        pattern="""VELO Networks :: Internet Sehat dan Aman""",
        location_found="body",
        source=[
            "https://velo.co.id/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190905T052510Z_AS24207_I540tCMJL3Wtb3cJ4oOCQaH7Fv44n2rn8kLkMubuSLLipSctue?input=http://www.gayegypt.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["ID"],
        notes="Indonesian ISP Velo Networks block page.",
    ),

    SimpleBlockPagePattern(
        name="isp_id_tri_forward",
        common_name="ID ISP Tri Block",
        pattern="""restricted.tri.co.id""",
        location_found="header",
        source=[
            "https://tri.co.id/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20191005T031241Z_AS45727_93jXiGYrI1w8wHNC9FVzF5zuylmtgOToSGsA0mgYubk132ZKuV?input=http://www.nclrights.org/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["ID"],
        notes="Indonesian ISP XL forward to the block page.",
    ),

    SimpleBlockPagePattern(
        name="isp_id_tri_block",
        common_name="ID ISP Tri Block",
        pattern="""restricted.tri.co.id/""",
        location_found="body",
        source=[
            "https://tri.co.id/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20191005T031241Z_AS45727_93jXiGYrI1w8wHNC9FVzF5zuylmtgOToSGsA0mgYubk132ZKuV?input=http://www.nclrights.org/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["ID"],
        notes="Indonesian ISP XL block page.",
    ),

    SimpleBlockPagePattern(
        name="isp_id_lintasarta_block",
        common_name="ID ISP Lintasarta Block",
        pattern="""<title>IdOLA Lintasarta</title>""",
        location_found="body",
        source=[
            "https://www.lintasarta.net/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190605T140849Z_AS4800_bKVUk4pjoLXBQOUdWBLnQOPZfWfDPGCSoURwopRoEj0O4ZjOKG?input=http://www.tsroadmap.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP lintasarta block page Done via dns to domain dnsfilter2.idola.net.id.
              This appears to be a TrustPositif list based DNS filter but customized to the ISP""",
    ),

    SimpleBlockPagePattern(
        name="isp_kr_sktelecom_youthhazard_optin_forward_1",
        common_name="KR ISP SK Telecom Youth Hazard Block",
        pattern="""cleanmobile01.nate.com""",
        location_found="body",
        source=[
            "https://www.sktelecom.com/index.html"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20181227T081659Z_AS4766_7o3rxATU3P7DL8LCWRZU4t84ZionEuDMZwlOwFv1v1JqjKr57r?input=http://www.utopia-asia.com",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["KR"],
        notes="South Korean ISP SK Telecom forward to a block page titled Youth Hazard Block <machine translation>",
    ),

    SimpleBlockPagePattern(
        name="isp_kr_sktelecom_youthhazard_optin_forward_2",
        common_name="KR ISP SK Telecom Youth Hazard Block",
        pattern="""cleanmobile02.nate.com""",
        location_found="body",
        source=[
            "https://www.sktelecom.com/index.html"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20181011T032321Z_AS4766_I8APdOqg57wWTVKRvpZJ0uDaHbzHlcrmD3cpmrKuQrJXFsrcnU?input=http://www.gayegypt.com",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["KR"],
        notes="South Korean ISP SK Telecom forward to a block page titled Youth Hazard Block <machine translation>",
    ),

    SimpleBlockPagePattern(
        name="isp_kr_sktelecom_youthhazard_optin_block",
        common_name="KR ISP SK Telecom Youth Hazard Block",
        pattern="""<title>청소년 유해차단서비스</title>""",
        location_found="body",
        source=[
            "https://www.sktelecom.com/index.html"
        ],
        exp_url ="",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["KR"],
        notes="South Korean ISP SK Telecom forward to a block page titled Youth Hazard Block <machine translation>",
    ),

    SimpleBlockPagePattern(
        name="isp_np_worldlink_forward",
        common_name="NP ISP Worldlink Block",
        pattern="""blockdomain.worldlink.com.np""",
        location_found="header",
        source=[
            "https://thenextweb.com/insider/2018/10/01/nepal-blocks-porn-sites-after-spate-of-sexual-assaults/#:~:targetText=Last%20month%2C%20Nepal's%20government%20issued,rising%20number%20of%20rape%20cases.",
            "https://apnews.com/9977d94dacd94c76a032bf89a220b35f/Nepal-says-it-has-blocked-25,000-websites-in-pornography-ban"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20191118T090209Z_AS17501_cqniUNeXAKeoabJN6Zr7EwpuebIM4f7g2fCAZqN0SfYOuMZMcD?input=http://www.newnownext.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["NP"],
        notes="NP ISP Worldlink Forward to Block",
    ),

    SimpleBlockPagePattern(
        name="isp_np_worldlink_block",
        common_name="NP ISP Worldlink Block",
        pattern="""nta.gov.np/en/notice-regarding-site-block""",
        location_found="body",
        source=[
            "https://thenextweb.com/insider/2018/10/01/nepal-blocks-porn-sites-after-spate-of-sexual-assaults/#:~:targetText=Last%20month%2C%20Nepal's%20government%20issued,rising%20number%20of%20rape%20cases.",
            "https://apnews.com/9977d94dacd94c76a032bf89a220b35f/Nepal-says-it-has-blocked-25,000-websites-in-pornography-ban"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20191118T090209Z_AS17501_cqniUNeXAKeoabJN6Zr7EwpuebIM4f7g2fCAZqN0SfYOuMZMcD?input=http://www.newnownext.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["NP"],
        notes="NP ISP Worldlink Forward to Block",
    ),

    SimpleBlockPagePattern(
        name="isp_ye_yemennet_ns_forward_1",
        common_name="YE ISP Yemennet Block",
        pattern="""http://82.114.160.94/webadmin/deny/""",
        location_found="body",
        source=[
            "https://adsl.yemen.net.ye/"
        ],
        exp_url ="",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["YE"],
        notes="YE ISP Yemennet Block.  This matches IP iframe forward of the Netsweeper box",
    ),

    SimpleBlockPagePattern(
        name="isp_ye_yemennet_ns_forward_2",
        common_name="YE ISP Yemennet Block",
        pattern="""http://deny.yemen.net.ye/webadmin/deny""",
        location_found="body",
        source=[
            "https://adsl.yemen.net.ye/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190104T220611Z_AS30873_kt947qO6Y9Hl4z6vwpmVq7G4psKKkNjEhJffySOv7sDGYoRbgZ?input=http://amygoodloe.com/lesbian-dot-org/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["YE"],
        notes="YE ISP Yemennet Block.  This matches the DNS variant of the iframe forward of the Netsweeper box",
    ),

    SimpleBlockPagePattern(
        name="isp_kr_lg_cleanweb_optin_forward",
        common_name="KR ISP LG U Plus Cleanweb Block",
        pattern="""http://cleanweb1.uplus.co.kr/kren""",
        location_found="header",
        source=[
            "http://uplus.co.kr/home/Index.hpi"
        ],
        exp_url ="",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["KR"],
        notes="KR ISP LG U Plus Cleanweb Block",
    ),


    SimpleBlockPagePattern(
        name="isp_de_vodafone_optin_forward",
        common_name="DE ISP Vodafone Optin Block",
        pattern="""hotspot.vodafone.de/access_denied.html""",
        location_found="header",
        source=[
            "https://www.jugendschutzprogramm.de/eltern/#website_melden"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200127T113040Z_AS31334_f2WzvfEf8rj0X645IsaTmrojbWpB4VpU48c7TRifHnwrEPT1J7?input=http://www.nclrights.org/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["DE"],
        notes="DE ISP Vodafone Optin Forward to Block",
    ),

    SimpleBlockPagePattern(
        name="isp_de_vodafone_optin_block",
        common_name="DE ISP Vodafone Optin Block",
        pattern="""The Website you try to access is only recommended for persons over the age of 18.""",
        location_found="body",
        source=[
            "https://www.jugendschutzprogramm.de/eltern/#website_melden"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200127T113040Z_AS31334_f2WzvfEf8rj0X645IsaTmrojbWpB4VpU48c7TRifHnwrEPT1J7?input=http://www.nclrights.org/",
        confidence_no_fp=8,
        scope="isp",
        expected_countries=["DE"],
        notes="DE ISP Vodafone Optin Block",
    ),

    SimpleBlockPagePattern(
        name="isp_ca_shaw_courtblock",
        common_name="CA ISP Shaw Block Page for Court Order",
        pattern="""Access to this site has been blocked by an Order issued by the Federal Court of Canada""",
        location_found="body",
        source=[
            "https://mobilesyrup.com/2019/11/18/federal-court-order-isps-block-piracy-service/"
        ],
        exp_url ="",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["CA"],
        notes="CA ISP Shaw Block Page for Court Order",
    ),

    SimpleBlockPagePattern(
        name="isp_ca_rogers_courtblock",
        common_name="CA ISP Rogers Block Page for Court Order",
        pattern="""Access to the location you have attempted to reach has been disabled pursuant to an Order&nbsp;of the Federal Court (Canada)""",
        location_found="body",
        source=[
            "https://mobilesyrup.com/2019/11/18/federal-court-order-isps-block-piracy-service/"
        ],
        exp_url ="",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["CA"],
        notes="CA ISP Shaw Block Page for Court Order",
    ),

    SimpleBlockPagePattern(
        name="isp_th_dtac_accessurlblock_forward",
        common_name="TH ISP DTAC Block",
        pattern="""http://124.40.225.20/?accessurl=""",
        location_found="body",
        source=[
            "http://www.dtac.co.th/home.html"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200213T120219Z_AS24378_W6w9AwtqzGx0p9Rr4O83ktxhRHZJk9lQWutj6k5bndi208V4lA?input=http://www.gboysiam.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["TH"],
        notes="""
            TH ISP DTAC Blockpage Forward with IFrame using AccessURL device.  This was attributed to DTAC
            because the blockpage IP is on that ASN for DTAC.
        """,
    ),

    SimpleBlockPagePattern(
        name="isp_th_cxloxinfo_accessurlblock_forward",
        common_name="TH ISP CSLox Info Block",
        pattern="""http://103.208.24.21/?accessurl=""",
        location_found="body",
        source=[
            "https://www.csloxinfo.com/"
        ],
        exp_url ="",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["TH"],
        notes="""
            TH ISP CSLoxInfo Blockpage Forward with IFrame using AccessURL. This was attributed to CSLox because
            block page IP is on that ASN POP-IDC powerby CxLox
        """,
    ),

    SimpleBlockPagePattern(
        name="isp_gb_pobroadband_virusguard_forward",
        common_name="GB ISP Post Office Broadband VirusGuard Block",
        pattern="""http://account.pobroadband.co.uk/SelfCare.UI/SafeGuard/VirusGuard?accessurl=""",
        location_found="body",
        source=[
            "https://account.pobroadband.co.uk/SelfCare.UI"
        ],
        exp_url ="",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["GB"],
        notes="""
            GB ISP Post Office Broadband Blockpage Forward with IFrame using AccessURL. This is for an anti-malware
            blocking service.
        """,
    ),

    SimpleBlockPagePattern(
        name="isp_gb_talktalk_virusalert_forward",
        common_name="GB ISP TalkTalk Virus Alert Block",
        pattern="""http://www.talktalk.co.uk/notices/virus-alerts.html?accessurl=""",
        location_found="body",
        source=[
            "https://www.talktalk.co.uk/"
        ],
        exp_url ="",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["GB"],
        notes="""
            GB ISP TalkTalk Blockpage Forward with IFrame using AccessURL. This is for an anti-malware
            blocking service.
        """,
    ),

    SimpleBlockPagePattern(
        name="isp_pk_mobillink_block_forward",
        common_name="PK ISP Mobillink Block",
        pattern="""http://119.73.65.87:8080/redirect.html?accessurl=""",
        location_found="body",
        source=[
            "https://jazz.com.pk/"
        ],
        exp_url ="",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["PK"],
        notes="""
            PK ISP Mobillink (now Jazz) Blockpage Forward with IFrame using AccessURL.
        """,
    ),

    SimpleBlockPagePattern(
        name="isp_pk_nayatel_block_optin",
        common_name="PK ISP Nayatel Opt In Block",
        pattern="""As per your subscription of Nayatel Safeweb service, the website you are trying to access is blocked for your viewing""",
        location_found="body",
        source=[
            "https://nayatel.com/safe-web/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200215T032555Z_AS23674_baOoSlSUE3rUC8Vtezp4K1QuLCGKasBKezHCHAmQvKnsOUDfel?input=http://www.globalgayz.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["PK"],
        notes="""
        PK ISP Nayatel Safeweb Blockpage - Opt in filter.
        """,
    ),

    SimpleBlockPagePattern(
        name="isp_bh_batelco_block_forward",
        common_name="BH ISP Batelco Block",
        pattern="""www.anonymous.com.bh""",
        location_found="body",
        source=[
            "https://citizenlab.ca/2016/09/tender-confirmed-rights-risk-verifying-netsweeper-bahrain/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200103T214930Z_AS5416_Cb0eigi9DgBdD9lrQfZLTSckVYANzKDOzI5LSd9yPbFcJNEUuT?input=http://www.gay.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["BH"],
        notes="""
        BH ISP Batelco Netsweeper Blockpage via anonymous.com.bh
        """,
    ),

    SimpleBlockPagePattern(
        name="isp_bh_viva_block_forward",
        common_name="BH ISP VIVA Block",
        pattern="""www.viva.com.bh/static/block""",
        location_found="body",
        source=[
            "https://citizenlab.ca/2016/09/tender-confirmed-rights-risk-verifying-netsweeper-bahrain/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20180821T225240Z_AS51375_arIbEdkOsq47wsCE8tRpJWQuIeDN8adphRYo1e76drI3rZWRWr?input=http://gaytoday.com",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["BH"],
        notes="""
        BH ISP VIVA Blockpage via http://www.viva.com.bh/static/block
        """,
    ),

    SimpleBlockPagePattern(
        name="isp_bh_mena_telecom_block_forward",
        common_name="BH ISP Mena Telecom Block",
        pattern="""menatelecom.com/deny_page.html""",
        location_found="body",
        source=[
            "https://citizenlab.ca/2016/09/tender-confirmed-rights-risk-verifying-netsweeper-bahrain/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20170220T113603Z_AS39015_Lamk4jT9RlMfeIjwMbg4oi8xBU67dBgnWwzD7Nb4UhihIaR0Ap?input=http://gaytoday.com",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["BH"],
        notes="""
        BH ISP MENA Telecom Blockpage via http://www.viva.com.bh/static/block
        """,
    ),

    SimpleBlockPagePattern(
        name="isp_kw_fasttelco_block_forward",
        common_name="KW ISP Fast Telecom Block",
        pattern="""blocked.fasttelco.net/?dpid=""",
        location_found="body",
        source=[
            "https://www.fasttelco.net/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20180424T055755Z_AS21050_QLeo5RlFyonKjcaYnvSrqnR7RGqxhhWjruATjHvNKO8CkQreyV?input=http://www.gayscape.com",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["KW"],
        notes="""
        KW ISP FastTelco Blockpage which is a Netsweeper device
        """,
    ),

    SimpleBlockPagePattern(
        name="isp_kw_zain_block_forward",
        common_name="KW ISP Zain Block",
        pattern="""http://restrict.kw.zain.com""",
        location_found="body",
        source=[
            "https://www.kw.zain.com/ar/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190119T193411Z_AS42961_SQB6LNLFohvV3rpS64yaMnpxRQQnzB27maZudlZJxy0wpVUQFe?input=http://gaytoday.com",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["KW"],
        notes="""
        KW ISP Zain Blockpage forward which is a netsweeper device via http://restrict.kw.zain.com:8080/webadmin/deny/index.php
        """,
    ),

    SimpleBlockPagePattern(
        name="isp_kw_viva_block_forward",
        common_name="KW ISP Viva Block",
        pattern="""http://pay.viva.com.kw/images/access-en.jpg""",
        location_found="body",
        source=[
            "http://viva.com.kw/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190323T153406Z_AS47589_XNLYup0tsRncJtSX00WpeMPXC3VZWJhiCFjx5FWLZzCfNhZHk1?input=http://gaytoday.com/",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["KW"],
        notes="""
        KW ISP VIVA Blockpage forward
        """,
    ),

    SimpleBlockPagePattern(
        name="isp_in_airtel_block_forward",
        common_name="IN ISP Airtel Block",
        pattern="""http://www.airtel.in/dot/?dpid=""",
        location_found="body",
        source=[
            "https://www.airtel.in/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20170704T113906Z_AS24560_wfOnnh9CsrttSEJuRH2QRnOhMxICg8j1yVQRMkMd6V54d3qCgS?input=http://www.gayegypt.com",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["IN"],
        notes="""
        IN ISP Airtel Blockpage forward with Netsweeper device
        """,
    ),

    SimpleBlockPagePattern(
        name="isp_sd_sudatel_tpra_block_forward",
        common_name="SD ISP Sudatel Block",
        pattern="""/webadmin/deny/ptra/blocking.html""",
        location_found="body",
        source=[
            "https://www.sudatel.sd/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20181108T073326Z_AS33788_ZqpA2lJ2Rhs9pcjwp4fOIoDqNUMynmyBI5YKkaZI3c1HfDK1su?input=http://www.gayscape.com",
        confidence_no_fp=10,
        scope="isp",
        expected_countries=["SD"],
        notes="""
        SD ISP Sudatel Blockpage forward via a Netsweeper device
        """,
    ),

    # PROVIDER SIDE BLOCKS

    SimpleBlockPagePattern(
        name="prov_vkontakte_rkn_geoblock",
        common_name="VKontakte RKN GeoBlock",
        pattern="""://vk.com/blank.php?rkn=""",
        location_found="header",
        source=[
            "https://vk.com"
        ],
        exp_url="https://explorer.ooni.org/measurement/20200809T060553Z_AS6697_WHViLvwEDfLrt3yRqACQW09MnDhCy6jynycEEfObNuAApaBTpv?input=https://vk.com/pramenofanarchy",
        confidence_no_fp=10,
        scope="prov",
        expected_countries=["RU"],
        notes="""
        Russian social network Vkontakte implements geoblocks on certain pages by forwarding via url:
        https://vk.com/blank.php?rkn=<ID>
        
        If you are outside the target country you are forwarded to the page otherwise a blockpage is 
        presented (see: exp_url)
        """,
    ),

    # INSTITUTIONAL BLOCKS

    SimpleBlockPagePattern(
        name="inst_edu_id_telkomuniversity_forward",
        common_name="ID Institutional Block - Telkom University",
        pattern="""internet-sehat.telkomuniversity.ac.id""",
        location_found="header",
        source=[
            "https://telkomuniversity.ac.id/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180315T084438Z_AS133357_LeDGv9wMP20hFNfN2nqsvJxL1vUKOFZ0grMlnMJXACYHkmPLNB?input=http://www.ifge.org",
        confidence_no_fp=10,
        scope="inst",
        expected_countries=["ID"],
        notes="Indonesian University owned by the largest telco. Has a seperate filtering system. This matches the 30x forward to the blockpage",
    ),

    SimpleBlockPagePattern(
        name="inst_edu_id_telkomuniversity_block",
        common_name="ID Institutional Block - Telkom University",
        pattern="""<title>Internet Sehat Telkom University</title>""",
        location_found="body",
        source=[
            "https://telkomuniversity.ac.id/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180315T084438Z_AS133357_LeDGv9wMP20hFNfN2nqsvJxL1vUKOFZ0grMlnMJXACYHkmPLNB?input=http://www.ifge.org",
        confidence_no_fp=10,
        scope="inst",
        expected_countries=["ID"],
        notes="Indonesian University owned by the largest telco. Has a seperate filtering system. This matches the actual blockpage",
    ),

    SimpleBlockPagePattern(
        name="inst_edu_my_uitm_captiveportal_forward",
        common_name="ID Institutional Block - Univesiti Teknologi Mara",
        pattern="""https://wifi.uitm.edu.my""",
        location_found="header",
        source=[
            "https://uitm.edu.my/index.php/en/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20190829T162515Z_AS24020_0ezmhWkibgyIWMDFfSZmCMhLKQewB5r6nwsf53v7OqCbAMyKRi?input=http://gaytoday.com/",
        confidence_no_fp=10,
        scope="inst",
        expected_countries=["MY"],
        notes="Malaysian University captive portal",
    ),

    SimpleBlockPagePattern(
        name="inst_edu_my_uitm_captiveportal_login",
        common_name="ID Institutional Block - Univesiti Teknologi Mara",
        pattern="""https://wifi.uitm.edu.my""",
        location_found="body",
        source=[
            "https://uitm.edu.my/index.php/en/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20190829T162515Z_AS24020_0ezmhWkibgyIWMDFfSZmCMhLKQewB5r6nwsf53v7OqCbAMyKRi?input=http://gaytoday.com/",
        confidence_no_fp=10,
        scope="inst",
        expected_countries=["MY"],
        notes="Malaysian University captive portal",
    ),

    SimpleBlockPagePattern(
        name="inst_edu_sa_kacst_blockpage",
        common_name="SA Institutional Block - King Abdul Aziz City for Science and Technology",
        pattern="""://blocking-web-server.isu.net.sa/""",
        location_found="body",
        source=[
            "https://www.kacst.edu.sa/"
        ],
        exp_url="https://explorer.ooni.org/measurement/20180711T082508Z_AS15505_oTsIWsdnymUNFDsNnrCRIBb7hKzhU2GzmYv04oZvlUwQ2TicqG?input=http://gaytoday.com",
        confidence_no_fp=10,
        scope="inst",
        expected_countries=["SA"],
        notes="Saudi Center for Technology and Research blockpage",
    ),

    SimpleBlockPagePattern(
        name="inst_edu_taunton",
        common_name="Institutional Block - Taunton School",
        pattern="""Taunton School allow access to the following search engines""",
        location_found="body",
        source=[
            ""
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190523T171133Z_AS12513_H6Wc12khwbndgeJ9oKath0nvUZ4IeEcmNSCxmcTpYPe59MdSpV?input=http://www.grindr.com/",
        confidence_no_fp=10,
        scope="inst",
        expected_countries=["GB"],
        notes="Blockpage text seen in a preparatory school in South West England",
    ),

    SimpleBlockPagePattern(
        name="inst_edu_mn_public",
        common_name="Institutional Block - Minneapolis School",
        pattern="""https://staff.mpls.k12.mn.us/Depts/its/Pages/Block-Unblock-Requests.aspx""",
        location_found="body",
        source=[
            ""
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190205T194537Z_AS26638_xu2k6ZPnY9mHgeu3M6qgVGf1Q192E12OFtcpztNMDBleHkEJPM?input=http://www.grindr.com/",
        confidence_no_fp=10,
        scope="inst",
        expected_countries=["US"],
        notes="Blockpage text seen in a Minneapolis public school systems in the USA",
    ),

    SimpleBlockPagePattern(
        name="inst_edu_jeffco",
        common_name="Institutional Block - Jeffco School",
        pattern="""Jeffco Schools Internet Filtering Page""",
        location_found="body",
        source=[
            ""
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190321T164529Z_AS26661_gKN3hndB81x3e95ICECH0M7NVbk89s4pelMSjXFE3m89oA2F7p?input=http://www.gayegypt.com/",
        confidence_no_fp=10,
        scope="inst",
        expected_countries=["US"],
        notes="Public School in Colorado"
    ),

    SimpleBlockPagePattern(
        name="inst_corp_etisalat",
        common_name="Institutional Block - Minneapolis School",
        pattern="""it-security-operations@etisalat.ae""",
        location_found="body",
        source=[
            ""
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190708T075453Z_AS5384_VXPZQorUMS5VJxSy4BWbzITW3GGfQOWX9APTD9wBEJDCCDU4s5?input=http://gaytoday.com/",
        confidence_no_fp=9,
        scope="inst",
        expected_countries=["AE"],
        notes="Blockpage text seen in the Etisalat corporate blockpage which is a customized Websense",
    ),

    SimpleBlockPagePattern(
        name="inst_edu_runnet_forward",
        common_name="Institutional Block - RunNet Russian ISP Network",
        pattern="""block.runnet.ru""",
        location_found="header",
        source=[
            "https://runnet.ru/"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20180317T132423Z_AS51081_aZcek3lkL9VJGuaZN1Li0gUnBdcfjA0DDCM4Ed3lKvDWk24bK1?input=http://bluesystem.ru/",
        confidence_no_fp=10,
        scope="inst",
        expected_countries=["RU"],
        notes="Forward to a blockpage seen on RUNnet via DNS block.runnet.ru",
    ),

    SimpleBlockPagePattern(
        name="inst_edu_runnet_blockpage",
        common_name="Institutional Block - RunNet Russian ISP Network",
        pattern="""Dear user! Access to requested resource has been blocked by decision of public authorities of Russian Federation.""",
        location_found="header",
        source=[
            "https://runnet.ru/"
        ],
        exp_url ="",
        confidence_no_fp=7,
        scope="inst",
        expected_countries=["RU"],
        notes="Blockpage seen on RUNnet which has an english translation and a poem in the HTML comments.",
    ),

    SimpleBlockPagePattern(
        name="inst_corp_prometey_datacenter_blockpage",
        common_name="Institutional Block - Prometety Russian ISP Data Center",
        pattern="""zapret-info.prometey.me""",
        location_found="body",
        source=[
            "https://prometey.me/"
        ],
        exp_url="",
        confidence_no_fp=10,
        scope="inst",
        expected_countries=["RU"],
        notes="Blockpage seen on Prometey which is a data center and hosting provider in Russia.",
    ),

    # Suspicous - Suspected of Being a Block but With a High Likelihood of False Positives (typically no-render html and similar)

    SimpleBlockPagePattern(
        name="susp_blankhtml_1",
        common_name="Blank or No-Render HTML - Suspected Block",
        pattern="""<HTML></HTML>""",
        location_found="body",
        source=[
            ""
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200214T055338Z_AS9644_uqciOcQhoh9UyaaGyGKHWMhz3Yp5TbjMLT5lhJI6WR6zecwSmO?input=http://www.salganyc.org/",
        confidence_no_fp=5,
        scope="isp",
        expected_countries=[""],
        notes="Blank or No-Render HTML - Suspected Block",
    ),

    SimpleBlockPagePattern(
        name="susp_blankhtml_2",
        common_name="Blank or No-Render HTML - Suspected Block",
        pattern="""<html><body></body></html>""",
        location_found="body",
        source=[
            ""
        ],
        exp_url ="https://explorer.ooni.org/measurement/20181022T070006Z_AS6697_n0krMW0p7u9znXuMC8hP1Ta4iqtNI6Wla1MCZFUcxztm34bqSX?input=http://gayzona.com",
        confidence_no_fp=5,
        scope="isp",
        expected_countries=[""],
        notes="Blank or No-Render HTML - Suspected Block",
    ),

    SimpleBlockPagePattern(
        name="susp_blankhtml_3",
        common_name="Blank or No-Render HTML - Suspected Block",
        pattern="""<html><head></head><body><!-- vbe --></body></html>""",
        location_found="body",
        source=[
            ""
        ],
        exp_url ="https://explorer.ooni.org/measurement/20180321T011244Z_AS4766_Xac2i8753DmXqeNcy3X0MYdiqiQWQdDiP1uQ0t84gQQ4S9M0iH?input=http://koreapinkmap.com/",
        confidence_no_fp=5,
        scope="isp",
        expected_countries=[""],
        notes="Blank or No-Render HTML - Suspected Block",
    ),


    # Injections - Benign (injb)

    SimpleBlockPagePattern(
        name="injb_routerupdate",
        common_name="Injection Benign Router Update",
        pattern="""/main/fwUpInfoBlock.htm""",
        location_found="body",
        source=[
            "https://twitter.com/lucb1e/status/1160197669148614658"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190801T061900Z_AS51207_OWeMqPyEDS81UJKlXTX2KlnJ0PSh0vkpIa2RNSkMp82F1Ps56n?input=http://www.gmhc.org/",
        confidence_no_fp=10,
        scope="injb",
        expected_countries=[],
        notes="Common but benign injection that is done when router needs update"
    ),

    SimpleBlockPagePattern(
        name="injb_ru_mts_paybill",
        common_name="Injection Benign Router Update",
        pattern="""http://unblock.mts.ru""",
        location_found="header",
        source=[
            "https://twitter.com/lucb1e/status/1160197669148614658"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190606T115638Z_AS8359_1AxAk5m7nGRoC2uLKul3UzQhvjFxQhwfI5jpdEYqyegSAIghmh?input=http://instinctmagazine.com/",
        confidence_no_fp=10,
        scope="injb",
        expected_countries=["RU"],
        notes="Russian ISP MTS - Notice to pay bill"
    ),

    SimpleBlockPagePattern(
        name="injb_th_3bb_paybill",
        common_name="Thai ISP 3bb pay bill notice",
        pattern="""http://110.164.252.137/wpwarn/soft_bd/wpcbt_res.php""",
        location_found="header",
        source=[
            "https://pantip.com/topic/34029658"
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190314T223836Z_AS45758_saZmEbyWARgKDPY5FS8JmbrexGQAUUAHO0naE3K4jqMrEPuVfD?input=http://instinctmagazine.com/",
        confidence_no_fp=10,
        scope="injb",
        expected_countries=["TH"],
        notes="Thai ISP 3bb - Notice to pay bill"
    ),

    # Vague Blocking-ish Keywords

    SimpleBlockPagePattern(
        name="vbw_web_page_blocked",
        common_name="Vague Block Words",
        pattern="""Web Page Blocked""",
        location_found="body",
        source=[
            ""
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200213T165957Z_AS31242_dOxoMkg9lZqvXsFm9088Fywi7WcFyRSGpq8fHB3PYfDo1FUFtD?input=http://www.amnestyusa.org/the-state-of-lgbt-rights-worldwide/",
        confidence_no_fp=8,
        scope="vbw",
        expected_countries=[],
        notes="Just a vague word that is likely to be found in a blockpage"
    ),

    SimpleBlockPagePattern(
        name="vbw_webpage_blocked",
        common_name="Vague Block Words",
        pattern="""Webpage Blocked""",
        location_found="body",
        source=[
            ""
        ],
        exp_url ="",
        confidence_no_fp=8,
        scope="vbw",
        expected_countries=[],
        notes="Just a vague word that is likely to be found in a blockpage"
    ),

    SimpleBlockPagePattern(
        name="vbw_web_site_blocked",
        common_name="Vague Block Words",
        pattern="""Web Site Blocked""",
        location_found="body",
        source=[
            ""
        ],
        exp_url ="https://explorer.ooni.org/measurement/20190530T060325Z_AS9930_aFIp6ijOM0HCyMp1Zo0BA01CHkisHlohZcn9WmB3R43ijK8LYt?input=http://www.gayrice.com/",
        confidence_no_fp=8,
        scope="vbw",
        expected_countries=[],
        notes="Just a vague word that is likely to be found in a blockpage"
    ),

    SimpleBlockPagePattern(
        name="vbw_websiteblocked",
        common_name="Vague Block Words",
        pattern="""Website Blocked""",
        location_found="body",
        source=[
            ""
        ],
        exp_url ="https://explorer.ooni.org/measurement/20200215T002609Z_AS22616_M3OibwnD9Mun2WwDftbEOy5Iv2KI1lyjjsqaQaqF0W5UPKyPlA?input=http://www.gayhealth.com/",
        confidence_no_fp=8,
        scope="vbw",
        expected_countries=[],
        notes="Just a vague word that is likely to be found in a blockpage"
    ),

]