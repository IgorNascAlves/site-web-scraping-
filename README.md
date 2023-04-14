# site-web-scraping-

[Site Exemplo](https://igornascalves.github.io/site-web-scraping-/)


API exemplo

https://idolizedbriefchief.popoflipe.repl.co/produtos?regiao=norte&ano=2022


# Docker

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
