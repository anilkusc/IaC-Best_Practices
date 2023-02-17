

class ServerFactoryModule:

    def __init__(self,name,subnet_id,sg_id) -> None:
        self.name = name
        self.subnet_id = subnet_id
        self.sg_id = sg_id
        self.resources = self.build()

    def build(self):
        return{
                 "aws_instance":[
                    {
                       self.name:[
                          {
                             "ami":"ami-06e0ce9d3339cb039",
                             "instance_type":"t2.micro",
                             "vpc_security_group_ids" : [self.sg_id],
                             "subnet_id"              : self.subnet_id                  
                          }
                       ]
                    }
                 ]
              }