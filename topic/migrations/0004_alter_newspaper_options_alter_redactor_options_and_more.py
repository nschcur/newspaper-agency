# Generated by Django 5.0 on 2024-01-09 19:31

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("topic", "0003_alter_redactor_years_of_experience"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="newspaper",
            options={"ordering": ("published_date",)},
        ),
        migrations.AlterModelOptions(
            name="redactor",
            options={"ordering": ("id",)},
        ),
        migrations.AlterModelOptions(
            name="topic",
            options={"ordering": ("name",)},
        ),
        migrations.RemoveField(
            model_name="newspaper",
            name="publish_date",
        ),
        migrations.AddField(
            model_name="newspaper",
            name="additional_topics",
            field=models.ManyToManyField(related_name="topics", to="topic.topic"),
        ),
        migrations.AddField(
            model_name="newspaper",
            name="published_date",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="newspaper",
            name="publishers",
            field=models.ManyToManyField(
                related_name="newspaper_redactors", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="newspaper",
            name="title",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="newspaper",
            name="topic",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="subjects",
                to="topic.topic",
            ),
        ),
        migrations.AlterField(
            model_name="redactor",
            name="years_of_experience",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MaxValueValidator(50),
                    django.core.validators.MinValueValidator(1),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="topic",
            name="name",
            field=models.CharField(max_length=255),
        ),
    ]
