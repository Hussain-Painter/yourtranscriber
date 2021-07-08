from flask import Flask, render_template, request, redirect
import speech_recognition as sr

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def index():
    #this method renders the html template as well as process the audio file and generate text
    transcript = ""
    if request.method == "POST":
        print("Form data received")
        if "file" not in request.files: #in case someone spams our API with too many requests 
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "": #if no file has been submitted
            return redirect(request.url)
        
        if file:
            recognizer = sr.Recognizer()
            audio_file = sr.AudioFile(file) 
            with audio_file as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)
            print(transcript)
            



    return render_template("index.html", transcript = transcript)
        

if __name__ == '__main__':
    app.run(threaded = True)

