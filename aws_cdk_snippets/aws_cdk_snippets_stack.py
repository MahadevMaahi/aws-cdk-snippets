from aws_cdk import (
    # Duration,
    aws_s3 as _s3,
    aws_kms as _kms,
    core
    # aws_sqs as sqs,
)
from constructs import Construct

class MyArtifactBucketStack(core.Stack):

    def __init__(self, scope: Construct, construct_id: str, is_prod = False, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        myKey = _kms.Key.from_key_arn(
            self,
            "myKeyId",
            self.node.try_get_context('prod')['kms_arn']
            )

        # The code that defines your stack goes here
        if is_prod:
            artifactBucket = _s3.Bucket(
                self,
                "myProdArtifactBucketid",
                versioned=True,
                encryption=_s3.BucketEncryption.KMS,
                encryption_key=myKey,
                removal_policy=core.RemovalPolicy.RETAIN
            )
        else:
            artifactBucket = _s3.Bucket(
                self,
                "myDevArtifactBucketId",
                removal_policy=core.RemovalPolicy.DESTROY
            )
