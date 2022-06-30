## jenkins-test-docker

Testando o jenkins localmente usando o docker.


### Requerimentos

- docker
- openssl ( para a criação do certificado "autoassinado" com o comando *keytool* )


### Configuração inicial

```bash
mkdir -p {certs,jenkins_home}
```

#
# docker exec my-jenkins cat /var/jenkins_home/secrets/initialAdminPassword
# ou
# cat ./jenkins_home/secrets/initialAdminPassword


### Certificado "autoassinado"

A senha do certificado será: *mypassword*

Execute o comando:

```bash
keytool -genkey -keyalg RSA -alias selfsigned -keystore certs/jenkins_keystore.jks -storepass mypassword -keysize 4096
```

preencha os dados do certicado autoassinado e pode passar para o próximo passo.

### Executando o container

Lavante o container com o comando:

```bash
docker-compose up -d
```

para verificar execute:

```bash
docker ps
```

### Acessando o Jenkins

Para acessar o Jenkins, use um navegador que aceite certificados autoassinado, como o Firefox por exemplo:

https://{IP_DA_SUA_MAQUINA}:8443
https://localhost:8443

Ao acessar será solicitado inicialmente uma chave de autorização que você poderá obter em:


```bash
sudo cat ./jenkins_home/secrets/initialAdminPassword
```

ou pode usar o docker para isso:

```bash
docker exec my-jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

Depois será preciso instalar os plugins e setar o seu usuário e senha.


### Teste realizado no:

- Linux