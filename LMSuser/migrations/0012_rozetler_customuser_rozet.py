# Generated by Django 4.2.5 on 2023-11-09 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LMSuser', '0011_customuser_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rozetler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='rozet_pic')),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='rozet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LMSuser.rozetler'),
        ),
    ]
