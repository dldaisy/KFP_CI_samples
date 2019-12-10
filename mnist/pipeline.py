import kfp.dsl as dsl
from kfp.gcp import use_gcp_secret
import argparse

# Get commit id to tag image
parser = argparse.ArgumentParser()
parser.add_argument('--commit_id', help='Commit Id', type=str)
args = parser.parse_args()


@dsl.pipeline(
   name='mnist pipeline',
   description='A pipeline to train a model on mnist dataset and start a tensorboard.'
)
def mnist_pipeline():
   train_step = dsl.ContainerOp(
       name='train mnist model',
       image='gcr.io/dldaisy-project/mnist_train:latest',
       file_outputs = {'logdir': '/logdir.txt'},
   ).apply(use_gcp_secret('user-gcp-sa'))

   visualize_step = dsl.ContainerOp(
      name = 'visualize training result with tensorboard',
      image = 'gcr.io/dldaisy-project/mnist_tensorboard:latest',
      command = ['python'],
      arguments = ['./tensorboard.py', '--logdir %s' % train_step.outputs['logdir']]
      output_artifact_paths={'mlpipeline-ui-metadata': '/mlpipeline-ui-metadata.json'}
   ).apply(use_gcp_secret('user-gcp-sa'))

if __name__ == '__main__':
   import kfp.compiler as compiler
   compiler.Compiler().compile(mnist_pipeline, __file__ + '.zip')