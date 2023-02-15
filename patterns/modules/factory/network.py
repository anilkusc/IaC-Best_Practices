
class AWS_Network:
    def __init__(self):
        self.network_name = 'test-network'
        self.resource = self._build()
    def _build(self):
        return {
            "resource": [
                {
                  "aws_vpc": [
                    {
                      f'{self.network_name}': [
                        {
                          "cidr_block": "10.0.0.0/16"
                        }
                      ]
                    }
                  ]
                }
            ]
        }
