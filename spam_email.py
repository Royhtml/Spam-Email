import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import random
from getpass import getpass

class SpamEmailDesigner:
    def __init__(self):
        self.templates = {
            "promo": self._promo_template,
            "lottery": self._lottery_template,
            "phishing": self._phishing_template
        }
        self.colors = {
            "red": "#FF0000",
            "green": "#00FF00",
            "blue": "#0000FF",
            "yellow": "#FFFF00",
            "purple": "#800080"
        }
    
    def _promo_template(self, recipient):
        subject = f"🎉 Promo Spesial Hanya untuk Anda, {recipient.split('@')[0]}!"
        
        color = random.choice(list(self.colors.values()))
        html = f"""
        <html>
            <body style="font-family: Arial, sans-serif; max-width: 600px; margin: auto;">
                <div style="background-color: {color}; padding: 20px; text-align: center;">
                    <h1 style="color: white;">PROMO MENGEJUTKAN!</h1>
                </div>
                <div style="padding: 20px;">
                    <p>Halo {recipient.split('@')[0]},</p>
                    <p>Kami memberikan diskon <b>90%</b> khusus untuk Anda!</p>
                    <p>Produk terbaik kami sekarang bisa Anda dapatkan dengan harga yang tidak akan Anda temukan di tempat lain.</p>
                    <p style="text-align: center;">
                        <a href="http://bukan-scam.com/klik-disini" 
                           style="background-color: {color}; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">
                           KLIK DISINI UNTUK MENDAPATKANNYA!
                        </a>
                    </p>
                    <p>Tawaran ini hanya berlaku 24 jam. Jangan lewatkan kesempatan ini!</p>
                    <p>Best regards,<br>Tim Promosi</p>
                </div>
                <div style="background-color: #f0f0f0; padding: 10px; text-align: center; font-size: 12px;">
                    <p>Jika Anda tidak ingin menerima email ini, abaikan saja (tapi Anda akan menyesal).</p>
                </div>
            </body>
        </html>
        """
        return subject, html
    
    def _lottery_template(self, recipient):
        subject = "🏆 SELAMAT! Anda Memenangkan Hadiah $10.000!"
        
        html = """
        <html>
            <body style="font-family: Arial, sans-serif; max-width: 600px; margin: auto;">
                <div style="background-color: gold; padding: 20px; text-align: center;">
                    <h1>ANDA ADALAH PEMENANG!</h1>
                </div>
                <div style="padding: 20px;">
                    <p>Kepada Yang Terhormat,</p>
                    <p>Kami dengan senang hati mengumumkan bahwa Anda telah memenangkan hadiah utama sebesar <b>$10.000</b>!</p>
                    <p>Ini bukan lelucon - Anda benar-benar beruntung!</p>
                    <p style="text-align: center;">
                        <a href="http://bukan-scam.com/klaim-hadiah" 
                           style="background-color: gold; color: black; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold;">
                           KLIK DISINI UNTUK MENGKLIM HADIAH ANDA
                        </a>
                    </p>
                    <p>Anda hanya memiliki 1 jam untuk mengklaim hadiah ini sebelum diberikan ke orang lain.</p>
                    <p>Salam hangat,<br>Tim Undian Internasional</p>
                </div>
                <div style="background-color: #f0f0f0; padding: 10px; text-align: center; font-size: 12px;">
                    <p>Undian ini 100% legal dan sah (percayalah).</p>
                </div>
            </body>
        </html>
        """
        return subject, html
    
    def _phishing_template(self, recipient):
        subject = "⚠️ PERINGATAN: Masalah dengan Akun Anda"
        
        html = f"""
        <html>
            <body style="font-family: Arial, sans-serif; max-width: 600px; margin: auto;">
                <div style="background-color: #FF4500; padding: 20px; text-align: center;">
                    <h1 style="color: white;">PERINGATAN KEAMANAN</h1>
                </div>
                <div style="padding: 20px;">
                    <p>Halo Pengguna,</p>
                    <p>Kami mendeteksi aktivitas mencurigakan pada akun Anda. Untuk melindungi akun Anda, kami perlu memverifikasi identitas Anda.</p>
                    <p style="text-align: center;">
                        <a href="http://bukan-scam.com/verifikasi-sekarang" 
                           style="background-color: #FF4500; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">
                           VERIFIKASI AKUN ANDA SEKARANG
                        </a>
                    </p>
                    <p>Jika Anda tidak melakukan verifikasi dalam 24 jam, akun Anda akan <b>dibekukan secara permanen</b>.</p>
                    <p>Terima kasih atas pengertian Anda,<br>Tim Keamanan</p>
                </div>
                <div style="background-color: #f0f0f0; padding: 10px; text-align: center; font-size: 12px;">
                    <p>Email ini dikirim secara otomatis. Jangan membalas email ini.</p>
                </div>
            </body>
        </html>
        """
        return subject, html
    
    def get_template(self, template_name, recipient):
        if template_name in self.templates:
            return self.templates[template_name](recipient)
        else:
            return self._promo_template(recipient)

class SpamEmailSender:
    def __init__(self):
        self.designer = SpamEmailDesigner()
    
    def send_spam(self, sender_email, sender_password, recipient_emails, template_name="promo", attachment_path=None):
        # Membuat koneksi ke server SMTP
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            
            for recipient in recipient_emails:
                # Membuat email
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = recipient
                
                # Mendapatkan template
                subject, html = self.designer.get_template(template_name, recipient)
                msg['Subject'] = subject
                
                # Menambahkan body HTML
                msg.attach(MIMEText(html, 'html'))
                
                # Menambahkan attachment jika ada
                if attachment_path:
                    with open(attachment_path, 'rb') as f:
                        img_data = f.read()
                    image = MIMEImage(img_data, name=Path(attachment_path).name)
                    msg.attach(image)
                
                # Mengirim email
                server.sendmail(sender_email, recipient, msg.as_string())
                print(f"Email berhasil dikirim ke {recipient}")
            
            server.quit()
            print("Semua email telah berhasil dikirim!")
        
        except Exception as e:
            print(f"Error: {e}")

# Contoh penggunaan
if __name__ == "__main__":
    print("=== SPAM EMAIL SENDER (EDUKASI) ===")
    print("""
    Peringatan: 
    - Script ini hanya untuk tujuan edukasi
    - Mengirim email spam adalah ilegal
    - Jangan gunakan untuk tujuan nyata
    """)
    
    sender_email = input("Email pengirim (Gmail): ")  # Perhatikan nama variabel di sini
    password = input("Password (tidak disarankan) atau App Password: ")
    recipients = input("Email penerima (pisahkan dengan koma): ").split(',')
    template = input("Pilih template (promo/lottery/phishing): ").lower()
    
    sender = SpamEmailSender()  # Ini membuat objek SpamEmailSender
    sender.send_spam(
        sender_email=sender_email.strip(),  # Gunakan variabel sender_email bukan sender
        sender_password=password.strip(),
        recipient_emails=[r.strip() for r in recipients],
        template_name=template
    )