class AWS_VPC_Factory:
    def __init__(self,name,cidr,tags,azs,private_subnets,public_subnets,enable_nat_gateway,enable_vpn_gateway):
        self.name = name
        self.cidr = cidr
        self.azs = azs
        self.private_subnets = private_subnets
        self.public_subnets = public_subnets
        self.enable_nat_gateway = enable_nat_gateway
        self.enable_vpn_gateway = enable_vpn_gateway
        self.tags = tags
        self.resource = self._build()
    def _build(self):
        return {
                 self.name:[
                    {
                       "azs":self.azs,
                       "cidr":self.cidr,
                       "enable_nat_gateway":self.enable_nat_gateway,
                       "enable_vpn_gateway":self.enable_vpn_gateway,
                       "name":self.name,
                       "private_subnets":self.private_subnets,
                       "public_subnets":self.public_subnets,
                       "source":"terraform-aws-modules/vpc/aws",
                       "tags":self.tags
                    }
                    ]
                }