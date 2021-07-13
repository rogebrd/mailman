cd backend
zip --symlinks -r lambda.zip lambda.py
aws s3 cp lambda.zip s3://mailman-deployment-bucket/build/lambda.zip 

cd ../cloudformation
aws cloudformation update-stack \
--stack-name mailman-development \
--template-body file://main.yaml \
--capabilities CAPABILITY_NAMED_IAM