
class NetworkFactoryModule:
    def __init__(self,name) -> None:
        self.name = name
    
    def outputs(self):
        return self.name

    def build(self):
        return{
                  "resource": [
                    {
                      "aws_vpc": [
                        {
                          self.name: [
                            {
                              "cidr_block": "10.0.0.0/16"
                            }
                          ]
                        }
                      ]
                    },
                    {
                      "aws_subnet": [
                        {
                          self.name: [
                            {
                              "cidr_block": "10.0.1.0/24",
                              "vpc_id": f'${{aws_vpc.{self.name}.id}}'
                            }
                          ]
                        }
                      ]
                    }
                  ]
                }    