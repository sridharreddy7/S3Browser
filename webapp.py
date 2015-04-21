from flask import Flask,render_template,request,json
from boto.s3.connection import S3Connection

app = Flask(__name__)


@app.route('/')
def bucket():
    return render_template('form.html')


@app.route('/submit' , methods=['POST'])
def submit():
  access = request.form.get('access_key')
  secret = request.form.get('secret_key')
  conn = S3Connection(access,secret)
  bucket1 = request.form.get('bucket_name')
  bucket = conn.get_bucket(bucket1)
  bucklist=[]
  name=[]
  for key in bucket.list():
    bucklist.append(key.name.encode('utf-8'))
    name.append(key.generate_url(expires_in=1000, method='GET', headers=None,query_auth=True, force_http=False))
  

  return render_template('results.html' , bucket=json.dumps(bucklist), name= json.dumps(name))


if __name__ == '__main__':

    app.run(debug=True)
