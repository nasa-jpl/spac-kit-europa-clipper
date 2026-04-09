"""UVS Metadata packet structure."""
import copy

import ccsdspy

from ccsds.packets.europa_clipper.common import METADATA_FIELDS

# specifically for UVS metadata packetm the following 2 fields are swapped,
# unlike the metadata packets for all the other instruments
uvs_metadata_fields = copy.copy(METADATA_FIELDS)
uvs_metadata_fields[6] = METADATA_FIELDS[7]
uvs_metadata_fields[7] = METADATA_FIELDS[6]

metadata_uvs = ccsdspy.VariableLength(
    uvs_metadata_fields,
    apid=1537,
    name="metadata_reason",
    description="UVS Metadata packet structure, "
                "note that the order of the 'data_start_time' and 'data_stop_time' fields "
                "is swapped compared to the other metadata packets.",
)
