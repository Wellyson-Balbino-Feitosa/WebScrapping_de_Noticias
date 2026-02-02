import streamlit as st
import requests
from bs4 import BeautifulSoup

# FAZ UM REQUEST PARA 'GET' OS PORTAIS DE NOTICIAS
response_penoticias= requests.get('https://pernambuconoticias.com.br/')
response_diariosertao= requests.get('https://www.diariodosertao.com.br/')


# BEAUTIFULSOUP UTILIZA O LEITOR HTML PADRÃO DO PYHTON PARA LER O HTML DO SITE
html_pernambuconoticias= BeautifulSoup(response_penoticias.text, 'html.parser')
html_diariosertao= BeautifulSoup(response_diariosertao.text, 'html.parser')

# BUSCA A TAG 'A' ONDE CONTEM OS LINKS DAS NOTICIAS
noticias_pernambunconoticias= html_pernambuconoticias.find_all('a', attrs={'class':'p-url'})
noticias_diariodosertao= html_diariosertao.find_all('a')

# FUNÇÃO PARA FILTRAR TITULOS QUE ESTIVEREM EM DIFERENTES TAGS HTML
def extrair_titulo(link):
    """
    Extrai o título de uma notícia a partir de um link HTML. Cumpre a função de filtrar títulos que podem estar em diferentes atributos e tags ou mesmo vazios.
    
    :param link: url da noticia
    :return: titulo da noticia ou None se não encontrado
    """

    
    titulo = link.get_text(" ", strip=True)
    

    if titulo:
        return titulo

    for attr in ("title", "aria-label"):
        if link.get(attr):
            return link.get(attr).strip()

    img = link.find("img")
    if img and img.get("alt"):
        return img.get("alt").strip()

    return None

# LISTA QUE FILTRA SOMENTE AS URLS COM NOTICIAS NO ENDEREÇO
noticias_filtradas_diariodosertao= [
    link for link in noticias_diariodosertao
    if link.get('href').startswith('https://www.diariodosertao.com.br/noticias/')
    and extrair_titulo(link)
]


# LISTA DE ESTRELAS DE FEEDBACK
estreals_avaliacao= ['um','dois','tres','quatro','cinco']


## PARA A CONSTRUÇÃO DO SITE, A ORDEM É IMPORTANTE

st.title('WebScrapping de Noticias de Pernambuco :material/browse_activity:')
st.caption('O melhor centralizador de noticias para que você não se sinta perdido')
st.divider()
st.subheader(':material/star: Este WebScrapping é:')
st.badge(label='Confiável',icon=':material/done_outline:', color='green')
st.badge(label='Responsivo', icon=':material/pinch:', color='violet')
st.badge(label='Otimiza seu tempo', icon=':material/clock_arrow_up:', color='blue')
st.divider()
## BLOCO 1
st.header(':material/arrow_right_alt: Noticias do portal: Pernambuconoticias.com.br')
# ESTA PARTE AQUI VAI PERCORRER TODOS OS LINKS DAS NOTICIAS E MOSTRAR NO STREAMLIT USANDO GENEATOR EXPRESSION
st.write(f'Titulo: **{link.get_text().upper()}** | \nLink: {link.get("href")}\n\n' for link in noticias_pernambunconoticias)
st.badge(label='Avalie sua experiência com este portal:', icon=':material/search:', color='yellow')
selecionado_feedback1= st.feedback('stars', key='selecionado_feedback1')
if selecionado_feedback1:
    st.markdown(f'Você selecionou {estreals_avaliacao[selecionado_feedback1]} estrelas para o portal {html_pernambuconoticias.title.string}!')

st.divider()

## BLOCO 2
st.header(':material/arrow_right_alt: Noticias do portal: Diariodosertao.com.br')
st.write(f'Titulo: **{links.get_text(strip=True).upper()}** | \nLink: {links.get('href')}\n\n'for links in noticias_filtradas_diariodosertao)
st.badge(label='Avalie sua experiência com este portal:', icon=':material/search:', color='yellow')
selecionado_feedback2= st.feedback('stars', key='selecionado_feedback2')
if selecionado_feedback2:
    st.markdown(f'Você selecionou {estreals_avaliacao[selecionado_feedback2]} estrelas para o portal {html_diariosertao.title.string}!')




