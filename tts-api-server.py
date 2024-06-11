from flask import Flask , request , send_file
from TTSService import TTSService
import time, tempfile

HOST = '10.105.173.241'
PORT = 5000

app = Flask(__name__)
service = TTSService()
@app.route('/tts', methods = ['POST'])
def text_to_speech():
    json:dict = request.get_json()
    text = json['text']
    start = time.time()
    data = service.text_to_speech(text)
    f = tempfile.NamedTemporaryFile(suffix='.wav', delete=False)
    f.write(data)
    print('file path: {}'.format(f.name))
    end = time.time()
    elapsed = end - start 
    print('elapsed: {}'.format(elapsed))
    response = send_file(f.name, as_attachment=True, download_name='data.wav', mimetype='.wav')
    f.close()
    return response
if __name__ == '__main__':
    # from waitress import serve
    # serve(app, host=HOST, port=PORT)
    app.run(host=HOST,debug=False, port=PORT)