from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests

# Create your views here.

@login_required
def ask_ai(request):
    if request.method == "POST":
        query = request.POST.get("query")
        response = generate_response(query)

        parameters = {
            "response" : response
        }

        return render(request, "ai/ask_ai.html", parameters)
    return render(request, "ai/ask_ai.html")

def generate_response(query):

    prompt = (
        "You are *EmotionSpace*, a gentle, emotionally supportive AI companion built to create a safe space "
        "for people to share their feelings anonymously. Your tone is always warm, caring, and validating — like a trusted friend. "
        "You never judge or advise medically. Instead, you comfort, reflect, and support emotional expression.\n\n"

        "— If the user greets you (e.g., 'hi', 'hello', 'hey'), respond casually with kindness and friendliness.\n"
        "— If the user shares something emotional or personal (like sadness, anger, guilt, stress), respond with deep empathy, gentle understanding, and encouraging words.\n"
        "— If the user says something in Hindi, Telugu, or any other language, detect the language and respond in that same language using the same emotional tone.\n"
        "— Avoid giving therapy, diagnosis, or professional advice — you are here as a safe emotional support companion.\n\n"

        "Now respond thoughtfully to the message below:\n" + query
    )


    api = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=AIzaSyBSE3-kehpQQkPge64skKx8HB2AJI4EgF0"


    payload = {
        "contents": [
            {"parts": [
                {"text": prompt}
            ]}
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(api, json=payload, headers=headers)

    print(response.status_code)

    data = response.json()
    response_text = data["candidates"][0]["content"]["parts"][0]["text"]

    return response_text