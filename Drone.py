class Drone:
    def __init__(self, motores, cameras, ano_construcao, nome, altitude):
        self.motores = motores
        self.cameras = cameras
        self.ano_construcao = ano_construcao
        self.nome = nome
        self.altitude = altitude

    def dados(self):
        return (f"Nome do Drone: {self.nome}\n"
                f"Número de Motores: {self.motores}\n"
                f"Quantidade de Câmeras: {self.cameras}\n"
                f"Ano de Construção: {self.ano_construcao}\n"
                f"Altitude Máxima: {self.altitude} metros\n") #Atributo de livre escolha

class FrotaDrones:
    def __init__(self):
        self.drones = []

    def adicionar(self, drone):
        self.drones.append(drone)

    def exibir(self):
        print("-//Lista de Drones//-")
        for idx, drone in enumerate(self.drones, start=1):
            print(f"Drone {idx}:")
            print(drone.dados())
            print()

    def individual(self, indice):
        if 1 <= indice <= len(self.drones):
            print("Dados individuais do drone:")
            print(self.drones[indice - 1].dados())
        else:
            print("Índice inválido.")

    def rankear_drones_por_ano_construcao(self):
        ranked_drones = sorted(self.drones, key=lambda x: x.ano_construcao, reverse=True)
        print("-//Ranking de Drones por Ano de Construção//-")
        for idx, drone in enumerate(ranked_drones, start=1):
            print(f"{idx}. Nome do Drone: {drone.nome}, Ano de Construção: {drone.ano_construcao}")
        print()

    def rankear_drones_por_altitude(self):
        ranked_drones = sorted(self.drones, key=lambda x: x.altitude, reverse=True)
        print("-//Ranking de Drones por Altitude Máxima//-")
        for idx, drone in enumerate(ranked_drones, start=1):
            print(f"{idx}. Nome do Drone: {drone.nome}, Altitude Máxima: {drone.altitude} metros")
        print()

if __name__ == "__main__":
    frota = FrotaDrones()

    drone1 = Drone(5, 6, 2024, "Caipora", 690)
    drone2 = Drone(2, 1, 2019, "Boitatá", 340)
    drone3 = Drone(4, 3, 2021, "Curupira", 267)

    frota.adicionar(drone1)
    frota.adicionar(drone2)
    frota.adicionar(drone3)

    frota.rankear_drones_por_ano_construcao()

    frota.rankear_drones_por_altitude() #Escolhi como método de livre escolha

    frota.individual(1) 

    frota.individual(2) 
    
    frota.individual(3) 
