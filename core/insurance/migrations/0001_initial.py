# Generated by Django 4.0.10 on 2024-02-06 08:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('emplooye', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('emplooye', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emplooye.emplooye')),
            ],
        ),
    ]
