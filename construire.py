#!/usr/bin/env python3
"""Génère le site statique de LoupeCard (accueil, confidentialité, assistance) en français et en anglais.

Usage : python3 site/construire.py          → écrit site/public/
L'adresse de contact se règle dans CONTACT ci-dessous.
"""
import shutil
from datetime import date
from pathlib import Path

ICI = Path(__file__).resolve().parent
SORTIE = ICI / "public"
CONTACT = "geoffrey.mariette@gmail.com"   # provisoire, en attendant une adresse sur le domaine
MAJ = date(2026, 11, 19)
LOGO = (ICI / "logo.svg").read_text()

T = {
    "fr": {
        "pages": {"index": "index.html", "confidentialite": "confidentialite.html", "assistance": "assistance.html"},
        "nav": {"index": "L'app", "confidentialite": "Confidentialité", "assistance": "Assistance"},
        "autre": ("en", "English"),
        "maj": f"Mise à jour le {MAJ.day} novembre {MAJ.year}",
        "mention": "LoupeCard n'est ni affiliée, ni approuvée, ni sponsorisée par Nintendo, Creatures, GAME FREAK ou The Pokémon Company. "
                   "Les noms et marques cités appartiennent à leurs propriétaires respectifs.",
        "index": ("LoupeCard, le scanner du collectionneur", """
<h1>Sais tout de suite si une carte te manque.</h1>
<p class="chapo">Dans un bac de vrac, en brocante ou en boutique : vise le bas d'une carte avec ton iPhone, LoupeCard te dit en une seconde si elle manque à ta collection.</p>
<div class="carte">
  <p>L'app lit le code imprimé au bas de la carte, par exemple <span class="code">PAL FR 123/193</span>. Pour les séries plus anciennes, elle utilise le numéro et le symbole de la série.</p>
  <div class="verdicts">
    <div class="verdict manque"><strong>Il te manque</strong><span>avec la version à chercher et son prix</span></div>
    <div class="verdict"><strong>Tu l'as déjà</strong><span>passe à la suivante</span></div>
    <div class="verdict"><strong>Série non suivie</strong><span>avec son prix indicatif</span></div>
  </div>
</div>
<h2>Pensée pour le terrain</h2>
<ul>
  <li>Fonctionne sans réseau : la lecture se fait sur l'iPhone.</li>
  <li>Toutes les séries, du Set de Base aux plus récentes.</li>
  <li>Bilan de la session : combien de cartes vues, combien te manquent, pour quel budget.</li>
</ul>
<p>Bientôt sur l'App Store.</p>"""),
        "confidentialite": ("Politique de confidentialité", f"""
<h1>Politique de confidentialité</h1>
<p class="maj">{{maj}}</p>
<p class="chapo">En bref : LoupeCard ne collecte aucune donnée personnelle. Rien ne quitte ton iPhone.</p>
<h2>La caméra</h2>
<p>LoupeCard utilise la caméra uniquement pour lire le texte imprimé au bas des cartes. Les images sont analysées sur ton iPhone, par la reconnaissance de texte intégrée à iOS, puis supprimées aussitôt. Elles ne sont ni enregistrées dans ta photothèque, ni envoyées à qui que ce soit.</p>
<h2>Ta collection</h2>
<p>La liste de tes cartes et l'historique de tes scans restent stockés sur ton appareil. Nous n'y avons pas accès.</p>
<h2>Ce que nous ne faisons pas</h2>
<ul>
  <li>Pas de compte à créer.</li>
  <li>Pas de publicité, pas de traceur, pas d'outil de mesure d'audience.</li>
  <li>Pas de vente ni de partage de données : nous n'en avons pas.</li>
</ul>
<h2>Achats intégrés</h2>
<p>Si l'app propose un jour des fonctions payantes, le paiement sera traité par Apple. Nous ne recevons ni ton nom, ni tes coordonnées bancaires.</p>
<h2>Ce site</h2>
<p>Ce site ne dépose aucun cookie et ne charge aucune ressource tierce.</p>
<h2>Contact</h2>
<p>Une question sur cette politique : <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>
<p>Si cette politique change, la nouvelle version sera publiée sur cette page avec sa date de mise à jour.</p>"""),
        "assistance": ("Assistance", f"""
<h1>Assistance</h1>
<p class="chapo">Un souci, une idée, une série mal reconnue ? Écris-nous à <a href="mailto:{CONTACT}">{CONTACT}</a>, nous répondons en général sous 48 heures.</p>
<h2>Questions fréquentes</h2>
<h3>L'app ne lit pas le code de ma carte.</h3>
<p>Rapproche l'iPhone pour que le code en bas à gauche de la carte remplisse le cadre, et allume la lampe si la lumière est faible. Tu peux aussi utiliser la saisie manuelle : tape par exemple <span class="code">PAL 123</span> ou le nom de la carte.</p>
<h3>L'app me propose plusieurs séries.</h3>
<p>Les cartes d'avant 2023 n'impriment pas de code de série, seulement un symbole. Quand plusieurs séries ont le même nombre de cartes, LoupeCard affiche leurs symboles : touche celui qui correspond à ta carte.</p>
<h3>Mes images sont-elles envoyées quelque part ?</h3>
<p>Non. La lecture se fait entièrement sur ton iPhone. Voir la <a href="confidentialite.html">politique de confidentialité</a>.</p>
<p>Quand tu nous écris pour un problème, indique si possible le modèle de ton iPhone, ta version d'iOS et le code imprimé sur la carte concernée.</p>"""),
    },
    "en": {
        "pages": {"index": "index.html", "confidentialite": "privacy.html", "assistance": "support.html"},
        "nav": {"index": "The app", "confidentialite": "Privacy", "assistance": "Support"},
        "autre": ("fr", "Français"),
        "maj": f"Last updated November {MAJ.day}, {MAJ.year}",
        "mention": "LoupeCard is not affiliated with, endorsed or sponsored by Nintendo, Creatures, GAME FREAK or The Pokémon Company. "
                   "All names and trademarks belong to their respective owners.",
        "index": ("LoupeCard, the collector's scanner", """
<h1>Know instantly whether you need a card.</h1>
<p class="chapo">In a bulk bin, at a flea market or in a shop: point your iPhone at the bottom of a card and LoupeCard tells you in a second whether it is missing from your collection.</p>
<div class="carte">
  <p>The app reads the code printed at the bottom of the card, such as <span class="code">PAL EN 123/193</span>. For older sets it uses the card number and the set symbol.</p>
  <div class="verdicts">
    <div class="verdict manque"><strong>You need it</strong><span>with the version to look for and its price</span></div>
    <div class="verdict"><strong>You have it</strong><span>move on to the next one</span></div>
    <div class="verdict"><strong>Set not tracked</strong><span>with an indicative price</span></div>
  </div>
</div>
<h2>Built for the field</h2>
<ul>
  <li>Works offline: reading happens on your iPhone.</li>
  <li>Every set, from Base Set to the latest ones.</li>
  <li>Session summary: cards seen, cards missing, and the budget.</li>
</ul>
<p>Coming soon to the App Store.</p>"""),
        "confidentialite": ("Privacy policy", f"""
<h1>Privacy policy</h1>
<p class="maj">{{maj}}</p>
<p class="chapo">In short: LoupeCard collects no personal data. Nothing leaves your iPhone.</p>
<h2>Camera</h2>
<p>LoupeCard uses the camera only to read the text printed at the bottom of cards. Images are analysed on your iPhone by the text recognition built into iOS, then deleted right away. They are never saved to your photo library or sent to anyone.</p>
<h2>Your collection</h2>
<p>Your card list and scan history are stored on your device. We have no access to them.</p>
<h2>What we don't do</h2>
<ul>
  <li>No account to create.</li>
  <li>No ads, no trackers, no analytics.</li>
  <li>No selling or sharing of data: we don't have any.</li>
</ul>
<h2>In-app purchases</h2>
<p>If the app offers paid features in the future, payment will be handled by Apple. We never receive your name or payment details.</p>
<h2>This website</h2>
<p>This website sets no cookies and loads no third-party resources.</p>
<h2>Contact</h2>
<p>Questions about this policy: <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>
<p>If this policy changes, the new version will be posted on this page with its update date.</p>"""),
        "assistance": ("Support", f"""
<h1>Support</h1>
<p class="chapo">A problem, an idea, a set that isn't recognised? Email us at <a href="mailto:{CONTACT}">{CONTACT}</a>, we usually reply within 48 hours.</p>
<h2>Frequently asked questions</h2>
<h3>The app doesn't read my card's code.</h3>
<p>Move the iPhone closer so the code in the bottom-left corner fills the frame, and turn on the torch in low light. You can also type the card: for example <span class="code">PAL 123</span> or the card name.</p>
<h3>The app offers several sets.</h3>
<p>Cards printed before 2023 have no set code, only a symbol. When several sets have the same card count, LoupeCard shows their symbols: tap the one that matches your card.</p>
<h3>Are my images sent anywhere?</h3>
<p>No. Reading happens entirely on your iPhone. See the <a href="privacy.html">privacy policy</a>.</p>
<p>When reporting a problem, please include your iPhone model, iOS version and the code printed on the card.</p>"""),
    },
}


def page(langue, cle):
    t = T[langue]
    titre, corps = t[cle]
    courant = ' aria-current="page"'
    nav = "".join(f'<a href="{t["pages"][k]}"{courant if k == cle else ""}>{t["nav"][k]}</a>' for k in t["pages"])
    autre, nom_autre = t["autre"]
    lien_autre = f'../{autre}/{T[autre]["pages"][cle]}'
    return f"""<!doctype html>
<html lang="{langue}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{titre} · LoupeCard</title>
<link rel="stylesheet" href="../style.css">
<link rel="icon" href="../logo.svg" type="image/svg+xml">
<link rel="alternate" hreflang="{autre}" href="{lien_autre}">
</head>
<body>
<header>
  <a class="marque" href="{t['pages']['index']}">{LOGO}LoupeCard</a>
  <nav>{nav}<a href="{lien_autre}" lang="{autre}">{nom_autre}</a></nav>
</header>
<main>{corps.replace("{maj}", t["maj"])}</main>
<footer>
  <div class="liens">{nav}</div>
  <div>{t['mention']}</div>
</footer>
</body>
</html>
"""


def main():
    shutil.rmtree(SORTIE, ignore_errors=True)
    for langue in T:
        (SORTIE / langue).mkdir(parents=True)
        for cle, fichier in T[langue]["pages"].items():
            (SORTIE / langue / fichier).write_text(page(langue, cle), encoding="utf-8")
    shutil.copy(ICI / "style.css", SORTIE / "style.css")
    shutil.copy(ICI / "logo.svg", SORTIE / "logo.svg")
    # Racine : français si le navigateur est en français, anglais sinon.
    (SORTIE / "index.html").write_text("""<!doctype html><html><head><meta charset="utf-8"><title>LoupeCard</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<script>location.replace((navigator.language||'').toLowerCase().startsWith('fr')?'fr/':'en/')</script>
<noscript><meta http-equiv="refresh" content="0;url=en/"></noscript></head>
<body><a href="fr/">Français</a> · <a href="en/">English</a></body></html>
""", encoding="utf-8")
    print(f"site généré dans {SORTIE} ({sum(1 for _ in SORTIE.rglob('*.html'))} pages)")


if __name__ == "__main__":
    main()
