#!/usr/bin/python
# -*- Mode: Python; python-indent: 8; indent-tabs-mode: t -*-

import sys, os, argparse, errno

def find_service(service, runlevel):
	priority = -1

	for l in os.listdir("/etc/rc%i.d" % runlevel):
		if len(l) < 4:
			continue

		if l[0] != 'S' or l[3:] != service:
			continue

		p = int(l[1:3])

		if p >= 0 and p <= 99 and p >= priority:
			priority = p;

	return priority

def lookup_database(services):
	try:
		database = open("/var/lib/systemd/sysv-convert/database", "r")
	except IOError, e:
		if e.errno != errno.ENOENT:
			raise e

		return {}

	found = {}
	k = 0

	for line in database:
		service, r, p = line.strip().split("\t", 3)
		k += 1

		try:
			runlevel = int(r)
			priority = int(p)
		except ValueError, e:
			sys.stderr.write("Failed to parse database line %i. Ignoring." % k)
			continue

		if runlevel not in (2, 3, 4, 5):
			sys.stderr.write("Runlevel out of bounds in database line %i. Ignoring." % k)
			continue

		if priority < 0 or priority > 99:
			sys.stderr.write("Priority out of bounds in database line %i. Ignoring." % k)
			continue

		if service not in services:
			continue

		if service not in found:
			found[service] = {}

		if runlevel not in found[service] or found[service][runlevel] < priority:
			found[service][runlevel] = priority

	return found

def mkdir_p(path):
	try:
		os.makedirs(path, 0755)
	except OSError, e:
		if e.errno != errno.EEXIST:
			raise e

if os.geteuid() != 0:
	sys.stderr.write("Need to be root.\n")
	sys.exit(1)

parser = argparse.ArgumentParser(description='Save and Restore SysV Service Runlevel Information')

parser.add_argument('services', metavar='SERVICE', type=str, nargs='+',
		    help='Service names')

parser.add_argument('--save', dest='save', action='store_const',
		    const=True, default=False,
		    help='Save SysV runlevel information for one or more services')

parser.add_argument('--show', dest='show', action='store_const',
		    const=True, default=False,
		    help='Show saved SysV runlevel information for one or more services')

parser.add_argument('--apply', dest='apply', action='store_const',
		    const=True, default=False,
		    help='Apply saved SysV runlevel information for one or more services to systemd counterparts')

a = parser.parse_args()

if a.save:
	for service in a.services:
		if not os.access("/etc/rc.d/init.d/%s" % service, os.F_OK):
			sys.stderr.write("SysV service %s does not exist.\n" % service)
			sys.exit(1)

	mkdir_p("/var/lib/systemd/sysv-convert")
	database = open("/var/lib/systemd/sysv-convert/database", "a")

	for runlevel in (2, 3, 4, 5):
		priority = find_service(service, runlevel)

		if priority >= 0:
			database.write("%s\t%s\t%s\n" % (service, runlevel, priority))

elif a.show:
	found = lookup_database(a.services)

	if len(found) <= 0:
		sys.stderr.write("No information about passed services found.\n")
		sys.exit(1)

	for service, data in found.iteritems():
		for runlevel, priority in data.iteritems():
			sys.stdout.write("SysV service %s enabled in runlevel %s at priority %s\n" % (service, runlevel, priority))

elif a.apply:
	for service in a.services:
		if not os.access("/lib/systemd/system/%s.service" % service, os.F_OK):
			sys.stderr.write("systemd service %s.service does not exist.\n" % service)
			sys.exit(1)

	found = lookup_database(a.services)

	if len(found) <= 0:
		sys.stderr.write("No information about passed services found.\n")
		sys.exit(1)

	for service, data in found.iteritems():
		for runlevel in data.iterkeys():

			sys.stderr.write("ln -sf /lib/systemd/system/%s.service /etc/systemd/system/runlevel%i.target.wants/%s.service\n" % (service, runlevel, service))

			mkdir_p("/etc/systemd/system/runlevel%i.target.wants" % runlevel)

			try:
				os.symlink("/lib/systemd/system/%s.service" % service,
					   "/etc/systemd/system/runlevel%i.target.wants/%s.service" % (runlevel, service))
			except OSError, e:
				if e.errno != errno.EEXIST:
					raise e

else:
	parser.print_help()
