import json
import os
class AWS_RDS:
    def __init__(self):
        self.name = 'test-user'
        self.organization = os.environ.get('USER','test-organization')
        self.project_id = f'{self.name}-{self.organization}'
        self.resource = self._build()
    def _build(self):
        return {
               "resource": [
                {
                  "aws_db_instance": [
                    {
                      "default": [
                        {
                          "allocated_storage": 10,
                          "db_name": self.project_id,
                          "engine": "mysql",
                          "engine_version": "5.7",
                          "instance_class": "db.t3.micro",
                          "parameter_group_name": "default.mysql5.7",
                          "password": "foobarbaz",
                          "skip_final_snapshot": True,
                          "username": "foo"
                        }
                      ]
                    }
                  ]
                }
              ]
            }

if __name__ == "__main__":
    project = AWS_RDS()
    with open('main.tf.json', 'w') as outfile:
        json.dump(project.resource, outfile, sort_keys=True, indent=4)