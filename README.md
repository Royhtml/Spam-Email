<img src = "https://www.hoster.co.id/panduan/images/email/spam-email-2.jpg" width="100%" height="auto">

# Spam-Email
Spam email adalah pesan yang tidak diminta dan dikirim secara massal ke banyak penerima. Spam email bisa berupa promosi produk, penawaran palsu, pesan phishing, atau bahkan malware. Spam email dapat mengganggu produktivitas dan berpotensi membahayakan keamanan online Anda. 

# Spam Email Sender (Edukasi)

**Peringatan**: 
- Script ini hanya untuk tujuan edukasi
- Mengirim email spam adalah ilegal di banyak negara
- Jangan gunakan untuk tujuan nyata
- Gunakan hanya pada lingkungan terkendali untuk tujuan pembelajaran

## Persyaratan
- Python 3.x
- Akun Gmail (disarankan menggunakan App Password)

## Instalasi

### Untuk Termux (Android)
1. Buka Termux dan update package:
   ```bash
   pkg update && pkg upgrade
   ```

2. Install Python dan dependensi yang diperlukan:
   ```bash
   pkg install python git
   ```

3. Clone repository ini (jika ada) atau buat file manual:
   ```bash
   git clone https://github.com/Royhtml/Spam-Email
   cd spam-email-sender
   ```

4. Install requirements :
   ```bash
   pip install -r requirements.txt
   ```

5. Jalankan program:
   ```bash
   python spam_email.py
   ```

### Untuk Linux (Debian/Ubuntu)
1. Update sistem dan install Python:
   ```bash
   sudo apt update && sudo apt upgrade
   sudo apt install python3 python3-pip git
   ```

2. Clone repository atau buat file manual:
   ```bash
   git clone [repo-url] (jika tersedia)
   cd spam-email-sender
   ```

3. Install requirements:
   ```bash
   pip3 install -r requirements.txt
   ```

4. Jalankan program:
   ```bash
   python3 spam_email.py
   ```

## Cara Menggunakan
1. Jalankan script dengan perintah di atas
2. Masukkan informasi yang diminta:
   - Email pengirim (harus Gmail)
   - Password (disarankan menggunakan App Password)
   - Email penerima (bisa multiple, pisahkan dengan koma)
   - Pilihan template (promo/lottery/phishing)

## Catatan Keamanan
1. Untuk Gmail, Anda perlu membuat App Password jika menggunakan 2FA:
   - Buka https://myaccount.google.com/
   - Ke "Security" > "App passwords"
   - Buat password untuk aplikasi "Mail" di perangkat "Other"

2. Script ini mungkin tidak bekerja jika:
   - Akun Gmail pengirim tidak mengizinkan akses aplikasi kurang aman
   - Firewall memblokir koneksi SMTP

3. Sangat disarankan untuk:
   - Menggunakan akun Gmail khusus untuk testing
   - Tidak menggunakan password akun utama
   - Hanya mengirim ke email Anda sendiri untuk testing

## Disclaimer
Script ini dibuat semata-mata untuk tujuan edukasi tentang cara kerja email dan teknik social engineering. Penulis tidak bertanggung jawab atas penyalahgunaan script ini.
