"""Package file. Logic needed for auto-discoverability of the submodules."""
import importlib
import pkgutil

# needs to be loaded first
__all__ = ["ccsds.packets.europa_clipper.common"]
import ccsds.packets.europa_clipper.common  # noqa


def __getattr__(name):
    for _, modname, _ in pkgutil.iter_modules(__path__):
        if modname == name and "common" not in modname:
            module = importlib.import_module(f"{__name__}.{name}")
            globals()[name] = module
            return module
    raise AttributeError(name)


def __dir__():
    return list(globals()) + [
        name for _, name, _ in pkgutil.iter_modules(__path__)
    ]
