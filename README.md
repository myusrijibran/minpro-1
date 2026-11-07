# CAPSTONE-PBO-PRISMATV

## 1. Nama Program

**Prisma TV - Sistem Informasi Manajemen Program Televisi dan Penyiaran**

## 2. Deskripsi Singkat

Prisma TV merupakan aplikasi desktop berbasis Java yang dikembangkan untuk mengelola sistem operasional penyiaran stasiun televisi secara terstruktur. Aplikasi ini dirancang untuk menangani berbagai entitas utama penyiaran, mulai dari manajemen akun pengguna dengan hak akses bertingkat (Admin, Petugas Jadwal, Petugas Konten), pengelolaan data program televisi, kanal penyiaran, pencatatan mitra kerja sama, pengolahan konten digital beserta lampirannya, hingga penyusunan jadwal penyiaran harian.

Dalam pembangunannya, proyek ini menerapkan arsitektur **Model-View-Controller (MVC)** yang dipadukan dengan pola **DAO (Data Access Object)** untuk memisahkan lapisan antarmuka, logika bisnis, dan interaksi basis data. Koneksi ke database MySQL ditangani secara terpusat menggunakan JDBC dengan dependensi `mysql-connector-j` versi `8.4.0` via Apache Maven, sementara antarmuka grafisnya dibangun menggunakan komponen **Java Swing (GUI Builder NetBeans)**.

## 3. Fitur Utama Program

### 3.1 Autentikasi dan Login Berbasis Role (`LoginController` & `PenggunaDAO`)
- Pengguna memasukkan *username* dan *password* melalui form login interaktif.
- Sistem mengecek kredensial ke database menggunakan `PenggunaDAO.login()`. Jika data valid dan akun berstatus aktif, sistem membaca peran (*role*) pengguna secara polimorfik dan mengarahkan ke menu utama yang sesuai (Admin, Petugas Jadwal, atau Petugas Konten).
- Jika input kosong atau salah, form menampilkan pesan peringatan berwarna merah secara langsung melalui komponen `lblPesan` tanpa menutup aplikasi.

### 3.2 Manajemen Akun dan Hak Akses Pengguna (`Admin`)
- Admin memiliki hak penuh untuk mengelola data akun pengguna di dalam sistem.
- Mendukung pengelolaan tabel turunan pengguna seperti `Admin`, `PetugasJadwal`, dan `PetugasKonten` yang masing-masing membawa atribut spesifik penugasan.

### 3.3 Pengelolaan Program Televisi (`ProgramTV`)
- Mengelola data katalog program siaran televisi.
- Pencatatan meliputi nama program, kategori program, URL streaming/informasi, status program aktif/non-aktif, serta relasi kepemilikan data yang dikontrol oleh Admin.

### 3.4 Pengelolaan Kanal dan Mitra Kerja Sama (`Kanal` & `Mitra`)
- Mencatat daftar kanal siaran berdasarkan platform dan jenis medianya.
- Mengelola data perusahaan atau instansi mitra kerja sama, jenis kontrak, status kemitraan, alamat email, hingga nilai kontrak kerja sama.

### 3.5 Manajemen Konten, Lampiran, dan Publikasi (`Konten`)
- Petugas Konten dapat mencatat, menyusun, dan mengelola materi konten siaran.
- Dilengkapi dengan fitur pengelolaan lampiran berkas konten (`LampiranKonten`) serta penjadwalan publikasi konten ke kanal siaran tertentu (`PublikasiKonten`).

### 3.6 Penjadwalan Tayang Siaran (`JadwalTayang`)
- Petugas Jadwal dapat menyusun waktu mulai, waktu selesai, tanggal tayang, dan status jadwal penyiaran suatu program pada kanal tertentu secara spesifik.

### 3.7 Monitor Data dan Manajemen Sesi (`SesiLogin`)
- Menyediakan menu pemantauan data secara global (*read-only*) untuk meninjau informasi program, konten, jadwal, dan mitra.
- Sesi pengguna aktif dikelola secara aman melalui class `SesiLogin`, di mana pengguna dapat melakukan *logout* untuk mengakhiri sesi dan kembali ke halaman login.

## 4. Tech Stack

| Komponen | Teknologi | Kegunaan pada Prisma TV |
|---|---|---|
| Bahasa pemrograman | Java | Membangun seluruh logika berorientasi objek, entitas data, dan pengendali aplikasi. |
| Database | MySQL / MariaDB | Menyimpan tabel relasional (`pengguna`, `program_tv`, `kanal`, `mitra`, dll). |
| Koneksi database | JDBC (Java Database Connectivity) | Menghubungkan class `Koneksi` Java ke server database MySQL lokal. |
| Database driver | MySQL Connector/J (`8.4.0`) | Driver resmi yang diunduh via Maven untuk menjembatani komunikasi Java dan MySQL. |
| GUI | Java Swing (NetBeans GUI Builder) | Membangun antarmuka desktop (`login.java`, form menu, tabel data, tombol interaktif). |
| Build tool | Apache Maven | Mengatur dependensi proyek, versi Java, dan proses *build* aplikasi. |

## 5. Perancangan Sistem

### 5.1 Flowchart

Flowchart digunakan untuk menjelaskan alur proses aplikasi dari awal dijalankan sampai fitur digunakan oleh masing-masing *role* (Admin, Petugas Jadwal, Petugas Konten).

<details>
<summary><b>Flowchart menu utama</b></summary>
<img width="827" height="454" alt="image" src="https://github.com/user-attachments/assets/d0004fc0-dc22-43a9-a6e8-ddedb31a8cce" />

![Flowchart menu utama](Gambar/flowchart-menu utama.png)

</details>

<details>
<summary><b>Flowchart monitor data</b></summary>
<img width="584" height="1225" alt="image" src="https://github.com/user-attachments/assets/8f11cbb9-d711-4890-a380-49142c2813be" />

![Flowchart monitor data](Gambar/flowchart-monitor data.png)

</details>

<details>
<summary><b>Flowchart Menu Admin</b></summary>
<img width="455" height="701" alt="image" src="https://github.com/user-attachments/assets/8cecfd25-91f5-4fec-a19b-65c8cfda8350" />

![Flowchart Menu Admin](Gambar/flowchart-Menu Admin.png)

</details>

<details>
<summary><b>Flowchart Admin – Menu Program </b></summary>
<img width="827" height="612" alt="image" src="https://github.com/user-attachments/assets/348346e6-3864-426f-901b-92ff96194347" />

![Flowchart Admin – Menu Program ](Gambar/flowchart-Admin – Menu Program l.png)

</details>

<details>
<summary><b>Flowchart Admin  Menu Mitra </b></summary>

<img width="825" height="528" alt="image" src="https://github.com/user-attachments/assets/e7c5503a-e8f0-4f62-b10d-fba48f0f956f" />

![Flowchart Admin - Menu Mitra ](Gambar/flowchart-Admin  Menu Mitra .png)

</details><details>
<summary><b>Flowchart Admin - Menu Kerja Sama </b></summary>

<img width="826" height="518" alt="image" src="https://github.com/user-attachments/assets/7576dd37-5f03-4961-8526-0cc919f3318d" />

![Flowchart Admin - Menu Kerja Sama ](Gambar/flowchart Admin - Menu Kerja Sama .png)

</details><details>
<summary><b>Flowchart Admin - Menu Kanal </b></summary>

<img width="826" height="492" alt="image" src="https://github.com/user-attachments/assets/97ba21dc-bf72-4f58-9348-91cf0c4c07b1" />

![Flowchart Admin - Menu Kanal ](Gambar/Admin - Menu Kanal .png)

</details><details>
<summary><b>Flowchart Menu Petugas Konten </b></summary>

<img width="515" height="652" alt="image" src="https://github.com/user-attachments/assets/e8890f0e-dc00-4b38-8d2e-307daccba867" />

![Flowchart Menu Petugas Konten ](Gambar/Menu Petugas Konten .png)

</details><details>
<summary><b>Flowchart Petugas Konten - Menu Konten </b></summary>

<img width="826" height="624" alt="image" src="https://github.com/user-attachments/assets/c4edc0c9-46a3-43b0-a7c1-0005b6496ee0" />

![Flowchart Petugas Konten - Menu Konten](Gambar/Petugas Konten - Menu Konten.png)

</details><details>
<summary><b>Flowchart Petugas Konten - Menu Publikasi</b></summary>

<img width="826" height="600" alt="image" src="https://github.com/user-attachments/assets/ee50b66e-59eb-4e0b-811e-ec9f1e8a7a92" />

![Flowchart Petugas Konten - Menu Publikasi](Gambar/Petugas Konten - Menu Publikasi.png)

</details><details>
<summary><b>Flowchart Petugas Jadwal - Menu Jadwal </b></summary>

<img width="708" height="552" alt="image" src="https://github.com/user-attachments/assets/7141df46-c595-4128-980a-c75a17af0903" />

![Flowchart Petugas Jadwal  Menu Jadwal ](Gambar/Petugas Jadwal  Menu Jadwal .png)
</details>


### 5.2 Use Case Diagram


<img width="741" height="935" alt="image" src="https://github.com/user-attachments/assets/ba5d9f83-0431-41ed-870c-15adc686d57e" />



Use Case Diagram menggambarkan interaksi aktor dengan sistem Prisma TV:

- **Admin:** Melakukan login, mengelola akun pengguna, mengontrol data program TV, kanal, mitra, dan kerja sama.
- **Petugas Konten:** Melakukan login, mencatat dan mengelola konten siaran, lampiran file, serta publikasi konten.
- **Petugas Jadwal:** Melakukan login, menyusun, mengubah, dan memantau jadwal tayang program pada kanal siaran.

### 5.3 Entity Relationship Diagram (ERD)

<img width="1593" height="1064" alt="ERD LOGICAL PRISMA" src="https://github.com/user-attachments/assets/9745e123-7b77-435a-be71-06c4f37a38f0" />

<img width="1458" height="1008" alt="ERD RELATIONAL PRISMA" src="https://github.com/user-attachments/assets/97d8f2c1-6576-426f-b692-7b7a1ad419df" />


ERD mendefinisikan relasi tabel dalam database `prisma`, yang menghubungkan entitas induk `pengguna` dengan tabel turunan (`admin`, `petugas_jadwal`, `petugas_konten`), serta relasi transaksional ke tabel `program_tv`, `kanal`, `mitra`, `kerja_sama`, `konten`, `lampiran_konten`, `publikasi_konten`, dan `jadwal_tayang`.

## 6. Struktur Folder/Package

Proyek ini dibangun menggunakan struktur 5 *package* Maven untuk menerapkan prinsip pemisahan tanggung jawab (*Separation of Concerns*):

```text
src/main/java/
 ├── main/
 │    └─ Main.java
 ├── model/
 │    ├─ Pengguna.java (Abstract Class)
 │    ├─ Admin.java
 │    ├─ PetugasJadwal.java
 │    ├─ PetugasKonten.java
 │    └─ [Entitas Lain: ProgramTV.java, Kanal.java, Mitra.java, dll]
 ├── model.dao/
 │    ├─ Koneksi.java
 │    ├─ DAO.java (Interface)
 │    └─ [Implementasi DAO: PenggunaDAO.java, ProgramTVDAO.java, dll]
 └── controller/
      ├─ BaseController.java (Abstract Class)
      ├─ SesiLogin.java
      ├─ LoginController.java
      └─ [Controller Fitur Lainnya]
 └── view/
      ├─ login.java (Java Swing GUI Form)
      ├─ [Form Swing Lainnya: FormMenuAdmin.java, dll]
      ├─ TabelHelper.java
      └─ FormHelper.java
```

Penjelasan Package Berdasarkan Implementasi Nyata
main

File Utama: Main.java

Penjelasan: Berfungsi sebagai titik masuk (entry point) aplikasi. Method di Main.java langsung mengeksekusi jendela form login pertama melalui baris new login().setVisible(true);.

model

File Utama: Pengguna.java, Admin.java, ProgramTV.java, dll.

Penjelasan: Menampung struktur entitas data murni (POJO) dan abstract class induk. Class di package ini sama sekali tidak memuat query SQL, murni hanya merepresentasikan kolom-kolom tabel database ke dalam atribut objek Java.

model.dao

File Utama: Koneksi.java, DAO.java, PenggunaDAO.java, dll.

Penjelasan: Pusat penanganan komunikasi basis data. Class Koneksi.java menggunakan JDBC DriverManager.getConnection("jdbc:mysql://localhost:3308/prisma", ...) untuk menghubungkan aplikasi ke database prisma. Seluruh query SQL dieksekusi di dalam class implementasi DAO seperti PenggunaDAO.java.

controller

File Utama: LoginController.java, SesiLogin.java, dll.

Penjelasan: Menjadi jembatan logika antara View dan Model. Contohnya, LoginController.java menerima parameter input teks dari login.java, memvalidasi kekosongan teks, lalu memanggil PenggunaDAO.login() dan menyimpan sesi aktif ke SesiLogin.java.

view

File Utama: login.java, TabelHelper.java, FormHelper.java

Penjelasan: Berisi antarmuka visual (JFrame Form) yang dibuat melalui NetBeans GUI Builder. Dilengkapi dengan class utilitas pendukung seperti TabelHelper.java untuk mempermudah pengisian data ke dalam JTable.

## 7. Penerapan 4 Pilar OOP (Disertai Contoh Kode Riil Program)

### 7.1 Encapsulation (Enkapsulasi)
Penerapan dalam Prisma TV: Seluruh atribut pada class entitas (seperti username, password, namaLengkap) disembunyikan menggunakan access modifier private. Akses baca dan tulis mutlak dikendalikan melalui method getter dan setter publik.

Contoh pada kode (model.Pengguna.java):

```
public abstract class Pengguna {
    private int idPengguna;
    private String username; // Atribut diproteksi dengan private

    public String getUsername() { 
        return username; 
    }
    public void setUsername(String username) { 
        this.username = username; 
    }
}
```

### 7.2 Inheritance (Pewarisan)
Penerapan dalam Prisma TV: Diterapkan pada hierarki pengguna aplikasi. Class Admin, PetugasJadwal, dan PetugasKonten bertindak sebagai subclass yang mewarisi seluruh atribut umum serta constructor dari superclass abstract Pengguna menggunakan keyword extends dan super().

Contoh pada kode (model.Admin.java):

```
public class Admin extends Pengguna {
    private String tanggalPenugasan;

    public Admin(int idPengguna, String namaLengkap, String username, String password, String statusAkun, String tanggalPenugasan) {
        super(idPengguna, namaLengkap, username, password, statusAkun); // Mewarisi konstruktor induk
        this.tanggalPenugasan = tanggalPenugasan;
    }
}
```

### 7.3 Polymorphism (Polimorfisme)
Penerapan dalam Prisma TV: Diterapkan melalui mekanisme method overriding pada fungsi getRole(). Setiap subclass pengguna mengimplementasikan ulang method ini dengan mengembalikan teks peran yang spesifik, sehingga objek bertipe Pengguna dapat menghasilkan perilaku dinamis saat dipanggil di controller.

Contoh pada kode (Admin.java vs PetugasJadwal.java):

```
Java
// Di dalam Admin.java:
@Override
public String getRole() { return "Admin"; }

// Di dalam PetugasJadwal.java:
@Override
public String getRole() { return "Petugas Jadwal"; }
```

### 7.4 Abstraction (Abstraksi)
Penerapan dalam Prisma TV: Diterapkan melalui abstract class (Pengguna, BaseController) dan interface generik DAO<T>. Interface ini menetapkan standar baku operasi CRUD (tambah, ubah, hapus, getSemua, cari) yang wajib dipatuhi oleh seluruh class DAO tanpa membocorkan detail perintah SQL ke lapisan tampilan.

Contoh pada kode (model.dao.DAO.java):

```
Java
public interface DAO<T> {
    void tambah(T entity);
    void ubah(T entity);
    void hapus(int id);
    List<T> getSemua();
    List<T> cari(String keyword);
}
```
