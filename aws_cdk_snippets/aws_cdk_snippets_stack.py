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
            versioned=False,
            encryption=_s3.BucketEncryption.S3_MANAGED,
            block_public_access=_s3.BlockPublicAccess.BLOCK_ALL
        )

        myBucket = _s3.Bucket(
            self,
            "myBucketObjectId"
        )

        snsTopicName = "mySNSTopic"

        if not core.Token.is_unresolved(snsTopicName) and len(snsTopicName) > 10 :
            raise ValueError("Length of the Topic Name can be atmost 10")

        output_1 = core.CfnOutput(
            self,
            "myBucketOutput1",
            value = myBucket.bucket_name,
            description = f"My First CDK Bucket",
            export_name = "myBucketOutput1"
        )
        # example resource
        # queue = sqs.Queue(
        #     self, "AwsCdkSnippetsQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
