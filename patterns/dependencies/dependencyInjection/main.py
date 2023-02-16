import boto3
import json
import ipaddress

def get_network(id):
    client = boto3.client('ec2')
    sn_all = client.describe_subnets()
    for sn in sn_all['Subnets'] :
        if sn['SubnetId'] == id:
            return sn

class ServerFactoryModule:
    def __init__(self,name,subnet_id):
        self.name = name
        self.network = get_network(subnet_id)
        self.ip = self.allocate_last_ip_address_in_range()
        self.resources = self.build()
    def allocate_last_ip_address_in_range(self):
        ip = ipaddress.IPv4Network(self.network['CidrBlock'])
        return format(ip[-2])
    def build(self):
        return {
            "provider": [
              {
                "aws": [
                  {
                    "region": "eu-west-1",
                  }
                ]
              }
            ],
           "resource":[
              {
                 "aws_network_interface":[
                    {
                       self.name:[
                          {
                             "private_ips":[
                                self.ip
                             ],
                             "subnet_id":self.network['SubnetId']
                          }
                       ]
                    }
                 ]
              },
              {
                 "aws_instance":[
                    {
                       self.name:[
                          {
                             "ami":"ami-06e0ce9d3339cb039",
                             "instance_type":"t2.micro",
                             "network_interface":[
                                {
                                   "device_index":0,
                                   "network_interface_id": f'${{aws_network_interface.{self.name}.id}}'
                                }
                             ]
                          }
                       ]
                    }
                 ]
              }
           ]
        }
if __name__ == "__main__":
    server = ServerFactoryModule(name='test', subnet_id='subnet-03ed90679c3fe6ef9')
    with open('main.tf.json', 'w') as outfile:
        json.dump(server.resources, outfile, sort_keys=True, indent=4)
    #print(get_network("subnet-03ed90679c3fe6ef9"))