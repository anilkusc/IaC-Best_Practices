import json

class EC2Factory:
    def __init__(self,name,tags={}):
        self.name = name
        self.tags = tags
        self.resource = self._build()
    def _build(self):
        resources = []
        resources.append({
                      "aws_instance": [
                        {
                          self.name: [
                            {
                              "ami": "ami-2757f631",
                              "instance_type": "t2.micro",
                              "tags": self.tags
                            }
                          ]
                        }
                      ]
                    })
        return resources