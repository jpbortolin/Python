from cgi import print_arguments

codigo = 0

codigo = int(input("Digite o código da origem do produto"))

if codigo == 1:
    print("Sul")

if codigo == 5 or codigo == 6:
    print("Nordeste")

if codigo == 7 or codigo == 8 or codigo == 9:
    print("Sudeste")

if codigo >= 10 and codigo <= 20:
    print("Centro Oeste")