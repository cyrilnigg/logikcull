Take two CSV files from Logikcull, dedupe them and create a search string which can be used to quickly cull documents.
<br>
To run:
<br>
python dedupe.py inputfile_1.csv inputfile_2.csv output.txt
<br>
output.txt returns search syntax with up to 40k characters for file_ids in inputfile_2.csv that are duplicates in inputfile_1.csv