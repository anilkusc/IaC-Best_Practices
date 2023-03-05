class AWS_EC2_Factory:
    def __init__(self,name,subnet_id,monitoring,sg_ids,instance_type,ami,tags):
        self.name = name
        self.subnet_id = subnet_id
        self.monitoring = monitoring
        self.sg_ids = sg_ids
        self.instance_type = instance_type
        self.ami = ami
        self.tags = tags
        self.resource = self._build()
    def _build(self):
        return {
                "ec2_instance": [
                  {
                    "ami": self.ami,
                    "instance_type": self.instance_type,
                    #"key_name": "user1",
                    "monitoring": self.monitoring,
                    "name": self.name,
                    "subnet_id": self.subnet_id,
                    #"version": "~\u003e 3.0",
                    "vpc_security_group_ids": self.sg_ids,
                    "tags":self.tags,
                    "source": "terraform-aws-modules/ec2-instance/aws"
                  }
                ]
              }  