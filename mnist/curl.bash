#!/bin/bash
data='{"name":'\""ci-$1"\"', "code_source_url": "", 
"package_url": {"pipeline_url": "https://storage.googleapis.com/test-pipeline-version/'"$1"'/pipeline.zip"}, 
"resource_references": [{"key": {"id": '\""$2"\"', "type":3}, "relationship":1}]}'
curl -H "Content-Type: application/json" -X POST -d "$data" http://34.68.34.55:8888/apis/v1beta1/pipeline_versions