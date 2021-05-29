def maxindex(steps,badindex):
  i=0
  j=1
  tempstep=steps
  while(steps>0):
    if i+j!=badindex:
      i+=j
    j+=1
  scenario1=i
  i=0
  j=2
  tempstep-=1
  while(tempstep>0):
    if i+j!=badindex:
      i+=j
    j+=1
  scenario2=i
  return scenario1 if scenario1>scenario2 else scenario2
'''
sample input:
2
2
o/p:3
0+1=1
1+2=3
sample input2:
3
3
scenario1:
1)0+1=1
2)1+2=3 so it ramains 1
3)1+3=4
scenario2:
1)0 remains itself
2)0+2=2
3)2+3=5
output:5'''
