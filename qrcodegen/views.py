import qrcode
from django.shortcuts import render
from django.http import HttpResponse


def generate_qr_code(request):
    if request.method == 'POST':
        
        qr_code_data = request.POST.get('data')

        # Generate the QR code image
        qr_code = qrcode.QRCode()
        qr_code.add_data(qr_code_data)
        qr_code.make()

        # Set the QR code options
        qr_code_image = qr_code.make_image(fill='black', back_color='white')

        # Serve the image as a response
        response = HttpResponse(content_type="image/png")
        qr_code_image.save(response, "PNG")
        return response
    else:
        return render(request, 'generate_qr_code.html')
