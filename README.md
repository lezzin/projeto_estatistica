<h1 align="center"> 📊 <br> Estatísticas</h1>

![Estatísticas](https://github.com/lezzin/projeto_estatistica/assets/103830032/812a9087-113b-4943-95d5-ced039bcfc2d)

<h4 align="center"><a href="https://leandroadrian.pythonanywhere.com">Acessar projeto</a></h4>

---

Um aplicativo web de aprendizado construído com Django. Este aplicativo permite aos usuários visualizar matérias, conteúdos e realizar exercicios para fixação do aprendizado, além de visualizar sua pontuação.

## Recursos

- Sistema de login
- Visualizar lista de matérias
- Visualizar conteúdo das matérias
- Realizar lista de exercicios relacionados a determinada matéria
- Visualizar pontuação
- Sistema de ranking

## Guia de instalação

Para usar o aplicativo Estatistica:

Localmente:<br>

### Passo 1: Configurar o Ambiente Virtual

```bash
pip install virtualenv
python -m venv nome_do_seu_ambiente
source nome_do_seu_ambiente/bin/activate   # No Linux/Mac
nome_do_seu_ambiente\Scripts\activate      # No Windows
```

### Passo 2: Instalar o Django

```bash
pip install django 
```

### Passo 3: Configurar o Banco de Dados MySQL

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

### Passo 4: Aplicar migrações

```bash
python manage.py migrate
```

### Passo 5: Criar um Superusuário (Opcional)

```bash
python manage.py createsuperuser
```

### Passo 6: Iniciar o Servidor de Desenvolvimento

```bash
python manage.py runserver
```

Acesse http://127.0.0.1:8000/ no navegador para ver o seu projeto em execução localmente.

Lembre-se de consultar a documentação oficial do Django e MySQL em caso de dúvidas:
[Django](https://www.djangoproject.com/),
[MySQL](https://www.mysql.com/).

## Tecnologias utilizadas:

* Django
* HTML
* Bootstrap
* JavaScript
* MySQL 

## Contato

Você pode me encontrar nas seguintes redes sociais:

[![Instagram](https://img.shields.io/badge/Instagram-0E6212?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/leandroadrian_/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0E6212?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/leandro-adrian)
