# visualizer with html

def datahtml(
    html_path
):
    import json
    from tensorflow.python.lib.io import file_io
    rendered_template = """<html>
        <head></head>
        <body><p>Hello World!</p></body>
        </html>"""
    file_io.write_string_to_file(html_path, rendered_template)

    metadata = {
        'outputs' : [{
        'type': 'web-app',
        'storage': 'gcs',
        'source': html_path,
        }]
    }
    with file_io.FileIO('/mlpipeline-ui-metadata.json', 'w') as f:
        json.dump(metadata, f)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--html_path', type = str)
    parser.add_argument('--train_file_path', type = str)
    args = parser.parse_args()

    datahtml(args.html_path)
