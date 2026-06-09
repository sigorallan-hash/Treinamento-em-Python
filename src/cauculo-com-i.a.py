def validar_cpf(cpf_original):
    # Remove caracteres não numéricos (pontos, traços), caso o usuário os digite
    cpf_original = ''.join(filter(str.isdigit, cpf_original))

    # Verifica se o CPF tem exatamente 11 dígitos
    if len(cpf_original) != 11:
        print("CPF inválido: deve conter exatamente 11 dígitos.")
        return False

    # Rejeita CPFs com todos os dígitos iguais (ex: 111.111.111-11)
    if len(set(cpf_original)) == 1:
        print("CPF inválido: todos os dígitos são iguais.")
        return False

    # ── Cálculo do 1º dígito verificador ──────────────────────────────────────
    # Pega os 9 primeiros dígitos do CPF
    cpf_9 = cpf_original[:9]

    # Multiplica cada dígito pelo peso de 10 a 2 e soma os resultados
    resultado = 0
    peso = 10
    for i in range(9):
        resultado += int(cpf_9[i]) * peso
        peso -= 1

    # O 1º dígito verificador é 0 se o resto for menor que 2,
    # caso contrário é 11 menos o resto
    resto = resultado % 11
    primeiro_digito = "0" if resto < 2 else str(11 - resto)
    cpf_10 = cpf_9 + primeiro_digito  # CPF com 10 dígitos (9 + 1º verificador)

    # ── Cálculo do 2º dígito verificador ──────────────────────────────────────
    # Multiplica cada um dos 10 dígitos pelo peso de 11 a 2 e soma os resultados
    resultado = 0
    peso = 11
    for i in range(10):
        resultado += int(cpf_10[i]) * peso
        peso -= 1

    # Mesma lógica: 0 se resto < 2, senão 11 - resto
    resto = resultado % 11
    segundo_digito = "0" if resto < 2 else str(11 - resto)
    cpf_completo = cpf_10 + segundo_digito  # CPF completo com 11 dígitos

    # ── Verificação final ──────────────────────────────────────────────────────
    if cpf_completo == cpf_original:
        print(f"CPF {cpf_original[:3]}.{cpf_original[3:6]}.{cpf_original[6:9]}-{cpf_original[9:]} é VÁLIDO.")
        return True
    else:
        print("CPF INVÁLIDO: os dígitos verificadores não conferem.")
        return False


# ── Execução principal ─────────────────────────────────────────────────────────
cpf_original = input("Digite seu CPF (apenas números): ")
validar_cpf(cpf_original)