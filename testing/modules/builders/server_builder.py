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
                 private_subnets = ["10.0.1.0/24"],
                 public_subnets  = ["10.0.2.0/24"],
                 enable_nat_gateway = True,
                 enable_vpn_gateway = False,
                 monitoring = False,
                 ami = "ami-065793e81b1869261",
                 instance_type="t2.micro",
                 sg_ids=[]
                  ):
        self._resources = []
        self.name=name
        self.cidr=cidr
        self.azs=azs
        self.sg_ids=sg_ids
        self.monitoring=monitoring
        self.private_subnets=private_subnets
        self.public_subnets=public_subnets
        self.enable_nat_gateway=enable_nat_gateway
        self.enable_vpn_gateway=enable_vpn_gateway
        self.ami=ami
        self.instance_type=instance_type
        self.vpc_name="vpc-"+name+"-"+tags["env"]
        self.ec2_name="server-"+name+"-"+tags["env"]
        self.subnet_id= f'${{module.{self.vpc_name}.private_subnets[0]}}' #f'${{module.{self.vpc_name}.private_subnets[0]}}',
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
        ec2 = AWS_EC2_Factory(name=self.ec2_name,
                              monitoring = self.monitoring,
                              subnet_id = self.subnet_id,
                              instance_type = self.instance_type,
                              ami = self.ami,
                              sg_ids = self.sg_ids,
                              tags=tags.resource)
        self._resources.append(ec2.resource)
        
    def build(self):
        return {
            'module': self._resources
        }