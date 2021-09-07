
## OpenNMS Importer

A simple python tool for OpenNMS requisitions. This tool is used to import nodes in `.xml` format from a `nodes.yml` file to a Horizon instance.

Add nodes to `nodes.yml` and run `python3 opennms-importer.py`.

```
python3 opennms-importer.py -u admin -p some-password -r Firewalls -b https://opennms.example.com

```
  
```
usage: opennms-importer.py [-h] [-u USERNAME] [-p PASSWORD] [-b BASE_URL]
                           [-r REQUISITION] [-l]

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        Horizon admin username
  -p PASSWORD, --password PASSWORD
                        Horizon admin password
  -b BASE_URL, --base_url BASE_URL
                        Horizon base_url
  -r REQUISITION, --requisition REQUISITION
                        Import nodes to requisition
  -l, --list            List available horizon requisitions
```
