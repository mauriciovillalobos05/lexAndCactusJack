# Compilación
parser: parser.tab.c lex.yy.c
	gcc -o parser lex.yy.c parser.tab.c -ll

# Archivos generados por Bison
parser.tab.c parser.tab.h: parser.y
	bison -d -o parser.tab.c parser.y

# Archivo generado por Flex
lex.yy.c: lexer.l parser.tab.h
	flex -o lex.yy.c lexer.l

# Ejecutar el parser y pasarle las instrucciones al CPU visualizer
run: parser
	./parser < instructions.txt | python3 ../cpu.py

# Limpiar archivos generados
clean:
	rm -f parser parser.tab.c parser.tab.h lex.yy.c
