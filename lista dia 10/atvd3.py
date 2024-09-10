idade  = int(input("informe uma idade: "))

if idade < 12:
    print("A pessoa é criança.")
elif 12 <= idade < 18:
    print("A pessoa adolescente.")
elif 18 <= idade < 60:
    print("A pessoa é adulto.")
else:
    print("A pessoa é idosa.")
