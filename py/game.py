import tkinter as tk

class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

    def attack_opponent(self, opponent):
        damage = max(0, self.attack - opponent.defense)
        opponent.take_damage(damage)
        return damage


def attack_clicked():
    global player, enemy, player_health_label, enemy_health_label
    if player.is_alive() and enemy.is_alive():
        player_damage = player.attack_opponent(enemy)
        update_ui()
        enemy_damage = enemy.attack_opponent(player)
        update_ui()
        message_text.insert(tk.END, f"You attacked {enemy.name} for {player_damage} damage!\n")
        message_text.insert(tk.END, f"{enemy.name} counter-attacked for {enemy_damage} damage!\n")
        message_text.see(tk.END)  # Scroll to the end of the message

def update_ui():
    global player, enemy, player_health_label, enemy_health_label
    player_health_label.config(text=f"{player.name} Health: {player.health}")
    enemy_health_label.config(text=f"{enemy.name} Health: {enemy.health}")

def main():
    global player, enemy, player_health_label, enemy_health_label, message_text
    player = Character("Player", 100, 10, 5)
    enemy = Character("Enemy", 100, 8, 4)

    window = tk.Tk()
    window.title("Fighting Game")

    player_health_label = tk.Label(window, text=f"{player.name} Health: {player.health}")
    enemy_health_label = tk.Label(window, text=f"{enemy.name} Health: {enemy.health}")
    attack_button = tk.Button(window, text="Attack", command=attack_clicked)

    player_health_label.pack()
    enemy_health_label.pack()
    attack_button.pack()

    # Text widget to display messages
    message_text = tk.Text(window, height=10, width=40)
    message_text.pack()

    window.mainloop()

if __name__ == "__main__":
    main()
