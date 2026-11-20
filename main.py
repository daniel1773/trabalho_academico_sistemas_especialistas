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

                    # Evita conclusões repetidas
                    if regra.conclusao not in fatos:

                        fatos.add(regra.conclusao)
                        novas_conclusoes = True

                        print(f"[Nova Conclusão] {regra.conclusao}")

        return fatos



if __name__ == "__main__":
    motor = Motor()

    
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

    
    motor.add_regra(
        Regra(
            ["cartao_vencido"],
            "recusar_pagamento"
        )
    )

   
    motor.add_regra(
        Regra(
            ["senha_incorreta"],
            "solicitar_nova_senha"
        )
    )

    
    motor.add_regra(
        Regra(
            ["senha_incorreta_varias_vezes"],
            "bloquear_cartao"
        )
    )

    
    motor.add_regra(
        Regra(
            ["saldo_insuficiente"],
            "recusar_pagamento"
        )
    )

    
    motor.add_regra(
        Regra(
            ["compra_internacional", "valor_alto"],
            "verificar_compra"
        )
    )

    
    motor.add_regra(
        Regra(
            ["muitas_compras_seguidas"],
            "atividade_suspeita"
        )
    )

    
    motor.add_regra(
        Regra(
            ["atividade_suspeita", "valor_alto"],
            "solicitar_verificacao"
        )
    )

    
    motor.add_regra(
        Regra(
            ["cartao_roubado"],
            "bloquear_cartao"
        )
    )

    
    motor.add_regra(
        Regra(
            ["cartao_clonado"],
            "suspeita_de_fraude"
        )
    )

    
    motor.add_regra(
        Regra(
            ["cliente_novo", "valor_alto"],
            "analisar_compra"
        )
    )

    
    motor.add_regra(
        Regra(
            ["dispositivo_desconhecido"],
            "verificar_identidade"
        )
    )

    
    motor.add_regra(
        Regra(
            ["endereco_entrega_diferente", "valor_alto"],
            "solicitar_verificacao"
        )
    )

    
    motor.add_regra(
        Regra(
            ["pagamento_aprovado"],
            "confirmar_pagamento"
        )
    )

    
    motor.add_regra(
        Regra(
            ["confirmar_pagamento", "produto_disponivel"],
            "preparar_pedido"
        )
    )

    
    motor.add_regra(
        Regra(
            ["preparar_pedido", "endereco_confirmado"],
            "liberar_entrega"
        )
    )

    
    motor.add_regra(
        Regra(
            ["bloquear_compra"],
            "avisar_cliente"
        )
    )

    
    fatos = {
        "cartao_recusado_varias_vezes",
        "valor_alto",
        "compra_madrugada"
    }

    print("=-= Sistema de Varejo - Antifraude =-=")

    
    resultado = motor.verificar(fatos)
