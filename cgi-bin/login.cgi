#!/usr/bin/python
#-*- coding: utf8 -*-

var=raw_input()
usuario=var.split("&")[0].split("=")[1]
senha=var.split("&")[1].split("=")[1]

def cabecalho():
	print("content-type: text/html")
	print("")

#def processos():
#	cabecalho()
#	print ("<h1>Processos</h1>")
#	print ("<textarea">)
#	ps = open("/var/www/html/cgi-bin/processos.log", "r")
#	html=ps.read()
#	ps.close()
#	print(html)
#	print("</textarea>")

def menu():
	cabecalho()
	f = open("/var/www/html/menu.html", "r")
	html=f.read()
	f.close()
	print(html)

def erro():
	cabecalho()
	print("<h1>Login Falhou...</h1>")

if usuario == "grupo2" and senha == "123":
	menu()
else:
	erro()

