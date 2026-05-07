import json
from django.http import JsonResponse

def login(request):
    if request.method == "POST":
        data = json.loads(request.body)

        username = data.get("username")
        password = data.get("password")

        # SIMPLE MOCK USERS (you can later connect DB)
        users = {
            "admin": {"password": "admin123", "role": "Admin"},
            "doctor1": {"password": "doc123", "role": "Doctor"},
            "patient1": {"password": "pat123", "role": "Patient"}
        }

        if username in users and users[username]["password"] == password:
            return JsonResponse({
                "success": True,
                "role": users[username]["role"],
                "message": "Login successful"
            })

        return JsonResponse({
            "success": False,
            "message": "Invalid credentials"
        })

    return JsonResponse({"error": "Method not allowed"}, status=405)