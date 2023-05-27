import simple_matrix_api
from simple_matrix_api.client import Client
import argparse
import json

READ_SIZE = 50_000_000


def upload_large_file(
    username: str,
    password: str,
    file_input: str,
    file_output: str,
    matrix_url: str,
):
    client: Client = simple_matrix_api.login(username, password, matrix_url)
    urls: list[str] = []
    with open(file_input, "rb") as input:
        while True:
            content = input.read(READ_SIZE)
            if (len(content) == 0):
                break
            urls.append(client.upload("_", content))
    with open(file_output, "w") as output:
        json.dump(urls, output)


def download_large_file(
    username: str,
    password: str,
    file_input: str,
    file_output: str,
    matrix_url: str,
):
    client: Client = simple_matrix_api.login(username, password, matrix_url)

    with open(file_input, "r") as input:
        urls: list[str] = json.load(input)
        with open(file_output, "wb") as output:
            for url in urls:
                content_part = client.get_file(url)
                if content_part != None:
                    output.write(content_part)


parser = argparse.ArgumentParser()
parser.add_argument("username")
parser.add_argument("password")
parser.add_argument("file_input")
parser.add_argument("file_output")
parser.add_argument("-m", "--matrix")
parser.add_argument("-d", "--download", action='store_true')
args = parser.parse_args()

matrix_address = args.matrix if args.matrix != None else "matrix.org"

if args.download:
    print("Downloading")
    download_large_file(args.username, args.password, args.file_input,
                        args.file_output, matrix_address)

else:
    print("Uploading")
    upload_large_file(args.username, args.password, args.file_input,
                      args.file_output, matrix_address)
