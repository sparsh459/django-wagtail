# Generated by Django 3.2.15 on 2023-05-24 08:38

import django.db.models.deletion
import modelcluster.fields
import wagtail.blocks
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
        ("wagtailcore", "0083_workflowcontenttype"),
        ("home", "0002_create_homepage"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="homepage",
            options={"verbose_name": "Home Page", "verbose_name_plural": "Home Pages"},
        ),
        migrations.AddField(
            model_name="homepage",
            name="banner_cta",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.page",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="banner_image",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="banner_subtitle",
            field=wagtail.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="banner_title",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="content",
            field=wagtail.fields.StreamField(
                [
                    (
                        "cta",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(
                                        max_length=60, required=True
                                    ),
                                ),
                                (
                                    "text",
                                    wagtail.blocks.RichTextBlock(
                                        features=["bold", "italic"], required=True
                                    ),
                                ),
                                (
                                    "button_page",
                                    wagtail.blocks.PageChooserBlock(required=False),
                                ),
                                ("button_url", wagtail.blocks.URLBlock(required=False)),
                                (
                                    "button_text",
                                    wagtail.blocks.CharBlock(
                                        default="Learn More",
                                        max_length=40,
                                        required=True,
                                    ),
                                ),
                            ]
                        ),
                    )
                ],
                blank=True,
                null=True,
                use_json_field=True,
            ),
        ),
        migrations.CreateModel(
            name="HomePageCarouselImages",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "carousel_image",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="carousel_images",
                        to="home.homepage",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
    ]