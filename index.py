# Willi
# Nama: Prajudi William Chrisdeardo
# Asal Kampus: Universitas Gunadarma

# Import library terlebih dahulu.
import json
import re

# Membuka file JSON
file_json = open("data.json");

# Parsing data JSON
data = json.loads(file_json.read());

# Soal
# Dengan Menggunakan Bahasa python lakukan hal-hal berikut:
# 1. Lakukan request api ke link berikut: https://reqres.in/api/users?page=1
print(data)
# 2. Dengan menggunakan json ambil data dengan user id 5.
print(data['data'][4])
# 3. Dengan menggunakan REGEX ambil data nama image dari setiap user (conton hasil User 1 =  "1-image.jpg") dan seterusnya.

# Silahkan upload file python yang anda buat dengan nama anda.