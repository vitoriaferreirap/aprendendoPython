#E python NAO é necessario declarar o tipo de variavel ecplicitamente.
idade = 25;
print(idade);

idade = 30;
print(idade);
print(type(idade)); #descobre tipo

idade = 10.5;
print(idade);
print(type(idade)); #descobre tipo

idade = "s";
print(idade);
print(type(idade)); #descobre tipo

#Tipagem estatica opcional
idade: int = 70;
print(idade);
idade = 10.5; #vai funcionar mas com umm (aviso se usar mypy)
print(idade);
