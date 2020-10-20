libs = [ "epd1in02"
, "epd1in54"
, "epd1in54b"
, "epd1in54b_V2"
, "epd1in54c"
, "epd1in54_V2"
, "epd2in7"
, "epd2in7b"
, "epd2in9"
, "epd2in9bc"
, "epd2in9b_V2"
, "epd2ind"
, "epd2in13"
, "epd2in13bc"
, "epd2in13b_V3"
, "epd2in13d"
, "epd2in13_V2"
, "epd2in66"
, "epd3in7"
, "epd4in2"
, "epd4in2bc"
, "epd4in2b_V2"
, "epd5in65f"
, "epd5in83"
, "epd5in83bc"
, "epd5in83b_V2"
, "epd7in5"
, "epd7in5bc"
, "epd7in5bc_V2"
, "epd7in5b_HD"
, "epd7in5_HD"
, "epd7in5_V2"]

with open("epd.py", "w") as file: 
    # Writing data to a file 
    for lib in libs:
        file.write(f"import {lib}\n")
    file.write(f"\n")
    for lib in libs:
        file.write(f"def get_{lib}():\n\treturn {lib}.EPD()\n\n")