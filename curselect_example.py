import random
from curses import A_UNDERLINE
from curselect import curselect

def main():

    tapok = ["Marhapörkölt",
              "Steak",
              "Bárányoldalas",
              "Aranygaluska",
              "Vínersniccel",
              "Véreshurka",
              "Babgulyás",
              "Piddza",
              "Kirántotthús rizsával",
              "Grillcsirke sztékburesszel",
              "Gyros patkányhúsból tortijjával vagy nélküle",
              "Hembörgör cocából mer a marha drága",
              "Csirke farhát (politikai)",
              "Szusi",
              "Tömlőssajttal töltött rántott párizsi",
              "Túroscsusza",
              "Szilvalekváros",
              "Grízes",
              "Tésztás",
              "Derelye",
              "Hitlerszalonna",
              "Sztálinsonka",
              "Jó táp",
              "Mai menü",
              "Cigánypecsenye",
              "Sztékburesz",
              "Losz pojjosz hermánosz",
              "Cigarettacsikk",
              "Hajszál"
             ]

    menu = curselect.CurSelect(tapok, title="Étlap", ret_type="value", pagination=15, char="~~ ", highlight=A_UNDERLINE)
    valasztott = menu.activate()

    if valasztott != None:
        print("Jó étvágyat kívánunk a " + valasztott.lower() + "hoz!")
        return
    print("Mai ajánlatunk a döntésképteleneknek: " + random.choice(tapok) + "\nJó étvágyat!")

if __name__ == "__main__":
    main()
