"""ECM Metadata packet structure."""
import ccsdspy

from ccsds.packets.europa_clipper.common import METADATA_FIELDS

metadata_eiswac = ccsdspy.VariableLength(
    METADATA_FIELDS,
    apid=1665,
    name="metadata_eiswac",
    description="EISWAC Metadata packet structure"
)
