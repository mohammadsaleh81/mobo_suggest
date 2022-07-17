# Generated by Django 3.2 on 2022-07-17 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='modified time')),
                ('deleted_time', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='deleted time')),
                ('deleted', models.BooleanField(default=False, editable=False, verbose_name='deleted')),
                ('title', models.CharField(max_length=128, verbose_name='title')),
                ('text', models.TextField(verbose_name='text')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'sent'), (1, 'seen'), (2, 'not sent')], verbose_name='status')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
    ]
