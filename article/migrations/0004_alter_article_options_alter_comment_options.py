# Generated by Django 5.1.3 on 2024-12-06 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_alter_article_article_image_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_date']},
        ),
    ]
