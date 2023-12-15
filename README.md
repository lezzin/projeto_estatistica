![Foto do projeto](https://github.com/lezzin/projeto_estatistica/assets/103830032/953f34ab-c6ce-46b4-9e5c-470e6e30fc04)

Um aplicativo web de aprendizado construído com Django. Este aplicativo permite aos usuários visualizar matérias, conteúdos e realizar exercicios para fixação do aprendizado, além de visualizar sua pontuação.

## Recursos

- Sistema de login
- Visualizar lista de matérias
- Visualizar conteúdo das matérias
- Realizar lista de exercicios relacionados a determinada matéria
- Visualizar pontuação
- Sistema de ranking

## Começando

Para usar o aplicativo Estatistica:

Localmente:<br>
# Iniciando um Projeto Django com MySQL

## Passo 1: Configurar o Ambiente Virtual

```bash
pip install virtualenv
python -m venv nome_do_seu_ambiente
source nome_do_seu_ambiente/bin/activate   # No Linux/Mac
nome_do_seu_ambiente\Scripts\activate      # No Windows
```

## Passo 2: Instalar o Django

```bash
pip install django 
```

## Passo 3: Configurar o Banco de Dados MySQL

```bash
pip install mysqlclient
```

**lembre-se de criar o banco de dados antes através do phpmyadmin**
Atualize as configurações do banco de dados em settings.py: :

```
# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_seu_banco_de_dados',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '3306',  # Porta padrão do MySQL
    }
}
```

## Passo 4: Aplicar migrações

```bash
python manage.py migrate
```

## Passo 5: Criar um Superusuário (Opcional)

```bash
python manage.py createsuperuser
```

## Passo 6: Iniciar o Servidor de Desenvolvimento

```bash
python manage.py runserver
```

Acesse http://127.0.0.1:8000/ no navegador para ver o seu projeto em execução localmente.

Lembre-se de consultar a documentação oficial do Django e MySQL em caso de dúvidas.
[Django]([https://github.com/lezzin/projeto_estatistica/assets/103830032/953f34ab-c6ce-46b4-9e5c-470e6e30fc04](https://www.djangoproject.com/))
[MySQL]([https://github.com/lezzin/projeto_estatistica/assets/103830032/953f34ab-c6ce-46b4-9e5c-470e6e30fc04](https://www.mysql.com/))

Hospedagem:<br>
Basta acessar o link: [clique aqui para acessar]([https://lista-tarefas-xi.vercel.app/](https://leandroadrian.pythonanywhere.com/))
