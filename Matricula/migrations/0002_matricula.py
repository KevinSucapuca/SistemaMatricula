# Generated by Django 4.2.3 on 2023-07-31 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Matricula', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('turno', models.CharField(max_length=15)),
                ('modalidad', models.CharField(max_length=20)),
                ('alumnoMatricula', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Matricula.alumno')),
                ('cicloMatricula', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Matricula.ciclo')),
            ],
        ),
    ]
