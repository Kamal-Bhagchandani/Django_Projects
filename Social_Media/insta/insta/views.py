from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from rest_framework.reverse import reverse_lazy


def hello(request):
    return HttpResponse('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Forgot Password | Instagram</title>
    <style>
        /* Ensure the body takes up the full height of the screen */
        html, body {
            height: 100%;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            background-color: #fafafa;
            font-family: Arial, sans-serif;
        }

        .container {
            background-color: white;
            width: 350px;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        h2 {
            text-align: center;
            font-size: 24px;
            color: #333;
        }

        .input-group {
            margin-bottom: 20px;
        }

        .input-group input {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            font-size: 14px;
        }

        .input-group input:focus {
            border-color: rgb(216, 3, 3);
            outline: none;
        }

        .btn {
            width: 100%;
            padding: 12px;
            background-color: rgb(216, 3, 3);
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
        }

        .btn:hover {
            background-color: rgb(200, 3, 3);
        }

        .back-to-login {
            text-align: center;
            margin-top: 20px;
        }

        .back-to-login a {
            color: rgb(216, 3, 3);
            text-decoration: none;
        }

        .back-to-login a:hover {
            text-decoration: underline;
        }

        /* Footer styling */
        .footer {
            text-align: center;
            font-size: 12px;
            color: #999;
            margin-top: 30px;
            margin-bottom: 20px; /* Space between footer and page bottom */
        }
    </style>
</head>
<body>

<div class="container">
    <h2>Forgot Password</h2>
    <form action="#">
        <div class="input-group">
            <input type="text" name="email_or_phone" placeholder="Email or Phone Number" required>
        </div>
        <button type="submit" class="btn">Send Reset Link</button>
    </form>
    <div class="back-to-login">
        <p>Remember your password? <a href="/login">Back to Login</a></p>
    </div>
</div>

<div class="footer">
    <p>© 2025 Insta_Clone</p>
</div>

</body>
</html>
''')

def home(request):
    return render(request,'home.html')

class Register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"
