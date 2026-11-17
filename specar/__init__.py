# SPDX-License-Identifier: Apache-2.0
"""Old name of the `stridear` package. `import specar` and `import specar.<module>` return the stridear modules."""
import importlib
import importlib.abc
import importlib.util
import sys

import stridear


class _Alias(importlib.abc.MetaPathFinder, importlib.abc.Loader):
    def find_spec(self, name, path=None, target=None):
        if name.startswith("specar."):
            return importlib.util.spec_from_loader(name, self)
        return None

    def create_module(self, spec):
        return importlib.import_module("stridear" + spec.name[len("specar"):])

    def exec_module(self, module):
        pass


sys.meta_path.insert(0, _Alias())
sys.modules[__name__] = stridear
