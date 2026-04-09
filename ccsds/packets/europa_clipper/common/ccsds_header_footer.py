"""CCSDS Secondary header and CRC footer."""
import ccsdspy


SECONDARY_HEADER = [
    ccsdspy.PacketField(
        name="Instrument SCLK Time second", bit_length=8 * 4, data_type="uint",
        description="Time tag, J2000 (seconds)"
    ),
    ccsdspy.PacketField(
        name="Instrument SCLK Time subsec", bit_length=8 * 2, data_type="uint",
        description="Fractional time (1/216 seconds)"
    ),
    ccsdspy.PacketField(name="Accountability ID", bit_length=8 * 4, data_type="uint",
                        description="Accountability ID"),
]

CRC_FOOTER = ccsdspy.PacketField(
    name="PEC (CRC-16-CCITT)", bit_length=16, data_type="uint",
    description="Packet Error Control field, using CRC-16-CCITT algorithm"
)
