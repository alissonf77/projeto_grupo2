#!/bin/bash

case $1 in
	bind9) $(systemctl $2 $1) ;;
	nagios3) $(systemctl $2 $1) ;;
	firewall) $(bash -c firewall $2) ;;
	*) exit 1 ;;
esac
