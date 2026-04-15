"""
Management command to seed initial portfolio data.
Run: python manage.py seed_data
"""
from django.core.management.base import BaseCommand
from portfolio.models import Project, Skill


class Command(BaseCommand):
    help = "Seeds initial projects and skills data"

    def handle(self, *args, **kwargs):
        # Clear existing
        Project.objects.all().delete()
        Skill.objects.all().delete()

        # Projects
        projects = [
            {
                "title": "CapitalNest",
                "description": (
                    "An AI-powered stock market platform that provides real-time insights, "
                    "portfolio tracking, and predictive analytics using machine learning models. "
                    "Features include live market data, sentiment analysis, and smart alerts."
                ),
                "tech_stack": "Python, Django, TensorFlow, REST API, PostgreSQL, Chart.js",
                "github_link": "https://github.com/parshvajshahbhuj-ux/capitalnest",
                "live_demo": "",
            },
            {
                "title": "TravelMate",
                "description": (
                    "An AI travel planner that generates personalized itineraries based on "
                    "user preferences, budget, and travel style. Integrates with maps and "
                    "booking APIs for a seamless end-to-end travel planning experience."
                ),
                "tech_stack": "Django, Python, OpenAI API, PostgreSQL, Bootstrap, JavaScript",
                "github_link": "https://github.com/parshvajshahbhuj-ux/travelmateps",
                "live_demo": "",
            },
            {
                "title": "Kidzee",
                "description": (
                    "An interactive kids learning platform with gamified lessons, quizzes, "
                    "and progress tracking. Built with a robust Java backend and a relational "
                    "database schema designed for scalability and multi-user support."
                ),
                "tech_stack": "Java, Spring Boot, MySQL, DBMS, HTML, CSS, JavaScript",
                "github_link": "https://github.com/parshvajshahbhuj-ux/kidzee",
                "live_demo": "",
            },
            {
                "title": "CoreInventory",
                "description": (
                    "A full-featured inventory management system designed for businesses to "
                    "track stock levels, manage products, and streamline supply chain operations. "
                    "Features real-time updates, low-stock alerts, and detailed reporting dashboards."
                ),
                "tech_stack": "Python, Django, PostgreSQL, HTML, CSS, JavaScript",
                "github_link": "https://github.com/parshvajshahbhuj-ux/CoreInventory-1-",
                "live_demo": "",
            },
            {
                "title": "AI Project Evaluator Platform",
                "description": (
                    "An intelligent platform that evaluates software projects using AI. "
                    "Analyzes code quality, architecture, documentation, and best practices "
                    "to provide actionable feedback scores and improvement suggestions for developers."
                ),
                "tech_stack": "Python, Django, OpenAI API, JavaScript, PostgreSQL, REST API",
                "github_link": "https://github.com/parshvajshahbhuj-ux/ai-project-evaluator-platform",
                "live_demo": "",
            },
            {
                "title": "AI Voice Detector",
                "description": (
                    "A machine learning-powered voice detection system that identifies and "
                    "classifies audio inputs in real time. Uses deep learning models for "
                    "speaker recognition, voice activity detection, and audio classification."
                ),
                "tech_stack": "Python, TensorFlow, Flask, JavaScript, Web Audio API, NumPy",
                "github_link": "https://github.com/poojanparekh-26/ai-voice-detector",
                "live_demo": "",
            },
        ]

        for p in projects:
            Project.objects.create(**p)
            self.stdout.write(self.style.SUCCESS(f"  Created project: {p['title']}"))

        # Skills
        skills = [
            ("Java", "Programming"),
            ("Python", "Programming"),
            ("JavaScript", "Programming"),
            ("Django", "Web"),
            ("Flask", "Web"),
            ("Node.js", "Web"),
            ("HTML & CSS", "Web"),
            ("REST APIs", "Web"),
            ("MySQL", "Database"),
            ("PostgreSQL", "Database"),
            ("MongoDB", "Database"),
            ("Git & GitHub", "Tools"),
            ("Docker", "Tools"),
            ("VS Code", "Tools"),
            ("Postman", "Tools"),
        ]

        for name, category in skills:
            Skill.objects.create(name=name, category=category)
            self.stdout.write(self.style.SUCCESS(f"  Created skill: {name}"))

        self.stdout.write(self.style.SUCCESS("\nSeed data loaded successfully."))
