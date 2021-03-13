# PS5 Monitor/Bot

Meant to run in a Kubernetes Environment. Continually checks a given website to see if the ps5 is available. If so, publish 
to an AWS topic.

Future Improvements:

Add support for walmart, target and amazon websites. Implement checkout capabilities.

## Setup

You will need to have an AWS SNS topic to publish to and credentials for an IAM User with permission to publish to said topic.

1. To test locally, pull the public.ecr.aws/h2r1m7n0/ps5monitor docker image.
2. Pointing to your docker-desktop Kubernetes cluster, create the secret holding your aws IAM user credentials. Run `kubectl create secret generic bb-secret --from-file=./credentials` (this command assumes you are in the same directory where the aws credentials file lies).
3. Edit the bb-aws-topic secret in bestbuy/manifest.yml. Add the arn for the AWS topic you want to publish to.
4. cd into the bestbuy directory. Run `kubectl apply -f manifest.yml`

 