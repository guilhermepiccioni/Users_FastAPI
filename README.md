# Aplicação Fastapi com Docker e PostgreSQL

Aqui tem um programa simples onde pode ser cadastrado um usuario, salvando em banco de dados, 
poder ser alterado e deletado.

Para iniciar o processo, primeiro temos que ter o docker instalado em sua maquina, 
tendo isto, execute o comando:
```
make db_run
```
Após executar o comando acima, acesse o browser e digite localhost:5050. Iremos conectar o banco de dados.

Coloque as credenciais informadas do arquivo docker-compose.yml do pgadmin.
```
PGADMIN_DEFAULT_EMAIL: admin@admin.com
PGADMIN_DEFAULT_PASSWORD: admin
```
<img height="300" src="/Users/guilhermepiccioni/Desktop/Screenshot 2022-11-14 at 12.41.59.png" width="300"/>
<img height="300" src="/Users/guilhermepiccioni/Desktop/Screenshot 2022-11-14 at 12.42.24.png" width="300"/>

Feita a conexão, aplique o seguinte comando:
```
make fastapi_run
```
Agora, acesse o navegador atraves da porta disponivel pelo FastApi.

---------------------------------------------------------------------------------------------------------------------
###### English
# Fastapi application with Docker and PostgreSQL

Here is a simple program where a user can be registered, saved in a database, changed and deleted.

To start the process, first we have to have docker installed on your machine, having this, run the command:
```
make db_run
```
After executing the above command, access the browser and type localhost:5050. We will connect the database.

Put the credentials provided from pgadmin's docker-compose.yml file.
```
PGADMIN_DEFAULT_EMAIL: admin@admin.com
PGADMIN_DEFAULT_PASSWORD: admin
```
Once connected, run the following command:
```
make fastapi_run
```
Now, access the browser through the port available through FastApi.