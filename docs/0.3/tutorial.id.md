---
layout: default
title: Tutorial web.py 0.3
---

# Tutorial

Bahasa Lain : [Inggris](/docs/0.3/tutorial) | [China 简体中文](/docs/0.3/tutorial.zh-cn) | [Perancis](/docs/0.3/tutorial.fr) | ...

## Ringkasan

* [Memulai](#starting)
* [Penanganan URL](#urlhandling)
* [GET dan POST: perbedaannya](#getpost)
* [Memulai server](#start)
* [Menggunakan template](#templating)
* [Form](#forms)
* [Menggunakan database](#databasing)
* [Selama pengembangan](#developing)
* [Berikutnya?](#whatnext)

## Memulai

Jadi Anda mengerti Python dan ingin membuat sebuah website. web.py 
menyediakan kode untuk membuatnya mudah. 

Apabila Anda ingin mengikuti keseluruhan tutorial, Anda perlu 
menginstall Python, web.py, flup, psycopg2 dan PostgreSQL (atau 
database yang ekuivalen dan driver untuk Python). Lihatlah halaman <a 
href="/install">install</a> untuk detilnya. 

Mari kita mulai.

<a name="urlhandling"> </a>
## Penanganan URL

Bagian paling penting dari setiap website adalah struktur URL yang 
digunakan. URL yang Anda gunakan bukan saja merupakan sesuatu yang 
pengunjung Anda lihat dan email ke teman-temannya, namun juga 
merupakan model mental dari bagaimana website Anda bekerja. Pada 
website populer seperti [del.icio.us](http://del.icio.us/), URL bahkan 
merupakan bagian dari user interface. web.py memudahkan kita untuk 
membuat URL yang bagus. 

Untuk memulai aplikasi web.py Anda, buatlah file teks baru (mari kita 
beri nama `code.py`) dan ketikkan:

    import web

Ini akan mengimport modul web.py. 

Sekarang, kita perlu beri tahu web.py tentang struktur URL kita. Mari 
kita mulai dengan yang sederhana:

    urls = (
      '/', 'index'
    )

Bagian pertama merupakan [regular expressions](http://osteele.com/tools/rework/) yang cocok dengan sebuah 
URL, seperti `/`, `/help/faq`, `/item(\d+)` dan sebagainya (contoh: 
`\d+` akan cocok dengan deretan digit). Tanda kurung akan cocok dengan 
bagian dari data untuk dipergunakan nantinya. Bagian kedua merupakan 
nama class di mana request akan dikirim, seperti `index`, `view`, 
`welcomes.hello` (yang akan merujuk pada class `hello` dari modul 
`welcomes`),atau `get_\1`. `\1` akan digantikan dengan tangkapan 
pertama dari regular expression yang digunakan; tangkapan lainnya akan 
dilewatkan ke fungsi yang Anda buat. 

Baris ini menyatakan bahwa kita ingin agar URL `/` (contoh: halaman 
depan sebuah website) akan ditangani oleh class dengan nama `index`. 

<a name="getpost"> </a>
## GET dan POST: perbedaannya

Sekarang kita ingin menulis class `index`. Walau sebagian besar 
pengunjung tidak memperhatikan pada saat browsing, browser Anda 
mempergunakan bahasa yang dikenal sebagai HTTP untuk berkomunikasi 
dengan World Wide Web. Detilnya memang tidak penting, tapi pada 
dasarnya, pengunjung web meminta kepada web server untuk melakukan 
fungsi tertentu (seperti `GET` atau `POST`) pada URL (seperti `/` atau 
`/foo?f=1`). 

`GET`, yang kita kenal, akan meminta teks dari halaman web. Pada saat 
Anda mengetikkan `harvard.edu` di web browser Anda, browser tersebut 
akan meminta kepada web server Harvard untuk `GET /`. Yang kita kenal 
juga, `POST`, umum digunakan pada saat mengirimkan form-form tertentu, 
seperti pada saat berbelanja online. Anda menggunakan `POST` pada saat 
aksi dari pengiriman sebuah request akan _melakukan sesuatu_ (seperti 
charge kartu kredit atau memroses sebuah order). Perhatikanlah, karena 
URL `GET` dapat diindeks oleh search engine, yang mana umumnya Anda  
inginkan untuk sebagian besar halaman Anda, tapi _tidak_ Anda inginkan 
untuk hal-hal seperti memroses order (bayangkan jika Google mencoba 
untuk membeli segalanya di website Anda). 

Di dalam kode web.py kita, kita bedakan dengan jelas antara keduanya:

    class index:
        def GET(self):
            return "Hello, world!"

Fungsi `GET` akan dipanggil oleh web.py setiap saat seseorang membuat 
request `GET` untuk `/`. 

Sekarang kita perlu membuat sebuah aplikasi dengan menyatakan URL yang 
kita miliki dan meminta kepada web.py untuk memulai melayani halaman 
web:

    if __name__ == "__main__": 
        app = web.application(urls, globals())
        app.run()        

Pertama, kita meminta kepada web.py untuk membuat sebuah aplikasi 
dengan URL yang kita daftarkan di atas, dengan mencari class-class 
dari namespace global file ini. Dan, akhirnya, kita meminta web.py 
untuk menjalankan server untuk aplikasi yang kita buat sebelumnya. 

Perhatikanlah bahwa walaupun saya telah banyak berbicara, kita 
sebenarnya hanya memiliki lima baris kode. Itulah yang Anda perlukan 
untuk membuat sebuah aplikasi web.py yang lengkap. 

Untuk lebih mudahnya, berikut adalah kode lengkapnya:

    import web
    
    urls = (
        '/', 'index'
    )
    
    class index:
        def GET(self):
            return "Hello, world!"
    
    if __name__ == "__main__":
        app = web.application(urls, globals())
        app.run()

<a name="start"> </a>
## Memulai server

Apabila Anda ke command line dan mengetikkan:

    $ python code.py
    http://0.0.0.0:8080/

Maka aplikasi web.py Anda akan menjalankan sebuah web server 
sesungguhnya di komputer Anda. Kunjungilah URL tersebut dan seharusnya 
Anda akan melihat tulisan: "Hello, world!" (Anda dapat menambahkan 
alamat IP/port setelah "code.py" untuk mengontrol di mana web.py akan 
menjalankan server. Anda juga dapat memintanya untuk menjalankan 
server `fastcgi` atau `scgi`.)

**Catatan**: Anda dapat menentukan port yang ingin digunakan di command 
line seperti ini, jika Anda tidak dapat atau tidak ingin menggunakan 
nilai default:

    $ python code.py 1234


<a name="templating"> </a>
## Menggunakan template

Menulis HTML di dalam Python bisa menjadi merepotkan; lebih nyaman 
untuk menulis Python di dalam HTML. Untungnya, web.py membuatnya cukup 
mudah. 

Mari buat direktori untuk menyimpan template kita (kita berikan nama 
`templates`). Di dalamnya, buatlah file baru dengan nama diakhiri 
dengan HTML (kita berikan nama `index.html`). Sekarang, di dalam file 
tersebut, Anda dapat menulis HTML seperti biasanya:

    <em>Hello</em>, world!

Atau, Anda bisa gunakan bahasa template milik web.py untuk menambahkan 
kode ke dalam HTML Anda:

    $def with (name)
    
    $if name:
        I just wanted to say <em>hello</em> to $name.
    $else:
        <em>Hello</em>, world!

Seperti yang bisa Anda lihat, template sangat mirip dengan file Python 
kecuali dengan adanya statemen `def with` di awal file (menyatakan apa 
yang dilewatkan ke template) dan `$` yang ada di awal setiap kode. 
Saat ini, template.py mengharuskan statement `def with` merupakan 
baris pertama file. Perhatikanlah juga bahwa web.py secara otomatis 
akan mengescape setiap variabel yang digunakan di sini, sehingga 
apabila `name` diberikan nilai yang mengandung kode HTML tertentu, 
secara otomatis akan diescape dan tampil sebagai teks biasa. Apabila 
Anda ingin menonaktifkan fitur ini, gantilah `$name` dengan `$:name`. 

Sekarang, mari kembali ke `code.py`. Di bawah baris pertama, tambahkan:

    render = web.template.render('templates/')

Ini akan meminta web.py untuk mencari template ke dalam direktori 
`templates`. Kemudian, gantilah `index.GET` menjadi:

    name = 'Bob'    
    return render.index(name)

('index' adalah nama template dan 'name' merupakan argumen yang 
dilewatkan kepadanya)

Kunjungilah website Anda, yang harusnya akan menyapa hello kepada Bob. 

Tapi, katakanlah kita ingin agar pengunjung dapat memasukkan namanya 
sendiri. Gantilah dua baris yang kita tambahkan di atas dengan:

    i = web.input(name=None)
    return render.index(i.name)

Kunjungilah `/` dan harusnya, hello kepada dunia akan ditampilkan. 
Kunjungilah `/?name=Joe` dan harusnya, hello kepada Joe akan 
ditampilkan. 

Tentu saja, memiliki `?` tersebut di URL tidaklah cantik. Mari ganti 
definisi URL di bagian atas kode menjadi:

    '/(.*)', 'index'

Dan ganti definisi `index.GET` menjadi:

    def GET(self, name):
        return render.index(name)

Dan hapuslah baris yang mengatur name. Sekarang, kunjungilah `/Joe` 
dan harusnya, hello kepada Joe akan ditampilkan. 

Apabila Anda ingin belajar lebih lanjut tentang template, kunjungilah 
<a href="/docs/0.3/templetor">halaman templetor</a>.

<a name="forms"> </a>
## Form

Modul form dari web.py memungkinkan pembuatan form HTML, mendapatkan 
input dari user, dan melakukan validasi sebelum input diproses atau 
ditambahkan ke dalam database. Apabila Anda ingin belajar lebih lanjut 
tentang modul form web.py, bacalah [Dokumentasi](/docs/0.3) or 
kunjungilah link langsung ke [Pustaka Form](/form).

<a name="databasing"> </a>
## Menggunakan database

**Catatan:** Sebelum Anda dapat mulai menggunakan database, 
pastikanlah pustaka untuk mengakses database telah terinstall. Untuk 
database MySQL, gunakanlah 
[MySQLdb](http://sourceforge.net/project/showfiles.php?group_id=22307) 
dan untuk database PostgreSQL, gunakanlah [psycopg2](http://initd.org/pub/software/psycopg/).

Pertama, Anda perlu membuat objek database.

    db = web.database(dbn='postgres', user='username', pw='password', db='dbname')

(Sesuaikanlah -- terutama `username`, `password`, dan `dbname` -- 
dengan setup Anda. Pengguna MySQL juga perlu mengubah definisi `dbn` 
ke `mysql`.)

Ini adalah semua yang perlu Anda lakukan -- web.py secara otomatis 
akan menangani koneksi dan diskoneksi dari database. 

Pada interface admin dari engine database yang Anda gunakan, buatlah sebuah 
tabel sederhana di dalam database Anda:

    CREATE TABLE todo (
      id serial primary key,
      title text,
      created timestamp default now(),
      done boolean default 'f'    );

Dan tambahkan sebuah baris:

    INSERT INTO todo (title) VALUES ('Learn web.py');

Kembalilah mengedit `code.py` dan gantilah `index.GET` menjadi nilai 
berikut, menimpa seluruh isi fungsi sebelumnya: 

    def GET(self):
        todos = db.select('todo')
        return render.index(todos)

Dan gantilah handler URL untuk hanya menerima `/` seperti berikut:

    '/', 'index',

Edit dan gantilah keseluruhan isi `index.html` sehingga menjadi 
berikut:

    $def with (todos)
    <ul>
    $for todo in todos:
        <li id="t$todo.id">$todo.title</li>
    </ul>

Kunjungilah kembali website Anda dan Anda harusnya akan melihat sebuah 
item todo: "Learn web.py". Selamat! Anda telah membuat sebuah aplikasi 
lengkap yang membaca dari database. Sekarang, mari kita membuatnya 
dapat juga menulis ke database. 

Pada bagian akhir dari `index.html`, tambahkanlah:

    <form method="post" action="add">
    <p><input type="text" name="title" /> <input type="submit" value="Add" /></p>
    </form>

Dan gantilah definisi URL menjadi:

    '/', 'index',
    '/add', 'add'

(Hati-hatilah dengan koma-koma yang ada. Apabila Anda tidak 
menuliskannya, Python akan menggabungkan semuanya sehingga menjadi 
`'/index/addadd'` dan bukannya daftar URL Anda!)

Sekarang, tambahkanlah class lain:

    class add:
        def POST(self):
            i = web.input()
            n = db.insert('todo', title=i.title)
            raise web.seeother('/')

(Perhatikanlah bagaimana kita menggunakan `POST` untuk ini?)

`web.input` memungkinkan kita untuk mengakses setiap variabel yang 
dikirim oleh user lewat sebuah form. 

**Catatan:** Untuk dapat mengakses data dari berbagai item yang 
bernama sama, dalam format list (contoh: berbagai checkbox yang 
semuanya memiliki atribut name="name"), pergunakanlah:

    post_data=web.input(name=[])

`db.insert` akan menambahkan nilai ke dalam tabel database `todo` dan 
mengembalikan nilai ID dari baris baru. `seeother` akan melakukan 
redireksi ke suatu URL. 

`web.input`, `db.query` dan fungsi lainnya di web.py mengembalikan 
"objek Storage", yang mirip dengan dictionary, namun Anda bisa 
melakukan `d.foo` selain `d['foo']`. Ini akan menjadikan kode lebih 
bersih. 

Untuk detil lebih lanjut, termasuk untuk semua fungsi web.py, bacalah 
[dokumentasi](/docs/0.3).

<a name="developing"> </a>
## Selama pengembangan

web.py juga memiliki beberapa alat bantu untuk membantu kita melakukan 
debugging. Pada saat berjalan dengan web server bawaan, web.py akan 
menjalankan aplikasi pada modus debug. Dalam modus tersebut, setiap 
perubahan pada kode dan template secara otomatis akan dibaca ulang dan 
pesan-pesan kesalahan akan mengandung lebih banyak informasi berguna. 

Modus debug ini tidak diaktifkan pada saat aplikasi berjalan pada web 
server sesungguhnya. Apabila Anda ingin menonaktifkan modus debug, 
Anda dapat menambahkan kode berikut sebelum membuat aplikasi/template:

    web.config.debug = False

<a name="whatnext"> </a>
## Berikutnya?

Sampai di sini dulu tutorial kita. Kunjungilah [buku resep](/cookbook/) 
dan [contoh kode](/src/) untuk contoh-contoh keren yang dapat Anda 
lakukan dengan web.py. Dan, jangan lupakan juga [referensi 
api](/docs/0.3/api).
