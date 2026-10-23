#Pipeline de Sanitização e Validação Defensiva de Dados

Este projeto simula uma camada crítica de tratamento e sanitização de dados cadastrais (especificamente números de CPF) no ecossistema de Back-end. Ele foi desenvolvido com o objetivo de demonstrar conceitos fundamentais de Engenharia de Dados, manipulação robusta de strings e Segurança Defensiva de Aplicações (AppSec) utilizando Python puro.

### 🚀 Funcionalidades

O script processa strings brutas de entrada, simulando dados recebidos de uma API externa ou formulário, e executa um pipeline de validação em múltiplas etapas:
1. **Segurança Defensiva:** Detecção e bloqueio preventivo contra ataques de injeção lógica (SQL Injection) através da auditoria de padrões maliciosos na string bruta.
2. **Sanitização de Dados:** Limpeza de ruídos estruturais (espaços, pontos, traços) utilizando Expressões Regulares (`re.sub`), garantindo a padronização do dado.
3. **Auditoria de Integridade:** Identificação e bloqueio de falsos-positivos matemáticos comuns (sequências repetidas inválidas como `111.111.111-11`).
4. **Validação Algorítmica:** Execução do algoritmo oficial de Módulo 11 da Receita Federal através de estruturas de repetição (`for`) para validar matematicamente os dois dígitos verificadores.
5. **Isolamento de Arquitetura:** Uso do bloco nativo `if __name__ == "__main__":` para isolar os testes unitários, garantindo que as funções de validação possam ser importadas por outros sistemas corporativos com segurança, sem disparar logs de teste.

### 🛠️ Tecnologias Utilizadas
* **Python 3.x** (Módulo nativo `re` para Regex e operadores matemáticos padrão)
