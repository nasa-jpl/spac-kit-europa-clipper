"""ECM Metadata packet structure."""
import ccsdspy

from ccsds.packets.europa_clipper.common import METADATA_FIELDS

metadata_pimsu = ccsdspy.VariableLength(
    METADATA_FIELDS,
    apid=1089,
    name="metadata_pimsu",
    description="PIMSU Metadata packet structure."
)
