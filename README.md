# 📝 Desafio Django: Mural de Avisos Comunitário



Este projeto é um desafio prático para consolidar os fundamentos do framework **Django**. O objetivo é transformar um protótipo de baixa fidelidade em uma aplicação funcional, aplicando o padrão **MTV (Model-Template-View)**.

## 🎯 Objetivo do Desafio
Construir um sistema simples onde usuários possam visualizar e cadastrar avisos categorizados (Eventos, Serviços ou Vendas).

---

## 🖼️ O Protótipo (Wireframe)

A interface deve seguir a estrutura básica abaixo:

### Home (Lista de Avisos)
```text
+-------------------------------------------------------------+
| [ LOGO ] Mural de Avisos                    ( + Novo Aviso )|
+-------------------------------------------------------------+
|                                                             |
| FILTRAR: [ Todos ] [ Eventos ] [ Serviços ] [ Vendas ]      |
|                                                             |
| +---------------------+      +---------------------+        |
| | Título do Aviso     |      | Título do Aviso     |        |
| | Categoria: Evento   |      | Categoria: Venda    |        |
| | [ Ver Detalhes ]    |      | [ Ver Detalhes ]    |        |
| +---------------------+      +---------------------+        |
|                                                             |
+-------------------------------------------------------------+
```

---

## 🛠️ Requisitos Técnicos

### 1. Modelagem (Models)
Crie um app chamado `mural` e um model `Aviso` com os campos:
* `titulo`: CharField (máx. 100 caracteres)
* `conteudo`: TextField
* `categoria`: CharField (usando `choices` para Eventos, Serviços e Vendas)
* `data_criacao`: DateTimeField (com `auto_now_add=True`)

### 2. Templates (Herança)
Utilize a herança de templates do Django:
* `base.html`: Contendo o esqueleto HTML e a barra de navegação.
* `lista_avisos.html`: Para listar os cards de avisos.
* `detalhe_aviso.html`: Para exibir o conteúdo completo.
* `form_aviso.html`: Para o formulário de cadastro.

### 3. Views e URLs
Implemente as seguintes rotas:
* `/`: Lista todos os avisos (ordenados do mais recente para o mais antigo).
* `/aviso/<int:id>/`: Exibe os detalhes de um aviso.
* `/novo/`: Exibe e processa o formulário de cadastro.

---

## 🚀 Como Executar (Instruções para o Aluno)

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/santos-santos/avisos.git
    ```
2.  **Crie e ative o ambiente virtual:**
    ```bash
    python -m venv .venv
    # Windows: .venv\Scripts\activate
    # Linux/Mac: source .venv/bin/activate
    ```
3.  **Instale o Django:**
    ```bash
    pip install django
    ```
4.  **Rode as migrações e inicie o servidor:**
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

---

## 🌟 Bônus (Opcional)
* Adicione estilização usando **Bootstrap**. 
* Implemente um campo de busca por título na página inicial.
* Crie uma funcionalidade para "Deletar" um aviso.

---

> **Dica do Instrutor:** Foque primeiro em fazer o dado sair do Banco de Dados e aparecer na tela. A estética é importante, mas a lógica do Django é sua prioridade hoje!

---
