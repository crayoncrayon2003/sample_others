import io
import csv
import boto3
from botocore.exceptions import ClientError

S3 = boto3.client(
        "s3",
        aws_access_key_id="admin",
        aws_secret_access_key="password",
        endpoint_url="http://localhost:9000"
    )

def carete_bucket(bucket: str):
    try:
        S3.head_bucket(Bucket=bucket)
        print(f"Bucket '{bucket}' already exists. Skipping creation.")
    except ClientError:
        S3.create_bucket(Bucket=bucket)
        print(f"Bucket '{bucket}' created successfully!")

def upload_csv_to_bucket(bucket: str, object_name: str, body):
    try:
        S3.put_object(Bucket=bucket, Key=object_name, Body=body)
    except Exception as e:
        print(f"Error uploading file: {e}")

def download_csv_from_bucket(bucket: str, object_name: str):
    try:
        response = S3.get_object(Bucket=bucket, Key=object_name)
        content = response["Body"].read().decode("utf-8")

        csv_buffer = io.StringIO(content)
        reader = csv.reader(csv_buffer)

        print(f"Contents of '{object_name}' from bucket '{bucket}':")
        for row in reader:
            print(row)

    except Exception as e:
        print(f"Error downloading or reading file: {e}")

# サンプル実行
if __name__ == "__main__":
    bucket = "test-bucket"
    object_name = "test-bucket"

    csv_buffer = io.StringIO()
    writer = csv.writer(csv_buffer)
    writer.writerow(["id", "name", "age"])
    writer.writerow([1, "Alice", 30])
    writer.writerow([2, "Bob", 25])
    writer.writerow([3, "Charlie", 35])

    carete_bucket(bucket)

    upload_csv_to_bucket(bucket, object_name, csv_buffer.getvalue())

    download_csv_from_bucket(bucket, object_name)
