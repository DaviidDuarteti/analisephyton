from fpdf import FPDF

class PDF(FPDF):

    def doc_title(self, label):
        self.set_font("helvetica", "B",16)
        self.cell(0, 10, label, 0, 1, align="C") 
        
        self.ln()
       
    
    def doc_text(self, text):
        self.set_font("helvetica", "",12)
        self.multi_cell(0, 7, text)
        self.ln()

  

    def doc_image(self, img, x, y, w, h):
        self.image(img, x, y, w, h)
        self.ln()

pdf = PDF()
pdf.add_page()


pdf.doc_title("Desigualdade Educacional Brasileira")

pdf.doc_text("A desigualdade educacional no Brasil é um problema significativo que afeta milhões de pessoas em todo o país. Ela se manifesta em várias dimensões, incluindo acesso desigual à educação, qualidade variável da educação, disparidades regionais e socioeconômicas, além de desafios específicos relacionados à educação indígena e quilombola. Aqui estão alguns pontos-chave sobre a desigualdade educacional brasileira:")

pdf.doc_text("Acesso desigual à educação: A desigualdade educacional começa com o acesso desigual à educação. Muitas crianças em comunidades de baixa renda ou áreas rurais têm dificuldade em acessar escolas de qualidade. A falta de infraestrutura adequada, transporte escolar e recursos educacionais pode ser um obstáculo significativo.")
pdf.doc_text("Disparidades regionais: O Brasil é um país vasto e diversificado, e as disparidades regionais em termos de qualidade e acesso à educação são notáveis. As regiões mais ricas, como o Sudeste, tendem a ter sistemas educacionais mais desenvolvidos, enquanto o Norte e o Nordeste enfrentam maiores desafios.")


pdf.image("regioes.png", 30, 150, 150, 150)

pdf.ln(150)
pdf.doc_text("Verificamos que o Sudeste, tem grande parte das vagas, e as outra regiões principalmente Norte e Centro Oeste sofre ainda mais para ter um ensino de qualidade.")
pdf.doc_text("Dentro dessa quantidade de vagas no Sudeste, maior parte esta na cidade de São Paulo, Usaremos como base a cidade que contém mais vagas dentro da região que contém mais vagas, para provar como existe desigualdade social.")
pdf.doc_text("A grande parte dessas vagas disponibilizada são de fins lucrativos, e assim tirando a possibilidade de muitos cidadões cursar o ensino superior por falta de verba.")



pdf.image("cat_estudo.png", 12,90,190,140)

pdf.ln(150)

pdf.doc_text("Esse grafico mostra a diferença expressiva de vagas com fins lucrativos para as gratuitas, com mais de 80 porcento das vagas sendo pagas, isso representa uma quantidade de dez milhões, quinhentos mil e treze vagas, enquanto temos uma quantidade de dois milhões, trezentos e oitenta e sete mil, quatrocentos e setenta e sete vagas gratuitas em uma cidade que há oito milhões, trinta e três mil estudantes, assim mostrando que apenas 29.70 porcento dos estudantes tem direito a uma vaga gratuita, como podemos ter igualdade onde mais de 70 porcento dos estudantes precisa ter condições financeiras para estudar. ")
pdf.doc_text("Com a falta de empregos e muitos empregados com baixa renda, os estudantes optão por uma formação mais rapida, para assim conseguir se encaixar no mercado de trabalho de forma mais agil.")


pdf.image("grau_ensino.png", 35,50,140,110)

pdf.ln(110)

pdf.doc_text("Conseguimos ver nitidamente que as vagas em tecnológo são as mais procuradas, por se tratar de uma vaga com o periodo menor e o valor também se encaixa ao periodo, acaba sendo uma opção mais viavel para os estudantes de baixa renda.")

pdf.doc_text("Também podemos ver que o estudo a distancia também vem se destacando entre as escolhas dos estudantes.")
pdf.image("modalidade.png", 50,210,120,85)

pdf.ln(110)

pdf.doc_text("Com a escolha de estudar em casa, o estudante consegue ter uma economia não somente no valor da faculdade, mas acaba gerando outras economias, se tornando uma opção melhor, mesmo não sendo a ideal para muitas qualificações.")

pdf.doc_text("Em São Paulo há muitas vagas em diversos cursos, porém vou listar 10 cursos que tem a maior quantidade de vagas, assim mostrando ser os cursos mais procurados e cogitados na grande região metropolitana.")


pdf.image("top_vagas.png", 10,70,190,130)

pdf.ln(145)

pdf.doc_text("Mas calma lá, essas vagas representa a quantidade total de vagas disponivel, agora vou apresentar os 10 cursos com mais vagas gratuitas.")
pdf.ln(10)

pdf.doc_text("Então se voçê é um estudante de baixa renda e esta a procura de formação gratuita, esses 10 cursos são os cursos com maior disponibilidade de vagas gratuitas, sendo assim tendo maior chance de conseguir uma bolsa, lembrando que esses dados são da região metropolitana de São Paulo.")

pdf.ln(20)



pdf.doc_text("Esses cursos são somente os 10 com maiores vagas, porém existe muitos outros cursos com inumeras vagas gratuitas..")

pdf.image("Top10_cursos_gratuitos.png", 10,30,190,130)

pdf.ln(130)
pdf.doc_text("Assim seguimos esperando que nosso pais invista muito mais em educação, para que todos tenham acesso a um ensino de qualidade.")

pdf.image("ictq-formatura.png",0,180,210,130)

pdf.ln(120)
pdf.doc_title("Pesquisa desenvolvida por David Duarte - 2023")

pdf.output("analise_phyton.pdf")