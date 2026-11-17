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
        fatos = set(fatos)
        novas_conclusoes = True

        while novas_conclusoes:
            novas_conclusoes = False

            # Percorre as regras
            for regra in self.regras:
                if regra.atende(fatos):

                    # Evita adicionar conclusões repetidas
                    if regra.conclusao not in fatos:

                        fatos.add(regra.conclusao)
                        novas_conclusoes = True

                        print(f"[Nova Conclusão] {regra.conclusao}")
        return fatos


# EXEMPLO
if __name__ == "__main__":
    motor = Motor()

    # Adicionando regras
    motor.add_regra(
        Regra(
            ["cartao_recusado_varias_vezes"],
            "suspeita_de_fraude"
        )
    )

    motor.add_regra(
        Regra(
            ["suspeita_de_fraude", "valor_alto"],
            "bloquear_compra"
        )
    )

    motor.add_regra(
        Regra(
            ["suspeita_de_fraude", "compra_madrugada"],
            "solicitar_verificacao"
        )
    )

    motor.add_regra(
        Regra(
            ["endereco_entrega_diferente", "eletronico_alto_valor"],
            "risco_de_roubo_de_conta"
        )
    )


    # Fatos conhecidos (exemplo: Cliente B)
    fatos = {
        "cartao_recusado_varias_vezes",
        "valor_alto",
        "compra_madrugada"
    }


    print("=-= Veredito de Antifraude =-=")

    # Executa o motor de inferência
    resultado = motor.verificar(fatos)