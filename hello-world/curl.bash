#!/bin/bash
# curl -H "Content-Type: application/json" -X GET http://34.70.82.171:8888/apis/v1beta1/pipeline_versions/7d37c72a-9e5f-4c59-9afc-7ca203552fb8

data='{"name":'\""ci-$1"\"', "code_source_url": "https://github.com/kubeflow/pipelines/tree/'"$1"'", "package_url": {"pipeline_url": "https://storage.googleapis.com/test-pipeline-version/'"$1"'/pipeline.zip"}, 
"resource_references": [{"key": {"id": '\""$2"\"', "type":3}, "relationship":1}]}'
# data='{"name":'\""ci-$1"\"', "package_url": {"pipeline_url": "https://storage.googleapis.com/jingzhangjz-kfp/pipeline.zip"}, "resource_references": [{"key": {"id": '\""$2"\"', "type":3}, "relationship":1}]}'
version=$(curl -H "Content-Type: application/json" -X POST -d "$data" http://34.70.82.171:8888/apis/v1beta1/pipeline_versions | jq -r ".id")

# create run
rundata='{"name":'\""$1-run"\"', "resource_references": [{"key": {"id": '\""$version"\"', "type":4}, "relationship":2}, {"key": {"id": "d5a136ac-f931-4d05-8c4c-97851a4ebd6b", "type":1}, "relationship": 1}]}'
echo "$rundata"
curl -H "Content-Type: application/json" -X POST -d "$rundata" http://34.70.82.171:8888/apis/v1beta1/runs