# Generated by Django 4.1.1 on 2022-09-13 06:59

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('titulo', models.CharField(max_length=50, verbose_name='Nombre')),
                ('description', models.TextField()),
                ('about_title', models.TextField(max_length=50, verbose_name='Titulo Nosotros')),
                ('about_text', models.TextField()),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email de contacto')),
                ('phone', models.CharField(max_length=20, verbose_name='Telefono de contacto')),
            ],
            options={
                'verbose_name': 'Home',
                'verbose_name_plural': 'Homes',
            },
        ),
        migrations.CreateModel(
            name='Suscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Suscriber',
                'verbose_name_plural': 'Suscribers',
            },
        ),
    ]
