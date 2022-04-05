#yesma chai k hunxa bhanda sea level bhanda mathi gayera feri sea level ma aauda mountain hunxa ra sea level bata tala gayera feri sea level ma aauda chai valley hunxa
#hamile le chai yo problem ma valley matra count garne

def countingValleys(steps, path):
    path=list(path)
    seaLevel=0
    valley=0
    for i in range(steps):
        if path[i]=="U":
            seaLevel+=1
        else:
            seaLevel-=1
        if seaLevel==0 and path[i]=="U":
            valley+=1
    
    print( valley)

steps=8
path="UDDDUDUU"
countingValleys(steps,path)