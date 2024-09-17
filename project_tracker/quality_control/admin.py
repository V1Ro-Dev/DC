from django.contrib import admin
from .models import BugReport, FeatureRequest


class BugReportInline(admin.TabularInline):
    model = BugReport
    extra = 0
    fields = ('title', 'project', 'task', 'description', 'status', 'priority', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at', 'project', 'task')
    can_delete = True
    show_change_ling = True


class FeatureRequestInline(admin.TabularInline):
    model = FeatureRequest
    extra = 0
    fields = ('title', 'project', 'task', 'description', 'status', 'priority', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at', 'project', 'task')
    can_delete = True
    show_change_ling = True


@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'project', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'project', 'task')
    search_fields = ('name', 'description')
    list_editable = ('status', )
    fieldsets = [
        (
            None,
            {
                "fields": ['title', 'description', 'project', 'task']
            }
        ),
        (
            "Priority and Bug status",
            {
                "fields": ["priority", "status"]
            }
        )
    ]


@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'project', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'project', 'task')
    search_fields = ('name', 'description')
    fieldsets = [
        (
            None,
            {
                "fields": ['title', 'description', 'project', 'task']
            }
        ),
        (
            "Priority and Feature status",
            {
                "fields": ["priority", "status"]
            }
        )
    ]