# Generated by Django 3.2.7 on 2021-09-10 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_of_Product', models.CharField(max_length=32)),
                ('Provide', models.CharField(max_length=32)),
                ('Date', models.DateField()),
                ('Price', models.FloatField()),
                ('Quantity', models.IntegerField()),
                ('Amount', models.FloatField()),
                ('Stock', models.IntegerField()),
            ],
        ),
    ]
