## Link Website
HEROKU : [link](https://lab02-pbp-abdul.herokuapp.com/)
## Tugas 3
* Json adalah format data standard. Json memiliki kepanjangan JavaScript Object Notation. XML merupakan format data standard. XML memiliki kepanjangan extensible markup language. HTML sendiri adalah bahasa markup yang digunakan pada web. Berdasarkan definisi HTML sudah berbeda dengan json atau XML. Hal ini dikarenakan HTML bukanlah suatu format data standard. Json dan XML memiliki beberapa perbedaaan :
    * Json dapat berupa array sedangkan XML tidak
    * XML lebih aman dibandingkan json
    * Json hanya mensuport utf-8 encoding sedangkan, XMl mensuport berabagai macam encoding
* Kita memerlukan data delivery agar kita dapat menghubungkan beberapa framework karena, setiap framework memiliki cara menyimpan atau menerima data yang berbeda maka perlu adanya format data standar untuk menghubungkan antar framework. Hal ini perlu dilakukan agar suatu web / mobile app dapat menjalankan fungsinya dengan baik
* Pertama saya membuat app baru dengan nama mywatchlist. Kedua saya mebuat urls.py pada app baru saya. Ketiga membuat model sebagai berikut
    * watched : BooleanField
    * title : CharField
    * rating : IntegerField
    * release_date : DateField
    * review : TextField

    kemudian saya membuat views berdasarkan model tersebut dan merendernya ke html supaya data bisa ditampilkan. Setelah itu buat views tambahan agar bisa menampilkan dalam bentuk json dan XML

* Postman :

**HTML**
[![Screenshot-2022-09-22-112743.png](https://i.postimg.cc/CKxZXjF7/Screenshot-2022-09-22-112743.png)](https://postimg.cc/bZ4N2SSS)
**json**
[![Screenshot-2022-09-22-112814.png](https://i.postimg.cc/xTGcds8g/Screenshot-2022-09-22-112814.png)](https://postimg.cc/dL1qHj8T)
**XML**
[![Screenshot-2022-09-22-112839.png](https://i.postimg.cc/kgfGQBxb/Screenshot-2022-09-22-112839.png)](https://postimg.cc/G4Tbr3gL)