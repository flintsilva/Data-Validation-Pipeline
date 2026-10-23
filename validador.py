import re

def calcular_digito(cpf_parcial, peso_inicial):
    """Função que faz o cálculo matemático da Receita Federal"""
    soma = 0
    # O loop ''for'' vai pegar cada número e multiplicar por um peso que diminui (10, 9, 8, ...)
    for numero in cpf_parcial:
        soma += int(numero) * peso_inicial
        peso_inicial -= 1
        
    resto = soma % 11
    if resto < 2:
        return "0"
    else:
        return str(11 - resto)

def limpar_e_validar_dados(cpf_bruto):
    print(f"\n Analisando dado recebido: {cpf_bruto} ")
    
    # 1. PREVENÇÃO DE ATAQUES --- SQL Injection
    caracteres_perigosos = ["'", "--", "OR", "or", "SELECT", "select"]
    for item in caracteres_perigosos:
        if item in cpf_bruto:
            print("⚠️ ALERTA: Tentativa de SQL Injection bloqueada!")
            return "Ataque Detectado"

    # 2. SANITIZAÇÃO --- Limpeza do dado
    cpf_limpo = re.sub(r'[^0-9]', '', cpf_bruto)
    
    # 3. VALIDAÇÃO DE TAMANHO E PADRÕES REPETIDOS
    # CPFs com todos os números iguais vão passa na matemática, mas serão inválidos.
    if len(cpf_limpo) != 11 or cpf_limpo == cpf_limpo[0] * 11:
        print("❌ ERRO: Tamanho inválido ou sequência repetida suspeita.")
        return "Formato Inválido"

    # 4. VALIDAÇÃO DOS DÍGITOS DO CPF
    # Pega os 9 primeiros números para descobrir qual deveria ser o 10º número
    primeiro_digito = calcular_digito(cpf_limpo[:9], 10)
    
    # Pega os 10 primeiros números para descobrir qual deveria ser o 11º número
    segundo_digito = calcular_digito(cpf_limpo[:10], 11)
    
    # Confere se os números calculados batem com os que o usuário digitou
    if cpf_limpo[9] == primeiro_digito and cpf_limpo[10] == segundo_digito:
        print(f"✅ SUCESSO: CPF limpo, autêntico e seguro: {cpf_limpo}")
        return "Seguro e Válido"
    else:
        print("❌ ERRO: Este CPF possui 11 dígitos, mas os números são falsos (Mapeamento falhou).")
        return "CPF Falso/Inválido"

# ===================================================================================================================================================#
# -------------------------------------------------------------ÁREA DE TESTES------------------------------------------------------------------------#
# ===================================================================================================================================================#
if __name__ == "__main__":
    # Teste 1: Um CPF inventado de 11 dígitos 
    limpar_e_validar_dados("123.456.789-10")
    
    # Teste 2: Uma sequência repetida comum que burlaria apenas o tamanho
    limpar_e_validar_dados("222.222.222-22")
    
    # Teste 3: Tentativa de ataque SQLi
    limpar_e_validar_dados("admin' OR 1=1")
    
    # Teste 4: Um CPF matematicamente válido real (Gerado para testes)
    limpar_e_validar_dados("529.982.247-25")
