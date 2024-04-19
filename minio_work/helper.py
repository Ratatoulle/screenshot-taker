from minio import Minio
from minio.error import S3Error
from io import BytesIO
import os
from dotenv import load_dotenv

USE_HTTPS = False


class MinioHelper:

    def __init__(self):
        load_dotenv()
        self.client = Minio(endpoint=os.environ.get("MINIO_HTTP"),
                            access_key=os.environ.get("MINIO_ROOT_USER"),
                            secret_key=os.environ.get("MINIO_ROOT_PASSWORD"),
                            secure=USE_HTTPS)
        self.bucket_name = os.environ.get("MINIO_BUCKET_NAME")
        self.create_bucket()

    def create_bucket(self):
        found = self.client.bucket_exists(self.bucket_name)
        if not found:
            self.client.make_bucket(self.bucket_name)
            print(f"Created bucket {self.bucket_name}")
        else:
            print(f"Bucket {self.bucket_name} already exists")

    def save_to(self, name: str, data: bytes):
        data_stream = BytesIO(data)
        self.client.put_object(self.bucket_name, name, data_stream, len(data))

    def get_from(self, name: str):
        try:
            obj = self.client.get_object(self.bucket_name, name)
        except S3Error:
            return None
        else:
            return obj


def main():
    src = "test-file.txt"
    dst = "500.txt"

    helper = MinioHelper()
    helper.save_to(dst, src)


if __name__ == "__main__":
    try:
        main()
    except S3Error as e:
        print("Error occured: ", e)
