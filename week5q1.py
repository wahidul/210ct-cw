b = input ("Enter sequence")

def findsequence(a):
  answer = [a[0]]
  for i in a[1:]:
    if answer[-1] + 1 is i:
      answer.append(i)
    if not len(answer) > 1:
      answer = [i]
    elif i < answer[-1] and len(answer) > 1:
      return answer
  return answer



print findsequence(b)
