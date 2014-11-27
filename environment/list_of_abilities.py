# All abilities available

from ..champion.ability import AbilityRawDamage, \
							   AbilityOverTime, \
							   AbilityHeal
# Abilities for Ahri

ahri_q = AbilityRawDamage('Orb of Deception',
				   		  cooldown=0,
				   		  damage=10)

ahri_w = AbilityOverTime('Foxfire bite',
					cooldown=3,
					turns=3,
					damage=25)

ahri_e = AbilityHeal('Charm',
					 cooldown=7,
					 health=20)

ahri_r = AbilityRawDamage('Dash',
						  cooldown=12,
						  damage=40)

# Abilities for Kata

kata_q = AbilityRawDamage('Bounding Blades',
						  cooldown=0,
						  damage=8)

kata_w = AbilityOverTime('Sinister Steel',
					cooldown=3,
					turns=2,
					damage=35)

kata_e = AbilityHeal('Shunpo',
					 cooldown=6,
					 health=15)

kata_r = AbilityRawDamage('Death Lotus',
						  cooldown=15,
						  damage=70)
