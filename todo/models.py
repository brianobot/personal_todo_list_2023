from django.db import models
from django.utils import timezone


DEADLINE = timezone.datetime(2023, 12, 31, tzinfo=timezone.utc)


class Todo(models.Model):
    """
    Model to represent the ToDo instances
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    descr = models.TextField()
    current_stats = models.SmallIntegerField(default=0)
    expected_stats = models.SmallIntegerField(default=100)

    @property
    def percent_completed(self):
        """calculates an returns the percent of the todo action that has been completed."""
        return round((self.current_stats/self.expected_stats) * 100.0, 2)

    @property
    def expected_daily_rate(self):
        """calculates and returns the expected daily rate from current stats
        needed to complete the todo action before the deadline"""
        rem_time = DEADLINE - timezone.now()
        rem_stats = self.expected_stats - self.current_stats
        return round(rem_stats/rem_time.days, 5)

    def __str__(self):
        return self.title

    def __repr__(self) -> str:
        return f"ToDo(title={self.title})"