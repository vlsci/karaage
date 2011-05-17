# Copyright 2007-2010 VPAC
#
# This file is part of Karaage.
#
# Karaage is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Karaage is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Karaage  If not, see <http://www.gnu.org/licenses/>.

""" Test LDAP Data"""

from django.conf import settings

test_ldif = [
    "dn: " + settings.LDAP_GROUP_BASE,
    "objectClass: organizationalUnit",
    "ou: Groups",
    "",
    "dn: " + settings.LDAP_USER_BASE,
    "objectClass: organizationalUnit",
    "ou: People",
    "",
    'dn: uid=kgtestuser1, ' + settings.LDAP_USER_BASE,
    'cn: Test User',
    'objectClass: inetOrgPerson',
    'objectClass: person',
    'objectClass: organizationalPerson',
    'objectClass: top',
    'objectClass: shadowAccount',
    'userPassword:: kklk',
    'o: Example',
    'sn: User',
    'mail: t.user@example.com',
    'givenName: Test',
    'uid: kgtestuser1',
    'shadowWarning: 10',
    'shadowMax: 99999',
    'shadowLastChange: 13600',
    'telephoneNumber: 45645',
    '',
    'dn: uid=kgtestuser2, ' + settings.LDAP_USER_BASE,
    'cn: Test User2',
    'objectClass: inetOrgPerson',
    'objectClass: person',
    'objectClass: organizationalPerson',
    'objectClass: top',
    'objectClass: shadowAccount',
    'userPassword:: kklk',
    'o: Example',
    'sn: User2',
    'mail: t.user2@example.com',
    'givenName: Test',
    'uid: kgtestuser2',
    'shadowWarning: 10',
    'shadowMax: 99999',
    'shadowLastChange: 13600',
    'telephoneNumber: 45645',
    '',
    'dn: uid=kgtestuser3, ' + settings.LDAP_USER_BASE,
    'cn: Test User3',
    'objectClass: inetOrgPerson',
    'objectClass: person',
    'objectClass: organizationalPerson',
    'objectClass: top',
    'objectClass: shadowAccount',
    'objectClass: posixAccount',
    'userPassword:: kklk',
    'o: Example',
    'sn: User3',
    'mail: t.user3@example.com',
    'givenName: Test',
    'uid: kgtestuser3',
    'shadowWarning: 10',
    'shadowMax: 99999',
    'shadowLastChange: 13600',
    'telephoneNumber: 45645',
    'uidNumber: 100',
    'gidNumber: 500',
    'homeDirectory: /home/kgtestuser3',
    'loginShell: /bin/bash',
    'gecos: Test User3 (Example)',
    '',
    'dn: uid=kgldaponly, ' + settings.LDAP_USER_BASE,
    'cn: LDAP Only',
    'objectClass: inetOrgPerson',
    'objectClass: person',
    'objectClass: organizationalPerson',
    'objectClass: top',
    'objectClass: shadowAccount',
    'objectClass: posixAccount',
    'userPassword:: kklk',
    'o: Example',
    'sn: Only',
    'mail: ldaponly@example.com',
    'givenName: LDAP',
    'uid: kgldaponly',
    'shadowWarning: 10',
    'shadowMax: 99999',
    'shadowLastChange: 13600',
    'telephoneNumber: 45645',
    'uidNumber: 100',
    'gidNumber: 500',
    'homeDirectory: /home/kgldaponly',
    'loginShell: /bin/bash',
    'gecos: LDAP Only (Example)',
    '',
    'dn: cn=Example, ' + settings.LDAP_GROUP_BASE,
    'objectClass: posixGroup',
    'gidNumber: 500',
    'cn: Example',
    'description: Example',
    '',
    'dn: cn=OtherInst, ' + settings.LDAP_GROUP_BASE,
    'objectClass: posixGroup',
    'gidNumber: 501',
    'cn: Example',
    'description: Example',
    '',
    'dn: cn=SamlInst, ' + settings.LDAP_GROUP_BASE,
    'objectClass: posixGroup',
    'gidNumber: 502',
    'cn: Example',
    'description: Example',
    '',
    'dn: cn=TestProject1, ' + settings.LDAP_GROUP_BASE,
    'objectClass: posixGroup',
    'gidNumber: 504',
    'cn: TestProject1',
    'description: TestProject1',
    'memberUid: kgtestuser3',
    '',
    ]
