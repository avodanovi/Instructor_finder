# Generated by Django 2.2.4 on 2019-09-04 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20190904_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='knows',
            field=models.ManyToManyField(blank=True, related_name='knows_subjects', to='app.Subject'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='learns',
            field=models.ManyToManyField(blank=True, related_name='learns_subjects', to='app.Subject'),
        ),
    ]
