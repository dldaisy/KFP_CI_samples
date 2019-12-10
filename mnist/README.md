# Mnist CI Pipeline

## What needs to be done before run
* Set up a trigger
* Substitute several constant in cloudbuild.yaml

`_GCR_PATH`: '[YOUR CLOUD REGISTRY], for example: gcr.io/my-project' \
`_GS_BUCKET`: '[YOUR GS BUCKET TO STORE PIPELINE AND LAUNCH TENSORBOARD], for example: gs://my-bucket'\
`_PIPELINE_ID`: '[PIPELINE ID TO CREATE A VERSION ON], get it on kfp UI' \
`_HOST_NAME`: '[EXTERNAL HOST NAME OF ml-pipeline service], read README.md for more info.'

* Set your container registy public


