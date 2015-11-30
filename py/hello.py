import skilstak.colors as c
"""This is my hello world program."""
def print_colors(message):
    print(c.rc() + message)
def print_plain(message):
    """This is my color function"""
    print(message)
 print_forever(message):
    while True:
          print(c.rc() + message)

def parse_args:
    from sys import argv
    name = "world"
    option = ""

    if len(argv) == 2:
        if argv[1].starswitch("-"):
            option = argv[1]
        else:
            name = argv[1]
        elif len(argv) > 2:
            option = argv[1]
            name = argv[2]

            return name, option


                  
                
