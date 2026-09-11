import pandas as pd
import re

# kanatization
# step 0: augment kana table with sokuon'd kanas
# step 0.5 augment n to kana (if we do longest first, then we should be able to replace all n)
# step 1: look up from kana table
# step 3: hope that's enough

kana_table = pd.read_csv(
    "./windows-kana-table.tsv",
    delimiter='\t', 
    # header= [i for i in range(0,12)],
    names=['rom', 'kana'],
    )
kanatize_dict = dict(zip(kana_table['rom'], kana_table['kana']))
sokuon_dict = {(rom[0] + rom): ('っ' + kana) for (rom, kana) in kanatize_dict.items() if rom[0] not in "aeioun"}
kanatize_dict |= sokuon_dict
kanatize_dict |= {'n' : 'ん'}

def kanatize(code: str) -> str:
	pattern = re.compile("|".join( 		# join all the patterns
		re.escape(rom) for rom in sorted( # escape (because some roms have -[])
			kanatize_dict.keys(), key=len, reverse=True))) # sort descneding to prioritize long
	return pattern.sub(lambda rom: kanatize_dict[rom.group(0)], code)


with open("./output.txt", 'w+', encoding="utf-16-le") as output_file:
	output_file.write("\ufeff")
	part_of_speech = "短縮よみ"
	with open("./Cangjie5.txt", 'r', encoding="utf-8") as cangjie_file:
		for line in cangjie_file.readlines():
			fields = line.split()
			char = fields[0]
			code = fields[1]

			reading = kanatize(code)
			output_file.write(reading + "\t" + char + "\t" + part_of_speech + "\n")