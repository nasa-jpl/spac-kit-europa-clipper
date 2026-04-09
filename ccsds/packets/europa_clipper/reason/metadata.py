"""ECM Metadata packet structure."""
import ccsdspy

from ccsds.packets.europa_clipper.common import METADATA_FIELDS

metadata_reason = ccsdspy.VariableLength(
    METADATA_FIELDS,
    apid=1601,
    name="metadata_reason",
    description="REASON Metadata packet structure",
)
