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

    #########
    # RUSSIAN RKN RELATED RESPONSES
    #########

    SimpleDNSReplyPattern(
        name="dns_isp_ru_rkn_netbynet",
        response="212.1.226.59",
        confidence_no_fp=10,
        exp_url="",
        source=[
            "http://www.netbynet.ru//"
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

    #########
    # INDONESIAN SEHAT RELATED RESPONSES

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
        response="124.81.92.132",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20170330T110102Z_AS4795_yod1sqqu9NwrIBlJDfMepLmyAp3zVxQK5QG6Qqux11QuioLrYJ?input=https://www.gay.com/",
        source=[
            "http://indosatm2.com/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Indosat Netsafe blockpage.  Note: Can probably also add a sig off of the intermediary CNAME here
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
        response="202.137.1.74",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20190612T150505Z_AS23700_e7qsqPDY72QkdwPcDeUb5NkHxZ9HgpHOuU8p5oNFp5uW4BJAk7?input=https://www.shoe.org/",
        source=[
            "https://www.firstmedia.com/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP FirstMedia blockpage. NOTE: can probably track this by CNAME (internetpositif)
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_melsa",
        response="202.138.224.15",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20181006T114052Z_AS9657_yU1pa9b0I0vRzcBU5OsWOV6phrI2FBxQosem0mJRQdKZupCPkE?input=http://www.bglad.com",
        source=[
            "https://www.melsa.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP Melsa blockpage. Note: can probably track this by CNAME (filter.melsa.id)
        """
    ),

    SimpleDNSReplyPattern(
        name="dns_isp_id_sehat_ptcentrin",
        response="202.146.255.7",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20190314T214950Z_AS17658_kybYxwcXIxWZYnX32z36B1ZprSLxFT3WpxY0g7sfuy0Uy7MLAo?input=https://www.ilga-europe.org/",
        source=[
            "http://www.centrin.net.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP PT Centrin Online blockpage. Note: Can probably also track this by CNAME
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
        response="202.51.96.7",
        confidence_no_fp=10,
        exp_url="https://explorer.ooni.org/measurement/20190924T072134Z_AS17995_Seinciq0527hnzfIuN4ZQvKYqy8NKBKGHK9vt01KkY79iofutj?input=http://www.gayhealth.com/",
        source=[
            "https://www.iforte.id/"
        ],
        scope="isp",
        expected_countries=["ID"],
        notes="""Indonesian ISP iForte blockpage. Note: Can probably track this by CNAME (trustpositif)
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
        notes="""Indonesian ISP Icon Comnets+ blockpage. Note: Can probably track via CNAME
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

    #########
    # NATIONAL-SCOPED RESPONSES
    #########

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