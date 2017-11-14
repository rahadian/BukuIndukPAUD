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
class Core():
	def dbase(self):
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
		print "Done"
		

info()
print "1.Tambah Peserta Didik Baru"
print "2.Edit Peserta Didik"
print "3.Exit"

z=raw_input("Apa yang ingin anda lakukan ?:")
z=int(z)
core=Core()
if z == 1:
	core.dbase()
elif z == 2:
	cursor.execute("SELECT no,nama from Daftar_Peserta_Didik")
	#row = cursor.fetchall()
	row = list (cursor.fetchall())
	for kol in row:
		print (str(kol[0])+" "+str(kol[1]))
	choice=raw_input("Apakah anda akan mengedit data?:[y/n]")
	if choice == "y":
		row = list (cursor.fetchall())
		for kol in row:
			print (str(kol[0])+" "+str(kol[1]))
		noedit=raw_input("Masukkan no. data yang akan diedit: ")
		print "=================================================="
		data=["1.Nama","2.Jenis kelamin","3.NIS","4.NISN","5.Rombel","6.Tempat lahir","7.Tgl lahir","8.NIK","9.Agama","10.Anak Berkebutuhan khusus(Ya/Tidak)","11.Alamat","12.RT","13.RW","14.Dusun","15.Kelurahan","16.Kecamatan","17.Kode pos","18.Jenis tinggal","19.Alat Transportasi","20.Tlp atau HP","21.Email","22.SKHUN","23.Penerima KPS(Ya/Tidak)","24.No KPS","25.Nama Ayah","26.Tahun lahir ayah","27.Jenjang pendidikan ayah","28.Pekerjaan ayah","29.Penghasilan ayah","30.Ayah berkebutuhan khusus(Ya/Tidak)","31.Nama ibu","32.Tahun lahir ibu","33.Jenjang pendidikan ibu","34.Pekerjaan ibu","35.Penghasilan ibu","36.Ibu berkebutuhan khusus(Ya/Tidak)","37.Nama wali","38.Tahun lahir wali","39.Jenjang pendidikan wali","40.Pekerjaan wali","41.Penghasilan wali","42.Cancel"]
		print "\n".join("%-50s %s"%(data[kol],data[kol+len(data)/2])
			for kol in range(len(data)/2))
		while True:
			dt=raw_input("Masukkan nomor jenis data yang akan diedit: ")
			dt=int(dt)
			if dt==1:
				namaedit=raw_input(a)
				cursor.execute("UPDATE Daftar_Peserta_Didik SET nama=%s, last_update=%s WHERE no=%s",(namaedit,now,noedit))
				db.commit()
				print "Done"
			elif dt==2:
				jkedit=raw_input(b)
				cursor.execute("UPDATE Daftar_Peserta_Didik SET jenis_kelamin=%s, last_update=%s WHERE no=%s",(jkedit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==3:
				nisedit=raw_input(c)
				cursor.execute("UPDATE Daftar_Peserta_Didik SET NIS=%s, last_update=%s WHERE no=%s",(nisedit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==4:
				nisnedit=raw_input("NISN: ")
				cursor.execute("UPDATE Daftar_Peserta_Didik SET NISN=%s , last_update=%s WHERE no=%s",(nisnedit,now,noedit))
				db.commit()
				print "Done"

			elif dt==5:
				rombeledit=raw_input("Rombel: ")
				cursor.execute("UPDATE Daftar_Peserta_Didik SET rombel=%s, last_update=%s WHERE no=%s",(rombeledit,now,noedit))
				db.commit()
				print "Done"
					
			elif dt==6:
				tmplahiredit=raw_input(d)
				cursor.execute("UPDATE Daftar_Peserta_Didik SET tempat_lahir=%s, last_update=%s WHERE no=%s",(tmplahiredit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==7:
				tgllahiredit=raw_input(e)
				cursor.execute("UPDATE Daftar_Peserta_Didik SET tgl_lahir=%s, last_update=%s WHERE no=%s",(tgllahiredit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==8:
				nikedit=raw_input(f)
				cursor.execute("UPDATE Daftar_Peserta_Didik SET NIK=%s, last_update=%s WHERE no=%s",(nikedit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==9:
				agamaedit=raw_input(g)
				cursor.execute("UPDATE Daftar_Peserta_Didik SET agama=%s, last_update=%s WHERE no=%s",(agamaedit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==10:
				kebkhusedit=raw_input(h)
				cursor.execute("UPDATE Daftar_Peserta_Didik SET kebutuhan_khusus=%s, last_update=%s WHERE no=%s",(kebkhusedit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==11:
				alamatedit=raw_input(i)
				cursor.execute("UPDATE Daftar_Peserta_Didik SET alamat=%s, last_update=%s WHERE no=%s",(alamatedit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==12:
				rtedit=raw_input("RT: ")
				cursor.execute("UPDATE Daftar_Peserta_Didik SET rt=%s, last_update=%s WHERE no=%s",(rtedit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==13:
				rwedit=raw_input("RW: ")
				cursor.execute("UPDATE Daftar_Peserta_Didik SET rw=%s, last_update=%s WHERE no=%s",(rwedit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==14:
				dusunedit=raw_input("Dusun: ")
				cursor.execute("UPDATE Daftar_Peserta_Didik SET dusun=%s, last_update=%s WHERE no=%s",(dusunedit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==15:
				keledit=raw_input("Kelurahan: ")
				cursor.execute("UPDATE Daftar_Peserta_Didik SET kelurahan=%s, last_update=%s WHERE no=%s",(keledit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==16:
				kecedit=raw_input("Kecamatan: ")
				cursor.execute("UPDATE Daftar_Peserta_Didik SET kec=%s, last_update=%s WHERE no=%s",(kecedit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==17:
				kodposedit=raw_input("Kode Pos: ")
				cursor.execute("UPDATE Daftar_Peserta_Didik SET kode_pos=%s, last_update=%s WHERE no=%s",(kodposedit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==18:
				tinggaledit=raw_input("Jenis Tinggal: ")
				cursor.execute("UPDATE Daftar_Peserta_Didik SET jenis_tinggal=%s , last_update=%sWHERE no=%s",(tinggaledit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==19:
				transedit=raw_input("Alat Transportasi: ")
				cursor.execute("UPDATE Daftar_Peserta_Didik SET alat_transportasi=%s, last_update=%s WHERE no=%s",(transedit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==20:
				hpedit=raw_input("Nomor Telepon atau HP: ")
				cursor.execute("UPDATE Daftar_Peserta_Didik SET tlp_hp=%s, last_update=%s WHERE no=%s",(hpedit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==21:
				mailedit=raw_input("Email: ")
				cursor.execute("UPDATE Daftar_Peserta_Didik SET email=%s , last_update=%s WHERE no=%s",(mailedit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==22:
				skhunedit=raw_input("SKHUN: ")
				cursor.execute("UPDATE Daftar_Peserta_Didik SET SKHUN=%s, last_update=%s WHERE no=%s",(skhunedit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==23:
				kpsedit=raw_input("Penerima KPS:(Ya/Tidak)")
				cursor.execute("UPDATE Daftar_Peserta_Didik SET penerima_KPS=%s , last_update=%s  WHERE no=%s",(kpsedit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==24:
				nokpsedit=raw_input("Nomor KPS: ")
				cursor.execute("UPDATE Daftar_Peserta_Didik SET no_KPS=%s, last_update=%s  WHERE no=%s",(nokpsedit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==25:
				nmayahedit=raw_input(j)
				cursor.execute("UPDATE Daftar_Peserta_Didik SET nama_ayah=%s, last_update=%s  WHERE no=%s",(nmayahedit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==26:
				thnayahedit=raw_input(k)
				cursor.execute("UPDATE Daftar_Peserta_Didik SET thn_lahir_ayah=%s, last_update=%s  WHERE no=%s",(thnayahedit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==27:
				pendayahedit=raw_input(l)
				cursor.execute("UPDATE Daftar_Peserta_Didik SET jenjang_pendidikan_ayah=%s, last_update=%s  WHERE no=%s",(pendayahedit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==28:
				pekayahedit=raw_input(m)
				cursor.execute("UPDATE Daftar_Peserta_Didik SET pekerjaan_ayah=%s, last_update=%s  WHERE no=%s",(pekayahedit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==29:
				pengayahedit=raw_input(n)
				cursor.execute("UPDATE Daftar_Peserta_Didik SET penghasilan_ayah=%s, last_update=%s  WHERE no=%s",(pengayahedit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==30:
				kebkhusayahedit=raw_input(o)
				cursor.execute("UPDATE Daftar_Peserta_Didik SET kebutuhan_khusus_ayah=%s, last_update=%s  WHERE no=%s",(kebkhusayahedit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==31:
				nmibuedit=raw_input(p)
				cursor.execute("UPDATE Daftar_Peserta_Didik SET nama_ibu=%s, last_update=%s  WHERE no=%s",(nmibuedit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==32:
				thnibuedit=raw_input(q)
				cursor.execute("UPDATE Daftar_Peserta_Didik SET thn_lahir_ibu=%s, last_update=%s  WHERE no=%s",(thnibuedit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==33:
				pendibuedit=raw_input(r)
				cursor.execute("UPDATE Daftar_Peserta_Didik SET jenjang_pendidikan_ibu=%s, last_update=%s  WHERE no=%s",(pendibuedit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==34:
				pekibuedit=raw_input(s)
				cursor.execute("UPDATE Daftar_Peserta_Didik SET pekerjaan_ibu=%s, last_update=%s  WHERE no=%s",(pekibuedit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==35:
				pengibuedit=raw_input(t)
				cursor.execute("UPDATE Daftar_Peserta_Didik SET penghasilan_ibu=%s, last_update=%s  WHERE no=%s",(pengibuedit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==36:
				kebkhusibuedit=raw_input(u)
				cursor.execute("UPDATE Daftar_Peserta_Didik SET kebutuhan_khusus_ibu=%s, last_update=%s  WHERE no=%s",(kebkhusibuedit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==37:
				nmawaliedit=raw_input("Nama Wali: ")
				cursor.execute("UPDATE Daftar_Peserta_Didik SET nama_wali=%s, last_update=%s  WHERE no=%s",(nmawaliedit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==38:
				thnwaliedit=raw_input(v)
				cursor.execute("UPDATE Daftar_Peserta_Didik SET thn_lahir_wali=%s, last_update=%s  WHERE no=%s",(thnwaliedit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==39:
				pendwaliedit=raw_input("Jenjang Pendidikan Wali: ")
				cursor.execute("UPDATE Daftar_Peserta_Didik SET jenjang_pendidikan_wali=%s, last_update=%s  WHERE no=%s",(pendwaliedit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==40:
				pekwaliedit=raw_input("Pekerjaan Wali: ")
				cursor.execute("UPDATE Daftar_Peserta_Didik SET pekerjaan_wali=%s, last_update=%s  WHERE no=%s",(pekwaliedit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==41:
				pengwaliedit=raw_input("Penghasilan Wali: ")
				cursor.execute("UPDATE Daftar_Peserta_Didik SET penghasilan_wali=%s, last_update=%s  WHERE no=%s",(pengwaliedit,now,noedit))
				db.commit()
				print "Done"
				
			elif dt==42:
				print "Canceled"
				exit()
			else:
				print "Maaf inputan angka salah,try again"
		

elif z == 3:
	exit()
else:
	print "Command not found"
	exit()
db.close()


