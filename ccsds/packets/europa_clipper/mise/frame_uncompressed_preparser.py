"""Uncompressed frame, pre-parsing packet."""
import ccsdspy
from ccsdspy.constants import BITS_PER_BYTE

frame_uncompressed_preparser = ccsdspy.VariableLength(
    [
        ccsdspy.PacketArray(
            name="data",
            data_type="uint",
            bit_length=BITS_PER_BYTE,
            array_shape="expand",
        )
    ],
    apid=1392,
    name="frame uncompressed pre-parser",
    description="Uncompressed frame, pre-parsing packet structure."
)

N = 0


def sequence():
    """Count packet sequences to identify packets sub-types of APID 1392.

    90 first packets are regular, 91st and 92nd are specifics.
    """
    global N  # pylint: disable=W0603
    N += 1
    if N <= 90:
        return "90th"
    if N == 91:
        return "91st"

    N = 0
    return "92nd"


frame_uncompressed_preparser.decision_fun = sequence
