import boto3 as b


class BaseResource:
    DefaultRegions = []
    DefaultResourceList = ['s3', 'ec2', 'vpc', 'eks']


class Resource:
    def __init__(self, region, name):
        resource_region = region
        resource_name = name

    def query_resource(self):
        pass

    def delete_resource(self):
        pass

    def update_resource(self):
        pass

    def create_resource(self):
        pass


if __name__ == '__main__':
    pass

