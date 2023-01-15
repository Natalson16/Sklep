# Generated by Django 4.1.4 on 2022-12-20 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Samochody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=30)),
                ('rok', models.DecimalField(decimal_places=0, max_digits=4)),
                ('cena', models.DecimalField(decimal_places=2, max_digits=10)),
                ('opis', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Samochód',
                'verbose_name_plural': 'Samochody',
            },
        ),
    ]