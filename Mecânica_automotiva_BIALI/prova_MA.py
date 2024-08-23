def menu_diagnostico():
    print("\nBem-vindo ao Diagnóstico Automotivo Express!")
    print("\nSelecione o tipo de problema que você está enfrentando:")
    print("1. Problemas no Motor")
    print("2. Problemas com os Freios")
    print("3. Problemas na Suspensão")
    print("4. Problemas Elétricos")
    print("5. Sair")

def diagnostico_motor(sintoma):
    sintomas_motor = {
        "não dá partida": "Possível problema no sistema de ignição ou combustível. Verifique as velas de ignição, bobina, e o sistema de combustível.",
        "falhas de ignição": "Possível problema no sistema de ignição. Verifique as velas de ignição, bobina e cabos.",
        "desempenho irregular": "Possível problema no sistema de combustível ou ignição. Verifique o filtro de combustível e as velas.",
        "motor aquecendo": "Possível problema no sistema de resfriamento. Verifique o nível de líquido de arrefecimento e a bomba d'água.",
        "barulho metálico": "Possível problema nas válvulas ou tuchos. Verifique o nível de óleo e a necessidade de ajuste nas válvulas.",
        "vibração em marcha lenta": "Possível problema nos coxins do motor ou na mistura de combustível. Verifique os coxins e o sistema de injeção.",
        "fumaça branca": "Possível vazamento de líquido de arrefecimento na câmara de combustão. Verifique a junta do cabeçote.",
        "fumaça preta": "Mistura rica de combustível. Verifique os injetores e o sensor de oxigênio.",
    }
    return sintomas_motor.get(sintoma, "Sintoma específico não reconhecido. Leve o veículo a um mecânico para uma análise mais detalhada.")

def diagnostico_freios(sintoma):
    sintomas_freios = {
        "barulho ao frear": "Possível desgaste das pastilhas de freio ou discos. Verifique as pastilhas de freio, discos e o fluido de freio.",
        "freios duros": "Possível problema no servo-freio ou fluido de freio baixo. Verifique o servo-freio e o fluido de freio.",
        "vibração ao frear": "Possível problema nos discos de freio. Verifique os discos de freio e as pastilhas.",
        "pedal de freio baixo": "Possível vazamento de fluido de freio ou bolhas de ar no sistema. Verifique o nível de fluido e o sistema de sangria.",
        "luz do freio acesa": "Possível problema no sensor de fluido de freio ou desgaste das pastilhas. Verifique o nível de fluido e as pastilhas.",
        "freios agarrando": "Possível problema com os cilindros de freio ou pinças. Verifique e limpe os componentes dos freios.",
        "ruído de metal": "Pastilhas de freio desgastadas completamente. Verifique as pastilhas imediatamente para evitar danos aos discos.",
    }
    return sintomas_freios.get(sintoma, "Sintoma específico não reconhecido. Leve o veículo a um mecânico para uma análise mais detalhada.")

def diagnostico_suspensao(sintoma):
    sintomas_suspensao = {
        "ruídos ao passar por buracos": "Possível problema nos amortecedores ou barra estabilizadora. Verifique os amortecedores, molas e barra estabilizadora.",
        "instabilidade na direção": "Possível problema nos amortecedores ou na geometria da suspensão. Verifique os amortecedores e a barra estabilizadora.",
        "veículo puxa para um lado": "Possível desalinhamento ou problema nos pneus. Verifique o alinhamento e a calibragem dos pneus.",
        "batidas secas": "Possível desgaste nas buchas ou nas juntas homocinéticas. Verifique as buchas, bieletas e as juntas.",
        "direção dura": "Possível problema na caixa de direção ou baixo nível de fluido hidráulico. Verifique a caixa de direção e o fluido.",
        "veículo rebaixado de um lado": "Possível problema nas molas ou nos amortecedores. Verifique o estado das molas e amortecedores.",
        "vibração excessiva": "Possível problema nos pneus, rodas ou coxins. Verifique o balanceamento e o estado dos pneus.",
    }
    return sintomas_suspensao.get(sintoma, "Sintoma específico não reconhecido. Leve o veículo a um mecânico para uma análise mais detalhada.")

def diagnostico_eletrico(sintoma):
    sintomas_eletricos = {
        "faróis não acendem": "Possível problema nos fusíveis ou na bateria. Verifique os fusíveis, fiação e bateria.",
        "painel falhando": "Possível problema no alternador ou fusíveis. Verifique os fusíveis e o alternador.",
        "bateria descarregando rapidamente": "Possível problema no alternador ou fuga de corrente. Verifique o alternador e possíveis curtos-circuitos.",
        "luz de bateria acesa": "Possível problema no alternador ou correia do alternador. Verifique o alternador e a tensão da correia.",
        "interruptores não funcionam": "Possível problema nos relés ou fiação. Verifique os relés e a fiação correspondente.",
        "som do carro não funciona": "Possível problema nos fusíveis, fiação ou na unidade de som. Verifique os fusíveis e conexões da unidade.",
        "sistema de ar-condicionado falhando": "Possível problema no compressor ou nos circuitos elétricos. Verifique o compressor, fusíveis e relés.",
        
    }
    return sintomas_eletricos.get(sintoma, "Sintoma específico não reconhecido. Leve o veículo a um mecânico para uma análise mais detalhada.")

def diagnosticar_problema():
    while True:
        menu_diagnostico()
        opcao = input("\nDigite o número da opção desejada: ")
        
        if opcao == "1":
            print("\nProblemas no Motor selecionado.")
            sintoma = input("Por favor, descreva o sintoma específico do motor: ").lower()
            resultado = diagnostico_motor(sintoma)
            print("\nDiagnóstico:", resultado)
        
        elif opcao == "2":
            print("\nProblemas com os Freios selecionado.")
            sintoma = input("Por favor, descreva o sintoma específico dos freios: ").lower()
            resultado = diagnostico_freios(sintoma)
            print("\nDiagnóstico:", resultado)
        
        elif opcao == "3":
            print("\nProblemas na Suspensão selecionado.")
            sintoma = input("Por favor, descreva o sintoma específico da suspensão: ").lower()
            resultado = diagnostico_suspensao(sintoma)
            print("\nDiagnóstico:", resultado)
        
        elif opcao == "4":
            print("\nProblemas Elétricos selecionado.")
            sintoma = input("Por favor, descreva o sintoma específico do sistema elétrico: ").lower()
            resultado = diagnostico_eletrico(sintoma)
            print("\nDiagnóstico:", resultado)
        
        elif opcao == "5":
            print("\nSaindo do Diagnóstico Automotivo Express. Obrigado por usar nossos serviços!")
            break
        
        else:
            print("\nOpção inválida. Por favor, selecione uma opção válida do menu.")

# Executar o diagnóstico
diagnosticar_problema()