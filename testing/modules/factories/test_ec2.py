import pytest
from ec2 import AWS_EC2_Factory



@pytest.fixture(scope="module")
def ec2():
    return AWS_EC2_Factory(
        name="test",
        subnet_id="test-id",
        monitoring=False,
        instance_type = "test",
        ami = "test",
        sg_ids = [],
        tags = {})

@pytest.fixture
def ec2_configuration(ec2):
    return ec2.resource


def test_configuration_for_ami(ec2_configuration):
    assert ec2_configuration['test'][0]['ami'] == "test"
