# Tarefas

- [x] Criar API em Flask
- [x] Cria pagina HTML
- [x] Criar API mock do Twitter
- [x] Colocar projeto em Docker
- [x] Colocar projeto em cloud
- [x] Configurar domínio
- [ ] Adicionar certificado
- [ ] Token-Based Authentication
- [ ] Transferir pagina do github pages
- [ ] CICD


# Links

## Site 

- https://igornascalves.github.io/site-web-scraping-/


## API

- Produtos: http://labdados.com/produtos?regiao=norte&ano=2022

- MockTweets: http://labdados.com/2/tweets/search/recent?query=datascience&{tweet_fields}=tweet.fields=author_id,conversation_id,created_at,id,in_reply_to_user_id,public_metrics,lang,text&{user_fields}=expansions=author_id%26user.fields=id,name,username,created_at&start_time=2023-04-11T00:00:00.00Z&end_time=2023-04-12T12:57:15.00Z



# Utilizar Docker 

Clone esse repositorio 

Para criar a imagem 

```
podman build . -t api-curso-xpto:v1.0
```

Para criar o container

```
podman run --rm -d --name api-curso -p 8080:8080 api-curso-xpto:v1.0
```

A aplicação vai ficar disponivel em:

http://localhost:8080/
