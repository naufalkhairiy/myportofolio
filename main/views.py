from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "fullname": "Naufal Khairiy Zulkarnain Sormin",
        "nickname": "Khairiy",
        "npm": "2506621850",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Second Year Computer Science @Universitas Indonesia"
            "Cyber Security and Robotics Enthusiast."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Khairiy",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)