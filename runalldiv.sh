#! /bin/bash

grep -F -f AD.txt 2022.csv > temp.csv
python adhisto.py temp.csv > AD.out

grep -F -f PPD.txt 2022.csv > temp.csv
python adhisto.py temp.csv > PPD.out

grep -F -f MICRO.txt 2022.csv > temp.csv
python adhisto.py temp.csv > MICRO.out

grep -F -f ND.txt 2022.csv > temp.csv
python adhisto.py temp.csv > ND.out

grep -F -f RTPS.txt 2022.csv > temp.csv
python adhisto.py temp.csv > RTPS.out

grep -F -f DIR.txt 2022.csv > temp.csv
python adhisto.py temp.csv > DIR.out

grep -F -f ESH.txt 2022.csv > temp.csv
python adhisto.py temp.csv > ESH.out

grep -F -f MAGNET.txt 2022.csv > temp.csv
python adhisto.py temp.csv > MAGNET.out

grep -F -f BEAMS.txt 2022.csv > temp.csv
python adhisto.py temp.csv > BEAMS.out

grep -F -f SQMS.txt 2022.csv > temp.csv
python adhisto.py temp.csv > SQMS.out

grep -F -f SRF.txt 2022.csv > temp.csv
python adhisto.py temp.csv > SRF.out

grep -F -f CRYO.txt 2022.csv > temp.csv
python adhisto.py temp.csv > CRYO.out

python adhisto.py 2022.csv > ALL.out

rm temp.csv
