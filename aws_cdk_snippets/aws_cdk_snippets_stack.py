from aws_cdk import (
    # Duration,
    aws_s3 as _s3,
    core
    # aws_sqs as sqs,
)
from constructs import Construct

class AwsCdkSnippetsStack(core.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        _s3.Bucket(
            self,
            "myBucketId",
            bucket_name="aws-cdk-snippet-stack-s3-bucket-name",
            versioned=True,
            encryption=_s3.BucketEncryption.KMS_MANAGED
        )
        # example resource
        # queue = sqs.Queue(
        #     self, "AwsCdkSnippetsQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
