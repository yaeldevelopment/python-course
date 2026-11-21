labels = [1, 0, 1, 1, 0, 1, 0, 0]
preds = [1, 0, 0, 1, 0, 1, 1, 0]
numsuccse=0
fp=0
fn=0
i=0
while i<len(labels):
    if labels[i]==preds[i]:
        numsuccse+=1
    else:
        if preds[i]==1:
           fp+=1
        else:
          fn+=1
    i+=1
print("numsuccse:",numsuccse/len(labels))
print("fp:",fp)
print("fn:",fn)
    