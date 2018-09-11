#coding: utf-8

import requests, servers_by_host, header

source_host = 'compute6'
destination_host = 'compute5'
servers_to_migrate = servers_by_host.get(source_host)

body = """
{
    "os-migrateLive": {
        "host": {destination_host},
        "block_migration": false,
        "disk_over_commit": false
    }
}
"""

for server in servers_to_migrate:

	r = requests.post('http://controller:8774/v2.1/servers/%s/action'%server, data=body, headers=header.get())
	print server + ' migrado para ' + destination_host
	print r
	print r.content