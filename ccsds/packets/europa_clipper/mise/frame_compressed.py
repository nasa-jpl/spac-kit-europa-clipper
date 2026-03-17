"""Compressed frame packet definition."""
import ccsdspy

from .decompression_converter import MISEDecompressionConverter
from ccsds.packets.europa_clipper.common import CRC_FOOTER
from ccsds.packets.europa_clipper.common import SECONDARY_HEADER

# offset_count = 48 + 32 + 16 + 32 + 9*4 + 4 + 14
comp_frame_pkt = ccsdspy.VariableLength(
    [
        *SECONDARY_HEADER,
        ccsdspy.PacketField(name="Row Origin", bit_length=9, data_type="uint", description="Window origin, row"),
        ccsdspy.PacketField(name="Column Origin", bit_length=9, data_type="uint", description="Window origin, column"),
        ccsdspy.PacketField(name="Window Rows", bit_length=9, data_type="uint", description="Window dimensions, rows"),
        ccsdspy.PacketField(name="Window Columns", bit_length=9, data_type="uint",
                            description="Window dimensions, columns"),
        ccsdspy.PacketField(name="Row Binning", bit_length=2, data_type="uint", description="Row binning"),
        ccsdspy.PacketField(name="Column Binning", bit_length=2, data_type="uint", description="Column binning"),
        # initial value (14bits), compressed frame and padding fields are including in this field
        # to make sure the fields is aligned on bytes.
        ccsdspy.PacketArray(
            name="Comp Data", bit_length=8, data_type="uint", array_shape="expand",
            description="Compressed pixel data. The first 14 bits are used for the P0,0 uncompressed value."
                        "then each pixel value is compressed on 4bits values are organized in strips of 320 pixels. "
                        "Padding bits are added at the end of the compressed stream to align on bytes."
        ),
        CRC_FOOTER,
    ]
)
comp_frame_pkt.description = "MISE Compressed frame packet definition."

converter = MISEDecompressionConverter(
    uncompressed_item_mask=0x3FFF,
    data_length_without_frame_bytes=4 * 9 + 2 * 2 + 14,
    differences_stored=True,
)

comp_frame_pkt.add_converted_field(
    ("Comp Data", "Window Columns", "Column Binning"), "Uncomp Data", converter
)
comp_frame_pkt.name = "comp_frame_pkt"
comp_frame_pkt.apid = 1393
