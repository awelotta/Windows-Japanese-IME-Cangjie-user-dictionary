To use: Download `output.txt`. From the Microsoft IME User Dictionary Tool, click Tool > Import from Text File. Then select `output.txt` where it is.

`windows-kana-table.tsv` contains romaji conversion table from the registry.

`kanatize.py` is the code. I used Gemini a lot yay! Basically, the Readings in the User Dictionary have to be the intermediate kana and can't be just romaji,
so my code just takes the Cangjie5 code and applies windows kana conversion rules while handling sokuon and ん.

This creates some more code conflicts since for example nn and n both map to ん, or tu and tsu both map to つ.

Cangjie5 codes sourced from https://github.com/Jackchows/Cangjie5 (mine might be out of date).
