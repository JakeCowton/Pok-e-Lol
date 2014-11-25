# All abilities available

from ..champion.ability import Ability_Q, Ability_W_Damage, \
							   Ability_E_Heal, Ability_R_Attack
# Abilities for Ahri

ahri_q = Ability_Q('Orb of Deception',
				   cooldown=1,
				   damage=10)

ahri_w = Ability_W_Damage('Foxfire bite',
						  cooldown=3,
						  turns=3,
						  damage=25)

ahri_e = Ability_E_Heal('Charm',
						cooldown=7,
						health=20)

ahri_r = Ability_R_Attack('Dash',
						  cooldown=12,
						  damage=40)

# Abilities for Kata

kata_q = Ability_Q('Bounding Blades',
					cooldown=1,
					damage=8)

kata_w = Ability_W_Damage('Sinister Steel',
						  cooldown=3,
						  turns=2
						  damage=35)

kata_e = Ability_E_Heal('Shunpo',
						cooldown=6,
						health=15)

kata_r = Ability_R_Attack('Death Lotus',
						  cooldown=15,
						  damage=70)