cd backend
zip --symlinks -r register.zip register_lambda.py
aws s3 cp register.zip s3://mailman-deployment-bucket/build/register.zip
zip --symlinks -r mailman.zip config.py fetch_email.py mailman_lambda.py
aws s3 cp mailman.zip s3://mailman-deployment-bucket/build/mailman.zip

cd ../cloudformation
aws cloudformation update-stack \
--stack-name mailman-development \
--template-body file://main.yaml \
--capabilities CAPABILITY_NAMED_IAM