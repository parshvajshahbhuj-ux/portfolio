from django.contrib import admin
from .models import Project, Skill, ContactMessage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "tech_stack", "created_at")
    list_filter = ("created_at",)
    search_fields = ("title", "description", "tech_stack")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    list_filter = ("category",)
    search_fields = ("name",)
    ordering = ("category", "name")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "email", "message")
    readonly_fields = ("name", "email", "message", "created_at")
    ordering = ("-created_at",)

    def has_add_permission(self, request):
        return False  # Messages come only from the contact form
