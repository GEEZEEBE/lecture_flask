from flask import Flask, render_template, request
from werkzeug import secure_filename
import os
app = Flask(__name__)
app.config [ 'UPLOAD_FOLDER'] = '/home/yojulab/Downloads'
app.config [ 'MAX_CONTENT_PATH'] = 5 * 1024 * 1024
@app.route('/request_files_submit')
def request_files_submit():
    return render_template('request_files_submit.html')

@app.route('/request_files_upload', methods = ['GET', 'POST'])
def request_files_upload():
    if request.method == 'POST':
        file01 = request.files['file01']
        filename01 = secure_filename(file01.filename)
        file01.save(os.path.join(app.config['UPLOAD_FOLDER'], filename01))
        return 'file uploaded successfully'
        
if __name__ == '__main__':
    app.run(debug = True)