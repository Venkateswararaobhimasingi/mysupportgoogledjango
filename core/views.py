from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
import google.generativeai as genai

genai.configure(api_key="AIzaSyDEV4I8_gmbwDN2eMfdHd_xBQaLzZ-oUoE")
model = genai.GenerativeModel("gemini-1.5-flash")

@api_view(['POST'])
def reply_content(request):
    data = json.loads(request.body)
    body = data.get("body", "")
    requirements = data.get("requirements", "")
    suggestions = data.get("suggestions", "")

    prompt = f"""You are an assistant generating an email reply.
Original message:
{body}

Requirements from user:
{requirements}

Suggestions from user:
{suggestions}

Now write a helpful email reply and suggest a subject."""
    
    result = model.generate_content(prompt)
    return Response({"reply": result.text})
