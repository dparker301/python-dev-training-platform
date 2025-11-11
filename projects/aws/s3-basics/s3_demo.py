import argparse, boto3, pathlib
def client(): return boto3.client('s3')
def cmd_upload(bucket, key, path): client().upload_file(path, bucket, key); print(f"Uploaded {path} to s3://{bucket}/{key}")
def cmd_list(bucket):
    resp = client().list_objects_v2(Bucket=bucket)
    for obj in resp.get('Contents', []): print(obj['Key'])
def cmd_download(bucket, key, path): client().download_file(bucket, key, path); print(f"Downloaded s3://{bucket}/{key} -> {path}")
if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--bucket", required=True); sub=ap.add_subparsers(dest="cmd")
    up=sub.add_parser("upload"); up.add_argument("path"); up.add_argument("--key", default=None)
    sub.add_parser("list")
    down=sub.add_parser("download"); down.add_argument("key"); down.add_argument("path")
    a=ap.parse_args()
    if a.cmd=="upload": p=pathlib.Path(a.path); cmd_upload(a.bucket, a.key or p.name, str(p))
    elif a.cmd=="list": cmd_list(a.bucket)
    elif a.cmd=="download": cmd_download(a.bucket, a.key, a.path)
    else: ap.print_help()
