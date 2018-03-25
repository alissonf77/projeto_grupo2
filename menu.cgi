#!/usr/bin/python
#-*- coding: utf8 -*-

var=raw_input()
import os
acao=var.split("=")[0]
print("content-type: text/html")
print("")

if acao == "d_i":
	os.system("sudo /usr/lib/cgi-bin/script.sh bind9 start")
	print("<h1>Iniciado...</h1>")
elif acao == "d_p":
	os.system("sudo /usr/lib/cgi-bin/script.sh bind9 stop")
	print("<h1>Parado...</h1>")
elif acao == "d_r":
	os.system("sudo /usr/lib/cgi-bin/script.sh bind9 restart")
	print("<h1>Reiniciado...</h1>")
elif acao == "n_i":
	os.system("sudo /usr/lib/cgi-bin/script.sh nagios3 start")
	print("<h1>Iniciado...</h1>")
elif acao == "n_p":
	os.system("sudo /usr/lib/cgi-bin/script.sh nagios3 stop")
	print("<h1>Parado...</h1>")
elif acao == "n_r":
	os.system("sudo /usr/lib/cgi-bin/script.sh nagios3 restart")
	print("<h1>Reiniciado...</h1>")
elif acao == "f_i":
	os.system("sudo /usr/lib/cgi-bin/firewall.sh")
	print("<h1>Iniciado...</h1>")
elif acao == "f_p":
	os.system("sudo /usr/lib/cgi-bin/sfirewall.sh")
	print("<h1>Parado...</h1>")
elif acao == "f_r":
	os.system("sudo /usr/lib/cgi-bin/rfirewall.sh")
	print("<h1>Reiniciado...</h1>")
