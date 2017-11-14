import MySQLdb
from datetime import datetime
now = datetime.now()
red = "\033[01;31m{0}\033[00m"
grn = "\033[01;36m{0}\033[00m"
merah = red.format("MERAH")
wajib = red.format("WAJIB DIISI")
a = red.format("Nama: ")
b = red.format("Jenis Kelamin: ")
c = red.format("NIS: ")
d = red.format("Tempat Lahir: ")
e = red.format("Tanggal Lahir: ")
f = red.format("NIK: ")
g = red.format("Agama: ")
h = red.format("Kebuhtuhan Khusus(Ya/Tidak): ")
i = red.format("Alamat: ")
j = red.format("Nama Ayah: ")
k = red.format("Tahun Lahir Ayah: ")
l = red.format("Jenjang Pendidikan Ayah: ")
m = red.format("Pekerjaan Ayah: ")
n = red.format("Penghasilan Ayah: ")
o = red.format("Ayah Berkebutuhan Khusus:(Ya/Tidak): ")
p = red.format("Nama Ibu: ")
q = red.format("Tahun Lahir Ibu: ")
r = red.format("Jenjang Pendidikan Ibu: ")
s = red.format("Pekerjaan Ibu: ")
t = red.format("Penghasilan Ibu: ")
u = red.format("Ibu Berkebutuhan Khusus:(Ya/Tidak): ")
v = red.format("Tahun Lahir Wali: ")
nol = red.format("0000")
tgl = red.format("YYYY-MM-DD")
db = MySQLdb.connect(host="localhost",user="root",passwd="toor",db="Buku_Induk")
cursor = db.cursor()
def info():
	print red.format("==============================================================")
	print grn.format("BUKU INDUK DAFTAR PESERTA DIDIK PAUD FAJAR ARRY MULIA")
	print red.format("==============================================================")
	print red.format("PERHATIAN !!!!!")
	print wajib+" untuk kolom tulisan berwarna "+merah
	print "Untuk pengisian Tahun Kelahiran jika dirasa tidak mengetahui cukup dengan mengisikan dengan format "+nol
	print "Untuk pengisian Tanggal Kelahiran dengan format "+tgl
	print grn.format("==============================================================================================")
info()
cursor.execute("INSERT INTO Daftar_Peserta_Didik (nama,jenis_kelamin,NIS,NISN,rombel,tempat_lahir,tgl_lahir,NIK,agama,kebutuhan_khusus,alamat,rt,rw,dusun,kelurahan,kec,kode_pos,jenis_tinggal,alat_transportasi,tlp_hp,email,SKHUN,penerima_KPS,no_KPS,nama_ayah,thn_lahir_ayah,jenjang_pendidikan_ayah,pekerjaan_ayah,penghasilan_ayah,kebutuhan_khusus_ayah,nama_ibu,thn_lahir_ibu,jenjang_pendidikan_ibu,pekerjaan_ibu,penghasilan_ibu,kebutuhan_khusus_ibu,nama_wali,thn_lahir_wali,jenjang_pendidikan_wali,pekerjaan_wali,penghasilan_wali,last_update)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
(raw_input(a),
raw_input(b),
raw_input(c),
raw_input("NISN: "),
raw_input("Rombel: "),
raw_input(d),
raw_input(e),
raw_input(f),
raw_input(g),
raw_input(h),
raw_input(i),
raw_input("RT: "),
raw_input("RW: "),
raw_input("Dusun: "),
raw_input("Kelurahan: "),
raw_input("Kecamatan: "),
raw_input("Kode Pos: "),
raw_input("Jenis Tinggal: "),
raw_input("Alat Transportasi: "),
raw_input("Nomor Telepon atau HP: "),
raw_input("Email: "),
raw_input("SKHUN: "),
raw_input("Penerima KPS:(Ya/Tidak)"),
raw_input("Nomor KPS: "),
raw_input(j),
raw_input(k),
raw_input(l),
raw_input(m),
raw_input(n),
raw_input(o),
raw_input(p),
raw_input(q),
raw_input(r),
raw_input(s),
raw_input(t),
raw_input(u),
raw_input("Nama Wali: "),
raw_input(v),
raw_input("Jenjang Pendidikan Wali: "),
raw_input("Pekerjaan Wali: "),
raw_input("Penghasilan Wali: "),
now))
db.commit()
db.close()
