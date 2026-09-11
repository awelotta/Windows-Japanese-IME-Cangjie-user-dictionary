from os import path
import pandas as pd


cangjie_file = r"C:\Users\awelo\Desktop\Cangjie stuff\jackchowscangjie5\Cangjie5\Cangjie5.txt"

cangjie_df = pd.read_csv(
    cangjie_file,
    delimiter='\t', 
    header= [i for i in range(0,12)],
    names=['char', 'code', 'note'],
    )

#example entry of cangjie_df
#𰷙	aashc	[u]
#example entry of target
#あｃ	𮲤	短縮よみ

pd.DataFrame(cangjie_df['code'], cangjie_df['char'])

明