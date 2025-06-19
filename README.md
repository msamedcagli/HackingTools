<h1>Hacking Tools</h1>
<ul>
  <li><a href="#MacAddress">Mac Address Changer</a></li>
  <li><a href="#NetScanner">Net Scanner</a></li>
  <li><a href="#MITM">Man in the Middle</a></li>
</ul>

<br><br>
<h2 id="#MacAddress">🛠️ MAC Adresi Değiştirme Scripti (Python)</h2>

<p>
Bu Python projesi, Linux işletim sistemlerinde bir ağ arayüzünün MAC adresini geçici olarak değiştirmek için kullanılır.
Güvenlik testlerinde anonimlik sağlamak, ağ üzerinde cihaz kimliğini gizlemek veya sadece pratik yapmak için kullanılabilir.
</p>

<hr>

<h3>📌 Ne İşe Yarar?</h3>

<p>Bir cihazın <strong>MAC (Media Access Control)</strong> adresi, ağa bağlanırken gönderilen fiziksel adresidir. Bu script sayesinde:</p>

<ul>
    <li>✅ MAC adresinizi terminal üzerinden kolayca değiştirebilirsiniz.</li>
    <li>🕵️ Ağ trafiğinde kimliğinizi gizleyebilirsiniz.</li>
    <li>🔐 MAC filtreleme olan ağlara farklı kimlikle bağlanabilirsiniz.</li>
    <li>💻 Sızma testleri ve etik hacking çalışmaları için ideal bir ortam hazırlayabilirsiniz.</li>
</ul>

<hr>

<h3>⚙️ Nasıl Kullanılır?</h3>

<h4>1. Script'i Kaydedin</h4>
<p><code>MacChangerTool.py</code> adıyla aşağıdaki Python kodunu kaydedin.</p>

<h4>2. Terminalden Çalıştırın</h4>
<p><strong>Root yetkisiyle çalıştırmak zorunludur.</strong></p>

<pre><code>python MacChangerTool.py --interface &lt;arayüz_adı&gt; --mac &lt;yeni_mac_adresi&gt;</code></pre>

<p><strong>Örnek kullanım:</strong></p>

<pre><code>python MacChangerTool.py --interface eth0 --mac 00:00:19:07:00:00</code></pre>

<hr>

<h3>📚 Kullanılan Kütüphaneler</h3>

<ul>
    <li><code>subprocess</code> – Terminal komutlarını çalıştırmak için kullanılır.</li>
    <li><code>optparse</code> – Komut satırı argümanlarını almak için kullanılır. (Python 3.2+ sürümler için <code>argparse</code> tercih edilir.)</li>
</ul>

<hr>

<h3>⚠️ Uyarılar</h3>

<ul>
    <li>Bu script yalnızca <strong>Linux</strong> sistemlerde çalışır.</li>
    <li><strong>Geçici</strong> olarak MAC adresi değiştirir. Cihaz yeniden başlatıldığında eski haline döner.</li>
    <li>Etik dışı kullanımlar tamamen kullanıcı sorumluluğundadır.</li>
</ul>

<hr>

<h3>🧠 Lisans</h3>

<p>Bu proje MIT lisansı ile lisanslanmıştır. Dilediğiniz gibi kullanabilir, dağıtabilir ve geliştirebilirsiniz.</p>

<br>
<hr><hr>
<br>

<h2 id="#NetScanner">🔍 NetScannerTool - Basit ARP Ağ Tarayıcısı</h2>

<p>
NetScannerTool, Python ve Scapy kullanarak bir yerel ağdaki cihazları tespit eden basit bir ağ tarama aracıdır.
ARP (Address Resolution Protocol) paketlerini kullanarak ağda canlı olan cihazları MAC adresleriyle birlikte listeler.
</p>

<h3>🛠 Özellikler</h3>

<ul>
  <li>ARP protokolü ile yerel ağ taraması</li>
  <li>Yayın (broadcast) üzerinden cihaz tespiti</li>
  <li>IP ve MAC adreslerini listeler</li>
  <li>Basit terminal arayüzü</li>
  <li><code>optparse</code> ile komut satırı üzerinden IP aralığı girme</li>
</ul>

<h3>📦 Kullanılan Kütüphaneler</h3>

<table>
  <thead>
    <tr>
      <th>Kütüphane</th>
      <th>Açıklama</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>scapy</code></td>
      <td>Düşük seviyeli ağ paketlerini oluşturma ve analiz etme</td>
    </tr>
    <tr>
      <td><code>optparse</code></td>
      <td>Komut satırı argümanlarını alma (Python yerleşik modülüdür)</td>
    </tr>
  </tbody>
</table>

<blockquote>
  <strong>Not:</strong> Bu betik Python 3 için optimize edilmiştir. Python 2 ile çalıştırmanız önerilmez.
</blockquote>

<hr>

<h3>🚀 Kurulum</h3>

<pre><code>sudo apt update
sudo apt install python3 python3-pip
pip3 install scapy

sudo python3 net_scanner.py -i 10.0.2.1/24
</code></pre>

<br>
<hr><hr>
<br>
<h2 id="#MITM">🛠️ Man in the Middle</h2>
<h3>Yakında Eklenecek</h3>


