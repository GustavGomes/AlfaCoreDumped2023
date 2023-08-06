from flask import jsonify, Request, Response
import base64, zlib
import os
from secrets import token_hex 
import pywhatkit
import zipfile

def UploadFile(request) -> Response:
    
    pdf_file_paths = './Media/PDF/'

    file = request.json['64base']
    fileType = request.json['type']
    userCpf = request.json['cpf']

    try:
        filename = userCpf + "_" + token_hex(16) + "." + fileType
        with open(pdf_file_paths + filename, "wb") as fh:
            fh.write(base64.b64decode(file))
        compress_file(pdf_file_paths + filename , pdf_file_paths + "2_" + filename )
    except Exception as e:
        print(e)	
        return Response(status=500)
    return Response(status=200)


def compress_file(input_file: str, output_file: str):
    file1 = open(input_file, 'rb')
    content = file1.read()
    file1.close()

    compressed_content = zlib.compress(content, 9)
    f = open(output_file, 'wb')
    f.write(compressed_content)
    f.close()

def sendZapMessage(message, number):
    pywhatkit.sendwhatmsg_instantly(
        phone_no= "+55" + number, 
        message=message,
    )
