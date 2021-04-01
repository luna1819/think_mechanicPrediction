# Generated by Django 2.2.3 on 2019-08-02 05:48

from django.db import migrations, models
import apps


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_auto_20190802_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='filemodel',
            name='file_save_name',
            field=models.CharField(default='1', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='filemodel',
            name='file_name',
            field=models.FileField(upload_to=apps.file_upload_path_for_db),
        ),
    ]