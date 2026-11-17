class Regra:
    def __init__(self, condicoes, conclusao):
        self.condicoes = set(condicoes)
        self.conclusao = conclusao
    
    def atende(self, fatos):
        return self.condicoes.issubset(fatos)


class Motor:
    def __init__(self):
        self.regras = []
    
    def add_regra(self, regra):
        self.regras.append(regra)
    
    def verificar(self, fatos):
        resultados = [regra.conclusao for regra in self.regras if regra.atende(fatos)]
        
        if resultados:
            print("=-= Veredito de Antifraude =-=")
            for res in resultados:
                print(f"=> {res}")
        else:
            print("=-= Sem alerta de fraudes =-=")


# Iniciando Programa
if __name__ == "__main__":
    motor = Motor()

    # Adicionando regras
    motor.add_regra(
        Regra(["cartao_recusado_varias_vezes", "valor_alto"], 
              "BLOQUEADO: Suspeita de teste de cartão (Carding).")
    )
    motor.add_regra(
        Regra(["endereco_entrega_diferente", "compra_madrugada", "eletronico_alto_valor"], 
              "ANÁLISE MANUAL: Alto risco de roubo de conta.")
    )

    # Testando cenários
    motor.verificar({"endereco_entrega_diferente", "compra_madrugada", "eletronico_alto_valor"})
    motor.verificar({"cartao_recusado_varias_vezes", "valor_alto"})