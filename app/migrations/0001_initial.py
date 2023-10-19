# Generated by Django 4.2.6 on 2023-10-19 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciado', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('senha', models.CharField()),
                ('tipo_usuario', models.CharField(choices=[('1', 'Administrador'), ('2', 'Usuário')], default='1', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='ResumoAtividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.IntegerField()),
                ('data', models.DateTimeField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Pontuacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('exercicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.exercicio')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.materia')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='exercicio',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.materia'),
        ),
        migrations.CreateModel(
            name='Conteudo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.materia')),
            ],
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensagem', models.CharField(max_length=45)),
                ('assunto', models.CharField(max_length=45)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Alternativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('status', models.CharField(choices=[('correta', 'Correta'), ('incorreta', 'Incorreta')], default='incorreta')),
                ('exercicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.exercicio')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.materia')),
            ],
        ),
    ]
