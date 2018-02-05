def isIsomorphic( s, t):
  return len(set(zip(s,t)))==len(set(s)) and len(set(zip(s,t)))==len(set(t))

s="foo"
t="egg"
d=set(s)

print isIsomorphic(s,t)