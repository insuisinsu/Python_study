# 08_classes/practice.py
# 클래스 (Classes) 학습

# 1. 클래스와 객체 생성
# Unit 클래스 생성
class Unit:
    def __init__(self, name, hp, damage): # 생성자
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{self.name} 유닛이 생성되었습니다.")
        print(f"체력 {self.hp}, 공격력 {self.damage}")

# 객체 생성 (인스턴스화)
marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# 멤버 변수 접근
print(f"유닛 이름: {tank.name}, 공격력: {tank.damage}")

# 레이스: 공중 유닛, 클로킹 가능
wraith1 = Unit("레이스", 80, 5)
# 객체에 외부에서 변수를 직접 추가할 수 있음 (파이썬 특징)
wraith1.clocking = True

if wraith1.clocking == True:
    print(f"{wraith1.name}은 현재 클로킹 상태입니다.")

# 2. 메서드(Method)와 상속(Inheritance)
# 공격 유닛 (Unit을 상속)
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp, damage) # 부모 클래스 생성자 호출

    def attack(self, location): # 메서드
        print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}]")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")

# 파이어뱃 객체 생성
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 데미지 두 번 입음
firebat1.damaged(25)
firebat1.damaged(30)
