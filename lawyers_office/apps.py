from django.apps import AppConfig


class LawyersOfficeConfig(AppConfig):
    name = 'lawyers_office'
    verbose_name = "lawyers office"

    def ready(self):
        from .models import Office, Link
        if not Office.objects.filter(name='o1').exists():
            Office.objects.create(name='o1')
        # if not Link.objects.all().exists():
            Link.objects.all().delete()
            Link.objects.create(name='New Case', url='new_case', active=True)
            Link.objects.create(name='All Comments', url='comment_list')
