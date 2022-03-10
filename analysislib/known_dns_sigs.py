from analysislib.dns_matcher import SimpleDNSReplyPattern

known_dns_sigs = [

    #########
    # GENERIC NO-RESPONSE SIGS
    #########

    SimpleDNSReplyPattern(
        name="dns_br_localhost",
        response="127.0.0.1",
        confidence_no_fp=10,
        exp_url = "https://explorer.ooni.org/measurement/20160809T002715Z_AS4818_iyzGIP1lTXMuul1n2gqn5KveO8IEHWBprt04tul57KJS7mFutA?input=http://www.mygoodasyou.com",
        source=[

        ],
        scope="br",
        expected_countries=[],
        notes="""
        A localhost reply, by convention this is a standard way to block access to content with DNS servers
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_br_allzero",
        response="0.0.0.0",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20170214T000041Z_AS5769_GwfnRAZ0NLH0wT56sefg2xc2iB07m354tQ0dA6IIL8mRz1CTXZ?input=http://www.lesbian.org",
        source=[

        ],
        scope="br",
        expected_countries=[],
        notes="""
        A 0.0.0.0 reply, by convention this is a standard way to block access to content with DNS servers
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_br_1234",
        response="1.2.3.4",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20190612T013439Z_AS17974_XnyS9G0FWELa7uamYqu2zGxaYOQVrFFvlb9KmzbXlChVfY76uV?input=https://www.scruff.com/",
        source=[

        ],
        scope="br",
        expected_countries=[],
        notes="""
        An A record with a 1.2.3.4 reply, this is a common false response to restrict access.
        """
    ),

    #########
    # PRODUCT SCOPED RESPONSES
    #########

    SimpleDNSReplyPattern(
        name="dns_prod_fortidns",
        response="208.91.112.55",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20190404T082635Z_AS6661_WCvp1TnPzuxfEVQl2ZjgPGkDiLXre1Lenrp1cUiwEUJ1oEk6PV?input=https://www.scruff.com/",
        source=[
            "https://docs.fortinet.com/document/fortigate/6.0.0/cookbook/124730/troubleshooting",
            "https://docs.fortinet.com/product/fortidns/1.3"
        ],
        scope="prod",
        expected_countries=[],
        notes="""Fortinet FortiDNS product
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_prod_securely_1",
        response="204.110.220.2",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://www.securly.com/"
        ],
        scope="prod",
        expected_countries=[],
        notes="""DNS filtering product for schools
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_prod_securely_2",
        response="52.52.63.90",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://www.securly.com/"
        ],
        scope="prod",
        expected_countries=[],
        notes="""DNS filtering product for schools
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_prod_id_nawala",
        response="180.131.146.7",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20170214T023529Z_AS17974_1hVbJGBPLdOsxQvNgIawwvABxfZuLNeVK5VaY1XWajguEt0yK3?input=http://www.lesbian.org",
        source=[
            "https://nawala.id/"
        ],
        scope="prod",
        expected_countries=["ID"],
        notes="""Indonesian Sehat DNS filtering product
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_prod_opendns_1",
        response="146.112.61.106",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20170209T174739Z_AS1136_wBIk5bny3acHUuSTuZ8sqtFnKcU47tiRY0LEw08s9m9VDZBsO3?input=http://gayromeo.com",
        source=[
            "https://www.opendns.com/cisco-opendns/"
        ],
        scope="prod",
        expected_countries=[],
        notes="""Cisco OpenDNS a popular DNS filtering system.  NOTE: there is probably a more sophisticated way to track
        these IE - CNAME used in the redir.
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_prod_opendns_2",
        response="208.69.32.164",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20191007T155258Z_AS20115_DS8uyNobQ0CH9o9fls70ftC1ItOJ7dK5OlMG3YBs7NYrIXQ2Ty?input=https://www.planetromeo.com/",
        source=[
            "https://www.opendns.com/cisco-opendns/"
        ],
        scope="prod",
        expected_countries=[],
        notes="""Cisco OpenDNS a popular DNS filtering system.  NOTE: there is probably a more sophisticated way to track
        these IE - CNAME used in the redir.
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_prod_ru_netpolice",
        response="159.255.26.69",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "http://www.netpolice.ru/"
        ],
        scope="prod",
        expected_countries=["RU"],
        notes="""Russian DNS based RKN filtering proudct.
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_prod_cleanbrowsing_1",
        response="185.228.168.254",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20190824T132919Z_AS5650_gwWRIicciG8fgrTzTFnuvsmlAHFOWgiAIAuDeL9RgH05TQsY3L?input=http://www.samesexmarriage.ca/",
        source=[
            "https://cleanbrowsing.org/"
        ],
        scope="prod",
        expected_countries=[""],
        notes="""Cleanbrowsing DNS content filter
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_prod_cleanbrowsing_2",
        response="207.246.127.171",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://cleanbrowsing.org/"
        ],
        scope="prod",
        expected_countries=[""],
        notes="""Cleanbrowsing DNS content filter
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_prod_cleanbrowsing_3",
        response="45.77.77.148",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://cleanbrowsing.org/"
        ],
        scope="prod",
        expected_countries=[""],
        notes="""Cleanbrowsing DNS content filter
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_prod_flashstart",
        response="185.236.104.104",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20180212T093619Z_AS12874_ivZ63xkT6Tqmlz8SyoIsbdkQNfN85CyNZTO1ZVeYTZFRh24xb8?input=http://www.gayscape.com",
        source=[
            "https://flashstart.com/"
        ],
        scope="prod",
        expected_countries=[""],
        notes="""Security focused DNS content filter
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_prod_smartdns_proxy",
        response="54.242.237.204",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://www.smartdnsproxy.com/Services"
        ],
        scope="prod",
        expected_countries=[""],
        notes="""A geoip avoidance/unblocking DNS service
    """
    ),

    SimpleDNSReplyPattern(
        name="dns_prod_skydns_1",
        response="193.58.251.1",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20171003T161217Z_AS15599_eoh3aUHQ7NV5LwWDA3Br8Hf3FGcgxG3s8mjxFd40cSWcV5BL23?input=http://lgbt.foundation/",
        source=[
            "https://www.skydns.ru/"
        ],
        scope="prod",
        expected_countries=["RU"],
        notes="""Russian DNS filter product
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_prod_skydns_2",
        response="193.58.251.11",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://www.skydns.ru/"
        ],
        scope="prod",
        expected_countries=["RU"],
        notes="""Russian DNS filter product
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_prod_skydns_3",
        response="95.217.66.240",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://www.skydns.ru/"
        ],
        scope="prod",
        expected_countries=["RU"],
        notes="""Russian DNS filter product
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_prod_cloudveil",
        response="45.32.203.129",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://www.cloudveil.org/"
        ],
        scope="prod",
        expected_countries=[""],
        notes="""Faith focused DNS filtering system provided by the Church of God in Christ, Mennonite.
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_prod_dnswatch_1",
        response="3.93.224.57",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://www.watchguard.com/wgrd-products/security-services/dnswatch"
        ],
        scope="prod",
        expected_countries=[""],
        notes="""Security focused DNS filter provided by WatchGuard Technologies
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_prod_dnswatch_2",
        response="52.206.227.167",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://www.watchguard.com/wgrd-products/security-services/dnswatch"
        ],
        scope="prod",
        expected_countries=[""],
        notes="""Security focused DNS filter provided by WatchGuard Technologies
    """
    ),

    SimpleDNSReplyPattern(
        name="dns_prod_safedns",
        response="195.46.39.11",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20191115T114711Z_AS12390_NIVFbxg8nx3pPxL5vbk2Fg4duFANRINLyvIaMNuzyDPiMdY2X3?input=https://bisexual.org/",
        source=[
            "https://www.safedns.com/en/"
        ],
        scope="prod",
        expected_countries=[""],
        notes="""SafeDNS filtering for home, edu, telecom.  Cloud based filtering product.
    """
    ),


    SimpleDNSReplyPattern(
        name="dns_prod_yandex_security_check",
        response="93.158.134.250",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20180919T192809Z_AS34984_Rlb0RqQAPfo5LqUQHWREV7c1sxNXcHSGHrVftNTgOoVBhAcu20?input=http://www.exgay.com",
        source=[
            "https://yandex.ru/safety/"
        ],
        scope="prod",
        expected_countries=["RU"],
        notes="""Yandex Check Site Security Status Response
        """
    ),

    #########
    # ISP SCOPED RESPONSES
    #########

    SimpleDNSReplyPattern(
        name="dns_isp_ca_shaw_block",
        response="64.59.135.158",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20220203T170239Z_webconnectivity_CA_6327_n1_3Qts0KFGq9BAcnb1?input=http%3A%2F%2Fdestv.me%2F",
        source=[
            "",
        ],
        scope="isp",
        expected_countries=["CA"],
        notes="""Canadian ISP Shaw blockpage"""
    ),


    SimpleDNSReplyPattern(
        name="dns_isp_ca_rogers_tva_telus_block",
        response="67.43.226.22",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20220203T103332Z_webconnectivity_CA_812_n1_7M7ZYtu8kInk4dU3?input=http%3A%2F%2Fapp.atntvv.cc%2F",
        source=[
            "",
        ],
        scope="isp",
        expected_countries=["CA"],
        notes="""CA ISP Rogers Telus and TVA Group joint Block Page"""
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_ca_rogers_tva_telus_block_2",
        response="173.209.39.114",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20220125T183515Z_webconnectivity_CA_577_n1_7mS6xLPAnfcGIgv4?input=http://app.atntvv.cc/",
        source=[
            "",
        ],
        scope="isp",
        expected_countries=["CA"],
        notes="""CA ISP Rogers Telus and TVA Group joint Block Page, alternate IP"""
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_ca_teksavvy_block",
        response="206.248.146.244",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20220203T004625Z_webconnectivity_CA_5645_n1_cGktKcvMOwO7Tr20?input=http%3A%2F%2Fapp.atntvv.cc%2F",
        source=[
            "",
        ],
        scope="isp",
        expected_countries=["CA"],
        notes="""CA ISP Teksavvy Block Page"""
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_au_telstra_block_1",
        response="101.167.166.53",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20220203T193446Z_webconnectivity_AU_1221_n1_E32NLhLwI1WJYE3p?input=http%3A%2F%2Fthepiratebay.org%2F",
        source=[
            "",
        ],
        scope="isp",
        expected_countries=["AU"],
        notes="""AU ISP Telstra Block Page"""
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_au_telstra_block_2",
        response="101.167.164.53",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20220203T193446Z_webconnectivity_AU_1221_n1_E32NLhLwI1WJYE3p?input=http%3A%2F%2Fthepiratebay.org%2F",
        source=[
            "",
        ],
        scope="isp",
        expected_countries=["AU"],
        notes="""AU ISP Telstra Block Page"""
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_au_tpg_block",
        response="202.136.99.184",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20220202T100548Z_webconnectivity_AU_7545_n1_jIoirPJjohcYOCvM?input=http%3A%2F%2Fthepiratebay.org%2F",
        source=[
            "https://www.lifehacker.com.au/2018/06/how-to-bypass-isp-blocking-of-the-pirate-bay-and-other-torrent-sites-for-free/",
        ],
        scope="isp",
        expected_countries=["AU"],
        notes="""AU ISP TPG Block Page"""
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_mm_myanmarnet_block",
        response="59.153.90.11",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20210208T105603Z_webconnectivity_MM_58952_n1_NEm53Iw0ysgcGt9J?input=http://www.facebook.com",
        source=[
            "http://myanmarnet.com/",
        ],
        scope="isp",
        expected_countries=["MM"],
        notes="""Myanmar ISP Myanmarnet blockpage"""
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_sg_starhub_block",
        response="202.156.3.53",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20210809T082132Z_webconnectivity_SG_55430_n1_7ImHaJauRVvTo2eF?input=http://www.playboy.com/",
        source=[
            "",
        ],
        scope="isp",
        expected_countries=["SG"],
        notes="""Singaporean ISP Starhub blockpage"""
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_pk_nayatel_surfsafely",
        response="203.82.48.83",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20161025T235721Z_AS23674_Lldjua1VqHuWrRcILrD3wrfRXiOVP5P3e0wHwJV1MACuOzBFwY?input=http://www.queerty.com",
        source=[
            "https://nayatel.com/"
        ],
        scope="isp",
        expected_countries=["PK"],
        notes="""Pakistani ISP Nayatels Surf Safely blockpage
    """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_pk_nayatel_safeweb",
        response="203.82.48.86",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20191206T015807Z_AS23674_BbXvUMwowxajbM9Q1pTeOp84pawo9ccTUsltC6B1vhyNHC2kkM?input=http://gaytoday.com/",
        source=[
            "https://nayatel.com/"
        ],
        scope="isp",
        expected_countries=["PK"],
        notes="""Pakistani ISP Nayatels Safeweb blockpage
"""
    ),

    #########
    # TURKISH RELATED RESPONSES
    #########

    SimpleDNSReplyPattern(
        name="dns_isp_tr_turknet_familyprofile",
        response="193.192.98.41",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://turk.net/"
        ],
        scope="isp",
        expected_countries=["TR"],
        notes="""Turkish ISP Turk Net optin family oriented DNS service 
        (this is DIFFERENT than the Turk Telecom secureinternet)
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_tr_turknet_socialmedia",
        response="193.192.98.42",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://turk.net/"
        ],
        scope="isp",
        expected_countries=["TR"],
        notes="""Turkish ISP Turk Net optin family oriented DNS service 
        (this is DIFFERENT than the Turk Telecom secureinternet)
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_tr_turknet_chat",
        response="193.192.98.43",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://turk.net/"
        ],
        scope="isp",
        expected_countries=["TR"],
        notes="""Turkish ISP Turk Net optin family oriented DNS service 
        (this is DIFFERENT than the Turk Telecom secureinternet)
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_tr_turknet_game",
        response="193.192.98.45",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://turk.net/"
        ],
        scope="isp",
        expected_countries=["TR"],
        notes="""Turkish ISP Turk Net optin family oriented DNS service 
        (this is DIFFERENT than the Turk Telecom secureinternet)
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_tr_turknet_chat_and_socialmedia",
        response="193.192.98.46",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://turk.net/"
        ],
        scope="isp",
        expected_countries=["TR"],
        notes="""Turkish ISP Turk Net optin family oriented DNS service 
        (this is DIFFERENT than the Turk Telecom secureinternet)
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_tr_turknet_game_and_socialmedia",
        response="193.192.98.47",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://turk.net/"
        ],
        scope="isp",
        expected_countries=["TR"],
        notes="""Turkish ISP Turk Net optin family oriented DNS service 
        (this is DIFFERENT than the Turk Telecom secureinternet)
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_tr_turknet_game_and_chat",
        response="193.192.98.48",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://turk.net/"
        ],
        scope="isp",
        expected_countries=["TR"],
        notes="""Turkish ISP Turk Net optin family oriented DNS service 
    (this is DIFFERENT than the Turk Telecom secureinternet)
    """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_tr_turknet_game_chat_socialmedia",
        response="193.192.98.49",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://turk.net/"
        ],
        scope="isp",
        expected_countries=["TR"],
        notes="""Turkish ISP Turk Net optin family oriented DNS service 
        (this is DIFFERENT than the Turk Telecom secureinternet)
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_by_mts",
        response="134.17.0.7",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://www.mts.by/",
            "https://explorer.ooni.org/measurement/20200808T195507Z_AS25106_hY9xbufjqUKiqPI5LZJ4IqiwfGMNcaOdrtKnwCaXADPRhSOL8J?input=http://intimby.net/"
        ],
        scope="isp",
        expected_countries=["BY"],
        notes="""
        Belarusian ISP block on mobile ISP MTS uses a DNS forward
        """
    ),

    #########
    # RUSSIAN RKN RELATED RESPONSES
    #########

    SimpleDNSReplyPattern(
        name="dns_isp_rostelecom_blocksystem",
        response="217.148.54.171",
        confidence_no_fp=7,
        exp_url="",
        source=[
            "https://rt.ru/"
        ],
        scope="isp",
        expected_countries=["RU"],
        notes="""
        Russian ISP Rostelecom but the filtering pattern is very different than what
        customers typically see.  This might be a small downstream players RKN
        implementation.
    """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_ru_rkn_skynet",
        response="185.37.129.10",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20190628T034744Z_AS35807_4XwiNixlQ8odJ6ek21IUmKwtvCecSOWoII5ZjwqzCCgx6Sx9a3?input=http://bluesystem.ru/",
        source=[
            "https://www.sknt.ru/"
        ],
        scope="isp",
        expected_countries=["RU"],
        notes="""
            Russian ISP Skynet RKN blockpage
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_ru_rkn_zencom",
        response="46.175.31.250",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://zencom.ru/"
        ],
        scope="isp",
        expected_countries=["RU"],
        notes="""
        Russian ISP Zencom RKN blockpage
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_ru_rkn_naukanet",
        response="46.175.31.250",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20200318T090603Z_AS8641_sZfld8WLVRMRZ6Oa6uj23WNddUJ5zFCFLL5JCNBqorFDn1P050?input=http://www.lesbi.ru/",
        source=[
            "https://www.naukanet.ru/"
        ],
        scope="isp",
        expected_countries=["RU"],
        notes="""
        Russian ISP Nauka-Svyaz RKN blockpage
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_ru_rkn_mastertel",
        response="83.69.208.124",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "http://mastertel.ru/"
        ],
        scope="isp",
        expected_countries=["RU"],
        notes="""
            Russian ISP Mastertel (business focused, telecom provider, datacenters, etc) RKN blockpage
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_ru_rkn_netbynet",
        response="212.1.226.59",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "http://www.netbynet.ru/"
        ],
        scope="isp",
        expected_countries=["RU"],
        notes="""Russian ISP NetByNet RKN blockpage
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_ru_rkn_smoltelecom",
        response="37.44.40.254",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "http://smoltelecom.ru/"
        ],
        scope="isp",
        expected_countries=["RU"],
        notes="""Russian ISP Smoltelecom blockpage
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_ru_rkn_enforta",
        response="87.241.223.133",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://www.enforta.ru/"
        ],
        scope="isp",
        expected_countries=["RU"],
        notes="""Russian ISP Enforta blockpage
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_ru_rkn_ertelecom",
        response="5.3.3.17",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20180313T233202Z_AS51645_dIEFx0okmP7iqOXN3x1p97EObb6Z1oLDQYOHFLVvfn7c0FKRW6?input=http://bluesystem.ru/",
        source=[
            "https://ertelecom.ru/"
        ],
        scope="isp",
        expected_countries=["RU"],
        notes="""Russian ISP Ertelecom  RKN blockpage
    """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_ru_AS52207",
        response="188.186.157.49",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20220305T120459Z_webconnectivity_RU_52207_n1_AlXw32CjmNRv0WxI?input=http%3A%2F%2Fwww.bbc.com%2Fnews",
        source=[
            ""
        ],
        scope="isp",
        expected_countries=["RU"],
        notes="""
        PTR record is k8s-lb-onlyhttp-cluster-ingress.static.cc.ertelecom.ru.
        Serves blockpage for: http://lawfilter.ertelecom.ru/
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_ru_AS51547",
        response="80.76.104.20",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20220304T163214Z_webconnectivity_RU_51547_n1_oUciU7VqaGrmL4HA?input=https%3A%2F%2Fwww.bbc.com%2Fnews%2Fworld-51235105",
        source=[
            ""
        ],
        scope="isp",
        expected_countries=["RU"],
        notes="""
        PTR records are block.tdsplus.ru & balance.tdsplus.ru.
        We get connection refused when attempting to access it.
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_ru_AS8790",
        response="85.142.29.248",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20220305T121053Z_webconnectivity_RU_8790_n1_OfI9eozoHc8C4Xkd?input=http%3A%2F%2Fwww.bbc.com%2Fnews",
        source=[
            ""
        ],
        scope="isp",
        expected_countries=["RU"],
        notes="""
        PTR record is block.runnet.ru.
        We get a blockpage when attempting to access it.
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_ru_AS35807",
        response="100.64.64.66",
        confidence_no_fp=7,
        exp_url="https://explorer.ooni.org/measurement/20220305T121024Z_webconnectivity_RU_35807_n1_QkCl4ZggAoowPpAI?input=http%3A%2F%2Fwww.bbc.com%2Fnews",
        source=[
            ""
        ],
        scope="isp",
        expected_countries=["RU"],
        notes="""
        Private IP space, but behaviour is consistent on AS35807 for blocked domains.
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_ru_AS15378",
        response="95.213.158.61",
        confidence_no_fp=7,
        exp_url="https://explorer.ooni.org/measurement/20220305T053351Z_webconnectivity_RU_15378_n1_wsIzPXq2OLRTBIAq?input=http%3A%2F%2Fwww.bbc.com",
        source=[
            ""
        ],
        scope="isp",
        expected_countries=["RU"],
        notes="""
        AS of returned IP is mapped to russian hosting provider AS49505 (SELECTEL).
        Pattern is consistent for several blocked sites.
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_ru_AS8427",
        response="188.43.20.67",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20220305T035626Z_webconnectivity_RU_8427_n1_6zMQbsKYAsOva4L7?input=https%3A%2F%2Fwww.bbc.com%2Frussian%2F",
        source=[
            ""
        ],
        scope="isp",
        expected_countries=["RU"],
        notes="""
        Serves a blockpage for ttk ISP
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_ru_AS52207_2",
        response="195.128.72.3",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20220304T055948Z_webconnectivity_RU_52207_n1_H0I8CD7nFoMYXxCx?input=https%3A%2F%2Fwww.bbc.com%2F",
        source=[
            ""
        ],
        scope="isp",
        expected_countries=["RU"],
        notes="""
        Serves a blockpage
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_ru_AS12389",
        response="31.28.24.3",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20220304T044651Z_webconnectivity_RU_12389_n1_BmRicVwEpc4HG72k?input=https%3A%2F%2Fwww.bbc.com%2F",
        source=[
            ""
        ],
        scope="isp",
        expected_countries=["RU"],
        notes="Serves a blockpage for citytelecom.ru"
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_ru_AS197460",
        response="46.175.31.251",
        confidence_no_fp=8,
        exp_url="https://explorer.ooni.org/measurement/20220305T044706Z_webconnectivity_RU_197460_n1_moH7izWEhyf8UJ81?input=https%3A%2F%2Fwww.bbc.com%2Fnews",
        source=[
            ""
        ],
        scope="isp",
        expected_countries=["RU"],
        notes="""
        Likely used to be a blockpage. The PTR record is
        host-46-175-31-251.rev.zencom.ru and the AS is AS197460, which is
        consistent with the network where we observe it.
        As of 2022-03-05 the session times out when attempting to fetch the
        index via HTTP (port 80 is open though).
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_ru_AS3335",
        response="84.237.49.190",
        confidence_no_fp=8,
        exp_url="https://explorer.ooni.org/measurement/20220304T062438Z_webconnectivity_RU_3335_n1_mn3OTB1761hQW6PB?input=https%3A%2F%2Fwww.bbc.com%2F",
        source=[
            ""
        ],
        scope="isp",
        expected_countries=["RU"],
        notes="""
        PTR record host190.49.237.84.nsu.ru and AS is AS3335.
        As of 2022-03-05 a 503 error is returned when accessing page.
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_ru_AS212614",
        response="62.33.207.197",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20220303T144538Z_webconnectivity_RU_212614_n1_GNQli0Mie4NBJrkp?input=https%3A%2F%2F200rf.com%2F",
        source=[
            ""
        ],
        scope="isp",
        expected_countries=["RU"],
        notes="""
        netname of the ip range is "TTK-SECURITY". As of 2022-03-05 you get
        connection refused when connecting to port 80.
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_ru_AS212614_2",
        response="62.33.207.196",
        confidence_no_fp=8,
        exp_url="https://explorer.ooni.org/measurement/20220303T144538Z_webconnectivity_RU_212614_n1_GNQli0Mie4NBJrkp?input=https%3A%2F%2F200rf.com%2F",
        source=[
            ""
        ],
        scope="isp",
        expected_countries=["RU"],
        notes="""
        netname of the ip range is "TTK-SECURITY". As of 2022-03-05 you get
        connection refused when connecting to port 80.
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_ru_AS60139",
        response="185.77.150.2",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20220303T120931Z_webconnectivity_RU_60139_n1_RqlkvqFzTf9cySzI?input=https%3A%2F%2Fwww.currenttime.tv%2Ftv%2Fschedule%2F92%2F",
        source=[
            ""
        ],
        scope="isp",
        expected_countries=["RU"],
        notes="Serves a cute cat blockpage"
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_ru_AS42429",
        response="77.238.226.53",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20220302T003421Z_webconnectivity_RU_42429_n1_4xzf7tPugdylxlAj?input=https%3A%2F%2Fwww.currenttime.tv%2Ftv%2Fschedule%2F92%2F",
        source=[
            ""
        ],
        scope="isp",
        expected_countries=["RU"],
        notes="Serves a blockpage"
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_ru_AS8369",
        response="78.29.1.40",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20220301T122933Z_webconnectivity_RU_8369_n1_M8IHOk8AdoWew7sE?input=https%3A%2F%2Fwww.currenttime.tv%2F",
        source=[
            ""
        ],
        scope="isp",
        expected_countries=["RU"],
        notes="""
        ASN of the IP is AS8369, which is consistent with the network of the
        measurement. Connections timeout when attempting to establish a
        connection on port 80.
        """
    ),

    #########
    # INDONESIAN SEHAT RELATED RESPONSES

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_telkomsel_baik",
        response="202.3.219.209",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20170316T024318Z_AS23693_CQPxlyILeqGXlHzFqGSCPR6MgtCBfZtbs3h2l37MOyiU77N1xP?input=http://www.bglad.com",
        source=[
            "http://telkomsel.com/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Telkomsel Internet Baik sehat blockpage
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_tri_cname",
        response="restricted.tri.co.id",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20200329T090119Z_AS45727_GqQe4DZduLsSaYZB6qnqeMpsNgJn7dTvEaoEFZ0eGGmjyBoQG4?input=https://www.scruff.com/",
        source=[
            "https://tri.co.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Tri blockpage, matches on the CNAME 
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_tri_ip",
        response="116.206.10.31",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20200329T090119Z_AS45727_GqQe4DZduLsSaYZB6qnqeMpsNgJn7dTvEaoEFZ0eGGmjyBoQG4?input=https://www.scruff.com/",
        source=[
            "https://tri.co.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Tri blockpage, matches on the IP
    """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_telkom_uzone",
        response="36.86.63.185",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20171025T095349Z_AS131709_vvCnDreaVjMN1MQ2imNyl4ynBG4EhIZRdWHJIBKgOexJSnaWcb?input=http://www.bglad.com",
        source=[
            "https://uzone.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Telkom Uzone sehat blockpage
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_telkom_uzone_mercusuar",
        response="internet-positif.org",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20191114T004142Z_AS17974_zSo1qO4rG5Isd8Rr2WGTHYV4hwK9jeGkR201ACNu7np3CxXqOQ?input=http://ilga.org/",
        source=[
            "https://uzone.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Telkom Uzone sehat blockpage. Mercusuar (lighthouse) is a branding of Telkomsel's Uzone. 
        This matches the CNAME record but IP was 118.97.116.27 at the time observed. 
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_telkom_bltsel_cname",
        response="mypage.blocked.bltsel",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20191114T004142Z_AS17974_zSo1qO4rG5Isd8Rr2WGTHYV4hwK9jeGkR201ACNu7np3CxXqOQ?input=http://ilga.org/",
        source=[
            "https://uzone.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Telkom blockpage. This is to match against the variant where Telkomsel DNS reply
        to this CNAME and was on IP 114.121.254.4
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_telkom_bltsel_ip",
        response="114.121.254.4",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20191114T004142Z_AS17974_zSo1qO4rG5Isd8Rr2WGTHYV4hwK9jeGkR201ACNu7np3CxXqOQ?input=http://ilga.org/",
        source=[
            "https://uzone.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Telkom blockpage. This is to match against the variant where Telkomsel DNS reply
        to CNAME mypage.blocked.bltsel and IP 114.121.254.4
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_tri_blockpage",
        response="180.214.232.61",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20170307T194134Z_AS45727_gEN976jgNQgOx6CuLiiYDb2flPY8CpNtRPcnrHTwjggcats4At?input=http://www.gay.com",
        source=[
            "https://tri.co.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Tri sehat blockpage.
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_bolt_block",
        response="202.62.29.1",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20170213T013637Z_AS4832_Y8ct5af944VzPhrMoeoll3Ap7MtHL97R2JBO0lEHto45vPYwFQ?input=http://www.gayscape.com",
        source=[
            "https://www.bolt.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Bolt"""
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_myrepublic_block",
        response="103.47.132.195",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20170916T151028Z_AS63859_OMzXkgk31oMZMCyxyswHDc9s7PcHYUDMAm8BEsKSmcioamnK0f?input=http://www.gayscape.com",
        source=[
            "https://myrepublic.co.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP My Republic"""
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_cbn_block",
        response="internetsehataman.cbn.net.id",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20190420T092536Z_AS135478_mLOlXUu4n0QwTV10X6nqZYFwh9aQga4i4fPo9fMomwk2IMV6Le?input=http://transsexual.org/",
        source=[
            "https://cbn.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP CBN"""
    ),


    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_xl_block",
        response="blockpage.xl.co.id",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20180324T031959Z_AS24203_oRMW0HPO6Z2u3lkA8d4uROtqX2fuKU6XH8ARB0JtGanxPSHX3L?input=https://www.scruff.com/",
        source=[
            "https://www.xl.co.id/id"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""
        Indonesian ISP XL blockpage. This is to match against the CNAME IP was 112.215.197.131
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_crypto_negatif",
        response="202.52.141.98",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "http://crypto.net.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Crypto DNS filtering (Negatif Konten)"""
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_jlm_negatif",
        response="150.107.140.200",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://jlm.net.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP JLM DNS filtering (Negatif Konten)"""
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_starnet_light",
        response="103.14.16.18",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20181006T114052Z_AS9657_yU1pa9b0I0vRzcBU5OsWOV6phrI2FBxQosem0mJRQdKZupCPkE?input=http://bisexual.org/",
        source=[
            "http://megavision.net.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Starnet DNS filtering (light variant)"""
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_starnet_dark",
        response="113.197.108.236",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20170620T000111Z_AS0_5is0TiDSWSWQSmW01Yc1B4kQFQsMmPhLT2vKSqFsVhuYzbPYvd?input=http://www.gayscape.com",
        source=[
            "http://megavision.net.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Starnet DNS filtering (dark variant)"""
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_citra",
        response="202.65.113.54",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20170920T165858Z_AS17974_3WOOOvd6aU5LlWGoP1mVIXMiXBDXaJpAwfkjP4IYR52V0nXvDF?input=http://www.advocate.com",
        source=[
            "https://citrahost.com//"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Citra blockpage
    """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_argon",
        response="103.195.19.54",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20170501T123218Z_AS17974_TQovh9GvtBR3FlRa5IfIH19tSRfiGUgUzEnGoh5sgdLI1m0OgY?input=http://www.ifge.org",
        source=[
            "http://www.argon.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Argon (Datacentre) blockpage
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_sumberdata",
        response="103.10.120.3",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "http://www.sumberdata.co.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Sumber Data blockpage
    """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_fibernet",
        response="27.123.220.197",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "http://fiber.net.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Fibernet blockpage
    """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_gooptix",
        response="103.108.159.238",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "http://connectivist.co.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Go-Optix blockpage
    """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_ltn",
        response="103.126.10.252",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "http://www.ltn.co.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Lintas Telematika Nusantara blockpage
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_utaramedia",
        response="103.142.60.250",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://utaramedia.net/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Utara Internet blockpage
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_bitsnet",
        response="103.19.56.2",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://bits.net.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Bitsnet blockpage
    """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_winetmedia",
        response="103.70.68.68",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "http://winetmedia.net/id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Winnet Media blockpage
    """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_foxlinemedia",
        response="103.83.96.242",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "http://www.foxline.net.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Foxline Media blockpage
    """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_hypernet_1",
        response="114.129.22.33",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20170323T040824Z_AS38758_zjtAoJrqVgnQCOYSHGqrVt4bSHxEUGnj0DvgJqHEJMKnnmllir?input=http://transsexual.org",
        source=[
            "https://hypernet.co.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Hypernet blockpage
    """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_hypernet_2",
        response="114.129.23.9",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://hypernet.co.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Hypernet blockpage
    """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_netsafeindosat_1",
        response="netsafe.indosatm2.com",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20170330T110102Z_AS4795_yod1sqqu9NwrIBlJDfMepLmyAp3zVxQK5QG6Qqux11QuioLrYJ?input=https://www.gay.com/",
        source=[
            "http://indosatm2.com/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Indosat Netsafe blockpage.  This is based off the CNAME record but was seen on IP 124.81.92.132
    """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_netsafeindosat_2",
        response="114.6.128.8",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20170608T035018Z_AS4761_HEJ2bT3U6QBEL4IdHLTPpWshehej9EcxiwssgeMxRTlBLQeLJx?input=http://www.glil.org",
        source=[
            "http://indosatm2.com/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Indosat Netsafe blockpage
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_nusanet",
        response="150.107.151.151",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://www.nusa.net.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Nusa Net blockpage
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_myrepublic",
        response="158.140.186.3",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20180601T040605Z_AS63859_uzo47992c80YC59mVTgn649d8nTkGPtm3Z8TZ69jdWAmMMMkCb?input=http://www.samesexmarriage.ca",
        source=[
            "https://myrepublic.co.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP MyRepublic blockpage
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_firstmedia",
        response="internetpositif3.firstmedia.com",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20190612T150505Z_AS23700_e7qsqPDY72QkdwPcDeUb5NkHxZ9HgpHOuU8p5oNFp5uW4BJAk7?input=https://www.shoe.org/",
        source=[
            "https://www.firstmedia.com/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP FirstMedia blockpage. Matches against a CNAME record IP was 202.137.1.74 when observed.
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_melsa",
        response="filter.melsa.net.id",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20181006T114052Z_AS9657_yU1pa9b0I0vRzcBU5OsWOV6phrI2FBxQosem0mJRQdKZupCPkE?input=http://www.bglad.com",
        source=[
            "https://www.melsa.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Melsa blockpage. Matches the CNAME record IP was 202.138.224.15
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_ptcentrin",
        response="block.centrin.net.id",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20190314T214950Z_AS17658_kybYxwcXIxWZYnX32z36B1ZprSLxFT3WpxY0g7sfuy0Uy7MLAo?input=https://www.ilga-europe.org/",
        source=[
            "http://www.centrin.net.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP PT Centrin Online blockpage. Matches the CNAME record, the IP was 202.146.255.7
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_lintasarta",
        response="202.152.4.67",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20190605T140849Z_AS4800_bKVUk4pjoLXBQOUdWBLnQOPZfWfDPGCSoURwopRoEj0O4ZjOKG?input=http://www.tsroadmap.com/",
        source=[
            "https://www.lintasarta.net/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian Business ISP Lintasarta blockpage
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_circleone",
        response="202.165.36.253",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "http://www.circleone.net.id/about/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Circle One blockpage
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_biznet",
        response="202.169.44.80",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20171105T072208Z_AS17451_7r3LG7AAcL538QaLjG44o23fmyWhbFiEOWEnbZfDhu1Lfpg6jF?input=http://www.grindr.com/",
        source=[
            "https://www.biznetnetworks.com/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Biznet blockpage
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_starcom",
        response="202.50.202.50",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://www.starcoms.net/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Starcom blockpage
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_iforte",
        response="trustpositif.iforte.net.id",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20190924T072134Z_AS17995_Seinciq0527hnzfIuN4ZQvKYqy8NKBKGHK9vt01KkY79iofutj?input=http://www.gayhealth.com/",
        source=[
            "https://www.iforte.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP iForte blockpage. Matches a CNAME record IP was 202.51.96.7
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_varnion_1",
        response="202.56.160.131",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20180119T081053Z_AS45287_NWeT8zKRcKd7z2WYMntHuw2GIwqK0zCAh0A5UnvxzKw4s9rN0u?input=http://www.gayhealth.com",
        source=[
            "https://www.varnion.com/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP (caters to hospitality industry) Varnion blockpage. Note: Does a very weird round robin with 
        a local hostname (just filter)
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_varnion_2",
        response="202.56.160.132",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20180119T081053Z_AS45287_NWeT8zKRcKd7z2WYMntHuw2GIwqK0zCAh0A5UnvxzKw4s9rN0u?input=http://www.gayhealth.com",
        source=[
            "https://www.varnion.com/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP (caters to hospitality industry) Varnion blockpage. Note: Does a very weird round robin with 
        a local hostname (just filter)
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_varnion_3",
        response="203.99.130.131",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20180224T051609Z_AS45287_IoqMH28cD0RwJsIYHmj0rMDUt8oigefrA7YweS4lZ0ahxrDrDy?input=http://www.gay.com/",
        source=[
            "https://www.varnion.com/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP (caters to hospitality industry) Varnion blockpage. Note: Does a very weird round robin with 
        a local hostname (just filter)
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_idnic_1",
        response="203.119.13.75",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20171120T160605Z_AS0_J83hVqCVk4VUk9IGei68s4rSrT0F9OWHa3EzXwz6iJaHcxCO6J?input=https://www.gay.com/",
        source=[
            "https://www.idnic.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian NIC blockpage
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_idnic_2",
        response="203.119.13.76",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20200130T121354Z_AS18103_6roxhkcpVP4ML3VyjL75G28deYvsJgocbDyeV8Ud6WBHAFTwy4?input=http://www.bglad.com/",
        source=[
            "https://www.idnic.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian NIC blockpage
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_hanastar",
        response="203.160.56.38",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "http://www.hanastar.net.id/en/index.php"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Hanastar ID blockpage
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_comnets",
        response="220.247.168.195",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20200213T075343Z_AS131111_n3Zv50ZiRaGIm7uCn3IwOIN879EzYbr3OV08aHpZdOIzsk83iT?input=https://www.ilga-europe.org/",
        source=[
            "http://www.iconpln.co.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Icon Comnets+ blockpage.
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_transhybrid_1",
        response="58.147.184.141",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://transhybrid.net.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Trans Hybrid blockpage
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_transhybrid_2",
        response="58.147.185.131",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://transhybrid.net.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Trans Hybrid blockpage
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_first",
        response="202.73.99.3",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20161003T063421Z_AS23700_BcAJiWTdgtzSTE5ezaPJoywgMdwm8hZm8yb6Hw3iUB8atIiJCI?input=http://transsexual.org",
        source=[
            "https://www.firstmedia.com/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP First Media blockpage"""
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_gmedia_cname",
        response="xblock.gmedia.net.id",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20190301T020519Z_AS55666_zcD5kLAL3QHZypge7Kppqp2ysd5p76afVPmvC7XlZ8zol52iEl?input=http://ilga.org/",
        source=[
            "https://gmedia.net.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP GMedia blockpage. Matches CNAME record with an IP of 49.128.177.13 when observed."""
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_gmedia_ip",
        response="49.128.177.13",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20180119T133726Z_AS55666_NfgRumGXxCBp0t0SjoNsX0KyrzzmQmoXbSoXzPfHgw9ICwI5zr?input=http://www.queernet.org",
        source=[
            "https://gmedia.net.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP GMedia blockpage. Matches cases where IP is used instead of CNAME."""
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_smartfren",
        response="internetsehat.smartfren.com",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20191225T231001Z_AS18004_hA8xsVHcbUOLZLKxI8kAQ2GV3yzQ8TpDNqUpHA1Sm3Mdb3yYVB?input=http://www.samesexmarriage.ca/",
        source=[
            "https://www.smartfren.com/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Smartfren blockpage."""
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_mncplay",
        response="internetpositif.mncplaymedia.com",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20180727T095622Z_AS17670_ryQ3v3ZDI2X8YI7FKTxeG9L5PEmgc0Z5N3bDIU7uusFaaIcuql?input=http://www.bglad.com",
        source=[
            "https://www.mncplay.id/en/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP MNC Play Media blockpage. Based on CNAME record although the IP address was 110.50.83.31 when seen."""
    ),

    SimpleDNSReplyPattern(
        name="dns_inst_id_sehat_telkomuniversity",
        response="dnssehat.telkomuniversity.ac.id",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20180315T084438Z_AS133357_LeDGv9wMP20hFNfN2nqsvJxL1vUKOFZ0grMlnMJXACYHkmPLNB?input=http://transsexual.org",
        source=[
            "https://telkomuniversity.ac.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian University, owned by PT Telekom, but has a seperate filtering system"""
    ),

    #

    #########
    # NATIONAL-SCOPED RESPONSES
    #########

    SimpleDNSReplyPattern(
        name="dns_nat_mm_transportcomms_block",
        response="167.172.4.60",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20210201T223944Z_webconnectivity_MM_133385_n1_LlJnFqnaVXNfXygL?input=http://www.hornybank.com/",
        source=[
            "https://ooni.org/post/2020-myanmar-blocks-websites-amid-covid19/"
        ],
        scope="nat",
        expected_countries=["MM"],
        notes="""
        A false DNS response with Ministry of Transport and Communications of Myanmar branding.
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_nat_th_mdes_illegal",
        response="125.26.170.3",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20201228T234534Z_webconnectivity_TH_131445_n1_deRHboYpdtGToSqk?input=http://www.bbc.com/news/world-asia-38126928/",
        source=[
            "https://www.matichon.co.th/politics/news_2396830/attachment/%E0%B8%97%E0%B8%A7%E0%B8%B5%E0%B8%953"
        ],
        scope="nat",
        expected_countries=["TH"],
        notes="""
        A false DNS response with Thai Ministry of Digital Economy and Society branding, suggesting this 
        site is illegal based on the computer crime act and gambling act.
        """
    ),

    # https://explorer.ooni.org/measurement/20201201T083449Z_webconnectivity_FR_3215_n1_XEo8R2qog4e2Qegg?input=http://khilafah.net/


    SimpleDNSReplyPattern(
        name="dns_nat_my_violates",
        response="175.139.142.25",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20190503T024619Z_AS4788_agTXVdX7lipOjGFLnaQQFSkxEMVNoXopd20czlazmSW5XIofs4?input=http://www.gaystarnews.com/",
        source=[
            "https://github.com/ooni/pipeline/issues/35"
        ],
        scope="nat",
        expected_countries=["MY"],
        notes="""
            This website is not available in Malaysia as it violate(s) the National law(s). DNS response
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_nat_mn_crc",
        response="218.100.84.78",
        confidence_no_fp=10,
        exp_url="",
        source=[
            ""
        ],
        scope="nat",
        expected_countries=["MN"],
        notes="""
            Mongolian block due to legal reasoning.
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_nat_tr_poison",
        response="195.175.254.2",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://www.bortzmeyer.org/files/bortzmeyer-google-dns-turkey.pdf",
            "https://labs.ripe.net/Members/emileaben/a-ripe-atlas-view-of-internet-meddling-in-turkey"
            "https://twitter.com/isik5/status/449915384762605568?lang=en",
            "https://www.abuseipdb.com/check/195.175.254.2",
            "https://eksisozluk.com/195-175-254-2--4192251"
        ],
        scope="nat",
        expected_countries=["TR"],
        notes="""
        A poisoned DNS reply used in Turkey since 2014
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_nat_it_adm_block",
        response="217.175.53.72",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20211023T083841Z_webconnectivity_IT_30722_n1_hPb937VUDh5Q2NoY?input=http://www.sportingbet.com/",
        source=[
            ""
        ],
        scope="nat",
        expected_countries=["IT"],
        notes="""
        Italian sport/gaming related DNS block
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_nat_it_agcom_block",
        response="83.224.65.74",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20211021T193015Z_webconnectivity_IT_30722_n1_Sk3HeZOfHero7Ir9?input=http://gamestorrents.com/",
        source=[
            ""
        ],
        scope="nat",
        expected_countries=["IT"],
        notes="""
        Italian copyright related DNS block
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_nat_id_trustpositif",
        response="trustpositif.kominfo.go.id",
        confidence_no_fp=10,
        exp_url="",
        source=[
            ""
        ],
        scope="nat",
        expected_countries=["ID"],
        notes="""
        Matches a CNAME record of the official Indonesidan filter TrustPositif
        """
    ),

#

    #########
    # IRAN RELATED NATIONAL RESPONSES
    #########

    SimpleDNSReplyPattern(
        name="dns_nat_ir_inject_1",
        response="10.10.34.34",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20170525T030641Z_AS50810_5iVwM98EMQORqXeZtbhiDquo9zifyYSMmE5AWTARCw3XJ1R4is?input=http://pesareghabile.blogspot.com",
        source=[
            "https://censorbib.nymity.ch/pdf/Aryan2013a.pdf"
        ],
        scope = "nat",
        expected_countries=["IR"],
        notes="""
            An injection to the Iranian national blockpage.
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_nat_ir_inject_2",
        response="10.10.34.35",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20180114T045727Z_AS61173_bkL7bV97kNEYVREkD0Lg4LnvnnlDtlNlbvA1jbzPlsncPdNlIm?input=http://queerquotes.blogspot.com",
        source=[
            "https://censorbib.nymity.ch/pdf/Aryan2013a.pdf"
        ],
        scope="nat",
        expected_countries=["IR"],
        notes="""
            An injection to the Iranian national blockpage.
        """
    ),

    #########
    # CHINA RELATED RESPONSES
    #########

    #########
    # CHINA RELATED NATIONAL RESPONSES
    #########

    SimpleDNSReplyPattern(
        name="dns_nat_cn_poison_01",
        response="8.7.198.45",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://viewdns.info/research/dns-cache-poisoning-in-the-peoples-republic-of-china/",
            "https://ora.ox.ac.uk/objects/uuid:33adc5ff-53d6-4f31-9596-c809de2417de/download_file?safe_filename=14092016-acm-alt-2015.pdf&file_format=application%2Fpdf&type_of_work=Conference+item"
        ],
        scope="nat",
        expected_countries=["CN"],
        notes="""
            A published poison reply IP related to Chinese GFW (ARIN)
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_nat_cn_poison_02",
        response="37.61.54.158",
        exp_url="",
        confidence_no_fp=10,
        source=[
            "https://viewdns.info/research/dns-cache-poisoning-in-the-peoples-republic-of-china/",
            "https://ora.ox.ac.uk/objects/uuid:33adc5ff-53d6-4f31-9596-c809de2417de/download_file?safe_filename=14092016-acm-alt-2015.pdf&file_format=application%2Fpdf&type_of_work=Conference+item"
        ],
        scope="nat",
        expected_countries=["CN"],
        notes="""
            A published poison reply IP related to Chinese GFW (European Regional Registry)
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_nat_cn_poison_03",
        response="46.82.174.68",
        confidence_no_fp=10,
        source=[
            "https://viewdns.info/research/dns-cache-poisoning-in-the-peoples-republic-of-china/",
            "https://ora.ox.ac.uk/objects/uuid:33adc5ff-53d6-4f31-9596-c809de2417de/download_file?safe_filename=14092016-acm-alt-2015.pdf&file_format=application%2Fpdf&type_of_work=Conference+item"
        ],
        scope="nat",
        expected_countries=["CN"],
        notes="""
        A published poison reply IP related to Chinese GFW (Deutsche Telecom)
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_nat_cn_poison_04",
        response="78.16.49.15",
        exp_url="https://explorer.ooni.org/measurement/20191205T074509Z_AS4134_snD532tevf4HneyRwKvtRLSxBppvIFgxGq8FwjFKH3R1eSVv1m?input=http://kareemazmy.blogspot.com/",
        confidence_no_fp=10,
        source=[
            "https://viewdns.info/research/dns-cache-poisoning-in-the-peoples-republic-of-china/",
            "https://ora.ox.ac.uk/objects/uuid:33adc5ff-53d6-4f31-9596-c809de2417de/download_file?safe_filename=14092016-acm-alt-2015.pdf&file_format=application%2Fpdf&type_of_work=Conference+item"
        ],
        scope="nat",
        expected_countries=["CN"],
        notes="""
        A published poison reply IP related to Chinese GFW (Esat Telecommunications Limited)
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_nat_cn_poison_05",
        response="93.46.8.89",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://viewdns.info/research/dns-cache-poisoning-in-the-peoples-republic-of-china/",
            "https://ora.ox.ac.uk/objects/uuid:33adc5ff-53d6-4f31-9596-c809de2417de/download_file?safe_filename=14092016-acm-alt-2015.pdf&file_format=application%2Fpdf&type_of_work=Conference+item"
        ],
        scope="nat",
        expected_countries=["CN"],
        notes="""
        A published poison reply IP related to Chinese GFW (Fastweb)
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_nat_cn_poison_06",
        response="159.106.121.75",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://viewdns.info/research/dns-cache-poisoning-in-the-peoples-republic-of-china/",
            "https://ora.ox.ac.uk/objects/uuid:33adc5ff-53d6-4f31-9596-c809de2417de/download_file?safe_filename=14092016-acm-alt-2015.pdf&file_format=application%2Fpdf&type_of_work=Conference+item"
        ],
        scope="nat",
        expected_countries=["CN"],
        notes="""
        A published poison reply IP related to Chinese GFW (DoD)
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_nat_cn_poison_07",
        response="203.98.7.65",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://viewdns.info/research/dns-cache-poisoning-in-the-peoples-republic-of-china/"
        ],
        scope="nat",
        expected_countries=["CN"],
        notes="""
        A published poison reply IP related to Chinese GFW (Telstra)
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_nat_cn_poison_08",
        response="59.24.3.173",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://ora.ox.ac.uk/objects/uuid:33adc5ff-53d6-4f31-9596-c809de2417de/download_file?safe_filename=14092016-acm-alt-2015.pdf&file_format=application%2Fpdf&type_of_work=Conference+item"
        ],
        scope="nat",
        expected_countries=["CN"],
        notes="""
        A published poison reply IP related to Chinese GFW (Korea Telecom)
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_nat_cn_poison_09",
        response="203.98.7.65",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://ora.ox.ac.uk/objects/uuid:33adc5ff-53d6-4f31-9596-c809de2417de/download_file?safe_filename=14092016-acm-alt-2015.pdf&file_format=application%2Fpdf&type_of_work=Conference+item"
        ],
        scope="nat",
        expected_countries=["CN"],
        notes="""
        A published poison reply IP related to Chinese GFW (Clix-NZ Telstra)
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_nat_cn_poison_10",
        response="243.185.187.39",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "https://ora.ox.ac.uk/objects/uuid:33adc5ff-53d6-4f31-9596-c809de2417de/download_file?safe_filename=14092016-acm-alt-2015.pdf&file_format=application%2Fpdf&type_of_work=Conference+item"
        ],
        scope="nat",
        expected_countries=["CN"],
        notes="""
        A published poison reply IP related to Chinese GFW 
        """
    ),

]
