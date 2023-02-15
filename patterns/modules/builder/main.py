import json
from load_balancer import LoadBalancerFactory
from waf import WAFFactory
from ec2 import EC2Factory
class EC2Module:
    def __init__(self,name):
        self._resources = []
        self.name=name
        self._resources = EC2Factory(self.name).resource
    def add_internal_load_balancer(self):
        self._resources.extend(LoadBalancerFactory(self.name, internal=True).resources)
    def add_external_load_balancer(self):
        self._resources.extend(LoadBalancerFactory(self.name, internal=False).resources)
    def add_firewall_rule(self):
        self._resources.extend(WAFFactory(self.name, addresses=["192.168.1.1/32"]).resources)
    def build(self):
        return {
            'resource': self._resources
        }

if __name__ == "__main__":
    ec2_module = EC2Module('test-ec2-server')
    ec2_module.add_external_load_balancer()
    ec2_module.add_firewall_rule()
    with open('main.tf.json', 'w') as outfile:
        json.dump(ec2_module.build(), outfile,sort_keys=True, indent=4)    