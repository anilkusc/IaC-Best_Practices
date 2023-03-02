import json
import sys
sys.path.insert(1, '../../../modules/builders')
sys.path.insert(1, '../../../modules/factories')
from ec2_builder import EC2Module

tags = {
        "company":"test",
        "domain":"mydomain",
        "tribe":"mytribe",
        "team":"team-a",
        "env":"dev",
        "squad":"",
        }

ec2_module = EC2Module('test-ec2-server',tags=tags,public=True)
with open('main.tf.json', 'w') as outfile:
    json.dump(ec2_module.build(), outfile,sort_keys=True, indent=4)