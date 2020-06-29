# Generated by Django 3.0.7 on 2020-06-28 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200628_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='photo',
        ),
        migrations.CreateModel(
            name='ImageGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Article')),
            ],
        ),
    ]