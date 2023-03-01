import sys
sys.path.insert(0, '../factories') 
import json
from tags import Tag_Factory
from server import AWS_EC2_Factory
from security_group import AWS_SG_Factory
from network import AWS_VPC_Factory,AWS_Subnet_Factory

class EC2Module:
    def __init__(self,name,tags):
        self._resources = []
        self.name=name
        self.vpc_name="vpc-"+name
        self.subnet_name="subnet-"+name
        self.sg_name="security-group-"+name
        self.ec2_name=name
        tags = Tag_Factory(company=tags["company"],env=tags["env"],domain=tags["domain"],tribe=tags["tribe"],team=tags["team"],squad=tags["squad"])        
        vpc = AWS_VPC_Factory(name=self.vpc_name,tags=tags.resource)
        self._resources.append(vpc.resource)
        subnet = AWS_Subnet_Factory(vpc_name=self.vpc_name,name=self.subnet_name,tags=tags.resource)
        self._resources.append(subnet.resource)
        sg = AWS_SG_Factory(vpc_name=self.vpc_name,name=self.sg_name,tags=tags.resource)
        self._resources.append(sg.resource)
        ec2 = AWS_EC2_Factory(sg_names=[self.sg_name],subnet_name=self.subnet_name,name=self.ec2_name,tags=tags.resource)
        self._resources.append(ec2.resource)
    def build(self):
        return {
            'resource': self._resources
        }