import json 

class s3Facade:
    def __init__(self,name) -> None:
        self.name = name

class s3Module:
    def __init__(self,name) -> None:
        self.name = name
        self.resources = self.build()

    def outputs(self):
        return s3Facade(self.name)
    
    def build(self):
        return{
              "resource": [
                {
                  "aws_s3_bucket": [
                    {
                      self.name: [
                        {
                          "bucket": self.name
                        }
                      ]
                    }
                  ]
                }
              ]
            }

class s3ACLModule:
    def __init__(self,bucket,acl) -> None:
        if not self.is_acl_config_valid(acl):
            print("Please enter valid acl config")
            exit()
        self.acl = acl
        self.bucket = bucket
        self.resources= self.build()
        
    def is_acl_config_valid(self,acl):
        if acl != "private" and acl != "public":
            return False
        return True
    
    def build(self):
        return{
              "resource": [
                {
                  "aws_s3_bucket_acl": [
                    {
                      self.bucket.name: [
                        {
                          "acl": "private",
                          "bucket": f'${{aws_s3_bucket.{self.bucket.name}.id}}'
                        }
                      ]
                    }
                  ]
                }
              ]
            } 

if __name__ == "__main__":
    
    bucket = s3Module('my-test-module')
    with open('bucket.tf.json', 'w') as outfile:
        json.dump(bucket.resources, outfile, sort_keys=True, indent=4)
    
    server = s3ACLModule(bucket.outputs(), 'private')
    with open('bucket_access.tf.json', 'w') as outfile:
        json.dump(server.resources, outfile, sort_keys=True, indent=4)