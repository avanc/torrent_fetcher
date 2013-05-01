# Copyright (C) 2013 Sven Klomp (mail@klomp.eu)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA  02110-1301, USA.


import urllib.request
import urllib.error
import os.path


import logging
logger = logging.getLogger(__name__)

TORRENT_URL="http://81.95.11.2/torrents/{0}"

def fetchTorrent(torrent_name, filename):
    url=TORRENT_URL.format(torrent_name)
    logger.debug("Fetch torrent from {0}".format(url))
    if (os.path.exists(filename)):
        logger.error("Output file already exists: {0}".format(filename))
        raise FileExistsError(filename)
    
    try:
        torrent = urllib.request.urlopen(url, timeout=2)
    except urllib.error.HTTPError as err:
        if (err.code==404):
            return False;
        else:
            raise err
    
    f = open(filename, "wb")
    f.write(torrent.readall())
    f.close()
    
    return True