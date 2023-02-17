import json
from server import ServerFactoryModule
from network import NetworkFactoryModule
from security_group import SGFactoryModule

class Mediator:
    
    def __init__(self,resource,**attributes) -> None:
        self.resources = self.create(resource,**attributes)
    
    def create(self,resource,**attributes):
        if isinstance(resource,ServerFactoryModule):
            network = NetworkFactoryModule(resource.name)
            resources = self.create(network)
            
        elif isinstance(resource,NetworkFactoryModule):
            network = SGFactoryModule(resource.name,resource.outputs())
            resources = self.create(network)

        else:
            resources = [resource]
            return resources
        