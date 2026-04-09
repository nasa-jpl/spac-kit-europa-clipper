"""ECM Metadata packet structure."""
import ccsdspy

from ccsds.packets.europa_clipper.common import METADATA_FIELDS

metadata_maspex = ccsdspy.VariableLength(
    METADATA_FIELDS,
    apid=1281,
    name="metadata_maspex",
    description="MASPEX Metadata packet structure",
)
