# Generated by Django 4.2.6 on 2023-11-20 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_conteudo_imagem_alter_exercicio_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='assunto',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='contato',
            name='mensagem',
            field=models.TextField(),
        ),
    ]
