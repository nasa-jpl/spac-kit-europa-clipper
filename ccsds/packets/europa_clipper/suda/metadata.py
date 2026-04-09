"""ECM Metadata packet structure."""
import ccsdspy

from ccsds.packets.europa_clipper.common import METADATA_FIELDS

metadata_suda = ccsdspy.VariableLength(
    METADATA_FIELDS,
    apid=1409,
    name="adp_metadata_suda",
    description="Metadata packet structure for SUDA"
)
