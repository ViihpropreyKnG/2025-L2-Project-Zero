# Functions go here
def make_statement(statement, decoration, lines=1):
   """Emphasises headings by adding decoration at the start and end"""

   middle = f"{decoration * 3} {statement} {decoration *3}"
   top_bottom = decoration * len(middle)

   if lines == 1:
      print(middle)
   elif  lines == 2:
      print(middle)
      print(top_bottom)

   else:
      print(top_bottom)
      print(middle)
      print(top_bottom)

make_statement(statement= "Viihproprey", decoration= "👑", lines= 3)
make_statement(statement= "Is The King", decoration= "😎", lines= 2)
make_statement(statement= "Of Whatsapp!", decoration= "!")

