# Interfaz para el comportamiento de ataque
class IAttackBehaviour():
    def attack(self,character):
        pass

# Comportamiento de ataque con espadas
class AttackSword(IAttackBehaviour):
    def attack(self,character):
        print(f'{character} ataca con una espada!') 

# Comportamiento de ataque con arco y flechas
class AttackBowAndArrows(IAttackBehaviour):
    def attack(self,character):
        print(f'{character} dispara con su arco y flechas!') 

# Comportamiento de ataque con puños
class AttackFist(IAttackBehaviour):
    def attack(self,character):
        print(f'{character} ataca con sus puños!') 

# Comportamiento de ataque con pistolas
class AttackGun(IAttackBehaviour):
    def attack(self,character):
        print(f'{character} dispara con su pistola!')  

# Comportamiento de ataque con hechizos magicos
class AttackMagic(IAttackBehaviour):
    def attack(self,character):
        print(f'{character} ataca con magia!')

# Interfaz para el comportamiento de movimiento
class IMovementBehaviour():
    def move(self,character):
        pass

# Comportamiento de no moverse
class MovementStandingStill(IMovementBehaviour):
    def move(self,character):
        print(f'{character} esta de pie y quieto.') 

# Comportamiento de moverse corriendo
class MovementRun(IMovementBehaviour):
    def move(self,character):
        print(f'{character} esta corriendo.') 

# Comportamiento de moverse a caballo
class MovementHorse(IMovementBehaviour):
    def move(self,character):
        print(f'{character} se mueve a caballo.') 

# Comportamiento de moverse con teletransportación
class MovementTeleport(IMovementBehaviour):
    def move(self,character):
        print(f'{character} se esta teletransportando.') 

# Clase base de un personaje
class Character:
    def __init__(self, chara_type, attack_behavior: IAttackBehaviour, move_behavior: IMovementBehaviour):
        self.chara_type = chara_type
        self.attack_behavior = attack_behavior
        self.move_behavior = move_behavior
    
    def perform_attack(self):
        self.attack_behavior.attack(self.chara_type)

    def start_movement(self):
        self.move_behavior.move(self.chara_type)

    def check_class(self):
        print(f'CLASE: {self.chara_type}')
    
# Clase concreta de un soldado
class Soldier(Character):
    def __init__(self):
        super().__init__("Soldado", AttackGun(), MovementRun())

# Clase concreta de un arquero
class Archer(Character):
    def __init__(self):
        super().__init__("Arquero", AttackBowAndArrows(), MovementStandingStill())

# Clase concreta de un caballero
class Knight(Character):
    def __init__(self):
        super().__init__("Caballero", AttackSword(), MovementHorse())

# Clase concreta de un peleador
class Fighter(Character):
    def __init__(self):
        super().__init__("Peleador", AttackFist(), MovementRun())

# Clase concreta de un mago
class Mage(Character):
    def __init__(self):
        super().__init__("Mago", AttackMagic(), MovementTeleport())
        
# Ejemplo de uso de todas las clases:
if __name__ == "__main__":

    soldado = Soldier()
    soldado.check_class()
    soldado.perform_attack()
    soldado.start_movement()
    print("\n")

    arquero = Archer()
    arquero.check_class()
    arquero.perform_attack()
    arquero.start_movement()
    print("\n")

    caballero = Knight()
    caballero.check_class()
    caballero.perform_attack()
    caballero.start_movement()
    print("\n")

    peleador = Fighter()
    peleador.check_class()
    peleador.perform_attack()
    peleador.start_movement()
    print("\n")

    mago = Mage()
    mago.check_class()
    mago.perform_attack()
    mago.start_movement()
    print("\n")