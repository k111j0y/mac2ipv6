#! /usr/bin/env python

import re

# mac = '00:0c:29:35:fa:33'

def mac2ipv6(mac):
	mac = re.sub(r'[.:-]', '', mac).lower()
	mac = mac[0:6] + 'fffe' + mac[6:]
	mac = hex(int(mac[0:2], 16) ^ 2)[2:].zfill(2) + mac[2:]
	print(':'.join(re.findall(r'.{4}', mac)))
