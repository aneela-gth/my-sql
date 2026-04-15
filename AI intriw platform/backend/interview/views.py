from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

questions = [
    "Tell me about yourself",
    "What are your strengths?",
    "Why should we hire you?",
    "What is Python?",
    "What are Python data types?",
    "Difference between list and tuple?",
    "What is dictionary in Python?",
    "What is function in Python?",
    "Explain OOP concepts in Python",
    "What is inheritance in Python?",
    "What is HTML?",
    "Difference between HTML and HTML5?",
    "What are semantic tags?",
    "What is CSS?",
    "What is Box Model in CSS?",
    "Difference between Flexbox and Grid?",
    "What is JavaScript?",
    "Difference between var let and const?",
]

current_index = 0
all_answers = []


@csrf_exempt
def start_interview(request):
    global current_index, all_answers

    current_index = 0
    all_answers = []

    return JsonResponse({
        "question": questions[current_index]
    })


@csrf_exempt
def submit_answer(request):
    global current_index, all_answers

    data = json.loads(request.body)
    answer = data.get("answer")

    all_answers.append({
        "question": questions[current_index],
        "answer": answer
    })

    current_index += 1

    if current_index < len(questions):
        return JsonResponse({
            "next_question": questions[current_index]
        })

    return JsonResponse({
        "feedback_summary": generate_feedback(all_answers)
    })


def generate_feedback(answers):
    return (
        "Interview completed successfully. "
        "Good communication skills. "
        "Improve confidence and technical depth. "
        "Practice more coding and project explanation."
    )



from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def signup(request):
    data = json.loads(request.body)

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if User.objects.filter(username=username).exists():
        return JsonResponse({"error": "User already exists"}, status=400)

    User.objects.create_user(
        username=username,
        email=email,
        password=password
    )

    return JsonResponse({"message": "Signup successful"})


@csrf_exempt
def login_user(request):
    data = json.loads(request.body)

    username = data.get("username")
    password = data.get("password")

    user = authenticate(username=username, password=password)

    if user:
        return JsonResponse({
            "message": "Login successful",
            "username": user.username
        })

    return JsonResponse({"error": "Invalid credentials"}, status=400)