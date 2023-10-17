from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Todo(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    )

    title = models.CharField(max_length=200, verbose_name=_("Task Title"))
    description = models.TextField(verbose_name=_("Description"))
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    due_date = models.DateField(verbose_name=_("Due Date"))
    status = models.CharField(verbose_name=_("Status"), max_length=50, default='pending', choices=STATUS_CHOICES)

    def clean(self):
        if self.due_date < timezone.now().date():
            raise ValidationError(_("Due date cannot be in the past."))
        
    class Meta:
        verbose_name = _("Todo")
        verbose_name_plural = _("Todos")