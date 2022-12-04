# Generated by Django 3.0.7 on 2022-12-04 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(choices=[('mobile', 'Mobile'), ('landline', 'Landline')], max_length=50)),
                ('dial', models.CharField(max_length=30)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='numbers', to='contacts.Contact')),
            ],
        ),
    ]
