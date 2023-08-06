from flask import jsonify, Request, Response
import base64, zlib
import os
from secrets import token_hex 
import pywhatkit
import zipfile
import fitz

def UploadFile(request) -> Response:
    
    pdf_file_paths = './Media/PDF/'

    file = request.json['64base']
    fileType = request.json['type']
    userCpf = request.json['cpf']

    try:
        filename = userCpf + "_" + token_hex(16) + "." + fileType
        with open(pdf_file_paths + filename, "wb") as fh:
            fh.write(base64.b64decode(file))
        compress_file(pdf_file_paths + filename , pdf_file_paths + "compressed_" + filename )
    except Exception as e:
        print(e)	
        return Response(status=500)
    return Response(status=200)


def compress_file(input_file: str, output_file: str):
    # Load PDF using pymupdf
    doc = fitz.open(pdf_file)
    compressed_pdf_bytes = doc.tobytes(
        deflate=True,
        garbage=4,
    )
    print(len(compressed_pdf_bytes)) # Check output of compressed pdf
    with open(output_file, "wb") as f:
        f.write(compressed_pdf_bytes)

def sendZapMessage(message, number):
     pywhatkit.sendwhatmsg_instantly(
         phone_no= "+55" + number, 
         message=message,
     )
