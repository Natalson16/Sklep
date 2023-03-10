# Generated by Django 4.1.4 on 2022-12-20 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Samochody', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Marka',
                'verbose_name_plural': 'Marki',
            },
        ),
        migrations.AddField(
            model_name='Samochody',
            name='marka',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Samochody.marka'),
        ),
    ]
