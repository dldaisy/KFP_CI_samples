import kfp.dsl as dsl
from kfp.gcp import use_gcp_secret
import argparse

@dsl.pipeline(
    name = "kaggle pipeline",
    description = "kaggle pipeline that go from download data, train model to display result"
)
def kaggle_houseprice():
    stepDownloadData = dsl.ContainerOp(
        name ='download dataset'
        image = 'gcr.io/dldaisy-project/houseprice:downloaddata',
        command = ['python', 'download_data.py'],
        args = ["--bucket_name", 'dldaisy-test']
        file_outputs = {'train_dataset': 'train.txt'}
    ).apply(use_gcp_secret('user-gcp-sa'))

    stepVisualizeTable = dsl.ContainerOp(
        name = 'visualize dataset',
        image = 'gcr.io/dldaisy-project/houseprice:visualize',
        command = ['python', 'visualize.py'],
        arguments = ['--train_file_path', '%s' % stepDownloadData.outputs['train_dataset']]
    ).apply(use_gcp_secret('user-gcp-sa'))

if __name__ == '__main__':
   import kfp.compiler as compiler
   compiler.Compiler().compile(kaggle_houseprice, __file__ + '.zip')
    """
    stepVisualizeHTML = dsl.ContainerOp(
        name = 'print data distribution'
        image = ''
    )
    stepTrainModel = dsl.ContainerOp(
        name = 'train mode'
    )
    stepTensorboard

    stepModelAnalysis

    stepModelServing
    """