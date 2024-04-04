from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage


def index(request):
    if request.method == "POST":
        try:
            form = ApplicationForm(request.POST)
            if form.is_valid():
                first_name = form.cleaned_data["first_name"]
                last_name = form.cleaned_data["last_name"]
                email = form.cleaned_data["email"]
                start_date = form.cleaned_data["start_date"]
                occupation = form.cleaned_data["occupation"]

                Form.objects.create(first_name=first_name, last_name=last_name, email=email,
                                    start_date=start_date, occupation=occupation)

                message_body = f"Thank you for your submission, {first_name}. \n" \
                               f"Here are your data: \n{first_name}\n{last_name}\n{start_date}\n" \
                               f"Occupation: {occupation}\n" \
                               f"Thank you!"
                email_message = EmailMessage("New job form submission", message_body, to=[email])
                email_message.send()

                messages.success(request, "Form submitted successfully!")

        except Exception as error:
            messages.error(request, str(error), extra_tags="danger")

    return render(request, "index.html")


def about(request):
    return render(request, "about.html")





































