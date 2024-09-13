import google.generativeai as genai
import gizliDosya
import gradio as gr

# Google Generative AI API anahtarınızı yapılandırın
genai.configure(api_key=gizliDosya.api_key)

# Modeli yükleyin
model = genai.GenerativeModel('gemini-pro')

# Prompt'a göre içerik oluşturan fonksiyon
def generate(prompt):
    cevap = model.generate_content(prompt)
    return cevap.text

# Gradio arayüzü için başlık ve açıklama
title = 'FIRAT ÜNİVERSİTESİ S.S.S'
description = 'FIRAT AI YE SORULARINIZI SORUN.'

# CSS ile özel tema
custom_css = """
body { 
    background-color: #800000; /* Bordo renk */
            color: white; 
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 260px;
            margin-top: 0;
            margin-bottom: 0;
            margin-left: 0;
            margin-right: 0;
            background-image: url("https://bilgisayarmf.firat.edu.tr/assets/front/img/home-new-img.jpeg");
            background-repeat: no-repeat; /* Resmin tekrar etmemesini sağla */
            background-position: right; /* Resmi sağ tarafta konumlandır */
            background-size: cover; /* Arka plan resmini kaplamasını sağla */
}

    
   



.gradio-container {
    border: 2px solid #FFD700; /* Altın sarısı */
    border-radius: 10px;
    padding: 20px;
    background-color: #FFFFFF; /* Beyaz renk */
    text-align: center;
    width: 60%;
    box-shadow: 0px 0px 10px 0px #000;
}
.input-textbox, .output-textbox {
    background-color: #FFFFFF;
    color: #000000;
    border: 1px solid #800000; /* Bordo renk */
    border-radius: 5px;
    width: 100%;
    margin: 10px auto;
    padding: 10px;
}
h1, h2 {
    color: #800000; /* Bordo renk */
}
.logo {
    width: 150px;
    height: auto;
    margin-bottom: 20px;
}
.gr-button-primary, .gr-button-flag, .gr-button-clear {
    background-color: #c2302c !important; /* Bordo renk */
    color: white !important; /* Beyaz renk */
    border: none !important;
    padding: 10px 20px !important;
    font-size: 16px !important;
    border-radius: 5px !important;
    cursor: pointer !important;
    margin-top: 10px !important;
}
.gr-button-primary:hover, .gr-button-flag:hover, .gr-button-clear:hover {
    background-color: #a12824 !important; /* Daha koyu bordo renk */
}
"""

# HTML içeriği (logo eklemek için)
# HTML içeriği (logo eklemek için)
html_content = """
<div style="display: flex; justify-content: center;">
    <div style="flex: 1; text-align: center;">
        <img src="https://www.firat.edu.tr/images/content_menu/16329166371.png" alt="Fırat Üniversitesi Logosu" width="300">
    </div>
    <div style="flex: 1; text-align: center;">
        <img src="https://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50?s=200" alt="Sağdaki Resim" style="width: 100%;">
    </div>
</div>
<h1>FIRAT ÜNİVERSİTESİ S.S.S</h1>
<h2>FIRAT AI'YE SORULARINIZI SORUN</h2>
"""


# Gradio arayüzü yapılandırması
interface = gr.Interface(
    fn=generate,
    inputs=gr.Textbox(lines=2, placeholder="Buraya sorunuzu yazın..."),
    outputs="text",
    title=title,
    description=description,
    css=custom_css,
    live=False  # Submit butonunu göstermek için live=False
)

# Gradio arayüzünü başlat
interface.launch(server_port=8080, share=True, inbrowser=True, server_name="0.0.0.0")

# HTML içeriğini Gradio'ya ekleyin
interface.get_config().update(description=html_content)






