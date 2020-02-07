import kfp.dsl as dsl
from kfp.gcp import use_gcp_secret

@dsl.pipeline(
   name='mnist pipeline',
   description='A pipeline to train a model on mnist dataset and start a tensorboard.'
)
def mnist_pipeline(
   storage_bucket: str,
   ):
   import os
   train_step = dsl.ContainerOp(
       name='train mnist model',
       image = os.path.join(args.gcr_address, 'mnist_train:latest'),
       command = ['python', '/mnist.py'],
       arguments = ['--storage_bucket', storage_bucket],
       file_outputs = {'logdir': '/logdir.txt'},
   )

   visualize_step = dsl.ContainerOp(
      name = 'visualize training result with tensorboard',
      image = os.path.join(args.gcr_address, 'mnist_tensorboard:latest'),
      command = ['python', '/tensorboard.py'],
      arguments = ['--logdir', '%s' % train_step.outputs['logdir']],
      output_artifact_paths={'mlpipeline-ui-metadata': '/mlpipeline-ui-metadata.json'}
   )

if __name__ == '__main__':
   import argparse
   parser = argparse.ArgumentParser()
   parser.add_argument('--gcr_address', type = str)
   args = parser.parse_args()
   
   import kfp.compiler as compiler
   compiler.Compiler().compile(mnist_pipeline, __file__ + '.zip')