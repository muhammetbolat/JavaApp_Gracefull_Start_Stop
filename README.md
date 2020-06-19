########################################################################################################################
#################################################       authSet.py      ################################################

Bu script ile application.properties dosyasında değiştirilmek istenilen alanlar auth.yml dosyasına girilir. Git reposuna
ip, şifre, kullanıcı adı bilgilerinin gönderilmesi doğru olmadığı için böyle bir çözüme başvurulmuştur.
Örneğin;
        Aşağodaki değişkenler değiştirilmek istenilsin
        application properties:
            mobile.jdbc.username=dummy_username
            mobile.jdbc.password=dummy_password


        auth.yml:
            mobile.jdbc.username: XXXXX
            main.jdbc.password: XXXXX

        auth.yml'daki değerler bu script çalıştırıldığında application.properties dosyasındaki değerlerle yer
        değiştirilir. En son hal şöyle olmaktadır.

            application properties:
            mobile.jdbc.username=XXXXXX
            mobile.jdbc.password=XXXXXX

########################################################################################################################
#################################################       stopApp.py      ################################################

Uygulamayı durdurmaya yarayan bu script büyük bir önem arz etmektedir. Durdurma işlemi sırasında belirli kontrolleri
yapmaktadır.

1. Uygulama veri tabanına bağlanır. STOPPED_ROUTE tablosunda ALL_ROUTE_STOPPED kaydınınn olup olmadığına bakar. Eğer
kayıt yoksa kayıt girilir. Kayıt var ise kayıtın var olduğu log'a yazılır ve bir sonraki adıma geçilir. Bu kayıt
eklendikten sonra uygulama route'ları yeniden başlamayacaktır.

2. Mevcut çalışan route'ların bitmesi beklenir. Bunun için ROUTE_PROCESS tablosunad FINISH_TIME değeri null olan ve
route ismi içerisinde create ve process içeren route'lar kontrol edilir. Bitene kadar beklenir.

3. Bu noktaya gelindiğinde tüm route'lar tamamlanmış ve yeni route oluşması engellenmiştir. Bu aşamadan sonra
uygulamanın process'ini bulup kill etme işlemine geçilecektir. Uygulama ismi esspro.jar olduğu için process'ler içinde
komut argümanı olarak esspro.jar geçen process'ler sonlandırılır. Sonlandırma işlemi yapıldıktan sonra tekrardan
tablo process'ler kontrol edilir. Eğer sorun var ise kod exception fırlatır ve diğer adımlara geçmez.

4. Uygulama tamamen durdu ve her şey hazır. Yeni uygulama başlatılmadan önce her ihtimale karşı ROUTE_PROCESS tablosunda
NULL olan değerler set edilir. Çünkü bizim için kritik olan '%createfile%' ve '%process%' route'larıdır. Örneğin,
import_usom route'u NULL kalmış olabilir. Temiz bir sayfa açmak adına bu değerler set edilir.

########################################################################################################################
################################################       startApp.py      ################################################

Uygulamayı tekrardan başlatan scriptdir.
1.) Uygulamayı başlatma için tıpkı operasyon ekibinin yaptığı gibi aşağıdaki script çalıştırılır.
    startup.command: nohup /usr/bin/java -jar esspro.jar &
