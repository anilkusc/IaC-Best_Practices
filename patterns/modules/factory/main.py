import json
import ipaddress
from network import AWS_Network
def generate_subnet_name(address):
    address_identifier = format(ipaddress.ip_network(address).network_address).replace('.', '-')
    return "subnetwork"+address_identifier

class Subnet_Factory:
    def __init__(self,address,region,network):
        self.name = generate_subnet_name(address)
        self.address = address
        self.network = network.network_name
        self.resource = self._build()
    def _build(self):
        return {
                "resource": [
                {
                  "aws_subnet": [
                    {
                      f'{self.name}': [
                        {
                          "cidr_block": "10.0.1.0/24",
                          "vpc_id": f'${{aws_vpc.{self.network}.id}}'
                        }
                      ]
                    }
                  ]
                }
                ]
            }

if __name__ == "__main__":
    network = AWS_Network()
    with open('main.tf.json', 'w') as outfile:
        json.dump(network.resource, outfile, sort_keys=True, indent=4)   
    
    subnets_and_regions= {
        '10.0.0.0/24': 'eu-west-1',
        '10.0.1.0/24': 'us-west-1',
        '10.0.2.0/24': 'us-east-1',
    }
    for address,region in subnets_and_regions.items():
        subnetwork = Subnet_Factory(address,region,network)
        with open(subnetwork.name+'.tf.json', 'w') as outfile:
            json.dump(subnetwork.resource, outfile, sort_keys=True, indent=4)