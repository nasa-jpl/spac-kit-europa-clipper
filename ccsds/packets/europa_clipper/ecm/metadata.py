"""ECM Metadata packet structure."""
import ccsdspy

from ccsds.packets.europa_clipper.common import METADATA_FIELDS

metadata_ecm = ccsdspy.VariableLength(
    METADATA_FIELDS,
    apid=1217,
    name="adp_metadata_ecm",
    description="Metadata packet for ECM, APID 1217"
)
