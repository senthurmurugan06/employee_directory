from django.core.management.base import BaseCommand
from employees.models import Employee
import random

NAMES = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Henry", "Ivy", "Jack"]
DEPARTMENTS = ["HR", "Engineering", "Sales", "Marketing"]

class Command(BaseCommand):
    help = 'Simulate refreshing employee data.'

    def handle(self, *args, **kwargs):
        Employee.objects.all().delete()
        used_names = set()
        for i in range(5):
            while True:
                name = random.choice(NAMES)
                if name not in used_names:
                    used_names.add(name)
                    break
            email = f"{name.lower()}@example.com"
            department = random.choice(DEPARTMENTS)
            Employee.objects.create(name=name, email=email, department=department)
        self.stdout.write(self.style.SUCCESS('Employee data refreshed!')) 