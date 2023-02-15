class WAFFactory:
    def __init__(self,name,addresses):
        self.name = name
        self.addresses = addresses
        self.resources = self._build()
    def _build(self):
        resources = []
        resources.append({
                          "aws_wafv2_ip_set": [
                            {
                              self.name: [
                                {
                                  "addresses": self.addresses,
                                  "description": self.name+" IP set",
                                  "ip_address_version": "IPV4",
                                  "name": self.name,
                                  "scope": "REGIONAL"
                                }
                              ]
                            }
                          ]
                        })        
        return resources