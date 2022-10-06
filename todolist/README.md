## Link Website
HEROKU : [link](https://lab02-pbp-abdul.herokuapp.com/)
## Tugas 4
* CSRF adalah Cross-site request forgery. Jika tidak ada CSRF token info - info penting seperti email akan muncul pada URL. CSRF token mengenkapsulasi info - info penting tersebut agar tidak disalahgunakan
* Ya, kita dapat membuat form secara manual. Jika kita ingin membuat form seperti yang digenerate oleh {{ form.as_table }} maka, kita dapat memulainya dengan membuat tabel. Kemudian kita dapat mengunakan html tag input untuk setiap entry dari form. Kemudian kita define type untuk setiap entry dari form yang akan kita buat.
* Form yang telah dibuat dengan django akan digenerate dengan django template language sehingga, muncul sebuah form dalam tampilah HTML. Kemudian setelah kita mengisi form dan mensubmitnya data tersebut akan diverivikasi oleh django, apakah data tersebut valid atau tidak. Jika valid maka data tersebut akan disave (disimpan dalam database). Data yang telah berada didatabase dapat ditampilkan dengan django template language.
* Pertama kita membuat app dan melakukan routing kepada app baru yang sudah kita buat. Kedua kita membuat model yang diperlukan untuk projek kita. Model yang diperlukan yaitu, user(berupa foreign key kepada pengguna dari app), date, tittle, dan description. Kemudian kita membuat form untuk login dan register. Untuk form login kita membuatnya secara manual dengan HTML. Form register digenerate secara otomatis dengan template UserCreationForm yang sudah ada pada django. Halaman untuk menambah task baru diimplementasikan dengan django modelform. Pada Form ini kita bisa mereference dari model kita yang sudah dibuat kemudian dijadikan Form. Page todolist menampilkan semua data yang dibuat oleh user. Untuk spesifikasi user yang membuat dapat difilter berdasarkan user tersebut pada django get. 

* Untuk penilaian bonus kita mengimplementasikan fungsi tambahan. Pada fungsi ini kita dapat mengubah nilai dari status pekerjaan menjadi True/False. yang kita lakukan adalah memanggil id dari task yang ingin kita ubah kemudian mengubah nilai dari statusnya. Pada fungsi delete kita memanggil id dari task yang ingin kita ubah kemudian menghapus data tersebut.

## Tugas 5
* Inline CSS akan memberikan styles pada tiap tag HTML. Inline CSS akan memberikan styles pada satu file HTML tersebut. External CSS membuat file styling sendiri kemudian file ini akan dilink kepada file HTML yang memerlukan style tersebut.

* 1. h1 sampai h6 : untuk menuliskan HTML heading dengan berbagai ukuran.
    2. hr : mencenak horizontal line
    3. img : merepresentasikan gambar pada HTML
    4. li : memberikan list item
    5. a : mendefinisikan hyperlink
    6. br : menghasilkan line break
    7. div : menspecify section dalam suatu code

* 1. Background : mengubah warna background
    2. margin : set margin suatu objek
    3. padding : set padding suatu objek
    4. font-family : specify font family dari suatu teks
    5. grid : property untuk memetakan page menjadi suatu grid.

* Membuat cards mengunakan bootstrap hal ini dapat dilakukan dengan menambahkan class card. class card sudah menjadi builtin pada Bootstrap. Kemudian ditambahkan containter yang berisi row dan col. row dan col ini dapat disetting dengan class sm, md, atau lg. class ini memperboleh maximum length dari suatu section. Hal ini membuat suatu page menjadi responsive. Kemudian untuk melakukan hover pada card dapat diimpelementasikan dengan css tambahan. Untuk melakukannya kita bisa mengubah behavior card-primary:hover. Fitur yang dibuat adalah membuat shadow ketika suatu card dihover. Maka kita dapat set shadow dari card-primary:hover.