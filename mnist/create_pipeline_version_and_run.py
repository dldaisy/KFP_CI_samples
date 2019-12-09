import kfp
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--version_name', help='Must exist. name of the new version. Must be unique.', type=str)
parser.add_argument('--run_name', help='name of the new run.', type=str, default='')
parser.add_argument('--package_url', help='Must exist. pipeline package url', type=str)
parser.add_argument('--pipeline_id', help = 'Must exist. pipeline id',type=str)
parser.add_argument('--experiment_id', help = 'experiment id',type=str)
parser.add_argument('--code_source_url', help = 'url of source code', type=str, default='')
args = parser.parse_args()

client = kfp.Client()
print('Now in create_pipeline_version_and_run.py...')
#create version
version_body = 
{"name": args.version_name, 
"code_source_url": args.code_source_url, 
"package_url": {"pipeline_url": args.package_url}, 
"resource_references": [{"key": {"id": args.pipeline_id, "type":3}, "relationship":1}]}
print('version body: {}', version_body)

response = client.pipelines.create_pipeline_version(body)

print('Now start to create a run...')
version_id = response.id
# create run
run_name = args.run_name if args.run_name else 'run' + version_id
resource_references = [{"key": {"id": version_id, "type":4}, "relationship":2}]
if args.experiment_id:
    resource_references.append({"key": {"id": args.experiment_id, "type":1}, "relationship": 1})
run_body={
    "name":run_name,
    "resource_references": resource_references
}
try:
    client.runs.create_run(run_body)
except:
    pass


    
