"""ECM Metadata packet structure."""
import ccsdspy

from ccsds.packets.europa_clipper.common import METADATA_FIELDS

metadata_radmon = ccsdspy.VariableLength(
    METADATA_FIELDS,
    apid=1025,
    name="metadata_radmon",
    description="RADMON Metadata packet structure",
)
