# This software and any associated files are copyright 2010 Brian Carver and
# Michael Lissner.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#  Under Sections 7(a) and 7(b) of version 3 of the GNU Affero General Public
#  License, that license is supplemented by the following terms:
#
#  a) You are required to preserve this legal notice and all author
#  attributions in this program and its accompanying documentation.
#
#  b) You are prohibited from misrepresenting the origin of any material
#  within this covered work and you are required to mark in reasonable
#  ways how any modified versions differ from the original version.


import sys
sys.path.append('/var/www/court-listener/alert')

import settings
from django.core.management import setup_environ
setup_environ(settings)

from search.models import Document
from juriscraper.lib.string_utils import harmonize, clean_string
from optparse import OptionParser
import re


def fixer(simulate=False, verbose=False):
    '''Remove leading slashes by running the new and improved harmonize/clean_string scipts'''
    docs = Document.objects.raw(r'''select Document.documentUUID
                                    from Document, Citation 
                                    where Document.citation_id = Citation.citationUUID and 
                                    Citation.case_name like '(%%';''')

    for doc in docs:
        # Special cases
        if 'Klein' in doc.citation.case_name:
            continue
        elif 'in re' in doc.citation.case_name.lower():
            continue

        # Otherwise, we nuke the leading parens.
        old_case_name = doc.citation.case_name
        new_case_name = harmonize(clean_string(re.sub('\(.*\)', '', doc.citation.case_name)))

        if verbose:
            print "Fixing document %s: %s" % (doc.pk, doc)
            print "        New for %s: %s" % (doc.pk, new_case_name)

        if not simulate:
            doc.citation.case_name = new_case_name
            doc.citation.save()


def main():
    usage = "usage: %prog [--verbose] [---simulate]"
    parser = OptionParser(usage)
    parser.add_option('-v', '--verbose', action="store_true", dest='verbose',
        default=False, help="Display log during execution")
    parser.add_option('-s', '--simulate', action="store_true",
        dest='simulate', default=False, help=("Simulate the corrections without "
        "actually making them."))
    (options, args) = parser.parse_args()

    verbose = options.verbose
    simulate = options.simulate

    if simulate:
        print "*******************************************"
        print "* SIMULATE MODE - NO CHANGES WILL BE MADE *"
        print "*******************************************"

    return fixer(simulate, verbose)
    exit(0)

if __name__ == '__main__':
    main()
