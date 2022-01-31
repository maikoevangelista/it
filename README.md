# Teste técnico para vaga de desenvolvimento

<div style="display: inline_block"><br>
  <img align="center" alt="Maiko" height="50" width="60" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"">
    </div> 
    
 #

Neste teste, será avaliada a sua habilidade de analisar, elaborar e implementar uma solução
para atender à solicitação recebida. Você deve seguir as boas práticas de desenvolvimento, tanto
sobre arquitetura de software quanto de código.
Lembre-se do conceito de **DRY**!
É importante ressaltar a importância sobre a implementação do software Orientado a Objetos
seguindo conceito do** S.O.L.I.D**:

[[S]ingle Responsibility Principle (Princípio da Responsabilidade Única)[O]pen/Closed Principle (Princípio do Aberto/Fechado)[L]iskov Substitution Principle (Princípio da Substituição de Liskov)[I]nterface Segregation Principle (Princípio da Segregação de Interfaces)[D]ependency Inversion Principle (Princípio da Inversão de Dependências)](https://pt.wikipedia.org/wiki/SOLID "[S]ingle Responsibility Principle (Princípio da Responsabilidade Única)[O]pen/Closed Principle (Princípio do Aberto/Fechado)[L]iskov Substitution Principle (Princípio da Substituição de Liskov)[I]nterface Segregation Principle (Princípio da Segregação de Interfaces)[D]ependency Inversion Principle (Princípio da Inversão de Dependências)")


##
Das especificações:
Construir um Web Service na Arquitetura REST, que no qual deverá ser possível realizar as
seguintes ações:**
1. Autenticação (JWT)
2. Criar Usuário
3. Editar Usuário
4. Deletar usuário (Logicamente)
5. Exibir dados do usuário
6. Atribuição de Permissão
7. Armazenar registros de endereço

##
Deverá ser criada uma camada de ACL simples.

- Dados do Usuário
- Nome
- E-mail
- Telefone
- CPF
- Telefone

Dados de Endereço
- Logradouro
- Número
- Bairro
- Complemento
- CEP


##
Requisitos da implementação

1. Utilize a linguagem Python/JS com algum Framework (Flask ou Django ou ExpressJS/AdonisJS);
2. Modelo ER de relacionamento de dados
3. Arquitetura REST
4. Utilização de Design Pattern como por exemplo:
a. Adapter (doc – Exemplo de aplicabilidade: Responses)
b. Abstract Factory (doc – Exemplo de aplicabilidade: Cadastro do Usuário)

##
Aspectos de avaliação:

1. Implementação e organização do código;
2. Validação de dados;
3. Armazenamento e Manipulação de dados;
4. Modularização;
5. Uso adequado dos verbos HTTP
6. Uso adequado dos Status Code HTTP
7. Criação de repositório para versionamento usando GIT;
8. Histórico e Organização de commits;
9. Documentação de com orientações de instalação e forma de uso (READ.MD);
10. Documentação de API Web Service (Recomenda-se o uso do Swagger)
11. Envie o link do repositório para o remetente do e-mail pelo qual você obteve este teste.
Entrega do projeto
1. Disponibilização através do github ou gitlab
2. Disponibilização das collections do postman
3. Disponibilização no modelo ER (Pode ser versionado – Coloque o modelo dentro de uma
pasta docs na raiz do projeto)
