# SumOne
Desktop Application for Python TKinter GUI Interface

Download for Python => https://www.python.org/downloads/

Comando no CMD depois da instalação do Python: pip install sqlite3     (Instalação do SQLite3 para persistencia dos dados)

Sistema Simples Desktop de Venda de Livro com TKinter, Python e SQLite.
Objetivo do sistema é adicionar venda, excluir venda, alterar venda, excluir a venda, e consultar as vendas realizadas.

1 - Arquivo Login.py, é uma tela de login simples, que comecei fazendo enquanto esperava um voô para floripa.(Descartar esse arquivo, foi a primeira tela de login de teste)

2 - Arquivo LoginNew.py, é uma tela de login um pouco mais robusta, onde podemos criar, e armazenar novas contas no SQLite.

3 - Para executar o projeto, basta clonar o projeto com git clone, ou fazer o download do arquivo .py, e para rodar, basta instalar o Python, e no terminal ou cmd, na pasta do arquivo, executar
o seguinte comando: python LoginNew.py após isso a aplicação irá rodar e aparecer na tela.

4 - Arquivo frontend.py, é o arquivo onde foi desenvolvido a parte de interface da aplicação, utilizando TKinter. Esse arquivo será chamado pelo LoginNew, depois que o metodo login() tiver o return da autenticação.

5 - Arquivo backend.py, é o arquivo onde foi desenvolvido a logica da aplicação, onde conseguimos realizar as vendas dos livros, com adição de venda, exclusão da venda, consulta da venda, alteração da venda e exclusão da venda.