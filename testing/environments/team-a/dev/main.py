import json
import sys
sys.path.insert(1, '../../../modules/builders')
sys.path.insert(1, '../../../modules/factories')
from server_builder import ServerBuilder

tags = {
        "company":"test",
        "domain":"mydomain",
        "tribe":"mytribe",
        "team":"team-a",
        "env":"dev",
        "squad":"test-squad"
        }

server = ServerBuilder(name='test-ec2-server',tags=tags)
with open('main.tf.json', 'w') as outfile:
    json.dump(server.build(), outfile,sort_keys=True, indent=4)