# Lista-de-clientes-Django
Navegar até Lista-de-clientes-Django/agenda e executar o edior 

# Para o correto funcionamento instalar as depedências abaixo

pip install django
pip install django-crispy-forms
pip install mysqlclient
pip install requests 

# Faça a criação do banco de dados mysql (recomendo fazer o uso do arquivo sql) 
# Faça a alteração referente ao banco de dados no arquivo settings.py linha 82 e 83

# Com as depedencias instaladas e o banco configurado, rodar os seguntes códigos

python manage.py migrate
python manage.py makemigrations
python manage.py runserver



