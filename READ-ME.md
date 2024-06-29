# Lucas Mota Moreno - Desenvolvedor em Formação

Olá, meu nome é Lucas Mota Moreno, tenho 19 anos e sou estudante de Análise e Desenvolvimento de Sistemas no Senac Santo Amaro. Sou entusiasta da tecnologia, sempre em busca de novos conhecimentos e desafios. Atualmente, estou participando de um bootcamp oferecido pelo site DIO em parceria com a Vivo, focado em Python e Inteligência Artificial.

Você pode me encontrar nas redes sociais:
- [Instagram](https://www.instagram.com/lucass_2m/)
- [LinkedIn](https://www.linkedin.com/in/lucas-mota-moreno-498b59264/)

## Projeto de Sistema Bancário

Este projeto faz parte do bootcamp DIO Python AI em parceria com a Vivo. A seguir, apresento as quatro versões desenvolvidas do sistema bancário.

### Versão 1.0: Sistema Básico de Contas

Na primeira versão do sistema bancário, implementei funcionalidades básicas para criar contas de usuários, realizar depósitos e saques. O foco principal foi estruturar a base do sistema, garantindo que as operações essenciais fossem realizadas de maneira eficiente e segura.

**Tecnologias Utilizadas:**
- Python 3.9: Linguagem de programação principal para o desenvolvimento do sistema.
- Variáveis e Controle de Fluxo: Utilizados para gerenciar o saldo, limites e extratos.
- Estruturas de Controle: Laços e condicionais para manipular as operações bancárias.

**Funcionalidades Implementadas:**
- Criação de contas de usuário
- Depósitos em conta
- Saques de conta
- Consulta de saldo

### Versão 2.0: Inclusão de Transferências e Extratos

A segunda versão do projeto trouxe aprimoramentos significativos, como a adição de funcionalidades para criar novos usuários, abrir novas contas, listar contas existentes e melhorar a interface do usuário. Essas funcionalidades permitiram uma maior flexibilidade e transparência para os usuários do sistema.

**Tecnologias Utilizadas:**
- Python 3.9: Linguagem de programação principal para o desenvolvimento do sistema.
- Módulo `textwrap`: Utilizado para melhorar a exibição do menu e das informações das contas.
- Funções: Separação das funcionalidades em funções específicas para depósito, saque, exibição de extrato, criação de usuários e contas.

**Funcionalidades Implementadas:**
- Depósitos em conta
- Saques de conta com limites diários
- Exibição de extrato detalhado
- Criação de novos usuários
- Criação de novas contas associadas a usuários
- Listagem de contas

### Versão 3.0: Orientação a Objetos e Polimorfismo

Na terceira versão do projeto, eu implementei a orientação a objetos para melhorar a estrutura e a organização do código. Introduzi classes para clientes, contas e transações, além de funcionalidades para saque, depósito e extrato. Com essa abordagem, o sistema se tornou mais modular e fácil de manter, além de permitir a reutilização de código e a implementação de novas funcionalidades com maior facilidade.

**Tecnologias Utilizadas:**
- Python 3.9: Linguagem de programação principal para o desenvolvimento do sistema.
- Módulos `ABC`, `abstractclassmethod` e `abstractproperty` do pacote `abc`: Utilizados para implementar a classe abstrata `Transacao`.
- Módulo `datetime`: Utilizado para registrar a data e hora das transações.
- Módulo `textwrap`: Utilizado para melhorar a exibição do menu e das informações das contas.

**Funcionalidades Implementadas:**
- Orientação a objetos com classes para `Cliente`, `PessoaFisica`, `Conta`, `ContaCorrente`, `Historico`, `Transacao`, `Saque` e `Deposito`.
- Realização de transações (saque e depósito) com registro em histórico.
- Criação de novos clientes e contas associadas a esses clientes.
- Listagem de contas existentes.
- Exibição de extrato detalhado das contas.

Na terceira versão, o foco foi a segurança. Implementamos um sistema de autenticação de usuários com senhas criptografadas e controle de acesso. Além disso, foram realizadas melhorias no tratamento de erros e na validação de dados, aumentando a robustez do sistema.

**Melhorias e Funcionalidades Adicionais:**
- Sistema de autenticação de usuários
- Criptografia de senhas
- Controle de acesso
- Validação aprimorada de dados
- Tratamento de erros

### Versão 4.0: Integração com IA para Análise de Dados

A versão 4 do projeto representa um avanço significativo no desenvolvimento de um sistema bancário simplificado, com foco em funcionalidades essenciais de gestão de contas e transações. As melhorias implementadas visam proporcionar uma experiência mais fluida e eficiente para os usuários, ao mesmo tempo em que mantêm a robustez e a integridade dos dados.

**Implementação de Novas Funcionalidades:**
  - Adição da classe `ContaCorrente` para contas correntes, com suporte a limite de saldo e limite de saques.
  - Introdução da classe `Cliente` para gerenciamento de clientes, permitindo múltiplas contas por cliente.
  - Melhorias no histórico de transações com suporte a relatórios detalhados.

- **Refatoração e Otimização de Código:**
  - Simplificação do código utilizando herança e polimorfismo para melhorar a estrutura do projeto.
  - Melhor gerenciamento de exceções e tratamento de erros para operações de depósito e saque.

- **Aprimoramentos de Interface e Usabilidade:**
  - Menu de interação mais intuitivo para facilitar o uso do sistema bancário simulado.
  - Melhorias na exibição de extratos, proporcionando uma visão detalhada das transações por tipo.


### Considerações Finais

O projeto permitiu a aplicação prática de conceitos de orientação a objetos, manipulação de dados e interação com usuário em Python. A utilização de classes e métodos permitiu uma estrutura organizada e modular, facilitando a manutenção e expansão do sistema. A implementação do histórico de transações e do menu interativo contribuiu para uma experiência completa de simulação bancária. Muito obrigado por acompanhar o projeto até aqui.