	
"""Write a function called most_frequent that takes a string and
prints the letters in decreasing order of frequency. Find text samples
from several different languages and see how letter frequency varies
between languages. Compare your results with the tables at
http://en.wikipedia.org/wiki/Letter_frequencies.
Solution: http://thinkpython2.com/code/most_frequent.py.
"""

def most_frequent(text):

	letters = set(text.lower())

	letter_frequency = []

	for char in letters:
		if char.isalpha():
			letter_frequency.append((text.count(char), char))

	letter_frequency.sort(reverse=True)

	result = []

	for freq, letter in letter_frequency:
		result.append(letter)

	return result

text_EN = 'TORONTO — During the applause, the celebratory elbow bumps, the camera flashes, Colette Cameron watched \
through tears as four of her colleagues got jabbed Monday with the country’s first coronavirus vaccinations. Then \
she removed her suit jacket to follow them herself.“It was overwhelming,” said Ms. Cameron, a registered nurse and \
social worker, who runs a nursing home in Toronto that experienced one of the city’s first outbreaks. “I wish \
everyone could have this support so nobody has to feel as alone as we did. We were desperate.”The start of Canada’s \
vaccine campaign was an emotional one, with the first precious doses going to people from nursing homes: health \
care workers in Toronto, and residents in both Montreal and Quebec City.That was recognition that nursing homes have \
been ground zero in Canada when it comes to both Covid-19’s cruel ravages and the storm of criticism over the \
country’s lack of preparation for it. More than 460,000 people have tested positive for the coronavirus in Canada, \
and 13,400 have died from it.“We have never distributed so many Kleenex boxes as the last few days,” said \
Sue Graham-Nutter, chief executive officer of the Rekai Centres, which runs two nursing homes in Toronto tapped \
to receive the country’s first vaccinations. “We have the images of what happened on the floors.”Less than a week \
after Canada became the third country in the world to approve the vaccine created by the American drugmaker Pfizer \
and a German firm, BioNTech, the first shipment arrived at a Montreal airport on Sunday night. From there, kicking \
off the country’s largest largest-ever inoculation program, the boxes of frozen vials were dispersed to 14 sites \
across most of the country that were equipped with special freezers for the vaccine, which needs to be kept at \
ultracold temperatures.'

text_ES = 'TORONTO - Durante los aplausos, los codazos de celebración, los flashes de la cámara, Colette Cameron miró \
entre lágrimas cuando cuatro de sus colegas recibieron el lunes las primeras vacunas contra el coronavirus del país. Luego \
se quitó la chaqueta del traje para seguirlos ella misma. “Fue abrumador”, dijo la Sra. Cameron, enfermera titulada y \
trabajador social, que dirige un hogar de ancianos en Toronto que experimentó uno de los primeros brotes de la ciudad. "Yo deseo \
todos podrían tener este apoyo para que nadie se sienta tan solo como nosotros. Estábamos desesperados ”. El comienzo de la \
La campaña de vacunación fue muy emotiva, y las primeras dosis preciosas fueron destinadas a personas de hogares de ancianos: salud \
cuidadores en Toronto y residentes tanto en Montreal como en la ciudad de Quebec. Ese fue un reconocimiento de que los asilos de ancianos tienen \
sido la zona cero en Canadá cuando se trata de los crueles estragos de Covid-19 y la tormenta de críticas sobre el \
la falta de preparación del país para ello. Más de 460.000 personas han dado positivo por coronavirus en Canadá, \
y 13,400 han muerto a causa de él. “Nunca habíamos distribuido tantas cajas de Kleenex como en los últimos días”, dijo \
Sue Graham-Nutter, directora ejecutiva de los Centros Rekai, que administra dos hogares de ancianos en Toronto, aprovechó \
recibir las primeras vacunas del país. “Tenemos las imágenes de lo que pasó en los pisos”. Menos de una semana \
después de que Canadá se convirtiera en el tercer país del mundo en aprobar la vacuna creada por la farmacéutica estadounidense Pfizer \
y una empresa alemana, BioNTech, el primer envío llegó a un aeropuerto de Montreal el domingo por la noche. A partir de ahí, pateando \
Fuera del programa de inoculación más grande de la historia del país, las cajas de viales congelados se distribuyeron en 14 sitios \
en la mayor parte del país que estaban equipados con congeladores especiales para la vacuna, que deben mantenerse en \
temperaturas ultra frías.'

text_RO = 'TORONTO - În timpul aplauzelor, cotul sărbătoresc, camera clipeste, Colette Cameron a urmărit \
printre lacrimi, patru dintre colegii ei au fost loviți luni cu primele vaccinări cu coronavirus din țară. Atunci \
și-a scos costumul pentru a-i urmări singură. „A fost copleșitor”, a spus doamna Cameron, o asistentă medicală înregistrată și \
asistent social, care conduce o casă de îngrijire medicală în Toronto, care a experimentat unul dintre primele focare ale orașului. "Eu doresc \
toată lumea ar putea avea acest sprijin, astfel încât nimeni să nu se simtă la fel de singur ca noi. Eram disperați. ”Începutul programului canadian \
campania de vaccinuri a fost una emoțională, primele doze prețioase fiind destinate persoanelor de la aziluri: sănătate \
lucrători de îngrijire din Toronto și rezidenți atât în ​​Montreal, cât și în orașul Quebec. Aceasta a fost recunoașterea faptului că \
a fost punctul zero în Canada când vine vorba atât de ravagiile crude ale lui Covid-19, cât și de furtuna de critici asupra \
lipsa de pregătire a țării pentru aceasta. Peste 460.000 de persoane au dat rezultate pozitive pentru coronavirus în Canada, \
și 13.400 au murit din cauza asta. „Nu am distribuit niciodată atât de multe cutii Kleenex ca în ultimele zile”, a spus \
Sue Graham-Nutter, director executiv al Centrelor Rekai, care administrează două case de îngrijire medicală din Toronto, a exploatat \
pentru a primi primele vaccinări din țară. „Avem imaginile a ceea ce s-a întâmplat la etaje.” Mai puțin de o săptămână \
după ce Canada a devenit a treia țară din lume care a aprobat vaccinul creat de medicul american Pfizer \
și o firmă germană, BioNTech, primul transport a sosit duminică seara pe un aeroport din Montreal. De acolo, lovind \
în afara celui mai mare program de inoculare cel mai mare din țară, cutiile de flacoane înghețate au fost dispersate în 14 locuri \
în cea mai mare parte a țării care au fost echipate cu congelatoare speciale pentru vaccin, care trebuie ținut la \
temperaturi ultracold. '

print("EN:",*most_frequent(text_EN))

print("ES:",*most_frequent(text_ES))

print("RO:",*most_frequent(text_RO))