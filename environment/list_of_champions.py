# All cahmpions available

from ..champion.champion import Champion
from list_of_abilities import *

ahri = Champion('Ahri',
				abilities={
							'Q': ahri_q,
							'W': ahri_w,
							'E': ahri_e,
							'R': ahri_r,
						  },
				ocean={

						'O':0,
						'C':0,
						'E':0,
						'A':0,
						'N':0
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

						'O':0,
						'C':0,
						'E':0,
						'A':0,
						'N':0
					  }
				)

champions = [ahri, kata]
