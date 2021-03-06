#!/usr/bin/env python

import pexpect
import sys
import os
import uuid

to=90
cc_home=os.environ['CLOUD_CLIENT_HOME']
nh=os.environ['NIMBUS_HOME']
logfile = sys.stdout
common_image = str(uuid.uuid1()).replace("-", "")
newname = str(uuid.uuid1()).replace("-", "")

cmd = "%s/bin/nimbus-public-image /etc/group %s" % (nh, common_image)
(x, rc)=pexpect.run(cmd, withexitstatus=1, logfile=logfile)
if rc != 0:
    print "failed create the public image"
    sys.exit(1)

cmd = "%s/bin/cloud-client.sh --run --name %s --hours .25 --newname %s" % (cc_home, common_image, newname)
child = pexpect.spawn (cmd, timeout=to, maxread=20000, logfile=logfile)
rc = child.expect ('Running:')
if rc != 0:
    print "group not found in the list"
    sys.exit(1)
handle = child.readline().strip().replace("'", "")
rc = child.expect(pexpect.EOF)
if rc != 0:
    print "run"
    sys.exit(1)

cmd = "%s/bin/cloud-client.sh --list" % (cc_home)
child = pexpect.spawn (cmd, timeout=to, maxread=20000, logfile=logfile)
line = child.readline()
while line:
    if line.find(newname) >= 0:
        print "image name is in list before hte image terminated"
        sys.exit(1)
    line = child.readline()

cmd = "%s/bin/cloud-client.sh --save --handle %s" % (cc_home, handle)
print cmd
(x, rc)=pexpect.run(cmd, withexitstatus=1)
print x
if rc != 0:
    print "failed to terminate"
    sys.exit(1)

found = False
cmd = "%s/bin/cloud-client.sh --list" % (cc_home)
child = pexpect.spawn (cmd, timeout=to, maxread=20000, logfile=logfile)
line = child.readline()
while line:
    if line.find(newname) >= 0:
        found = True
    line = child.readline()
if not found:
    print "new name not found after the images was saved"
    sys.exit(1)

cmd = "%s/bin/nimbus-public-image --delete %s" % (nh, common_image)
(x, rc)=pexpect.run(cmd, withexitstatus=1, logfile=logfile)
if rc != 0:
    print "failed create the public image"
    sys.exit(1)
sys.exit(0)
