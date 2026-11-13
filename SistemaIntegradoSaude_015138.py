
unidades = []
pacientes = []
proximo_numero = 1

opcao = ""

while opcao != "0":
    print("\n===== SISTEMA INTEGRADO DE SAÚDE - UÍGE =====")
    print("1 - Registar unidade de saúde")
    print("2 - Registar paciente")
    print("3 - Adicionar consulta ao histórico")
    print("4 - Consultar histórico de um paciente")
    print("5 - Listar unidades de saúde")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome da unidade: ")
        municipio = input("Município: ")
        servicos = input("Serviços disponíveis (separe por vírgula): ")
        unidade = {"nome": nome, "municipio": municipio, "servicos": servicos}
        unidades.append(unidade)
        print("Unidade registada com sucesso!")

    elif opcao == "2":
        nome = input("Nome do paciente: ")
        nascimento = input("Data de nascimento (dd/mm/aaaa): ")
        paciente = {
            "numero": proximo_numero,
            "nome": nome,
            "nascimento": nascimento,
            "historico": []   # lista de consultas
        }
        pacientes.append(paciente)
        print("Paciente registado! Número único:", proximo_numero)
        proximo_numero = proximo_numero + 1

    elif opcao == "3":
        numero = int(input("Número do paciente: "))
        encontrado = False
        for p in pacientes:
            if p["numero"] == numero:
                encontrado = True
                data = input("Data da consulta: ")
                unidade = input("Unidade de saúde: ")
                diagnostico = input("Diagnóstico: ")
                tratamento = input("Tratamento: ")
                consulta = {
                    "data": data,
                    "unidade": unidade,
                    "diagnostico": diagnostico,
                    "tratamento": tratamento
                }
                p["historico"].append(consulta)
                print("Consulta adicionada ao histórico!")
        if encontrado == False:
            print("Paciente não encontrado.")

    elif opcao == "4":
        numero = int(input("Número do paciente: "))
        encontrado = False
        for p in pacientes:
            if p["numero"] == numero:
                encontrado = True
                print("\nPaciente:", p["nome"])
                print("Nascimento:", p["nascimento"])
                if len(p["historico"]) == 0:
                    print("Sem consultas registadas.")
                else:
                    print("--- Histórico clínico ---")
                    for c in p["historico"]:
                        print("Data:", c["data"])
                        print("Unidade:", c["unidade"])
                        print("Diagnóstico:", c["diagnostico"])
                        print("Tratamento:", c["tratamento"])
                        print("-----------------------")
        if encontrado == False:
            print("Paciente não encontrado.")

    elif opcao == "5":
        if len(unidades) == 0:
            print("Nenhuma unidade registada.")
        else:
            for u in unidades:
                print("Unidade:", u["nome"], "| Município:", u["municipio"], "| Serviços:", u["servicos"])

    elif opcao == "0":
        print("A sair do sistema...")

    else:
        print("Opção inválida!")
