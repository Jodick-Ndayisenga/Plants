import tensorflow as tf
import os
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai
import joblib
import pickle
import json
from .models import *
import pandas as pd
from tensorflow import keras
from keras.preprocessing import image
import numpy as np
from PIL import Image



openai_Secret_key ="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"

openai.api_key = openai_Secret_key


class_names = ['Early blight', 'Late blight', 'Healthy']










class_names = ['Early blight', 'Late blight', 'Healthy']

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from tensorflow import keras
from keras.preprocessing import image
import numpy as np
from PIL import Image

earlyInfo = [
    {
        "recommendations": [
            {"Early Detection": "Regularly inspect your potato plants for symptoms of early blight, which include dark, irregularly shaped lesions on the leaves. Early detection allows for prompt action."},
            {"Pruning and Removal": "Remove and destroy infected leaves as soon as you spot them. This helps prevent the disease from spreading to healthy parts of the plant."},
            {"Fungicide Treatment": "Consider applying a fungicide specifically designed for early blight. Follow the manufacturer's instructions for application timing and rates."},
            {"Crop Rotation": "Practice crop rotation to reduce the buildup of disease in the soil. Avoid planting potatoes or other solanaceous crops (e.g., tomatoes) in the same location for at least two years."},
            {"Spacing and Ventilation": "Ensure proper spacing between potato plants to promote air circulation, which can reduce humidity and slow the spread of the disease."},
            {"Irrigation Management": "Water your potato plants at the base to keep the foliage dry. Damp foliage can encourage disease development."},
            {"Mulching": "Apply a layer of organic mulch to the soil around the plants to prevent soil from splashing onto the leaves, which can carry the disease."},
            {"Resistant Varieties": "Consider planting potato varieties that are known to be resistant to early blight."},
            {"Good Sanitation": "Clean your tools and equipment to prevent the spread of the disease between plants and fields.",}
        ]
    },
    {
        "background": [
            {"Background": '''
            Early blight disease, scientifically known as Alternaria solani, is a common and destructive fungal disease that affects potato plants (Solanum tuberosum) 
            as well as other solanaceous plants such as tomatoes. It can lead to reduced yields and lower quality tubers. Early blight is caused by the fungus Alternaria 
            solani and is typically more prevalent in warm and humid conditions.'''
            },
            {"Symptoms": '''
            Early blight primarily affects the leaves of potato plants. Symptoms typically 
            appear on the lower leaves first and may include small, dark brown to black circular lesions 
            with concentric rings. These lesions can grow larger and often have a target-like appearance. 
            As the disease progresses, leaves may turn yellow, wither, and eventually die. Infected tubers 
            can also develop shallow, sunken, dark lesions.
            '''
            },
            {"Spread": '''
            The fungus responsible for early blight can survive in the soil and on infected 
            plant debris. It can be spread by wind, rain, irrigation, and through contact with infected 
            plant material. The disease often starts on older, lower leaves and can move upward in the 
            plant canopy.
            '''
            }
        ]
    }
]

lateInfo = [
    {

    "recommendations" : [
    {"Remove and Destroy Infected Plants": "Act promptly by removing visibly infected potato plants from your field. By destroying these plants (through burning or burying), you prevent the late blight pathogen from producing spores that can infect healthy plants nearby."},
    {"Isolate and Quarantine": "To minimize the spread of late blight, establish a designated quarantine area for infected plants. This isolated zone acts as a barrier to prevent the disease from reaching healthy sections of your crop."},
    {"Apply Fungicides": "Consult with local experts or agricultural resources to select appropriate fungicides. Regular and timely applications can help control late blight and protect uninfected potato plants."},
    {"Monitor Weather Conditions": "Keep a vigilant eye on weather forecasts, particularly for cool, wet, and humid conditions that favor late blight development. Applying fungicides proactively, just before these conditions arise, can be highly effective."},
    {"Improve Air Circulation": "Adequate spacing between potato plants allows better air circulation, reducing humidity around the plants. This, in turn, hinders the rapid spread of late blight, which thrives in damp environments."},
    {"Crop Rotation": "Implement crop rotation to break the late blight disease cycle. By not planting potatoes or related crops in the same area for at least two years, you reduce the chances of encountering the disease again in subsequent seasons."},
    {"Seek Expert Advice": "Local agricultural experts and plant pathologists can provide valuable insights tailored to your specific region. Their advice on late blight management strategies will be based on local conditions and trends."},
    {"Copper-Based Home Remedies": "Consider using copper-based sprays like Bordeaux mixture or fixed copper as a preventive measure. While they may not offer complete protection in severe outbreaks, they can provide some defense against late blight."},
    {"Record Keeping": "Maintaining records of your actions and observations is essential for tracking the progression of late blight and assessing the effectiveness of your management strategies. These records will help inform your decisions in future growing seasons."}
]

    },
    {
    "background" : [
    {"Background": '''
    Late blight, caused by the oomycete pathogen Phytophthora infestans, is a highly destructive disease that affects potato and tomato crops. It gained historical significance during the 19th-century Irish Potato Famine, leading to widespread famine. This disease thrives in cool, wet conditions, making it a major concern in regions with temperate climates and high humidity..
    '''
    },
    {"Symptoms": '''
    Late blight exhibits several characteristic symptoms: first, irregularly shaped, water-soaked lesions appear on the leaves, often starting as dark spots that rapidly expand. Second, during periods of high humidity and cool temperatures, a white, cottony growth can develop on the undersides of the leaves, indicating active sporulation by the pathogen. Third, late blight can affect the stems, causing dark, sunken lesions, and it can also lead to brown, firm rot in infected tubers.
    '''
    },
    {"Spread": '''
    Late blight, caused by Phytophthora infestans, spreads through various means. It can be carried by wind to healthy plants, splash from infected leaves due to rain, survive in plant debris and soil for years, and be transmitted through human activity. These factors contribute to the disease's widespread impact in regions with temperate climates and high humidity.
    '''
    }
]

    }
]


healthyInfo = [
    {

    "recommendations" : [
    {"Plant Resistant Varieties": "Select potato varieties that are resistant to late blight. Resistant varieties can significantly reduce the risk of infection."},
            {"Proper Irrigation": "Water your potato plants carefully, avoiding excessive moisture on the leaves. Use drip irrigation or soaker hoses to keep the foliage dry."},
            {"Weed Control": "Keep the area around your potato plants free from weeds, which can provide shelter for the late blight pathogen."},
            {"Crop Monitoring": "Regularly inspect your potato plants for any signs of disease. Early detection can help prevent the spread of late blight."},
            {"Sanitize Equipment": "Clean and sanitize tools and equipment to prevent the spread of the pathogen from plant to plant."},
            {"Mulching": "Applying mulch around potato plants can help regulate soil temperature and moisture, reducing the risk of late blight."},
            {"Optimal Spacing": "Plant potatoes at the recommended spacing to ensure adequate air circulation and reduce humidity around the plants."},
            {"Fertilization": "Properly fertilize your potato plants to promote healthy growth and resilience to disease."},
            {"Scouting for Signs": "Regularly scout for signs of late blight in neighboring crops or wild hosts to detect potential sources of infection."}
        ]

    },
    {
    "background" : [
    {"History": '''
   Potatoes are a vital global staple crop, originating in South America and introduced to Europe in the 16th century. They offer nutritional value, versatility in cooking, and economic significance. Challenges include pest and disease management, but ongoing efforts aim to ensure their role in global food security.
    '''
    },
    {"Facts": '''
    Potatoes, originating in the Andes, are a versatile and nutritious crop with over 5,000 varieties. They are a good source of carbohydrates, vitamin C, potassium, and fiber, and can be prepared in various ways. This globally important staple crop faces challenges such as pests and diseases, but ongoing research aims to develop resilient varieties to ensure their continued role in feeding the world.
    '''
    },
    {"Jokes": '''
    Why did the potato go to the doctor? Because it was peeling unwell and feeling a little mashed up! And when it got there, it told the doctor, "I'm a real tuber of bad news!" The doctor replied, "Don't worry, you just need some couch potato time and you'll be a chipper spud in no time!" The potato chuckled and said, "Well, doc, I guess I just need to starch my sense of humor!"
    '''
    }
]

    }
]




model_filename = 'potatoes.h5'
model_path = os.path.join("Potato", "trained_model", "models", model_filename)
model = keras.models.load_model(model_path)

def preprocess_image(uploaded_image):
    img = Image.open(uploaded_image)
    img = img.resize((256, 256))  # Resize the image to match the model's input size
    img_array = np.array(img) / 255.0  # Normalize the image data if needed
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

    

@csrf_exempt
def predict(request):
    if request.method == 'POST':
        sent_image = request.FILES.get('image')
        try:
            im = preprocess_image(sent_image)
            result = model.predict(im)
            confidence = tf.reduce_max(result).numpy() * 100
            predicted_class = class_names[np.argmax(result)]
            early = late = healthy = False
            documentation = None

            if predicted_class == class_names[0]:
                early = True
            elif predicted_class == class_names[1]:
                late = True
            else:
                healthy = True

            # Define documentation based on the detected disease
            if early:
                documentation = earlyInfo
            elif late:
                documentation = lateInfo
            elif healthy:
                documentation = healthyInfo

            return JsonResponse({
                'confidence': "{:.2f}%".format(confidence),
                'early': early,
                'late': late,
                'healthy': healthy,
                'documentation': documentation,
            })
        except Exception as e:
            # Handle any exceptions that might occur during image processing or prediction
            print("Prediction error:", str(e))
            return JsonResponse({'message': 'Error processing the image.'})
    else:
        return JsonResponse({'message': 'Invalid request method.'})


def index(request):
    return render(request, 'Potato/html/base.html')

def askAgribot(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are AgriBot, a multilingual AI assistant expert in Agriculture trained by USIU AgriTech Team"},
            {"role": "user", "content":message},
        ]
    )
    
    answer = response.choices[0].message.content
    return answer

    

def agribot(request):
    if request.method == 'POST':
        message = request.POST['message']
        response = askAgribot(message)
        
        return JsonResponse({
            "response": response,
        })
    return render(request, 'Potato/html/agribot.html')

model_filename = 'potatoes.h5'
model_path = os.path.join("Potato", "trained_model", "models", model_filename)
model = keras.models.load_model(model_path)

def preprocess_image(uploaded_image):
    img = Image.open(uploaded_image)
    img = img.resize((256, 256))  # Resize the image to match the model's input size
    img_array = np.array(img) / 255.0  # Normalize the image data if needed
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

    

@csrf_exempt
def predict(request):
    if request.method == 'POST':
        sent_image = request.FILES.get('image')

        try:
            im = preprocess_image(sent_image)
            result = model.predict(im)
            confidence = tf.reduce_max(result).numpy() * 100
            predicted_class = class_names[np.argmax(result)]

            early= late= healthy = False

            if predicted_class == class_names[0]:early=True
            elif predicted_class == class_names[1]:late=True
            # else: healthy = True
            elif predicted_class == class_names[2]:healthy=True
            predicted_info = "Healthy",
            if early:predicted_info=earlyInfo
            elif late:predicted_info=lateInfo
            elif healthy:predicted_info=healthyInfo


            return JsonResponse({
                'confidence': "{:.2f}%".format(confidence),
                'early': early,
                'late': late,
                'healthy':healthy,
                'documentation': predicted_info,
                })
        except Exception as e:
            # Handle any exceptions that might occur during image processing or prediction
            print("Prediction error:", str(e))
            return JsonResponse({'message': 'Error processing the image.'})
    else:
        return JsonResponse({'message': 'Invalid request method.'})


def index(request):
    return render(request, 'Potato/html/base.html')

def askAgribot(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are AgriBot, a multilingual AI assistant expert in Agriculture trained by USIU AgriTech Team"},
            {"role": "user", "content":message},
        ]
    )
    
    answer = response.choices[0].message.content
    return answer

    

def agribot(request):
    if request.method == 'POST':
        message = request.POST['message']
        response = askAgribot(message)
        
        return JsonResponse({
            "response": response,
        })
    return render(request, 'Potato/html/agribot.html')
fertilizer_recommender = pickle.load(open(os.path.join("Potato", "trained_model", "models", "rf_pipeline.pkl"), "rb"))
crop_recommender = joblib.load(os.path.join("Potato", "trained_model", "models", "crop_recom.joblib"))

def predict_crop(nitrogen, phosphore, potassium, temperature, humidity, ph, rainfall):
    data = {
        'N': nitrogen,
        'P': phosphore,
        'K': potassium,
        'temperature': temperature,
        'humidity': humidity,
        'ph': ph,
        'rainfall': rainfall,
    }
    X = pd.DataFrame(data, index = [0])
    prediction_result = crop_recommender.predict(X)
    

    with open(os.path.join("Potato", "trained_model", "models", "crop_labels.json"), "r") as jsonfile:
        all_crop_names = json.load(jsonfile)
        return all_crop_names[str(prediction_result[0])]

def crop_recommendation(request):
    if request.method == 'POST':
        nitrogen = request.POST.get('N')
        phosphore = request.POST.get('P')
        potassium = request.POST.get('K')
        temperature = request.POST.get('C')
        humidity = request.POST.get('H')
        ph = request.POST.get('PH')
        rainfall = request.POST.get('mm')
        crop_one = predict_crop(nitrogen, phosphore, potassium, temperature, humidity, ph, rainfall)

        with open(os.path.join("Potato", "trained_model", "models", "additional.json"), "r") as jsonfile:
            all_crop_suggestions = json.load(jsonfile)
            two = all_crop_suggestions[crop_one][0]
            three = all_crop_suggestions[crop_one][1]
            first_class = AllPlants.objects.filter(title = crop_one)
            crop_two = AllPlants.objects.filter(title = two)
            crop_three = AllPlants.objects.filter(title = three)
            return render(request, 'Potato/html/crop_recommend.html', {"first_class":first_class, "second_class":crop_two, "third_class":crop_three})
        
    
    else:
        return render(request, 'Potato/html/crop_recommend.html')


def predict_fertilizer(temperature, humidity, moisture, soil_type, crop, nitrogen, potassium, phosphorus):
    prediction_result = fertilizer_recommender.predict([[temperature, humidity, moisture, soil_type, crop, nitrogen, potassium, phosphorus]])

    with open(os.path.join("Potato", "trained_model", "models", "fertilizer_name.json"), "r") as jsonfile:
        fertilizer_names = json.load(jsonfile)
        return fertilizer_names[str(prediction_result[0])]
    

def fertilizer_recommendation(request):
    if request.method == 'POST':
        # Fetch data from the form
        crop = request.POST.get('crop')
        soil_type = request.POST.get('soil_type')
        nitrogen = request.POST.get('N')
        phosphorus = request.POST.get('P')
        potassium = request.POST.get('K')
        temperature = request.POST.get('C')
        humidity = request.POST.get('H')
        moisture = request.POST.get('moi')
    
        fertilizer = predict_fertilizer(temperature, humidity, moisture, soil_type, crop, nitrogen, potassium, phosphorus)
        all_fertilizers = Picture.objects.filter(title = fertilizer)
        return render(request, 'Potato/html/fertilizer_recommender.html',{"all_fertilizers":all_fertilizers[::-1]})

    return render(request, 'Potato/html/fertilizer_recommender.html')

def myPlantInformation(request, plant_id):
    plant = AllPlants.objects.get(pk=plant_id)
    plantInfo = PlantInformation.objects.filter(item = plant)
    
    return render(request, 'Potato/html/plantInfo.html', {"plantInfo": plantInfo})
