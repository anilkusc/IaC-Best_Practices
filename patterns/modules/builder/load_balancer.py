class LoadBalancerFactory:
    def __init__(self,name,internal = False):
        self.name = name
        self.internal = internal
        self.resources = self._build()
    def _build(self):
        resources = []
        resources.append( {
              "aws_lb_listener": [
                {
                  "http": [
                    {
                      "default_action": [
                        {
                          "fixed_response": [
                            {
                              "content_type": "text/plain",
                              "message_body": "404: page not found",
                              "status_code": 404
                            }
                          ],
                          "type": "fixed-response"
                        }
                      ],
                      "load_balancer_arn": "",
                      "port": 80,
                      "protocol": "HTTP"
                    }
                  ]
                }
              ]
            })
        resources.append({
                          "aws_security_group": [
                            {
                              self.name: [
                                {
                                  "name": self.name
                                }
                              ]
                            }
                          ]
                        })
        resources.append({
                          "aws_alb": [
                            {
                              self.name: [
                                {
                                  "name": self.name,
                                  "security_groups": [
                                    f'${{aws_security_group.{self.name}.id}}'
                                  ],
                                  "subnets": [],
                                }
                              ]
                            }
                          ]
                        })        
        return resources