# Generated by Django 5.0.4 on 2024-04-16 18:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_post_conteudo_alter_post_fontes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Populacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='atores_envolvidos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.ator'),
        ),
        migrations.AlterField(
            model_name='post',
            name='municipio_atingido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.municipio'),
        ),
        migrations.AlterField(
            model_name='post',
            name='populacao_atingida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.populacao'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.tema'),
        ),
    ]