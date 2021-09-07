import yaml
import argparse
import requests
from io import StringIO
from jinja2 import Environment, FileSystemLoader

# importer arguments
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--username', help='Horizon admin username')
parser.add_argument('-p', '--password', help='Horizon admin password')
parser.add_argument('-b', '--base_url', help='Horizon base_url')
parser.add_argument('-r', '--requisition', help='Import nodes to requisition')
parser.add_argument('-l', '--list', help='List available horizon requisitions', action="store_true")
args = parser.parse_args()

# load horizon nodes yaml file
nodes = yaml.load(open('nodes.yml'),Loader=yaml.FullLoader)

# list available requisitions
if args.list:
    node_req = list(iter(nodes['Nodes']))
    print(yaml.dump(node_req, sort_keys=False, default_flow_style=False))

# load horizon nodes xml template
env = Environment(loader = FileSystemLoader('templates'), trim_blocks=True, lstrip_blocks=True)
template = env.get_template('node.j2')

# requests variables
auth = (args.username, args.password)
headers = {'content-type': 'application/xml'}
import_url = '{}/opennms/rest/requisitions/{}/nodes'.format(args.base_url, args.requisition)
scan_url = '{}/opennms/rest/requisitions/{}/import?rescanExisting=false'.format(args.base_url, args.requisition)

# renders horizon nodes yaml data to xml template based on requisition input   
# posts node data to horizon api and updates requisition
if args.requisition:
    for node in nodes['Nodes'][args.requisition]:
        with StringIO() as data:
            data.write(template.render(node))
            data.seek(0)
            requests.post(url=import_url, data=data, auth=auth, headers=headers)
            print(f"Importing {node['node_label']} to {args.requisition} requisition.")
            data.close()

    # scan and update requisition
    requests.put(url=scan_url, auth=auth)
    print(f"Importing of {args.requisition} complete.")