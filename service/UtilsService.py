from flask import jsonify, Request, Response


def UploadFile(request) -> Response:
    file = request
    print(file)
    #file.save('./Media/PDF/CPF/' + file.filename)
    return jsonify({'msg': 'File uploaded successfully'})