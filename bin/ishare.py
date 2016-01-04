# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from getpass import getpass
import hashlib
from optparse import OptionParser
import os
import time

import paramiko
from progressbar import Bar, Percentage, ProgressBar
from slugify import slugify


HOSTNAME = 'domain.tld'
USERNAME = 'username'

ROOT_PATH = 'https://domain.tld/'
DESTINATION_PATH = '/var/www/'

PROGRESS_BAR = ProgressBar(widgets=[Percentage(), Bar()], maxval=300).start()


def display_progress_bar(uploaded, total):
    PROGRESS_BAR.maxval = total
    PROGRESS_BAR.update(uploaded)


def main():
    parser = OptionParser(usage='usage %prog [options] filename',
                          version='%prog 1.0')

    parser.add_option('-p', '--private',
                      action='store_true',
                      dest='is_private',
                      default=False,
                      help='Push file into private folder')

    parser.add_option('-d', '--delete',
                      action='store_true',
                      dest='to_delete',
                      default=False,
                      help='Delete file from server')

    (options, args) = parser.parse_args()

    if len(args) != 1:
        parser.error('Wrong number of arguments')

    if options.to_delete:
        print 'Deleting: %s' % args[0]
        try:
            password = getpass()

            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(HOSTNAME, username=USERNAME, password=password)

            sftp = ssh.open_sftp()

            #
            sftp.lstat(DESTINATION_PATH + args[0])
            path_name = '/'.join(args[0].split('/')[0:-1])
            sftp.remove(DESTINATION_PATH + args[0])
            sftp.rmdir(DESTINATION_PATH + path_name)

            sftp.close()
            ssh.close()

            print 'Deleted'

        except Exception as error:
            print error

    else:
        if not os.path.exists(args[0]):
            parser.error('%s not found' % args[0])

        url = ROOT_PATH
        destination = DESTINATION_PATH
        if options.is_private:
            url += 'private/'
            destination += 'private/'
        else:
            url += 'public/'
            destination += 'public/'

        #
        if '.' in args[0]:
            basename = ''.join(args[0].split('.')[0:-1])
            extension = args[0].split('.')[-1]
        else:
            basename = args[0]
            extension = ''

        filename = slugify(basename) + '.' + extension
        timestamp = time.time()
        string_to_hash = '%d/%s' % (timestamp, filename)
        file_hash = hashlib.sha1(string_to_hash).hexdigest()

        #
        url += file_hash + '/' + filename
        destination_path = destination + file_hash
        destination = destination_path + '/' + filename

        print 'Uploading: %s' % args[0]
        try:
            password = getpass()

            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(HOSTNAME, username=USERNAME, password=password)

            sftp = ssh.open_sftp()
            sftp.mkdir(destination_path)

            sftp.put(args[0], destination, display_progress_bar)
            PROGRESS_BAR.finish()

            sftp.close()
            ssh.close()

            print 'I share: %s' % url

        except Exception as error:
            print error


if __name__ == '__main__':
    main()

