#!/usr/bin/python
#-*- coding: utf8 -*-

var=raw_input()
import os, re
Min=var.split("&")[0].split("=")[1]
Hor=var.split("&")[1].split("=")[1]
Dia=var.split("&")[2].split("=")[1]
Mes=var.split("&")[3].split("=")[1]
Sem=var.split("&")[4].split("=")[1]
Usr=var.split("&")[5].split("=")[1]
Cmd=var.split("&")[6].split("=")[1]

print("content-type: text/html")
print("")

if re.match ('^((Todos)|[0-9]|[1-5][0-9])$', minuto) \
    and re.match('^((Todos)|[0-9]|1[0-9]|2[0-3])$', hora) \
    and re.match('^((Todos)|[0-9]|[12][0-9]|3[01])$', ddm) \
    and re.match('^((Todos)|[1-9]|1[0-2])$', mes) \
    and re.match('^((Todos)|[0-7])$', dds) \
    and re.match('^((Todos)|[a-zA-Z]{1,})$', usu) \
    and re.match('((Todos)|[a-zA-Z0-9 +]{1,})', com):
	os.system("echo " +\
	minuto + " " +\
	hora + " " +\
	ddm + " " +\
	mes + " " +\
	dds + " " +\
	usu + " " +\
	com + ">> /etc/crontab")
	os.system("sudo sed -i s/todos/*/g /etc/crontab")
	print ("<h1>Agendamento realizado com sucesso!</h1>")
else:
	print("Agendamento Falhou!")
 
