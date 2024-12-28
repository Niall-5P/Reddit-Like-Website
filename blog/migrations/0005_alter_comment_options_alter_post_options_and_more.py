# Generated by Django 4.2.17 on 2024-12-26 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on']},
        ),
        migrations.AddField(
            model_name='post',
            name='challenge',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]