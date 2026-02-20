

from django.db import models


class Task(models.Model):
	task_master_id = models.CharField(max_length=100, unique=True)
	title = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	status = models.CharField(max_length=50, default='pending')
	attachment = models.FileField(upload_to='tasks/', null=True, blank=True)
	assigned_at = models.DateTimeField(auto_now_add=True)
	completed_at = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return f"{self.title} ({self.status})"


class Project(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Worker(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField(unique=True)
	is_active = models.BooleanField(default=True)
	joined_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


class Comment(models.Model):
	task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
	author = models.CharField(max_length=255)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"Comment by {self.author} on {self.task.title}"


class Attachment(models.Model):
	task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='attachments')
	file_url = models.URLField()
	uploaded_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"Attachment for {self.task.title}"
