import os
from pathlib import Path

DIR = Path(__file__).parent

DIR_OUTPUT = os.path.normpath( os.path.join(DIR, "../outputs/") )
DIR_TEMP   = os.path.normpath( os.path.join(DIR, "../tmp/json/") )

DIR_FONT = os.path.normpath( os.path.join(DIR, "../res/fonts") )

DIR_PHONICS = os.path.normpath( os.path.join(DIR, "../res/phonics/") )