from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Project, Skill
from .forms import ContactForm


def home(request):
    projects = Project.objects.all()[:3]
    skills = Skill.objects.all()
    skill_categories = {}
    for skill in skills:
        skill_categories.setdefault(skill.category, []).append(skill)
    context = {
        "projects": projects,
        "skill_categories": skill_categories,
        "meta_title": "Parshva Shah — Full Stack Developer & AI Enthusiast",
        "meta_description": "B.Tech CSE student building smart systems with code and creativity.",
    }
    return render(request, "portfolio/home.html", context)


def about(request):
    skills = Skill.objects.all()
    skill_categories = {}
    for skill in skills:
        skill_categories.setdefault(skill.category, []).append(skill)
    context = {
        "skill_categories": skill_categories,
        "meta_title": "About — Parshva Shah",
        "meta_description": "Learn more about Parshva Shah, a Full Stack Developer and AI enthusiast.",
    }
    return render(request, "portfolio/about.html", context)


def projects(request):
    all_projects = Project.objects.all()
    context = {
        "projects": all_projects,
        "meta_title": "Projects — Parshva Shah",
        "meta_description": "Explore projects built by Parshva Shah including AI platforms and web apps.",
    }
    return render(request, "portfolio/projects.html", context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    context = {
        "project": project,
        "meta_title": f"{project.title} — Parshva Shah",
        "meta_description": project.description[:160],
    }
    return render(request, "portfolio/project_detail.html", context)


def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for reaching out! I'll get back to you soon.")
            return redirect("contact")
    context = {
        "form": form,
        "meta_title": "Contact — Parshva Shah",
        "meta_description": "Get in touch with Parshva Shah for collaborations, internships, or projects.",
    }
    return render(request, "portfolio/contact.html", context)
