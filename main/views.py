from django.shortcuts import render, get_object_or_404, redirect

from main.models import Experience, Education, Project

from main.forms import ProjectForm, EducationForm

from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render

import datetime

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "fullname": "Naufal Khairiy Zulkarnain Sormin",
        "nickname": "Khairiy",
        "npm": "2506621850",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Second Year Computer Science @Universitas Indonesia | "
            "Cyber Security and Robotics Enthusiast."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "nickname": "Khairiy",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def get_education_json(request):
    """Return Education data as JSON, optionally filtered by institution."""
    institution_query = request.GET.get("institution", "").strip()

    educations = Education.objects.all()

    if institution_query:
        educations = educations.filter(
            institution__icontains=institution_query
        )

    educations = educations.order_by("-start_year")

    education_json = serializers.serialize(
        "json",
        educations
    )

    return HttpResponse(
        education_json,
        content_type="application/json"
    )


def show_education(request):
    """Display Education data after retrieving and deserializing its JSON representation."""
    json_response = get_education_json(request)

    educations = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8")
    )

    educations = [
        education.object
        for education in educations
    ]

    institution_query = request.GET.get(
        "institution",
        ""
    ).strip()

    context = {
        "nickname": "Khairiy",
        "education_list": educations,
        "institution_query": institution_query,
    }

    return render(request, "education.html", context)


def show_education_detail(request, education_id):
    education = get_object_or_404(
        Education,
        id=education_id
    )

    context = {
        "nickname": "Khairiy",
        "education": education,
    }

    return render(
        request,
        "education_detail.html",
        context
    )

@login_required(login_url="/login/")
def create_education(request):
    if not request.user.is_superuser:
            raise PermissionDenied
    """Create a new Education entry using EducationForm."""
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

    return render(request, "education_form.html", context)


@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
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
    """Update an existing Education entry identified by its UUID."""
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
        "page_title": "Edit Education",
        "submit_label": "Save Changes",
    }

    return render(request,"education_form.html", context)

@login_required(login_url="/login/")
def delete_education(request, education_id):
    if not request.user.is_superuser:
            raise PermissionDenied
    
    """Delete an Education entry through a POST request."""
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

    projects_json = serializers.serialize("json", projects, use_natural_foreing_keys= True)

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

@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.is_superuser:
            raise PermissionDenied
    
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silahkan login.")
        return redirect("main:login")

    context = {
        "nickname" : "Khairiy",
        "form" : form,
    }

    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "nickname": "Khairiy",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")