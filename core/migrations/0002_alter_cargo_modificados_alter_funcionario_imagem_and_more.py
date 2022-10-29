# Generated by Django 4.1.2 on 2022-10-29 21:31

import core.models
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='modificados',
            field=models.DateField(auto_now=True, verbose_name='Atualização'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='imagem',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to=core.models.get_file_path, variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='modificados',
            field=models.DateField(auto_now=True, verbose_name='Atualização'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='modificados',
            field=models.DateField(auto_now=True, verbose_name='Atualização'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='servicos',
            field=models.CharField(max_length=100, verbose_name='Serviço'),
        ),
    ]
