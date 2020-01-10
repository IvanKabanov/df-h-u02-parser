import csv

path='path/to/file'


f = open(path,"r")
lines = f.readlines()
result = {}
for x in lines:
	if x.startswith('migr-'):
		hostname = x.split('.', 1)[0]
		lastaddedhost = hostname
	else:
		u02_used = x.split()[2]
		measure = u02_used[-1]
		value = u02_used[:-1]
		if measure == 'G':
			result[lastaddedhost] = round(result.get(lastaddedhost, 0) + float(value))
		elif measure == 'T':
			result[lastaddedhost] = round(result.get(lastaddedhost, 0) + float(value)*1024)
		elif measure == 'M':
			result[lastaddedhost] = round(result.get(lastaddedhost, 0) + float(value)/1024)
		else:
			break

with open('output3.csv', 'w') as output:
    writer = csv.writer(output)
    for key, value in result.items():
        writer.writerow([key, value])

print(result)
