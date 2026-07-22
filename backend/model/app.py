from flask import Flask,request,jsonify
from flask_cors import CORS
import os 
from predict import predict_digit
app=Flask(__name__)
CORS(app)
UPLOADED_FOLDER="uploads"
if not os.path.exists(UPLOADED_FOLDER):
    os.makedirs(UPLOADED_FOLDER)
@app.route("/")
def home():
    return    "API IS RUNNING" 
@app.route("/predict",methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error:":"no image uploaded"}),400
    image=request.files["image"]
    image_path=os.path.join(UPLOADED_FOLDER,image.filename)
    image.save(image_path)
    digit=predict_digit(image_path)
    return jsonify({
        "prediction":digit
    })
if __name__=="__main__":
    app.run(debug=True)
