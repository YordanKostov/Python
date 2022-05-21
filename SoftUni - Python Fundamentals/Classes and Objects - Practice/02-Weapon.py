class Weapon:
    def __init__(self, bullets):
        self.bullets = int(bullets)

    def shoot(self):
        if self.bullets > 0:
            print('shooting...')
            self.bullets -= 1
        else:
            print('no bullets left')

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"


weapon = Weapon(5)
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
print(weapon)
