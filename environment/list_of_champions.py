# All cahmpions available

from ..champion.champion import Champion
from .list_of_abilities import *

# Normal Ahri
ahri = Champion('Ahri (Normal)',
				abilities={
							'Q': ahri_q,
							'W': ahri_w,
							'E': ahri_e,
							'R': ahri_r,
						  },
				ocean={

						'O':0.2,
						'C':1.0,
						'E':0.9,
						'A':0.5,
						'N':0.4
					  }
				)

# Illogical & Neurotic Ahri
veigar = Champion('Veigar (Illogical & Neurotic)',
				abilities={
							'Q': veigar_q,
							'W': veigar_w,
							'E': veigar_e,
							'R': veigar_r,
						  },
				ocean={

						'O':1.0,
						'C':0.1,
						'E':0.9,
						'A':0.1,
						'N':0.9
					  }
				)

# Very Logical Ahri
kassadin = Champion('Kassadin (Very Logical)',
				abilities={
							'Q': kassadin_q,
							'W': kassadin_w,
							'E': kassadin_e,
							'R': kassadin_r,
						  },
				ocean={

						'O':0.1,
						'C':1.0,
						'E':0.1,
						'A':1.0,
						'N':0.1
					  }
				)

kata = Champion('Katarina',
				abilities={
							'Q': kata_q,
							'W': kata_w,
							'E': kata_e,
							'R': kata_r,
						  },
				ocean={
						'O':0.8,
						'C':0.4,
						'E':0.6,
						'A':0.8,
						'N':0.9
					  }
				)

champions = [ahri, veigar, kassadin, kata]
