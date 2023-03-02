class AWS_EC2_Factory:
    def __init__(self,
                 sg_names,
                 subnet_name,
                 name="test",
                 ami="ami-065793e81b1869261",
                 instance_type="t2.micro",
                 monitoring = False,
                 public_ip = False,
                 tags={},
                 ):
        self.name = name
        self.ami = ami
        self.instance_type = instance_type
        self.monitoring = monitoring
        self.subnet_name = subnet_name
        self.sg_ids = self.create_securiy_group_ids(sg_names)
        self.public_ip = public_ip
        self.tags = tags
        self.resource = self._build()

    def create_securiy_group_ids(self,sgs):
        ids = []
        for sg_name in sgs:
            ids.append(f'${{aws_security_group.{sg_name}.id}}')
        return ids


    def _build(self):
        return{
                "aws_instance": [
                  {
                    self.name: [
                      {
                        "ami": self.ami,
                        "instance_type": self.instance_type,
                        "monitoring": self.monitoring,
                        "associate_public_ip_address": self.public_ip,
                        "subnet_id": f'${{aws_subnet.{self.subnet_name}.id}}',
                        "tags": self.tags,
                        "vpc_security_group_ids": self.sg_ids
                      }
                    ]
                  }
                ]
            }