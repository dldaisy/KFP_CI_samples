import kfp.dsl as dsl
from kfp.gcp import use_gcp_secret
import argparse

@dsl.pipeline(
    name = "kaggle pipeline",
    description = "kaggle pipeline that go from download data, train model to display result"
)
def kaggle_houseprice():
    stepDownloadData = dsl.ContainerOp(
        name ='download dataset',
        image = 'gcr.io/dldaisy-project/kaggle_download:latest',
        command = ['python', 'download_data.py'],
        arguments = ["--bucket_name", 'dldaisy-test'],
        file_outputs = {'train_dataset': '/train.txt'}
    ).apply(use_gcp_secret('user-gcp-sa'))

    stepVisualizeTable = dsl.ContainerOp(
        name = 'visualize dataset in table',
        image = 'gcr.io/dldaisy-project/kaggle_visualize_table:latest',
        command = ['python', 'visualize.py'],
        arguments = ['--train_file_path', '%s' % stepDownloadData.outputs['train_dataset']],
        output_artifact_paths={'mlpipeline-ui-metadata': '/mlpipeline-ui-metadata.json'}
    ).apply(use_gcp_secret('user-gcp-sa'))

    stepVisualizeHTML = dsl.ContainerOp(
        name = 'visualize dataset in html',
        image = 'gcr.io/dldaisy-project/kaggle_visualize_html:latest',
        command = ['python', 'visualize.py'],
        arguments = ['--train_file_path', '%s' % stepDownloadData.outputs['train_dataset'],
                     '--bucket_name', 'dldaisy-kaggle'],
        output_artifact_paths={'mlpipeline-ui-metadata': '/mlpipeline-ui-metadata.json'}
    ).apply(use_gcp_secret('user-gcp-sa'))

    stepSubmitResult = dsl.ContainerOp(
        name = 'submit result to kaggle competition',
        image = 'gcr.io/dldaisy-project/kaggle_submit:latest',
        command = ['python', 'submit_result.py'],
        arguments = ['--bucket_name', 'dldaisy-kaggle', '--submission_name', 'submission.csv']
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