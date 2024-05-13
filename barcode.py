import barcode
from barcode import Code128

def generate_barcode(data):
    code = Code128(data)
    code.save("barcode.png")
    print( "Barcode generate" )

data = "0714835489"
generate_barcode(data)