# TAHAP I
# ===============================================================================
# INISIALISASI & KONFIGURASI JENDELA UTAMA (GUI)
# ======= 1. Memanggil Pustaka Tkinter
import tkinter as tk

# ======= 2. Membuat Custom Variable jendela Utama Aplikasi
layar_utama = tk.Tk()

# ======= 3. Mengatur Atribut Jendela Aplikasi (Judul,Ukuran, dan Warna Baground)
layar_utama.title("kalkulator")
layar_utama.geometry("350x500")
layar_utama.configure(bg="#17171c")
#================================================================================

# TAHAP 2
#================================================================================
# DEKLARASI VARIABLEB PEMPROSES DATA
# Membuat Memeori Papan Hitung Sebagai Memori Penyimpan input String angka/operator
papan_hitung = ""
#================================================================================

# TAHAP 3
#================================================================================
#PEMBUATAN FUNGSI LOGIKA (DUMMY / SEMENTARA)
#Fungsi dikosongkan dengan 'pass' agar tombol yang akan dibuat bisa merujuk kefungsi ini
# ======= 1. Fungsi dummy untuk angka & operator
def_tekan_tombol(num):
   global papan_hitung
   papan_hitung = papan_hitung + str(num)
   string_tampilan.set(papan_hitung)

# ======= 2. Fungsi dummy untuk tombol sama dengan(=)
def hitung():
    global papan_hitung
    try:
      # Mengganti karakter visual menjadi operator python sebelum di hitung 
      total = str(eval(papan_hitung.replace)('x', '*').replace('','/').replace(',', '.')))
      string_tampilan.set(total)
      papan_hitung = total
    except:
      string_tampilan.set(total)
      papan_hitung = ""

# ======= 3. Fungsi dummy untuk tombol reset (c)
def hapus_semua():
    global papan_hitung
    papan_hitung = ""
    string_tampilan.set("")
# ==================================================================================

# TAHAP 4 
# ==================================================================================
# PEMBUATAN LAYAR TAMPILAN PAPAN ANGKA DAN OPERATOR
# ======= 1. membuat variable Tkinter untuk sinkronisasi teks pada komponen entry
string_tampilan = tk.StringVar()

# ======= 2. membuat komponen widget entry unutuk layar kalkulator
layar = tk.Entry(
  layar_utama,
  textvariable=string_tampilan,
  font=("helvetica", 36)
  bd=0,
  bg="#fafefa",
  fg="black"
  justify="right"
)
layar.pack(fill="both", ipadx=10, ipady=30, padx=10, pady=10)
# ===================================================================================

#  TAHAP 5 
# ===================================================================================
# PEMBUATAN DAN KONFIGURASI WIDGET FRAME TOMBOL
# ======= 1. Membuat frame khusus sebagai tempat melatakan susunan tombol
frame_tombol = tk.Frame(layar_utama, bg="#f6fbf7")
frame_tombol.pack(fill="both", expand=True, padx=10, pady=10,)
 
# ======= 2. Konfigurasi grid layout agar ukuran tombol bisa membesar/mengecil secara proporsional
for i in range(5):
   frame_tombol.rowconfigure(i, weight=1)
for i in range(4):
   frame_tombol.columconfigure(i, weight=1)
# ===================================================================================

# TAHAP 6
# ===================================================================================
# DESAIN DATA & RENDERING TOMBOL (GRID SYSTEM)
# ======= 1. pemetaan data konfigurasi tombol
# susunan data (Teks, Baris (row), Kolom (colum), Warna Bg, Warna Fg, Fungsi/Aksi)
tombol_config = [
   ('c', 0, 0, '#a5a5a5', 'black', hapus_semua),
   ('+/-', 0, 1, '#a5a5a5', 'black', lambda: tekan_tombol('-')),
   ('%', 0, 2, '#a5a5a5' 'black' lambda: tekan_tombol('/100')),
   ('÷', 0, 3, '#ff9f0a', 'white', lambda: tekan_tombol('÷')),

   ('1', 1, 0, '#333333', 'white', lambda: tekan_tombol('1')),
   ('2', 1, 1, '#333333', 'white', lambda: tekan_tombol('2')),
   ('3', 1, 2, '#333333', 'white', lambda: tekan_tombol('3')),
   ('x', 1, 3, '#ff9f0a', 'white', lambda: tekan_tombol('x')),

   ('4', 2, 0, '#333333', 'white', lambda: tekan_tombol('4')),
   ('5', 2, 1, '#333333', 'white', lambda: tekan_tombol('5')),
   ('6', 2, 2, '#333333', 'white', lambda: tekan_tombol('6')),
   ('-', 2, 3, '#ff9f0a', 'white', lambda: tekan_tombol('-')),
   


]







