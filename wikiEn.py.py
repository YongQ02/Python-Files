import wikipedia
function_directory = ['module', 'modules', 'index', 'help', 'helps']
closeProgram = ['close','exit','quit']
run = True

def RunProgram():
    index = input("Enter the topic you want to search: ")
    print('')
    print('')
    if index in function_directory:
        print("Go this website to explore more about python wikipedia function:\nhttps://wikipedia.readthedocs.io/en/latest/quickstart.html or https://wikipedia.readthedocs.io/en/latest/")
    else:
        try:
            content = wikipedia.summary(index)
            print(content)
        except wikipedia.exceptions.PageError:
            print(index + " does not match any pages. Try another query!")
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)       
    print('')
    print('')
    print('')

while run == True:
    RunProgram()