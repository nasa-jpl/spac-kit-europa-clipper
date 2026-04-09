"""ECM Metadata packet structure."""
import ccsdspy

from ccsds.packets.europa_clipper.common import METADATA_FIELDS

metadata_ethemis = ccsdspy.VariableLength(
    METADATA_FIELDS,
    apid=1473,
    name="adp_metadata_ethemis",
    description="Metadata packet for E-THEMIS APID 1473"
)
