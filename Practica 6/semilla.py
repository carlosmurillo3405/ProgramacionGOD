"""Genera akinator.json con una base amplia de personajes y videojuegos.

Cada entidad se describe con las etiquetas que son verdaderas para ella; todo
lo que no aparece se considera falso. Con eso se construye el árbol de
preguntas que usa Practica5_(Akinator).py.

Ejecútalo solo si quieres regresar la base a su estado inicial:
    py semilla.py
"""

import json
import os

# ---------------------------------------------------------------- preguntas
# clave: (prioridad, texto). La prioridad decide qué tan arriba del árbol
# puede aparecer la pregunta (0 = lo más general).
PREGUNTAS = {
    # --- nivel 0: qué tipo de cosa es ---
    "vj": (0, "¿Es un videojuego?"),
    # --- grandes familias ---
    "real": (1, "¿Es una persona que existe o existió en la vida real?"),
    "conocido": (2, "¿Es alguien del Centro Universitario de Tlajomulco que conoces en persona?"),
    "youtuber": (2, "¿Es creador de contenido en YouTube o Twitch?"),
    "cientifico": (2, "¿Se dedicó a la ciencia, las matemáticas o la tecnología?"),
    "mexicano_hist": (2, "¿Es un personaje importante de la historia de México?"),
    "comic": (2, "¿Aparece en cómics de superhéroes?"),
    # --- datos generales de personas ---
    "mujer": (4, "¿Es mujer?"),
    "mexicano": (3, "¿Es de México?"),
    "vive": (3, "¿Está vivo actualmente?"),
    "antes1900": (4, "¿Murió antes del año 1900?"),

    # --- científicos ---
    "fisico": (5, "¿Trabajó principalmente en física?"),
    "matematico": (5, "¿Destacó en matemáticas o en computación?"),
    "biologia": (5, "¿Trabajó en biología, química o medicina?"),
    "astronomia": (5, "¿Es famoso por la astronomía o el espacio?"),
    "inventor": (5, "¿Se le conoce sobre todo como inventor?"),
    "nobel": (6, "¿Ganó un Premio Nobel?"),
    "electricidad": (6, "¿Es famoso por sus trabajos con la electricidad?"),
    "aleman": (6, "¿Era de Alemania?"),
    "ingles": (6, "¿Era de Inglaterra?"),
    "eeuu": (6, "¿Era de Estados Unidos?"),
    "antiguo": (6, "¿Vivió en la Antigüedad, antes de la Edad Media?"),
    "divulgador": (7, "¿Es famoso por divulgar la ciencia en televisión o libros?"),
    "relatividad": (7, "¿Es famoso por la teoría de la relatividad?"),
    "gato_cuantico": (7, "¿Se le recuerda por un experimento imaginario con un gato?"),
    "bomba": (7, "¿Dirigió el proyecto de la bomba atómica?"),
    "tabla": (7, "¿Creó la tabla periódica de los elementos?"),
    "adn": (7, "¿Sus trabajos tienen que ver con la herencia y el ADN?"),
    "penicilina": (7, "¿Descubrió la penicilina?"),
    "programadora": (7, "¿Se le considera pionera de la programación?"),

    # --- historia de México ---
    "independencia": (5, "¿Participó en la Independencia de México?"),
    "revolucion": (5, "¿Participó en la Revolución Mexicana?"),
    "prehispanico": (5, "¿Vivió en la época prehispánica o durante la Conquista?"),
    "artista": (5, "¿Es famoso por el arte, las letras o el espectáculo?"),
    "presidente": (6, "¿Fue presidente de México?"),
    "militar": (6, "¿Fue militar, guerrero o caudillo?"),
    "sacerdote": (6, "¿Fue sacerdote, monja o religioso?"),
    "padre_patria": (7, "¿Se le llama el Padre de la Patria?"),
    "corregidora": (7, "¿Se le conoce como la Corregidora?"),
    "emperador": (7, "¿Llegó a ser emperador?"),
    "primer_pres": (7, "¿Fue el primer presidente de México?"),
    "dictador": (7, "¿Gobernó México más de 30 años seguidos?"),
    "pierna": (7, "¿Perdió una pierna y le hizo un funeral?"),
    "norte": (7, "¿Luchó en el norte del país?"),
    "tierra": (7, "¿Su lema fue «Tierra y Libertad»?"),
    "petroleo": (7, "¿Nacionalizó el petróleo?"),
    "azteca": (7, "¿Fue gobernante azteca o mexica?"),
    "conquistador": (7, "¿Fue un conquistador español?"),
    "pintor": (6, "¿Fue pintor o pintora?"),
    "actor": (6, "¿Fue actor de cine?"),
    "poeta": (6, "¿Fue poeta o escritor?"),
    "cantante": (7, "¿Es famoso también por cantar?"),
    "benemerito": (7, "¿Se le llama el Benemérito de las Américas?"),

    # --- cómics ---
    "marvel": (3, "¿Es de Marvel?"),
    "villano": (4, "¿Es un villano?"),
    "poderes": (4, "¿Tiene superpoderes?"),
    "vuela": (5, "¿Puede volar?"),
    "capa": (5, "¿Usa capa?"),
    "rojo": (5, "¿Su traje es principalmente rojo?"),
    "verde": (5, "¿Es de color verde?"),
    "vengador": (5, "¿Forma parte de los Vengadores?"),
    "liga": (5, "¿Forma parte de la Liga de la Justicia?"),
    "mutante": (6, "¿Es mutante de los X-Men?"),
    "millonario": (6, "¿Es millonario?"),
    "magia": (6, "¿Usa magia o hechicería?"),
    "dios": (6, "¿Es un dios nórdico?"),
    "joven": (6, "¿Es un adolescente?"),
    "payaso": (6, "¿Va maquillado como payaso?"),
    "animal": (6, "¿Es un animal o una planta que habla?"),
    "armadura": (7, "¿Pelea dentro de una armadura tecnológica?"),
    "escudo": (7, "¿Pelea con un escudo?"),
    "martillo": (7, "¿Pelea con un martillo?"),
    "garras": (7, "¿Tiene garras de metal?"),
    "ciego": (7, "¿Es ciego?"),
    "parche": (7, "¿Usa un parche en el ojo?"),
    "simbionte": (7, "¿Es un simbionte alienígena negro?"),
    "morado": (7, "¿Es de piel morada?"),
    "velocidad": (7, "¿Su poder es la súper velocidad?"),
    "agua_comic": (7, "¿Domina el mar?"),
    "anillo": (7, "¿Su poder viene de un anillo?"),
    "robot": (7, "¿Es mitad humano y mitad máquina?"),
    "calvo": (7, "¿Es calvo?"),
    "sidekick": (7, "¿Es el ayudante de otro héroe?"),
    "gato_comic": (7, "¿Su identidad está inspirada en un gato?"),
    "kripton": (7, "¿Viene del planeta Kriptón?"),
    "murcielago": (7, "¿Su símbolo es un murciélago?"),
    "rey": (7, "¿Es rey de su propio reino o país?"),
    "guante": (7, "¿Usa un guante con gemas?"),
    "hermano": (7, "¿Es hermano adoptivo de otro personaje?"),

    # --- youtubers ---
    "espanol_idioma": (3, "¿Hace su contenido en español?"),
    "espana": (4, "¿Es de España?"),
    "argentino": (5, "¿Es de Argentina?"),
    "gaming": (5, "¿Su canal es principalmente de videojuegos?"),
    "minecraft_yt": (5, "¿Es famoso por jugar Minecraft?"),
    "streamer": (5, "¿Es más streamer de Twitch que youtuber?"),
    "humor": (5, "¿Su contenido es de humor o sketches?"),
    "retos": (5, "¿Hace retos enormes y regala dinero?"),
    "vlogs": (5, "¿Hace vlogs de viajes?"),
    "terror_yt": (5, "¿Hace contenido de terror o misterio?"),
    "belleza": (5, "¿Hace contenido de belleza o estilo de vida?"),
    "cien_millones": (6, "¿Tiene más de 50 millones de suscriptores?"),
    "mascara": (7, "¿Duró años sin enseñar la cara, solo una máscara?"),
    "cod_yt": (7, "¿Se hizo famoso jugando Call of Duty?"),
    "fortnite": (7, "¿Se hizo famoso jugando Fortnite?"),
    "eventos": (7, "¿Organiza grandes eventos y narra peleas?"),
    "infantil": (7, "¿Su contenido es animado y para niños?"),

    # --- gente que conozco ---
    "profesor": (3, "¿Da clases?"),
    "lentes": (4, "¿Usa lentes?"),
    "moreno": (5, "¿Es moreno?"),
    "chino": (5, "¿Tiene el cabello chino?"),
    "friki": (5, "¿Es bien friki?"),
    "electronica": (6, "¿Enseña electrónica y programación estructurada?"),
    "tlajomulco": (6, "¿Vive en Tlajomulco de Zúñiga?"),

    # --- videojuegos ---
    "survival": (1, "¿Es un juego de supervivencia?"),
    "shooter": (1, "¿Es un juego de disparos?"),
    "simulador": (2, "¿Es un simulador?"),
    "party": (2, "¿Es un juego de fiesta para jugar con amigos en el sillón?"),
    "mundo_abierto": (3, "¿Es de mundo abierto?"),
    "fps": (3, "¿Se juega en primera persona?"),
    "dosd": (3, "¿Es en 2D?"),
    "multijugador": (3, "¿Se juega sobre todo en línea con otras personas?"),
    "crafteo": (4, "¿Puedes construir y craftear cosas?"),
    "postapo": (4, "¿Ocurre en un mundo post-apocalíptico?"),
    "espacio_vj": (4, "¿Ocurre en el espacio o en otro planeta?"),
    "zombis": (4, "¿Tiene zombis o infectados?"),
    "terror_vj": (4, "¿Es un juego de terror?"),
    "agua": (4, "¿Gran parte del juego ocurre en el agua?"),
    "cooperativo": (4, "¿Está pensado para jugarse en cooperativo?"),
    "gratis": (5, "¿Es gratis para jugar?"),
    "bloques": (5, "¿El mundo está hecho de bloques o voxeles?"),
    "rpg": (5, "¿Es un RPG con historia y niveles?"),
    "indie": (5, "¿Es un juego indie pequeño?"),
    "roguelike": (5, "¿Son partidas cortas que empiezan de cero al morir?"),
    "pelea": (5, "¿Es un juego de peleas?"),
    "estrategia": (5, "¿Es un juego de estrategia?"),
    "granja": (5, "¿Tiene granja o cultivos?"),
    "fabrica": (5, "¿Construyes fábricas y automatizas la producción?"),
    "camiones": (5, "¿Manejas camiones de carga?"),
    "metro_ruso": (5, "¿Ocurre en los túneles del metro de Moscú?"),
    "valve": (6, "¿Es de Valve?"),
    "bethesda": (6, "¿Es de Bethesda?"),
    "battleroyale": (6, "¿Es un battle royale?"),
    "crimen": (6, "¿Juegas como criminal?"),
    "militar_vj": (6, "¿Es de guerra realista con soldados?"),
    "tercera": (6, "¿Se ve al personaje desde atrás, en tercera persona?"),
    "bosque": (6, "¿Te persiguen caníbales en un bosque?"),
    "vikingos": (6, "¿Es de vikingos?"),
    "piratas": (6, "¿Es de piratas?"),
    "medieval": (6, "¿Es de la época medieval?"),
    "programacion": (6, "¿Se juega escribiendo código de programación?"),
    "dinosaurios": (6, "¿Puedes domar dinosaurios?"),
    "naves": (6, "¿Pilotas naves espaciales?"),
    "fantasmas": (6, "¿Cazas fantasmas?"),
    "puzzles": (6, "¿Es de resolver acertijos?"),
    "sandbox": (6, "¿Es un sandbox donde todo se vale y se juega con mods?"),
    "mojang": (7, "¿Es el juego de bloques más vendido de la historia?"),
    "hielo": (7, "¿Ocurre en una región helada?"),
    "secuela": (7, "¿Es una continuación, no la primera entrega?"),
    "tren": (7, "¿Viajas por Rusia en un tren?"),
    "primera": (7, "¿Es la primera entrega de su saga?"),
    "mesa": (7, "¿Sirve para jugar juegos de mesa?"),
    "social": (7, "¿Es para convivir con avatares, no para competir?"),
    "traidor": (7, "¿Hay un traidor entre los jugadores?"),
    "virus": (7, "¿Esparces una enfermedad por el mundo?"),
    "nostalgia": (7, "¿Imita sistemas operativos viejos?"),
    "dificil": (7, "¿Es famoso por ser dificilísimo?"),
    "burocracia": (7, "¿Revisas documentos y sellas pasaportes?"),
    "demonios": (7, "¿Matas demonios del infierno?"),
    "gato_vj": (7, "¿Es un gatito que golpea un tambor?"),
    "ruleta": (7, "¿Juegas a la ruleta rusa con una escopeta?"),
    "parkour": (7, "¿Escapas de los zombis haciendo parkour?"),
    "cocina": (7, "¿Hay que cocinar a toda velocidad?"),
    "babosas": (7, "¿Recolectas babosas de colores?"),
    "patos": (7, "¿Los personajes son patos armados?"),
    "papa": (7, "¿El protagonista es una papa?"),
    "dios_vj": (7, "¿Juegas como un dios sobre un mundo diminuto?"),
    "insectos": (7, "¿Exterminas insectos gigantes por la democracia?"),
    "destruccion": (7, "¿Los escenarios se destruyen por completo?"),
    "clases": (7, "¿Eliges entre nueve clases con sombrero?"),
    "portales": (7, "¿Abres portales para resolver los niveles?"),
    "extraccion": (7, "¿Entras, saqueas y hay que extraerse con vida?"),
    "vida_sim": (7, "¿Controlas la vida diaria de una familia?"),
    "hordas": (7, "¿Hay hordas que atacan cada siete días?"),
    "souls": (7, "¿Es difícil, con jefes al estilo Souls?"),
    "coches": (7, "¿Robas coches por la ciudad?"),
    "xbox": (7, "¿Su protagonista es un supersoldado de armadura verde?"),
    "guerra_mundial": (7, "¿Ocurre en la Segunda Guerra Mundial?"),
    "caballeros": (7, "¿Son caballeritos de dibujos que avanzan golpeando?"),
    "drogas": (7, "¿Manejas un negocio ilegal de drogas?"),
    "vr": (7, "¿Está pensado para realidad virtual?"),
    "competitivo": (7, "¿Es un shooter competitivo de rondas con bomba?"),
}

# ---------------------------------------------------------------- entidades
ENTIDADES = [
    # ======================== CIENTÍFICOS ========================
    ("Albert Einstein", "real cientifico fisico nobel aleman relatividad"),
    ("Isaac Newton", "real cientifico fisico matematico ingles antes1900"),
    ("Marie Curie", "real cientifico mujer fisico biologia nobel"),
    ("Nikola Tesla", "real cientifico fisico inventor electricidad"),
    ("Thomas Edison", "real cientifico inventor electricidad eeuu"),
    ("Charles Darwin", "real cientifico biologia ingles antes1900"),
    ("Galileo Galilei", "real cientifico fisico astronomia antes1900"),
    ("Stephen Hawking", "real cientifico fisico astronomia ingles divulgador"),
    ("Alan Turing", "real cientifico matematico ingles"),
    ("Ada Lovelace", "real cientifico mujer matematico ingles antes1900 programadora"),
    ("Louis Pasteur", "real cientifico biologia antes1900"),
    ("Gregor Mendel", "real cientifico biologia antes1900 adn sacerdote"),
    ("Niels Bohr", "real cientifico fisico nobel"),
    ("Erwin Schrödinger", "real cientifico fisico nobel gato_cuantico"),
    ("Werner Heisenberg", "real cientifico fisico nobel aleman"),
    ("Richard Feynman", "real cientifico fisico nobel eeuu"),
    ("Robert Oppenheimer", "real cientifico fisico eeuu bomba"),
    ("Rosalind Franklin", "real cientifico mujer biologia ingles adn"),
    ("Nicolás Copérnico", "real cientifico astronomia antes1900"),
    ("Arquímedes", "real cientifico matematico fisico antes1900 antiguo"),
    ("Leonardo da Vinci", "real cientifico inventor artista antes1900"),
    ("Carl Sagan", "real cientifico astronomia eeuu divulgador"),
    ("Dmitri Mendeléyev", "real cientifico biologia antes1900 tabla"),
    ("Grace Hopper", "real cientifico mujer matematico eeuu programadora"),
    ("Katherine Johnson", "real cientifico mujer matematico eeuu astronomia"),
    ("Alexander Fleming", "real cientifico biologia nobel ingles penicilina"),
    ("Mario Molina", "real cientifico mexicano biologia nobel"),
    ("Guillermo González Camarena", "real cientifico mexicano inventor"),

    # ===================== HISTORIA DE MÉXICO =====================
    ("Miguel Hidalgo", "real mexicano mexicano_hist independencia sacerdote antes1900 padre_patria"),
    ("José María Morelos", "real mexicano mexicano_hist independencia sacerdote militar antes1900"),
    ("Vicente Guerrero", "real mexicano mexicano_hist independencia militar presidente antes1900"),
    ("Ignacio Allende", "real mexicano mexicano_hist independencia militar antes1900"),
    ("Josefa Ortiz de Domínguez", "real mexicano mexicano_hist independencia mujer antes1900 corregidora"),
    ("Leona Vicario", "real mexicano mexicano_hist independencia mujer antes1900"),
    ("Agustín de Iturbide", "real mexicano mexicano_hist independencia militar antes1900 emperador"),
    ("Guadalupe Victoria", "real mexicano mexicano_hist independencia presidente antes1900 primer_pres"),
    ("Benito Juárez", "real mexicano mexicano_hist presidente antes1900 benemerito"),
    ("Porfirio Díaz", "real mexicano mexicano_hist presidente militar dictador"),
    ("Antonio López de Santa Anna", "real mexicano mexicano_hist presidente militar antes1900 pierna"),
    ("Francisco I. Madero", "real mexicano mexicano_hist presidente revolucion"),
    ("Venustiano Carranza", "real mexicano mexicano_hist presidente revolucion militar"),
    ("Pancho Villa", "real mexicano mexicano_hist revolucion militar norte"),
    ("Emiliano Zapata", "real mexicano mexicano_hist revolucion militar tierra"),
    ("Lázaro Cárdenas", "real mexicano mexicano_hist presidente militar petroleo"),
    ("Hernán Cortés", "real mexicano_hist prehispanico militar antes1900 conquistador"),
    ("Moctezuma II", "real mexicano mexicano_hist prehispanico antes1900 azteca"),
    ("Cuauhtémoc", "real mexicano mexicano_hist prehispanico antes1900 azteca militar"),
    ("La Malinche", "real mexicano mexicano_hist prehispanico mujer antes1900"),
    ("Nezahualcóyotl", "real mexicano mexicano_hist prehispanico antes1900 artista poeta rey"),
    ("Sor Juana Inés de la Cruz", "real mexicano mexicano_hist mujer artista poeta sacerdote antes1900"),
    ("Frida Kahlo", "real mexicano mexicano_hist mujer artista pintor"),
    ("Diego Rivera", "real mexicano mexicano_hist artista pintor"),
    ("Cantinflas", "real mexicano mexicano_hist artista actor humor"),
    ("Pedro Infante", "real mexicano mexicano_hist artista actor cantante"),
    ("Octavio Paz", "real mexicano mexicano_hist artista poeta nobel"),

    # =========================== CÓMICS ===========================
    ("Spider-Man", "comic marvel poderes rojo vengador joven"),
    ("Iron Man", "comic marvel vengador millonario vuela rojo armadura"),
    ("Capitán América", "comic marvel vengador escudo"),
    ("Thor", "comic marvel vengador poderes vuela capa dios martillo"),
    ("Hulk", "comic marvel vengador poderes verde"),
    ("Black Widow", "comic marvel vengador mujer"),
    ("Wolverine", "comic marvel mutante poderes garras"),
    ("Deadpool", "comic marvel poderes rojo humor"),
    ("Doctor Strange", "comic marvel vengador poderes capa magia"),
    ("Black Panther", "comic marvel vengador rey"),
    ("Venom", "comic marvel villano poderes simbionte"),
    ("Thanos", "comic marvel villano poderes morado guante"),
    ("Magneto", "comic marvel villano mutante poderes"),
    ("Scarlet Witch", "comic marvel vengador mujer poderes rojo magia"),
    ("Groot", "comic marvel poderes verde animal"),
    ("Rocket Raccoon", "comic marvel animal"),
    ("Daredevil", "comic marvel poderes rojo ciego"),
    ("Nick Fury", "comic marvel parche calvo"),
    ("Loki", "comic marvel villano poderes dios magia hermano"),
    ("Superman", "comic liga poderes vuela capa kripton"),
    ("Batman", "comic liga millonario capa murcielago"),
    ("Wonder Woman", "comic liga mujer poderes vuela"),
    ("Flash", "comic liga poderes rojo velocidad"),
    ("Aquaman", "comic liga poderes agua_comic"),
    ("Green Lantern", "comic liga poderes vuela verde anillo"),
    ("Cyborg", "comic liga poderes robot"),
    ("Joker", "comic villano payaso verde humor"),
    ("Harley Quinn", "comic villano mujer payaso"),
    ("Lex Luthor", "comic villano millonario calvo"),
    ("Robin", "comic capa joven sidekick"),
    ("Catwoman", "comic villano mujer gato_comic"),

    # ========================= YOUTUBERS =========================
    ("PewDiePie", "real youtuber vive gaming cien_millones"),
    ("MrBeast", "real youtuber vive retos cien_millones eeuu"),
    ("Markiplier", "real youtuber vive eeuu gaming terror_yt"),
    ("Jacksepticeye", "real youtuber vive gaming"),
    ("Dream", "real youtuber vive minecraft_yt mascara"),
    ("Technoblade", "real youtuber minecraft_yt"),
    ("DanTDM", "real youtuber vive minecraft_yt infantil"),
    ("elrubiusOMG", "real youtuber vive espanol_idioma espana gaming humor"),
    ("Vegetta777", "real youtuber vive espanol_idioma espana minecraft_yt"),
    ("Willyrex", "real youtuber vive espanol_idioma espana minecraft_yt cod_yt"),
    ("Mikecrack", "real youtuber vive espanol_idioma espana minecraft_yt infantil"),
    ("AuronPlay", "real youtuber vive espanol_idioma espana streamer humor"),
    ("TheGrefg", "real youtuber vive espanol_idioma espana streamer fortnite"),
    ("Ibai Llanos", "real youtuber vive espanol_idioma espana streamer eventos"),
    ("Fernanfloo", "real youtuber vive espanol_idioma gaming humor"),
    ("HolaSoyGerman", "real youtuber vive espanol_idioma humor"),
    ("Luisito Comunica", "real youtuber vive espanol_idioma mexicano vlogs"),
    ("Yuya", "real youtuber vive espanol_idioma mexicano mujer belleza"),
    ("Kimberly Loaiza", "real youtuber vive espanol_idioma mexicano mujer cantante"),
    ("Juan Guarnizo", "real youtuber vive espanol_idioma argentino streamer"),
    ("Dross Rotzank", "real youtuber vive espanol_idioma terror_yt"),
    ("Werevertumorro", "real youtuber vive espanol_idioma mexicano humor"),
    ("El Mariana", "real youtuber vive espanol_idioma mexicano streamer gaming"),
    ("Fede Vigevani", "real youtuber vive espanol_idioma retos"),
    ("Quackity", "real youtuber vive espanol_idioma mexicano minecraft_yt streamer"),

    # ====================== GENTE QUE CONOZCO ======================
    ("el profesor Alberto", "real conocido vive mexicano profesor moreno chino electronica"),
    ("Walter (Carlos)", "real conocido vive mexicano lentes moreno friki tlajomulco"),

    # ========================= VIDEOJUEGOS =========================
    ("Minecraft", "vj bloques survival crafteo mundo_abierto multijugador mojang"),
    ("Terraria", "vj dosd survival crafteo mundo_abierto bloques"),
    ("Fallout 4", "vj postapo rpg mundo_abierto bethesda fps"),
    ("Fallout 76", "vj postapo rpg mundo_abierto bethesda fps multijugador survival"),
    ("Metro Exodus", "vj postapo fps shooter metro_ruso tren"),
    ("Metro 2033 Redux", "vj postapo fps shooter metro_ruso primera"),
    ("Metro: Last Light", "vj postapo fps shooter metro_ruso secuela"),
    ("Grand Theft Auto V", "vj mundo_abierto crimen multijugador coches tercera"),
    ("Counter-Strike 2", "vj fps shooter multijugador valve gratis competitivo"),
    ("ARK: Survival Evolved", "vj survival mundo_abierto crafteo multijugador dinosaurios"),
    ("ASTRONEER", "vj espacio_vj survival crafteo mundo_abierto"),
    ("No Man's Sky", "vj espacio_vj survival mundo_abierto crafteo naves"),
    ("Elite Dangerous", "vj espacio_vj simulador naves multijugador"),
    ("Subnautica", "vj agua survival crafteo espacio_vj primera"),
    ("Subnautica: Below Zero", "vj agua survival crafteo espacio_vj hielo secuela"),
    ("Satisfactory", "vj fabrica crafteo mundo_abierto fps"),
    ("The Farmer Was Replaced", "vj programacion granja indie fabrica"),
    ("Sons Of The Forest", "vj survival terror_vj bosque crafteo secuela"),
    ("The Forest", "vj survival terror_vj bosque crafteo primera"),
    ("HELLDIVERS 2", "vj shooter espacio_vj cooperativo tercera insectos multijugador"),
    ("American Truck Simulator", "vj simulador camiones"),
    ("Euro Truck Simulator 2", "vj simulador camiones secuela"),
    ("Unturned", "vj zombis survival gratis bloques multijugador"),
    ("7 Days to Die", "vj zombis survival crafteo mundo_abierto hordas"),
    ("Duck Game", "vj dosd party patos multijugador pelea"),
    ("Remnant II", "vj shooter tercera rpg cooperativo souls secuela"),
    ("Halo: The Master Chief Collection", "vj fps shooter espacio_vj multijugador xbox"),
    ("PUBG: BATTLEGROUNDS", "vj battleroyale fps shooter multijugador gratis"),
    ("Tabletop Simulator", "vj simulador mesa multijugador"),
    ("Schedule I", "vj crimen simulador drogas multijugador"),
    ("Left 4 Dead 2", "vj zombis fps shooter cooperativo valve secuela"),
    ("Brotato", "vj roguelike dosd indie papa"),
    ("WorldBox", "vj simulador dios_vj dosd indie"),
    ("Borderlands 3", "vj fps shooter rpg cooperativo"),
    ("Sea of Thieves", "vj piratas mundo_abierto multijugador agua"),
    ("Brawlhalla", "vj pelea dosd gratis multijugador"),
    ("Phasmophobia", "vj terror_vj cooperativo fantasmas fps"),
    ("VRChat", "vj social gratis multijugador vr"),
    ("Garry's Mod", "vj sandbox valve multijugador"),
    ("Portal 2", "vj puzzles valve fps cooperativo portales secuela"),
    ("Stardew Valley", "vj granja dosd indie"),
    ("Among Us", "vj multijugador traidor dosd espacio_vj"),
    ("Valheim", "vj survival vikingos crafteo cooperativo"),
    ("Vampire Survivors", "vj roguelike dosd indie gratis"),
    ("Plague Inc: Evolved", "vj estrategia simulador virus"),
    ("Progressbar95", "vj indie nostalgia dosd"),
    ("Cuphead", "vj dosd dificil indie"),
    ("Papers, Please", "vj indie simulador dosd burocracia"),
    ("DOOM", "vj fps shooter demonios bethesda"),
    ("Bongo Cat", "vj gratis gato_vj indie"),
    ("Buckshot Roulette", "vj indie terror_vj ruleta"),
    ("Dying Light", "vj zombis fps mundo_abierto parkour"),
    ("Team Fortress 2", "vj fps shooter multijugador gratis valve clases"),
    ("Raft", "vj survival agua crafteo cooperativo"),
    ("Muck", "vj survival indie gratis roguelike"),
    ("Stick Fight: The Game", "vj party pelea dosd multijugador"),
    ("Gang Beasts", "vj party pelea multijugador"),
    ("Overcooked! 2", "vj party cooperativo cocina secuela"),
    ("Castle Crashers", "vj dosd cooperativo caballeros pelea"),
    ("Slime Rancher", "vj granja fps babosas"),
    ("Age of Empires II", "vj estrategia medieval"),
    ("THE FINALS", "vj fps shooter multijugador gratis destruccion"),
    ("Mortal Kombat 11", "vj pelea"),
    ("Arma 3", "vj fps shooter simulador militar_vj multijugador"),
    ("Hell Let Loose", "vj fps shooter militar_vj guerra_mundial multijugador"),
    ("ARC Raiders", "vj shooter tercera postapo extraccion multijugador"),
    ("Dead Rising 3", "vj zombis tercera mundo_abierto"),
    ("The Sims 4", "vj simulador vida_sim"),
]


def validar():
    """Revisa que no haya etiquetas inventadas ni entidades idénticas."""
    errores = []
    vistos = {}
    for nombre, etiquetas in ENTIDADES:
        for etiqueta in etiquetas.split():
            if etiqueta not in PREGUNTAS:
                errores.append(f"{nombre}: etiqueta desconocida '{etiqueta}'")
        huella = frozenset(etiquetas.split())
        if huella in vistos:
            errores.append(f"{nombre} es indistinguible de {vistos[huella]}")
        vistos[huella] = nombre
    return errores


def construir(items, usadas):
    """Arma el árbol escogiendo en cada paso la pregunta que mejor separa."""
    if len(items) == 1:
        return {"respuesta": items[0][0]}

    mejor = None
    for clave, (prioridad, _) in PREGUNTAS.items():
        if clave in usadas:
            continue
        si = [it for it in items if clave in it[1]]
        no = [it for it in items if clave not in it[1]]
        if not si or not no:
            continue
        puntaje = (prioridad, abs(len(si) - len(no)))
        if mejor is None or puntaje < mejor[0]:
            mejor = (puntaje, clave, si, no)

    if mejor is None:
        # Nada las separa: se pregunta directo por el nombre.
        nombre = items[0][0]
        return {
            "pregunta": f"¿Es {nombre}?",
            "si": {"respuesta": nombre},
            "no": construir(items[1:], usadas),
        }

    _, clave, si, no = mejor
    usadas = usadas | {clave}
    return {
        "pregunta": PREGUNTAS[clave][1],
        "si": construir(si, usadas),
        "no": construir(no, usadas),
    }


def probar(arbol):
    """Simula una partida por cada entidad y verifica que se adivine."""
    texto_a_clave = {t: k for k, (_, t) in PREGUNTAS.items()}
    fallos = []
    profundidades = []
    for nombre, etiquetas in ENTIDADES:
        tags = set(etiquetas.split())
        nodo, pasos = arbol, 0
        while "pregunta" in nodo:
            clave = texto_a_clave.get(nodo["pregunta"])
            if clave is None:                      # pregunta "¿Es <nombre>?"
                esperado = nodo["pregunta"][1:-1].removeprefix("Es ")
                nodo = nodo["si"] if esperado == nombre else nodo["no"]
            else:
                nodo = nodo["si"] if clave in tags else nodo["no"]
            pasos += 1
        if nodo["respuesta"] != nombre:
            fallos.append(f"{nombre} -> {nodo['respuesta']}")
        profundidades.append(pasos)
    return fallos, profundidades


def main():
    errores = validar()
    if errores:
        print("Hay problemas en los datos:")
        for e in errores:
            print("  -", e)
        return

    items = [(n, set(t.split())) for n, t in ENTIDADES]
    arbol = construir(items, frozenset())

    fallos, prof = probar(arbol)
    if fallos:
        print("El árbol no adivina bien:")
        for f in fallos:
            print("  -", f)
        return

    ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "akinator.json")
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(arbol, f, ensure_ascii=False, indent=2)

    print(f"Listo: {len(ENTIDADES)} personajes y juegos en la base.")
    print(f"Preguntas por partida: mínimo {min(prof)}, máximo {max(prof)}, "
          f"promedio {sum(prof) / len(prof):.1f}")


if __name__ == "__main__":
    main()
