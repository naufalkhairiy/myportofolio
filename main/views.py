from django.shortcuts import render, get_object_or_404, redirect

from main.models import Experience, Education, Project

from main.forms import ProjectForm, EducationForm

from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse


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

def create_education(request):
    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Education berhasil ditambahkan!")
        return redirect("main:show_education")

    context = {
        "nickname": "Khairiy",
        "form" : form,
        "page_title" : "Add Education",
        "submit_label" : "Add Education",
    }

    return render(request, "education_forms.html", context)

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "nickname": "Khairiy",
        "form": form,
    }

    return render(request, "projects_form.html", context)

def update_education(request, education_id):
    education = get_object_or_404(Education, id=education_id)

    form = EducationForm (
        request.POST or None,
        instance=education
    )

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Education berhasil diperbarui!")
        return redirect(
            "main:show_education_detail",
            education_id=education.id
        )

    context = {
        "nickname": "Khairiy",
        "form" : form,
        "paget_title": "Edit Education",
        "submit_label": "Save Changes",
    }

    return render(request,"education_form.html", context)

def delete_education(request, education_id):
    education = get_object_or_404(Education, id=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Education berhasil dihapus!")

    return redirect("main:show_education")


def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)

    return HttpResponse(
        projects_json,
        content_type="application/json"
    )


def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )

    projects = [project.object for project in projects]

    title_query = request.GET.get("title", "").strip()

    context = {
        "nickname": "Khairiy",
        "project_list": projects,
        "title_query": title_query,
    }

    return render(request, "project.html", context)


def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")