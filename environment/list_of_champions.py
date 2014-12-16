# All cahmpions available

from ..champion.champion import Champion
from .list_of_abilities import *

ahri = Champion('Ahri',
				abilities={
							'Q': ahri_q,
							'W': ahri_w,
							'E': ahri_e,
							'R': ahri_r,
						  },
				ocean={

						'O':1.0,
						'C':0.3,
						'E':0.9,
						'A':0.5,
						'N':0.4
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

champions = [ahri, kata]
