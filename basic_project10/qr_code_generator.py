# instal qrcode library to generate qr code
#instal pillow to show qr code

import qrcode
# taking UPI ID as a input
upi_id = input("Enter your UPI ID : ")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

#Defining the payment url bsaed on the UPI ID and the payment app
#You can modify these URLs based on the payment apps you ant to support

phonepe_url  = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url  = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
googlepay_url  = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#Create QR Code for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
googlepay_qr = qrcode.make(googlepay_url)

# save the qr code to image file(optional)
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
googlepay_qr.save('googlepay_qr.png')

#Display the qr code using pillow libraray
phonepe_qr.show()
paytm_qr.show()
googlepay_qr.show()

