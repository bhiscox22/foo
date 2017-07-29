# Code to fix
# 
# A python script with a little bug

expenses = {
"Food": "100",
"Rent": "1100",
"Taxes": "500"}

print "Monthly expenses:"
for ex in expenses:
	print "\t" + ex + ':\t$' + expenses[ex]

print "\nTotal expenses, excluding tax:"
total = expenses["Food"] + expenses["Rent"]
print '$' + total 

