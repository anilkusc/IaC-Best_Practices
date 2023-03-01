
class SG_Rule_Prototype:
    def __init__(self,**kwargs):
        self.resource = {
                          "description": kwargs.get('description', ""),
                          "cidr_blocks": kwargs.get('cidr_blocks', None),
                          "from_port": kwargs.get('from_port', 0),
                          "to_port": kwargs.get('to_port', 0),
                          "protocol": kwargs.get('protocol', -1),
                          "self": True,
                          "ipv6_cidr_blocks": ["::/0"],
                          "prefix_list_ids": [],
                          "security_groups": [],
                        }
        
class AWS_SG_Factory:
    def __init__(self,vpc_name,name="test",description="default description",tags={}):
        self.name = name
        self.description = description
        self.egress = [SG_Rule_Prototype(cidr_blocks=["0.0.0.0/0"]).resource]
        self.ingress = []
        self.vpc_name = vpc_name
        self.tags = tags
        self.resource = self._build()

    def add_ingress_rule(self,cidr_blocks,to_port,from_port=0,protocol="-1",description=""):
        self.ingress.append(SG_Rule_Prototype().resource)
        self.resource = self._build()
    
    def add_egress_rule(self,cidr_blocks,to_port,from_port=0,protocol="-1",description=""):
        self.egress.append(SG_Rule_Prototype())
        self.resource = self._build()


    def _build(self):
        return{
              "aws_security_group": [
                {
                  self.name: [
                    {
                      "description": self.description,
                      "egress": self.egress,
                      "ingress":self.ingress,
                      "name": self.name,
                      "vpc_id": f'${{aws_vpc.{self.vpc_name}.id}}',
                      "tags": self.tags,
                    }
                  ]
                }
              ]
            }