from flask import Flask, request, render_template, send_file, Response
from config import S3_ENDPOINT, S3_ACCESS_KEY, S3_SECRET_KEY, S3_BUCKET_NAME, SUPABASE_URL, SUPABASE_ANON_KEY
from botocore.client import Config
from io import BytesIO
import boto3
import mimetypes
import requests

app = Flask(__name__)

# Initialize S3 client (for list, download, stream only — not upload anymore)
s3 = boto3.client(
    's3',
    endpoint_url=S3_ENDPOINT,
    aws_access_key_id=S3_ACCESS_KEY,
    aws_secret_access_key=S3_SECRET_KEY,
    config=Config(signature_version='s3v4'),
    region_name='us-east-1'
)

@app.route('/')
def index():
    query = request.args.get("search", "").lower()
    files = s3.list_objects_v2(Bucket=S3_BUCKET_NAME).get("Contents", [])
    if query:
        files = [f for f in files if query in f["Key"].lower()]
    return render_template("index.html", files=files, search=query)


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    if not file:
        return "No file uploaded", 400

    filename = file.filename
    file_data = file.read()

    try:
        # Guess MIME type based on filename
        content_type = mimetypes.guess_type(filename)[0] or "application/octet-stream"

        headers = {
            "Authorization": f"Bearer {SUPABASE_ANON_KEY}",
            "Content-Type": content_type,
            "x-upsert": "true"
        }

        url = f"{SUPABASE_URL}/storage/v1/object/{S3_BUCKET_NAME}/{filename}"
        response = requests.post(url, headers=headers, data=file_data)

        if response.status_code in [200, 201]:
            return "Uploaded successfully", 200
        else:
            print(f"❌ Supabase upload error: {response.status_code} - {response.text}")
            return f"Upload failed: {response.text}", 500

    except Exception as e:
        print(f"❌ Upload error: {e}")
        return f"Upload failed: {str(e)}", 500


@app.route('/download/<filename>')
def download(filename):
    file_obj = s3.get_object(Bucket=S3_BUCKET_NAME, Key=filename)
    return send_file(BytesIO(file_obj['Body'].read()), download_name=filename, as_attachment=True)


@app.route('/stream/<filename>')
def stream(filename):
    range_header = request.headers.get('Range', None)
    file_obj = s3.get_object(Bucket=S3_BUCKET_NAME, Key=filename)
    data = file_obj['Body'].read()

    if range_header:
        start, end = range_header.replace('bytes=', '').split('-')
        start = int(start)
        end = int(end) if end else len(data) - 1
        chunk = data[start:end+1]
        return Response(chunk, status=206, mimetype=get_mime_type(filename), headers={
            'Content-Range': f'bytes {start}-{end}/{len(data)}',
            'Accept-Ranges': 'bytes',
            'Content-Length': str(len(chunk))
        })

    return Response(data, mimetype=get_mime_type(filename))

@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    try:
        s3.delete_object(Bucket=S3_BUCKET_NAME, Key=filename)
        return "Deleted successfully", 200
    except Exception as e:
        print(f"❌ Delete error: {e}")
        return f"Delete failed: {str(e)}", 500

def get_mime_type(filename):
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream'



if __name__ == '__main__':
    app.run(debug=True)
