# Convite Especial

class EncontroRomantico:
    def __init__(self, convidada, anfitriao):
        self.convidada = convidada
        self.anfitriao = anfitriao
        self.hora = "21:00"
        self.local = "Surpresa"

    def preparar_encontro(self):
        print(f"Querida {self.convidada},")
        print("\nTenho uma surpresa preparada para você...")
        print(f"A nossa noite começa às {self.hora}.")
        print("O local será revelado no momento certo!")
        print("\nTudo o que peço é que se prepare para um encontro único e inesquecível.")
        print(f"\nNos vemos logo, na hora e no local certo.\n")
        print(f"Com carinho, {self.anfitriao} ✨")


# Definindo os detalhes do encontro
convidada = "Lohana"
anfitriao = "Miguel"

# Criando e preparando o encontro
encontro = EncontroRomantico(convidada, anfitriao)
encontro.preparar_encontro()
