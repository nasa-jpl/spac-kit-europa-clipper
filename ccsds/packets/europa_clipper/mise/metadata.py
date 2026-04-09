"""ECM Metadata packet structure."""
import ccsdspy

from ccsds.packets.europa_clipper.common import METADATA_FIELDS

metadata_mise = ccsdspy.VariableLength(
    METADATA_FIELDS,
    apid=1345,
    name="metadata_mise",
    description="MISE Metadata packet structure"
)
