import json

class NetworkModuleOutput:
    def __init__(self):
        with open('network-outputs.tfstate', 'r') as network_state:
            network_attributes = json.load(network_state)
        self.id = network_attributes['outputs']['id']['value']

class ServerFactoryModule:
    def __init__(self,name):
        self.name = name
        self.network = NetworkModuleOutput()
        self.resources = self.build()
    
    def build(self):
        return {
                "resource": [
                  {
                        "aws_instance": [
                          {
                            self.name: [
                              {
                                "ami": "ami-005e54dee72cc1d00",
                                "instance_type": "t2.micro",
                                "network_interface": [
                                  {
                                    "device_index": 0,
                                    "network_interface_id": f'${{aws_network_interface.{self.name}.id}}'
                                  }
                                ]
                              }
                            ]
                          }
                        ]
                  },
                  {
                     "aws_network_interface":[
                        {
                           self.name:[
                              {
                                 "private_ips":[
                                    "172.16.10.100"
                                 ],
                                 "subnet_id": self.network.id,
                              }
                           ]
                        }
                     ]
                  }
                ]
                }        

if __name__ == "__main__":
    server = ServerFactoryModule(name='hello-world')
    with open('main.tf.json', 'w') as outfile:
        json.dump(server.resources, outfile, sort_keys=True, indent=4)