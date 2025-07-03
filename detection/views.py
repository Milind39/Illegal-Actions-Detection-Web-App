from django.conf import settings
from django.core.mail import send_mail
from django.http import StreamingHttpResponse, JsonResponse
from detect import generate_frames, start_detection, stop_detection, get_detected_object
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

is_streaming = False  # Flag to control streaming

def video_feed(request):
    """ Streams video feed to the frontend only when detection is running. """
    global is_streaming
    if not is_streaming:
        return JsonResponse({'error': 'Detection is not running'}, status=400)
    return StreamingHttpResponse(generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')

def home(request):
    """ Renders the homepage """
    return render(request, "home.html")

def blog(request):
    """ Renders the about page """
    return render(request, "blog.html")


def logout_user(request):
    """Logs out the user properly and clears the session."""
    if request.user.is_authenticated:
        logout(request)  # Properly logs out the user
        request.session.flush()  # Clear the session manually
        messages.success(request, "You have been logged out successfully.")
    return redirect('home')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass1')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in!!"))
            # Redirect to a success page.
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            messages.error(request, ("Invalid Username or Password"))
            return redirect('login')

    return render(request, "login.html")


def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # log in user
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ("You have been registered!!"))
            # Redirect to a success page.
            return redirect('home')
        else:
            messages.success(request, ("Whoops! there was a problem registering, try again..."))
            return redirect('register_user/')
    return render(request, "signup.html", {'form': form})

def check_login_status(request):
    """Check if the user is logged in"""
    if request.user.is_authenticated:
        return JsonResponse({'logged_in': True})
    return JsonResponse({'logged_in': False})


def detect(request):
    """ Renders the detection with the live video feed. """
    return render(request, "detect.html")

@login_required
def detect_object(request):
    global running

    if not running:
        return JsonResponse({'status': 'stream_stopped'})

    detected_object = get_detected_object()
    print("Detected Object:", detected_object)  # Debugging

    if detected_object == "smoking" and not request.session.get('email_sent', False):
        request.session['email_sent'] = True
        request.session.modified = True

        if request.user.is_authenticated:
            user_email = request.user.email
            send_mail(
                'Smoking Detected!',
                'The object "Smoking" has been detected.',
                settings.EMAIL_HOST_USER,
                [user_email],
                fail_silently=False,
            )
            print(f"Email sent to {user_email}")  # Debugging
        return JsonResponse({'status': 'email_sent'})

    return JsonResponse({'status': 'no_object_detected'})


def start_stream(request):
    """ Start object detection and video stream """
    global is_streaming
    if not is_streaming:
        is_streaming = True
        start_detection()
    return JsonResponse({'status': 'started'})

def stop_stream(request):
    """ Stop object detection and video stream """
    global is_streaming
    if is_streaming:
        is_streaming = False
        stop_detection()
    return JsonResponse({'status': 'stopped'})
