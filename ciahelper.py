import qrcode
import os
import http.server
import socketserver

def generateQRCode(text):
    """Generate QR Code from text."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image()
    img.save("qrcode.png")

def openHttpServer(port):
    """Open HTTP server on port."""
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), Handler)
    print("serving at port", port)
    httpd.serve_forever()

addressPrefix = 'http://10.0.0.2' #Your PC's IP address.


print("""-------------------------------------------------------
    CIA Helper Version 0.1
-------------------------------------------------------""")
print('Please put the cia files in the \'cia\' folder.')
print('Now scanning files...')
pathPrefix = os.getcwd()
path = 'cia'
files = os.listdir(pathPrefix + '/' + path)
for index in range(len(files)):
    if files[index].endswith('.cia'):
        print(str(index) + '    ' + files[index])
print('Please select the cia file you want to install.')
fileNumber = int(input('File: '))
generateQRCode(addressPrefix + ':8080/' + files[fileNumber])
os.system('open qrcode.png') #This may only work on macOS, please check it before using.
os.chdir(pathPrefix + '/' + path)
openHttpServer(8080)
print(files)