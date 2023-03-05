import sys
sys.path.insert(0, '../factories') 
import json
from tags import Tag_Factory
from ec2 import AWS_EC2_Factory
from vpc import AWS_VPC_Factory

class ServerBuilder:
    def __init__(self,
                 name,
                 tags,
                 cidr="10.0.0.0/16",
                 azs=["eu-west-1a", "eu-west-1b", "eu-west-1c"],
                 private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"],
                 public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"],
                 enable_nat_gateway = True,
                 enable_vpn_gateway = False,
                  ):
        self._resources = []
        self.name=name
        self.cidr=cidr
        self.azs=azs
        self.private_subnets=private_subnets
        self.public_subnets=public_subnets
        self.enable_nat_gateway=enable_nat_gateway
        self.enable_vpn_gateway=enable_vpn_gateway
        self.vpc_name="vpc-"+name
        tags = Tag_Factory(company=tags["company"],env=tags["env"],domain=tags["domain"],tribe=tags["tribe"],team=tags["team"],squad=tags["squad"])        
        vpc = AWS_VPC_Factory(name=self.vpc_name,
                              cidr=self.cidr,
                              private_subnets=self.private_subnets,
                              public_subnets=public_subnets,
                              azs=self.azs,
                              enable_nat_gateway=self.enable_nat_gateway,
                              enable_vpn_gateway=self.enable_vpn_gateway
                              ,tags=tags.resource)
        self._resources.append(vpc.resource)
        
    def build(self):
        return {
            'module': self._resources
        }