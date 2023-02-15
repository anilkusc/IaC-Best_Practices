import json

class AWS_Network:
    def __init__(self):
        self.network_name = 'test-network'
        self.subnet_name = 'test-subnet'
        self.resource = self._build()
    def _build(self):
        return {
            "resource": [
                {
                  "aws_vpc": [
                    {
                      f'{self.network_name}': [
                        {
                          "cidr_block": "10.0.0.0/16"
                        }
                      ]
                    }
                  ]
                },
                {
                  "aws_subnet": [
                    {
                      f'{self.subnet_name}': [
                        {
                          "cidr_block": "10.0.1.0/24",
                          "vpc_id": f'${{aws_vpc.{self.network_name}.id}}'
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