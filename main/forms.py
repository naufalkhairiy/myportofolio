from django.forms import ModelForm, TextInput, Textarea, URLInput, NumberInput
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

from main.models import Project,  Education

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/naufalkhairiy/myportofolio",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
        return title

    def clean_tech_stack(self):
        return strip_tags(self.cleaned_data["tech_stack"]).strip()

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()
    

class EducationForm(ModelForm):
    class Meta:
        model = Education

        fields = ["institution", "program", "start_year", "end_year", "website", "description"]

        labels = {"institution" : "Institution", "program":"Program", "start_year":"Start Year", "end_year" : "End Year", "website":"Institution Website", "description": "Description"}

        widgets = {
            "institution" : TextInput(
                attrs={
                    "placeholder":"Universitas Indonesia",
                }
            ),
            "program": TextInput(
                attrs={
                    "placeholder":"S1 Ilmu Komputer",
                }
            ),
            "start_year": TextInput(
                attrs={
                    "placeholder":"2025",
                }
            ),
            "end_year": TextInput(
                attrs={
                    "placeholder":"Leave blank if still ongoing",
                }
            ),
            "website":URLInput(
                attrs={
                    "placeholder":"https://www.ui.ac.id/",
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Describe your education experience",
                    "rows": 3,  
                }
            )
        }