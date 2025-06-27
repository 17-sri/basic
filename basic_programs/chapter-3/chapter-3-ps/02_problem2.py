#write a program to fill in a letter template given below with 'name' and 'date'
letter = '''Dear <|Name|>,
            you are selected!
            <|Date|>'''
print(letter.replace("<|Name|>","Srikanth").replace("<|Date|>","June 16 2025"))
# str.replace().replace()  function chaining