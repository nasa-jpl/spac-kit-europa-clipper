"""Package file."""
import pkgutil

# needs to be loaded first
__all__ = ["ccsds.packets.europa_clipper.common"]  # pylint: disable=undefined-all-variable
import ccsds.packets.europa_clipper.common  # pylint: disable=wrong-import-position

for loader, module_name, _ in pkgutil.walk_packages(__path__):
    if "test" not in module_name and "common" not in module_name:
        __all__.append(module_name)
        _module = loader.find_module(module_name).load_module(module_name)
        globals()[module_name] = _module

# need to be loaded last
import ccsds.packets.europa_clipper.test  # noqa # pylint: disable=wrong-import-position


__all__.append("ccsds.packets.europa_clipper.test")
