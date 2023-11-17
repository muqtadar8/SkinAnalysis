from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import requests

def query(filename):
    API_URL1 = "https://api-inference.huggingface.co/models/dima806/man_woman_face_image_detection"
    headers1 = {"Authorization": "Bearer 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"}
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL1, headers=headers1, data=data)
    return response.json()

def query1(filename):
    API_URL = "https://api-inference.huggingface.co/models/varun1505/face-characteristics"
    headers = {"Authorization": "Bearer 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"}
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()




def analyze_image(request):
    if request.method == "POST" and request.FILES['image']:
        uploaded_image = request.FILES['image']
 
        # Save the uploaded image to a temporary file
        with open("static/temp_image.jpg", "wb") as f:
            for chunk in uploaded_image.chunks():
                f.write(chunk)

        # Perform image analysis using your functions
        check, analysis_result = main("static/temp_image.jpg")
       
        return render(request, 'result.html', {'results': analysis_result, 'image' : uploaded_image, 'gender':check})

    return render(request, 'upload.html')

def main(path):
    one = query(path)
    if type(one) != str:
        if (float(one[0]['score']) > 0.2) and (float(one[1]['score']) > 0.2):
            return 0, "Please upload a single facial image"

        two = query1(path)

        if one[0]['label'] == 'man':
            if isinstance(two, list):
                # Filter out dictionaries with 'label' equal to 'skin redness'
                two = [item for item in two if isinstance(item, dict) and item.get('label') != 'skin redness']   
            return one[0]['label'], two
        else :
            return one[0]['label'], two
    else:
        return one, "Please upload a single facial image"

