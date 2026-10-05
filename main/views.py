import datetime

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import PermissionDenied
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from main.forms import EducationForm, ProjectForm
from main.models import Education, Experience, Project


def can_edit_education(user):
    """Superuser dan anggota Group Editor boleh mengubah Education."""
    return user.is_authenticated and (
        user.is_superuser
        or user.groups.filter(name="Editor").exists()
    )


def show_main(request):
    last_login = request.COOKIES.get(
        "last_login",
        "Belum ada sesi login / Cookie tidak ditemukan",
    )

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
    """Mengirim field Education yang aman melalui endpoint JSON."""
    institution_query = request.GET.get("institution", "").strip()
    educations = Education.objects.prefetch_related("starred_by")

    if institution_query:
        educations = educations.filter(
            institution__icontains=institution_query
        )

    if request.GET.get("sort") == "stars":
        educations = educations.annotate(
            star_total=Count("starred_by")
        ).order_by(
            "-star_total",
            "-start_year",
            "institution",
            "id",
        )
    else:
        educations = educations.order_by(
            "-start_year",
            "institution",
            "id",
        )

    data = []

    for education in educations:
        starred_users =  education.starred_by.all()

        is_starred = (
            request.user in starred_users
            if request.user.is_authenticated
            else False
        )

        data.append({
            "pk": str(education.id),
            "fields": {
                "institution" : education.institution,
                "program" : education. program,
                "start_year": education.start_year,
                "end_year": education.end_year,
                "website" : education.website,
                "description" : education.description,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
            },
        })
    return JsonResponse(data, safe=False)


def show_education(request):
    """Menampilkan halaman Education; data daftar dimuat melalui AJAX."""
    institution_query = request.GET.get("institution", "",).strip()


    context = {
        "nickname": "Khairiy",
        "institution_query": institution_query,
        "sort": request.GET.get("sort", ""),
        "form" : EducationForm(),
    }

    return render(request, "education.html", context)


def show_education_detail(request, education_id):
    education = get_object_or_404(
        Education,
        id=education_id,
    )

    context = {
        "nickname": "Khairiy",
        "education": education,
        "can_edit_education": can_edit_education(request.user),
    }

    return render(
        request,
        "education_detail.html",
        context,
    )


@login_required(login_url="main:login")
def create_education(request):
    """Hanya superuser yang boleh membuat Education."""
    if not request.user.is_superuser:
        raise PermissionDenied

    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(
            request,
            "Education berhasil ditambahkan!",
        )
        return redirect("main:show_education")

    context = {
        "nickname": "Khairiy",
        "form": form,
        "page_title": "Add Education",
        "submit_label": "Add Education",
    }

    return render(
        request,
        "education_form.html",
        context,
    )


@login_required(login_url="main:login")
def update_education(request, education_id):
    """Superuser dan Editor boleh mengubah Education."""
    if not can_edit_education(request.user):
        raise PermissionDenied

    education = get_object_or_404(
        Education,
        id=education_id,
    )

    form = EducationForm(
        request.POST or None,
        instance=education,
    )

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(
            request,
            "Education berhasil diperbarui!",
        )
        return redirect(
            "main:show_education_detail",
            education_id=education.id,
        )

    context = {
        "nickname": "Khairiy",
        "form": form,
        "page_title": "Edit Education",
        "submit_label": "Save Changes",
    }

    return render(
        request,
        "education_form.html",
        context,
    )


@login_required(login_url="main:login")
def delete_education(request, education_id):
    """Hanya superuser yang boleh menghapus Education."""
    if not request.user.is_superuser:
        raise PermissionDenied

    return _delete_education_post(
        request,
        education_id,
    )


@require_POST
def _delete_education_post(request, education_id):
    education = get_object_or_404(
        Education,
        id=education_id,
    )

    education.delete()

    messages.success(
        request,
        "Education berhasil dihapus!",
    )

    return redirect("main:show_education")


@login_required(login_url="main:login")
@require_POST
def toggle_education_star(request, education_id):
    """Memberikan atau membatalkan Star pada Education."""
    education = get_object_or_404(
        Education,
        id=education_id,
    )

    if education.starred_by.filter(
        pk=request.user.pk
    ).exists():
        education.starred_by.remove(request.user)
        message = "Star Education dibatalkan."
    else:
        education.starred_by.add(request.user)
        message = "Education diberi star."

    if request.headers.get("Accept") == "application/json":
        return JsonResponse({
            "message": message,
        })

    messages.success(request, message,)
    return redirect("main:show_education")


def get_projects_json(request):
    """Mengirim field Project yang aman melalui endpoint JSON."""
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.prefetch_related('starred_by').all()

    if title_query:
        projects = projects.filter(
            title__icontains=title_query
        )

    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(project.id),
            'fields': {
                        "title" : project.title,
                        "description" : project.description,
                        "tech_stack" : project.tech_stack,
                        "project_url" : project.project_url,
                        "project_image_url" : project.project_image_url,
                        "star_count": starred_users.count(),
                        "is_starred": is_starred,
                        "starred_by_names" : starred_by_names,
            }
        })
    
    return JsonResponse(data, safe=False)


def show_projects(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "nickname": "Khairiy",
        "title_query": title_query,
        "form": ProjectForm(),
    }

    return render(
        request,
        "project.html",
        context,
    )


@login_required(login_url="main:login")
def create_project(request):
    """Hanya superuser yang boleh membuat Project."""
    if not request.user.is_superuser:
        raise PermissionDenied

    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(
            request,
            "Proyek baru berhasil ditambahkan!",
        )
        return redirect("main:show_projects")

    context = {
        "nickname": "Khairiy",
        "form": form,
    }

    return render(
        request,
        "projects_form.html",
        context,
    )


@login_required(login_url="main:login")
def delete_project(request, project_id):
    """Hanya superuser yang boleh menghapus Project."""
    if not request.user.is_superuser:
        raise PermissionDenied

    project = get_object_or_404(
        Project,
        pk=project_id,
    )

    if request.method == "POST":
        project.delete()
        messages.success(
            request,
            "Project berhasil dihapus!",
        )

    return redirect("main:show_projects")


@login_required(login_url="main:login")
def toggle_star(request, project_id):
    """Memberikan atau membatalkan Star pada Project."""
    project = get_object_or_404(
        Project,
        pk=project_id,
    )

    if request.method == "POST":
        if project.starred_by.filter(
            pk=request.user.pk
        ).exists():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")


def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(
            request,
            "Akun berhasil dibuat. Silahkan login.",
        )
        return redirect("main:login")

    context = {
        "nickname": "Khairiy",
        "form": form,
    }

    return render(
        request,
        "register.html",
        context,
    )


def login_user(request):
    form = AuthenticationForm(
        request,
        data=request.POST or None,
    )

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)

        response = redirect("main:show_main")
        response.set_cookie(
            "last_login",
            datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
        )

        return response

    context = {
        "nickname": "Khairiy",
        "form": form,
    }

    return render(
        request,
        "login.html",
        context,
    )


def logout_user(request):
    logout(request)

    response = redirect("main:show_main")
    response.delete_cookie("last_login")

    return response

@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan proyek."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Proyek berhasil ditambahkan.", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

@require_POST
def create_education_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {
                "message": (
                    "hanya pemilik portofolio yang dapat "
                    "menambahkan education."
                )
            },
            status=403,
        )
    form = EducationForm(request.POST)

    if form.is_valid():
        education = form.save()

        return JsonResponse(
            {
                "message": "Education berhasil ditambahkan.",
                "pk" : str(education.id),
            },
            status = 201,
        )

    return JsonResponse(
        {
            "errors": form.errors.get_json_data(),
        },
        status =400,
    )