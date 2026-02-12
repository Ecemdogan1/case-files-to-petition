# case-files-to-petition
A legal engineering tool that converts unstructured case files into a structured petition draft. Extracts timeline, parties and dispute structure from raw case documents and generates a structured legal petition draft for lawyers. Dağınık dava dosyalarını yapılandırılmış bir dilekçe taslağına dönüştüren bir legal engineering aracıdır.
Avukatların en çok zaman harcadığı işlerden biri, dağınık halde bulunan dava dosyalarını okuyup olay örgüsünü çıkarmak ve buna göre dilekçe kurgulamaktır.
Sözleşmeler, faturalar, WhatsApp konuşmaları, e-postalar, tutanaklar, bilirkişi raporları… Tüm bu belgeler saatler süren manuel bir analiz gerektirir.
bu süreci modellemek için geliştirilmiş deneysel bir legal engineering projesidir.
Bu proje, dava dosyalarındaki metinleri analiz ederek:
Tarafları tespit eder
Tarihleri ve olayları çıkarır
Olayları kronolojik sıraya dizer
Uyuşmazlık türünü tahmin eder
Avukat için yapılandırılmış bir dilekçe taslağı üretir
Amaç, hukuki değerlendirme yapmak değil; avukatın üretim sürecini hızlandıracak bir iş akışı otomasyonu sağlamaktır.
Nasıl Çalışır?
Kullanıcı, dava dosyasındaki metinleri case_files/ klasörüne ekler.
Sistem:
Metinlerden kişi, tarih, para ve eylem bilgilerini çıkarır
Olayları zaman sırasına koyar
Uyuşmazlığın hukuki türünü tahmin eder
Olaylar, deliller ve hukuki değerlendirme başlıklarını içeren bir dilekçe taslağı oluşturur
Çıktılar
Program çalıştırıldığında:
case_summary.txt → Olay örgüsünün özeti
timeline.json → Kronolojik olay listesi
petition_draft.txt → Dilekçe taslağı
oluşturulur.
