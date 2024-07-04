import pandas as pd
from spremenljivke import *

pd.set_option("display.max_rows", 10)
%matplotlib inline

pot = os.path.join(mapa, slovar)
slovar = pd.read_csv(pot)

