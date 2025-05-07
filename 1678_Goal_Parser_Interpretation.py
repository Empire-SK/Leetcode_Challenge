class Solution(object):
    def interpret(self, command):
     result = ""
     i = 0
    
     while i < len(command):
         if command[i] == 'G':
             result += 'G'
             i += 1
         elif command.startswith("()", i):
             result += 'o'
             i += 2
         elif command.startswith("(al)", i):
             result += 'al'
             i += 4
         else:
             i += 1  # Skip unrecognized characters (shouldn't happen per problem constraints)
    
     return result