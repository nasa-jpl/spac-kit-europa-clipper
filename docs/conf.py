import importlib.metadata

# Project information
metadata = importlib.metadata.metadata("spac-kit-europa-clipper")
project = metadata["Name"]
author = metadata["Author"]
release = metadata["Version"]


extensions = [
    'spac_kit.autodocs',
    'sphinx_rtd_theme',
]

# Use Read the Docs theme for better sidebar navigation
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 4,  # Show up to 4 levels in sidebar
    'collapse_navigation': False,  # Keep sidebar expanded
}

# List of modules to scan for _BasePacket instances for stub generation
spacdocs_packet_modules = [
    'ccsds.packets.europa_clipper.e_themis',
    'ccsds.packets.europa_clipper.ecm',
    'ccsds.packets.europa_clipper.eisnac',
    'ccsds.packets.europa_clipper.eiswac',
    'ccsds.packets.europa_clipper.maspex',
    'ccsds.packets.europa_clipper.mise',
    'ccsds.packets.europa_clipper.pimsl',
    'ccsds.packets.europa_clipper.radmon',
    'ccsds.packets.europa_clipper.reason',
    'ccsds.packets.europa_clipper.suda',
    'ccsds.packets.europa_clipper.uvs',
]
