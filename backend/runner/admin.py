

from django.contrib import admin

from .models import Task, Project, Worker, Comment, Attachment

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
	list_display = ("id", "task_master_id", "title", "status", "assigned_at", "completed_at")
	search_fields = ("title", "task_master_id", "status")

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ("id", "name", "created_at", "updated_at")
	search_fields = ("name",)

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
	list_display = ("id", "name", "email", "is_active", "joined_at")
	search_fields = ("name", "email")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ("id", "task", "author", "created_at")
	search_fields = ("author", "task__title")

@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
	list_display = ("id", "task", "file_url", "uploaded_at")
	search_fields = ("task__title", "file_url")
