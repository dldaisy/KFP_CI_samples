"""
step #1: download data from kaggle website, and push it to gs bucket
"""

def processAndUpload(
    bucket_name
):
    from google.cloud import storage
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    output_blob = bucket.blob('train.csv')
    output_blob.upload_from_filename('train.csv')
    with open('train.txt', w) as f:
        f.write('gs://'+bucket_name+'/train.csv')
if __name__ == '__main__':
    import os
    os.system("kaggle competitions download -c house-prices-advanced-regression-techniques")
    os.system("unzip house-prices-advanced-regression-techniques")
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--bucket_name', type=str)
    args = parser.parse_args()

    processAndUpload(args.bucket_name)
    