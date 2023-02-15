import json

#Prototyping part
class StandartTags():
    def __init__(self):
        self.resource = {
            "company":"my-company",
            "automated": True,
            "domain": "test-domain"
        }

class EC2Factory:
    def __init__(self,name,tags={}):
        self.name = name
        self.tags = tags
        self.resource = self._build()
    def _build(self):
        return {
                  "resource": [
                    {
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
                    }
                  ]
                }
        
if __name__ == "__main__":
    network = EC2Factory("my-test-server",StandartTags().resource)
    with open('main.tf.json', 'w') as outfile:
        json.dump(network.resource, outfile, sort_keys=True, indent=4)    