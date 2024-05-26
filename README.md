# dailyemailsender
EN: Daily Email Report Sender Program
This Python program allows users to automatically send an email at a specified time every day. The program collects the user's email details, schedules the email to be sent, and automatically sends the email at the specified time.

Features of the Program
Graphical User Interface (GUI):

Provides a user-friendly interface for entering the necessary email information.
Includes fields for email addresses, subject, and content.
Has hour and minute selectors for the send time.
Theme Selection:

Users can change the appearance of the program and use the dark theme option.
Automatic Email Sending:

The program automatically sends the email at the time specified by the user.
Users are notified when the email is successfully sent or if an error occurs.
How the Program Works
Creating the User Interface (GUI):

The program uses the tkinter library to create a window and provides various input fields to collect the necessary information from the user.
Entering Email Information:

The user enters the sender's email address, recipient's email address, email password, subject, and content.
The user selects the appropriate time for sending the email using hour and minute selectors.
Sending the Email:

The program schedules the email to be sent at the specified time.
When the time arrives, the program initiates the email sending process and informs the user of the result.
Error and Information Notifications:

If there is an error in sending the email, an error message is displayed to the user.
If the email is sent successfully, an informational message is displayed to the user.
Brief Explanation of the Code
SMTP Settings: Gmail's SMTP server (smtp.gmail.com) and port (587) are used to send the email.
GUI Elements: Labels, entry fields, text box, hour and minute selectors (Combobox), and buttons are defined for user input.
Email Validation: A function is included to check if the email addresses are valid.
Sending Email: A function is defined to send the email using the user's information.
Scheduling: The schedule library is used to ensure the email is sent at the specified time.
Theme Switching: Users can switch between dark theme and normal theme.
How to Use the Code
Running the Program: Run this code in a Python environment.
Entering Information: In the opened window, enter the sender's and recipient's email addresses, password, email subject, and content. Select the send time.
Start: After entering the information, press the "Start" button.
Automatic Sending: The program will automatically send the email at the specified time.
This way, you can easily use this program for sending daily reports or reminders via email.




TR: Günlük E-posta Raporu Gönderici Programı
Bu Python programı, kullanıcıların günlük olarak belirli bir saatte otomatik e-posta göndermelerini sağlar. Program, kullanıcının e-posta bilgilerini alır, e-posta gönderimi için bir zamanlama yapar ve belirtilen saatte e-postayı otomatik olarak gönderir.

Programın Özellikleri
Grafik Kullanıcı Arayüzü (GUI):

Kullanıcı dostu bir arayüz ile e-posta gönderimi için gerekli bilgilerin girilmesini sağlar.
E-posta adresleri, konu ve içerik gibi bilgileri girebileceğiniz alanlar bulunur.
Gönderim saati için saat ve dakika seçicileri vardır.
Tema Seçimi:

Kullanıcılar, programın görünümünü değiştirebilir ve karanlık tema seçeneğini kullanabilirler.
Otomatik E-posta Gönderimi:

Program, kullanıcının belirttiği saatte otomatik olarak e-posta gönderir.
E-posta gönderimi başarılı olduğunda veya hata oluştuğunda kullanıcı bilgilendirilir.
Programın Nasıl Çalıştığı
Kullanıcı Arayüzü (GUI) Oluşturma:

Program, tkinter kütüphanesini kullanarak bir pencere oluşturur ve kullanıcıdan gerekli bilgileri toplamak için çeşitli giriş alanları sağlar.
E-posta Bilgilerinin Girilmesi:

Kullanıcı, gönderen e-posta adresi, alıcı e-posta adresi, e-posta şifresi, konu ve içeriği girer.
Gönderim saati için saat ve dakika seçicilerinden uygun zamanı seçer.
E-posta Gönderimi:

Program, belirtilen saatte e-posta göndermek için bir zamanlama yapar.
Zaman geldiğinde, program e-posta gönderme işlemini başlatır ve gönderim sonucunu kullanıcıya bildirir.
Hata ve Bilgi Bildirimi:

Eğer e-posta gönderiminde bir hata oluşursa, kullanıcıya bir hata mesajı gösterilir.
E-posta başarıyla gönderildiğinde, kullanıcıya bilgilendirme mesajı gösterilir.
Kısaca Kodun Açıklaması
SMTP Ayarları: E-posta göndermek için Gmail'in SMTP sunucusu (smtp.gmail.com) ve portu (587) kullanılır.
GUI Elemanları: Kullanıcının bilgi girmesi için etiketler (Label), giriş kutuları (Entry), metin kutusu (Text), saat ve dakika seçicileri (Combobox), ve butonlar (Button) tanımlanır.
E-posta Doğrulama: E-posta adreslerinin geçerli olup olmadığını kontrol eden fonksiyon bulunur.
E-posta Gönderimi: Kullanıcı bilgilerini kullanarak e-posta gönderen fonksiyon tanımlanır.
Zamanlama: schedule kütüphanesi kullanılarak e-postanın belirtilen saatte gönderilmesi sağlanır.
Tema Değiştirme: Kullanıcı, karanlık tema ve normal tema arasında geçiş yapabilir.
Kodun Kullanımı
Programı Çalıştırma: Python ortamında bu kodu çalıştırın.
Bilgi Girişi: Açılan pencerede gönderen ve alıcı e-posta adreslerini, şifreyi, e-posta konusunu ve içeriğini girin. Gönderim saatini seçin.
Başlat: Bilgileri girdikten sonra "Başlat" butonuna basın.
Otomatik Gönderim: Program, belirtilen saatte e-postayı otomatik olarak gönderecektir.
Bu şekilde, günlük olarak e-posta göndermeniz gereken raporlar veya hatırlatmalar için bu programı kolayca kullanabilirsiniz.
