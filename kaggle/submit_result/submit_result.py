"""
step #4: submit result to kaggle
"""

def downoadResult(
    bucket_name,
    submission_name
):
    from google.cloud import storage
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.get_blob(submission_name)
    blob.download_to_filename('submisstion.csv')

if __name__ == '__main__':
    import os
    os.system("kaggle competitions submit -c house-prices-advanced-regression-techniques -f submission.csv -m 'submit message'")
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--bucket_name', type=str)
    parser.add_argument('--submission_name', type=str)
    args = parser.parse_args()

    submitResult(args.bucket_name, args.submission_name)