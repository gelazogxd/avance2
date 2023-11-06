from django.contrib import admin

from .models import GrantGoal

# Register your models here.

# se le pone el punto(.) para indicar que esta en el mismo folfer


@admin.register(GrantGoal)
class GrantGoalAdmin(admin.ModelAdmin):
    list_display = [
        "gg_tittle",
        "timestamp",
        "days_duration",
        "final_date",
        "user"
    ]


