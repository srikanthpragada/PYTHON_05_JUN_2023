
def unique_chars(*names):
   chars = set()
   for n in names:
       chars = chars | set(n)

   return "".join(sorted(chars))


print( unique_chars("java", "c#", 'Python', 'javascript', 'c'))



