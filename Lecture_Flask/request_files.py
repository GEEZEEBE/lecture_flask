from flask import Flask, render_template, request, current_app, send_from_directory
from werkzeug import secure_filename
import os
app = Flask(__name__)
app.config [ 'UPLOAD_FOLDER'] = 'resources/uploads/'
app.config [ 'MAX_CONTENT_PATH'] = 5 * 1024 * 1024
@app.route('/request_files_submit')
def request_files_submit():
    return render_template('request_files_submit.html')

@app.route('/request_files_upload', methods = ['GET', 'POST'])
def request_files_upload():
    if request.method == 'POST':
        file01 = request.files['file01']
        filename01 = secure_filename(file01.filename)
        upload_folder = os.path.join(current_app.root_path, 
                                 current_app.config['UPLOAD_FOLDER'])
        file01.save(os.path.join(upload_folder, filename01))
        return 'file uploaded successfully'

@app.route('/request_files_show')
def request_files_show():
    return render_template('request_files_show.html')
        
@app.route('/image/get_local_download')        
def get_local_download(file_name='Screenshot_from_2017-12-09_18-10-04.png'):
    
    download_folder = os.path.join(current_app.root_path, 
                                 current_app.config['UPLOAD_FOLDER'])
    download_filename = file_name

    return send_from_directory(download_folder, 
                               download_filename, 
                               as_attachment=True, 
                               mimetype='image/jpg')    
        
if __name__ == '__main__':
    app.run(debug = True)
    