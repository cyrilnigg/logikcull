import pandas as pd
import sys

# import two csv files
# inner join on hash value

file_a_path = sys.argv[1]
file_b_path = sys.argv[2]
output_file_path = sys.argv[3]

search_limit = 40000

df_a = pd.read_csv(file_a_path, header=0, names=['id_a','hash'])
df_b = pd.read_csv(file_b_path, header=0, names=['id_b','hash'])

print "The initial file contains ", len(df_a), " documents"
print "The secondary file contains ", len(df_b), " documents"

# inner join on hash values
dup_df = pd.merge(left=df_a, right=df_b, on='hash')

# create frame containing ids from file_b that were dupes based on the hash
dup_ids = dup_df.id_b.drop_duplicates()

# open a text file to write to

output_file = open(output_file_path, "w")

#print search_string
count = 0
search_string = ''
check_string = ''
for i in dup_ids:
	file_string = 'file_id:' + i
	check_string += file_string + ' OR '
	count += 1
	#print len(search_string), len(check_string)
	if len(check_string) < search_limit:
		search_string += file_string + ' OR '
	else:
		#print search_string[:-4]
		output_file.write(search_string[:-4])
		output_file.write('\n')
		output_file.write('---------------NEW SEARCH--------------------')
		output_file.write('\n')
		print len(search_string)
		print len(check_string)
		print count, " Total documents in this search"
		raw_input('Press Enter')
		search_string = file_string
		check_string = file_string


#print search_string[:-4]
output_file.write(search_string[:-4])
print len(search_string)
print count, " Total documents in this search"
output_file.close()

