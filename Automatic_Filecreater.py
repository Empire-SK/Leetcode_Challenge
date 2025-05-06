def fixer(text):

    text = text.replace('.', '')            

    text = '_'.join(text.split())           

    filename = text + '.py'               

    

    with open(filename, 'w') as f:   

        f.write("")      


    print(f"{filename} created successfully!")


fixer("3000. Maximum Area of Longest Diagonal Rectangle")