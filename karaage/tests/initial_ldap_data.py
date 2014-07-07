# Copyright 2007-2014 VPAC
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

GROUP_DN = 'ou=Group, dc=python-ldap,dc=org'
ACCOUNT_DN = 'ou=Account, dc=python-ldap,dc=org'
PEOPLE_DN = 'ou=People, dc=python-ldap,dc=org'
PEOPLE_GROUP_DN = 'ou=PeopleGroup, dc=python-ldap,dc=org'

test_ldif = [
    "dn: " + GROUP_DN,
    "objectClass: organizationalUnit",
    "ou: Groups",
    "",
    "dn: " + ACCOUNT_DN,
    "objectClass: organizationalUnit",
    "ou: Account",
    "",
    "dn: " + PEOPLE_DN,
    "objectClass: organizationalUnit",
    "ou: People",
    "",
    "dn: " + PEOPLE_GROUP_DN,
    "objectClass: organizationalUnit",
    "ou: PeopleGroup",
    "",
    'dn: uid=kgtestuser3, ' + ACCOUNT_DN,
    'cn: Test User3',
    'objectClass: inetOrgPerson',
    'objectClass: person',
    'objectClass: organizationalPerson',
    'objectClass: top',
    'objectClass: shadowAccount',
    'objectClass: posixAccount',
    'userPassword: kklk',
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
    'dn: uid=kgtestuser3, ' + PEOPLE_DN,
    'cn: Test User3',
    'objectClass: inetOrgPerson',
    'objectClass: person',
    'objectClass: organizationalPerson',
    'objectClass: top',
    'userPassword: kklk',
    'o: Example',
    'sn: User3',
    'mail: t.user3@example.com',
    'givenName: Test',
    'uid: kgtestuser3',
    'telephoneNumber: 45645',
    '',
    'dn: uid=kgldaponly, ' + ACCOUNT_DN,
    'cn: LDAP Only',
    'objectClass: inetOrgPerson',
    'objectClass: person',
    'objectClass: organizationalPerson',
    'objectClass: top',
    'objectClass: shadowAccount',
    'objectClass: posixAccount',
    'userPassword: kklk',
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
    'dn: cn=Example, ' + GROUP_DN,
    'objectClass: posixGroup',
    'gidNumber: 500',
    'cn: Example',
    'description: Example',
    '',
    'dn: cn=OtherInst, ' + GROUP_DN,
    'objectClass: posixGroup',
    'gidNumber: 501',
    'cn: OtherInst',
    'description: Example',
    '',
    'dn: cn=SamlInst, ' + GROUP_DN,
    'objectClass: posixGroup',
    'gidNumber: 502',
    'cn: SamlInst',
    'description: Example',
    '',
    'dn: cn=TestProject1, ' + GROUP_DN,
    'objectClass: posixGroup',
    'gidNumber: 504',
    'cn: TestProject1',
    'description: TestProject1',
    'memberUid: kgtestuser3',
    '',
    'dn: cn=TestProject1, ' + PEOPLE_GROUP_DN,
    'objectClass: posixGroup',
    'gidNumber: 504',
    'cn: TestProject1',
    'description: TestProject1',
    'memberUid: kgtestuser3',
    '',
]
