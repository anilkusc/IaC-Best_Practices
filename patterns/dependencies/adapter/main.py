import json
import yaml

class AWSIAMAdapter:
    def __init__(self,metadata) -> None:
        aws_roles = {
            "viewers": "read",
            "editors": "write",
            "admins": "admin",
        }
        self.aws_users = []
        for permission,users in metadata.items():
            for user in users:
                self.aws_users.append((user,aws_roles.get(permission)))
    def outputs(self):
        return self.aws_users

class AWSIAMModule:
    def __init__(self,name,users) -> None:
        self.name = name
        self.users= users
        self.resources = self.build()
    
    def build(self):
        resources = []
        for user,role in self.users:
            resources.append({
              "aws_iam_user": [
                {
                  user: [
                    {
                      "name": user
                    }
                  ]
                }
              ]
            })
            resources.append({
                  "aws_iam_user_group_membership": [
                    {
                      user+role: [
                        {
                          "groups": [
                            role
                          ],
                          "user": f'${{aws_iam_user.{user}.name}}'
                        }
                      ]
                    }
                  ]
                })
        return {'resource': resources}

if __name__ == "__main__":
    with open("users.yaml", "r") as reader:
        users = yaml.safe_load(reader)
    users = AWSIAMAdapter(users["employes"])
    with open('main.tf.json', 'w') as outfile:
        json.dump(AWSIAMModule('test',users.outputs()).resources, outfile, sort_keys=True, indent=4) 