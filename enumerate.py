# help (enumerate)
software = ["Search", "Download", "Install", "Run"]
for i in range(len(software)):
    step = software [i]
    print (f"{i+1}. {step}")

print (list(enumerate(software)))
for i, step in enumerate (software):
    print (f"{i+1}. {step}")
    