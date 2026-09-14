from django.shortcuts import render, get_object_or_404

from main.models import Experience, Education


def show_main(request):
    context = {
        "fullname": "Naufal Khairiy Zulkarnain Sormin",
        "nickname": "Khairiy",
        "npm": "2506621850",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Second Year Computer Science @Universitas Indonesia | "
            "Cyber Security and Robotics Enthusiast."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "nickname": "Khairiy",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_education(request):
    context = {
        "nickname": "Khairiy",
        "education_list" : Education.objects.all().order_by("-start_year")
    }
    return render(request, "education.html", context)

def show_education_detail(request, education_id):
    education = get_object_or_404(Education, id=education_id)

    context = {
        "nickname": "Khairiy",
        "education": education,
    }

    return render(request, "education_detail.html", context)