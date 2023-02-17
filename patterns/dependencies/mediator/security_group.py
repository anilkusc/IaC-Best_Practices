
class SGFactoryModule:
    def __init__(self,name,vpc_name) -> None:
        self.name = name
        self.vpc_name = vpc_name
    
    def outputs(self):
        return ""

    def build(self):
        return{
                  "resource": [
                    {
                      "aws_security_group": [
                        {
                          "allow_tls": [
                            {
                              "description": "Allow TLS inbound traffic",
                              "egress": [
                                {
                                  "cidr_blocks": [
                                    "0.0.0.0/0"
                                  ],
                                  "from_port": 0,
                                  "protocol": "-1",
                                  "to_port": 0
                                }
                              ],
                              "ingress": [
                                {
                                  "cidr_blocks": [
                                    "0.0.0.0/0"
                                  ],
                                  "description": "allow all",
                                  "from_port": 0,
                                  "protocol": "-1",
                                  "to_port": 0
                                }
                              ],
                              "name": self.name,
                              "vpc_id": f'${{aws_vpc.{self.vpc_name}.id}}'
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }