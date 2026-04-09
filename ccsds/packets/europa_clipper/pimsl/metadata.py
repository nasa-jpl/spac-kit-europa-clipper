"""ECM Metadata packet structure."""
import ccsdspy

from ccsds.packets.europa_clipper.common import METADATA_FIELDS

metadata_pimsl = ccsdspy.VariableLength(
    METADATA_FIELDS,
    apid=1153,
    name="metadata_pimsl",
    description="PIMSL Metadata packet structure",
)
