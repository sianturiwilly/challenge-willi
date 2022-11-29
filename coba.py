import re

teks = """1. roti maryam.jpg
2. es teh manis.jpg
3. jus alpukat.jpg
4. roti buaya.jpg
5. durian.jpg
6. coklat.jpg
7. spageti.jpg
8. rambutan.jpg
9. nasi goreng.jpg
10. martabak.jpg
11. pecel.jpg"""

print("Teks:")
print(teks)

hasil = re.sub(r"(^|\n)(\d{1}\.)", r"\1a0aaaaa\2", teks)
hasil = re.sub(r"a0aaaaa", "0", hasil)

print("Hasil:")
print(hasil)