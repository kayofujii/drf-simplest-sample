# Generated by Django 3.2 on 2021-12-18 05:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('created_at', models.DateTimeField(auto_created=True, verbose_name='登録日時')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20, verbose_name='タイトル')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='価格')),
            ],
            options={
                'verbose_name': '本',
            },
        ),
    ]