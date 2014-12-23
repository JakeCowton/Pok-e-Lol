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
i_ahri = Champion('Ahri (Illogical & Neurotic)',
				abilities={
							'Q': ahri_q,
							'W': ahri_w,
							'E': ahri_e,
							'R': ahri_r,
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
l_ahri = Champion('Ahri (Very Logical)',
				abilities={
							'Q': ahri_q,
							'W': ahri_w,
							'E': ahri_e,
							'R': ahri_r,
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

champions = [ahri, i_ahri, l_ahri, kata]
