
# this dictioary contain the data to construct out tree_view
dict = {"main":[], "home":["branch 1", "branch 2", "branch 3"], "work":["branch 1", "branch 2", "branch 3", "branch 4"], "contact":["branch 1", "branch 2", "branch 3", "branch 4", "branch 5"]}




##### the core #####
for i in dict:
	escape = False
	if i == list(dict.keys())[-1]:
		print("└──",i ,end="\n")
		escape = True
	if not escape:
		print("├──",i ,end="\n")
	for j in dict[i]:
		if i == list(dict.keys())[-1]:
			if j == dict[i][-1]:
				print("    └──", j, end="\n")
				continue
			print("    ├──", j, end="\n")
			continue
		if j == dict[i][-1]:
			print("│   └──", j, end="\n")
			continue
		print("│   ├──", j, end="\n")