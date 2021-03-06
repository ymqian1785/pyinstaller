#-----------------------------------------------------------------------------
# Copyright (c) 2018-2018, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

from PyInstaller.utils.hooks import collect_submodules

# The ``eth_hash.utils.load_backend`` function does a dynamic import.
hiddenimports = collect_submodules('eth_hash.backends')
