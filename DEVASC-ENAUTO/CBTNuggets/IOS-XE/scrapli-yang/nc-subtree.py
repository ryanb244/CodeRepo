from scrapli_netconf.driver import NetconfScrape

my_device = {
    "host": "192.168.0.12",
    "auth_username": "cisco",
    "auth_password": "cisco",
    "auth_strict_key": False,
    "port": 830,
}

conn = NetconfScrape(**my_device)
conn.open()

ospf_filter = """
<ospf-oper-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf-oper">
    <ospf-state>
        <ospf-instance>
            <af>address-family-ipv4</af>
            <router-id>168430081</router-id>
            <ospf-area>
                <area-id>0</area-id>
                <ospf-interface>
                    <name>GigabitEthernet2</name>
                    <ospf-neighbor>
                        <neighbor-id>10.10.10.2</neighbor-id>
                            <state></state>
                </ospf-interface>
            </ospf-area>
        </ospf-instance>
    </ospf-state>
</ospf-oper-data>
"""

response = conn.get(filter_=ospf_filter, filter_type="subtree")
print(response.result)
