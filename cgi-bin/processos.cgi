#!/usr/bin/python
#-*- coding: utf8 -*-

var=raw_input()
menu=var.split("=")[0]

def cabecalho():
	print("content-type: text/html")
	print("")

def processos():
	cabecalho()
	print ("<h1>Processos:</h1>")
	print ("<textarea rows='100' cols='100' class='user'>")
	ps = open("/var/www/html/cgi-bin/processos.log", "r")
	html=ps.read()
	ps.close()
	print(html)
	print("</textarea>")

if menu == "PS":
	processos() 
