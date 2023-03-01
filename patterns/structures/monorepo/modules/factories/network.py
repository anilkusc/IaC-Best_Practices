class AWS_VPC_Factory:
    def __init__(self,name="test-network",cidr="10.0.0.0/16",tags={}):
        self.name = name
        self.cidr = cidr
        self.tags = tags
        self.resource = self._build()
    def _build(self):
        return {
                  "aws_vpc": [
                    {
                      f'{self.name}': [
                        {
                          "cidr_block": self.cidr,
                          "tags": self.tags                         
                        }
                      ]
                    }
                  ]
                }
    
class AWS_Subnet_Factory:
    def __init__(self,vpc_name,name="test-subnet",cidr="10.0.1.0/24",tags={}):
        self.name = name
        self.cidr = cidr
        self.vpc_name = vpc_name
        self.tags = tags
        self.resource = self._build()
    def _build(self):
        return  {
                  "aws_subnet": [
                    {
                      f'{self.name}': [
                        {
                          "cidr_block": self.cidr,
                          "vpc_id": f'${{aws_vpc.{self.vpc_name}.id}}',
                          "tags": self.tags  
                        }
                      ]
                    }
                  ]
                }
